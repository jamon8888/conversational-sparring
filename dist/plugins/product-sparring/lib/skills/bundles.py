"""Bundle management and synchronization."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

from .models import Bundle, Skill

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None  # type: ignore
    HAS_YAML = False


class BundleManager:
    """Manages skill bundles."""

    def __init__(self, config_path: Path, root_path: Path) -> None:
        """Initialize bundle manager.

        Args:
            config_path: Path to bundles.yaml
            root_path: Repository root path
        """
        self.config_path = config_path
        self.root_path = root_path
        self._bundles: Dict[str, Bundle] = {}

    def load(self) -> Dict[str, Bundle]:
        """Load bundles from configuration."""
        if not self.config_path.exists() or not HAS_YAML:
            return {}

        try:
            with open(self.config_path, encoding="utf-8") as f:
                data = yaml.safe_load(f) or {}
            
            bundles_data = data.get("bundles", {})
            for name, info in bundles_data.items():
                self._bundles[name] = Bundle(
                    name=name,
                    domain=info.get("domain", "general"),
                    description=info.get("description", ""),
                    skills=info.get("skills", []),
                    selectors=info.get("selectors", [])
                )
        except Exception:
            pass  # Fail gracefully

        return self._bundles

    def get_bundle(self, name: str) -> Optional[Bundle]:
        """Get a specific bundle by name."""
        if not self._bundles:
            self.load()
        return self._bundles.get(name)

    def resolve_bundle_skills(self, bundle_name: str, all_skills: List[Skill]) -> List[Skill]:
        """Resolve a bundle into a list of skills.

        Combines explicit skill lists with dynamic selectors.

        Args:
            bundle_name: Name of bundle to resolve
            all_skills: List of all available skills (from registry)

        Returns:
            List of resolved skills
        """
        bundle = self.get_bundle(bundle_name)
        if not bundle:
            return []

        resolved_skills: Set[str] = set()
        
        # 1. Add explicit skills
        for skill_name in bundle.skills:
            resolved_skills.add(skill_name)
            
        # 2. Process selectors
        # Example selectors:
        # - category: marketing
        # - keywords: [seo, content]
        for selector in bundle.selectors:
            category = selector.get("category")
            
            for skill in all_skills:
                if category and skill.category == category:
                    resolved_skills.add(skill.name)
        
        # Return Skill objects
        return [s for s in all_skills if s.name in resolved_skills]

    def sync_to_marketplace(self, marketplace_path: Path, all_skills: List[Skill]) -> None:
        """Sync bundles definition to .claude-plugin/marketplace.json.
        
        This generates the 'personas' section in marketplace.json to ensure bundles
        are recognized as plugins in Claude Code.

        Args:
            marketplace_path: Path to marketplace.json
            all_skills: List of all skills
        """
        if not marketplace_path.exists():
            return
            
        try:
            with open(marketplace_path, encoding="utf-8") as f:
                market_data = json.load(f)
            
            # Ensure framework for personas/domains exists
            if "personas" not in market_data:
                market_data["personas"] = {}
                
            # Group bundles by domain
            if not self._bundles:
                self.load()
                
            grouped_bundles: Dict[str, Dict[str, Any]] = {}
            domains: Dict[str, Set[str]] = {}
            
            for name, bundle in self._bundles.items():
                domain = bundle.domain
                if domain not in grouped_bundles:
                    grouped_bundles[domain] = {}
                    domains[domain] = set()
                
                # Resolve skills for this bundle to get the complete list
                resolved = self.resolve_bundle_skills(name, all_skills)
                skill_names = [s.name for s in resolved]
                
                grouped_bundles[domain][name] = {
                    "domain": domain,
                    "skills": skill_names,
                    "description": bundle.description
                }
                
                # Track unique domains for persona definition
                domains[domain].add(domain)

            # Update marketplace data
            # We map "domain" from bundle yaml to "persona" in marketplace.json
            # e.g. domain="c-level" -> persona="c-level"
            
            for domain_key, bundles_map in grouped_bundles.items():
                if domain_key not in market_data["personas"]:
                    market_data["personas"][domain_key] = {
                        "domains": list(domains[domain_key]), # A bit redundant but matching schema
                        "description": f"Bundles for {domain_key}",
                        "bundles": {}
                    }
                
                # Update bundles for this persona
                market_data["personas"][domain_key]["bundles"] = bundles_map

            with open(marketplace_path, "w", encoding="utf-8") as f:
                json.dump(market_data, f, indent=2)
                
        except Exception as e:
            pass
            # print(f"Failed to sync marketplace: {e}")
