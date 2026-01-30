"""Skills manager."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, TYPE_CHECKING

from .registry import SkillsRegistry
from .bundles import BundleManager

if TYPE_CHECKING:
    from ..ledger import SparringLedger
    from ..domains.loader import DomainConfig


class SkillsManager:
    """Manage skill installations using ledger for tracking."""

    def __init__(
        self,
        ledger: "SparringLedger",
        registry: Optional[SkillsRegistry] = None
    ) -> None:
        """Initialize skills manager.

        Args:
            ledger: SparringLedger instance for event storage
            registry: Optional SkillsRegistry (creates default if None)
        """
        self.ledger = ledger
        self.registry = registry or SkillsRegistry()
        
        # Initialize bundle manager
        root_path = self.registry.root_path
        self.bundle_manager = BundleManager(
            config_path=root_path / "config" / "bundles.yaml",
            root_path=root_path
        )

    def install_skill(
        self,
        skill_name: str,
        target: str = "claude-code"
    ) -> int:
        """Record skill installation event.

        Args:
            skill_name: Name of skill to install
            target: Installation target (claude-code, codex, etc.)

        Returns:
            Event ID

        Raises:
            ValueError: If skill not found in registry
        """
        skill = self.registry.get_skill(skill_name)
        if not skill:
            raise ValueError(f"Skill not found: {skill_name}")

        return self.ledger.append(
            kind="skill_install",
            content=json.dumps({
                "skill": skill_name,
                "category": skill.get("category"),
                "source": skill.get("source"),
            }, sort_keys=True),
            meta={"target": target}
        )

    def uninstall_skill(self, skill_name: str) -> int:
        """Record skill uninstallation event.

        Args:
            skill_name: Name of skill to uninstall

        Returns:
            Event ID
        """
        return self.ledger.append(
            kind="skill_uninstall",
            content=json.dumps({"skill": skill_name}, sort_keys=True),
            meta={}
        )

    def install_bundle(
        self,
        bundle_name: str,
        skills: List[str],
        domain: str,
        target: str = "claude-code"
    ) -> int:
        """Record bundle installation event.

        Args:
            bundle_name: Name of bundle (e.g., "ceo-starter")
            skills: List of skill names in bundle
            domain: Domain this bundle belongs to
            target: Installation target

        Returns:
            Event ID
        """
        return self.ledger.append(
            kind="bundle_install",
            content=json.dumps({
                "bundle": bundle_name,
                "skills": skills,
                "domain": domain,
            }, sort_keys=True),
            meta={"target": target}
        )

    def record_usage(self, skill_name: str, context: str = "") -> int:
        """Record skill usage event.

        Args:
            skill_name: Name of skill used
            context: Optional context description

        Returns:
            Event ID
        """
        return self.ledger.append(
            kind="skill_use",
            content=json.dumps({"skill": skill_name}, sort_keys=True),
            meta={"context": context} if context else {}
        )

    def record_feedback(
        self,
        skill_name: str,
        rating: int,
        comment: str = ""
    ) -> int:
        """Record skill feedback event.

        Args:
            skill_name: Name of skill
            rating: Rating (1-5)
            comment: Optional feedback comment

        Returns:
            Event ID
        """
        return self.ledger.append(
            kind="skill_feedback",
            content=json.dumps({
                "skill": skill_name,
                "rating": max(1, min(5, rating)),
                "comment": comment,
            }, sort_keys=True),
            meta={}
        )
    
    # ... (rest of methods like get_installed_skills, etc. remain the same conceptually)
    # Copied from original skills.py for backward compatibility
    
    def get_installed_skills(self) -> List[str]:
        """Get list of currently installed skills from ledger."""
        installed = set()
        uninstalled = set()

        for event in self.ledger.read_by_kind("skill_install"):
            content = json.loads(event["content"])
            installed.add(content["skill"])

        for event in self.ledger.read_by_kind("skill_uninstall"):
            content = json.loads(event["content"])
            uninstalled.add(content["skill"])

        # Include skills from bundle installs
        for event in self.ledger.read_by_kind("bundle_install"):
            content = json.loads(event["content"])
            installed.update(content.get("skills", []))

        return sorted(installed - uninstalled)
        
    def get_skill_usage_stats(self) -> Dict[str, int]:
        """Get usage count per skill."""
        stats: Dict[str, int] = {}
        for event in self.ledger.read_by_kind("skill_use"):
            content = json.loads(event["content"])
            skill = content["skill"]
            stats[skill] = stats.get(skill, 0) + 1
        return stats
        
    def get_skill_feedback_stats(self) -> Dict[str, Dict[str, Any]]:
        """Get feedback stats per skill."""
        stats: Dict[str, Dict[str, Any]] = {}
        for event in self.ledger.read_by_kind("skill_feedback"):
            content = json.loads(event["content"])
            skill = content["skill"]
            rating = content["rating"]
            comment = content.get("comment", "")

            if skill not in stats:
                stats[skill] = {"ratings": [], "comments": []}

            stats[skill]["ratings"].append(rating)
            if comment:
                stats[skill]["comments"].append(comment)

        # Compute averages
        for skill in stats:
            ratings = stats[skill]["ratings"]
            stats[skill]["avg_rating"] = sum(ratings) / len(ratings) if ratings else 0
            stats[skill]["count"] = len(ratings)

        return stats

    def get_recommended_skills(
        self,
        domain_config: "DomainConfig"
    ) -> List[Dict[str, Any]]:
        """Get recommended skills for a domain."""
        recommended = domain_config._raw.get("recommended_skills", [])
        results: List[Dict[str, Any]] = []
        for name in recommended:
            skill = self.registry.get_skill(name)
            if skill is not None:
                results.append(skill)
        return results

    def get_bundles(self, domain_config: "DomainConfig") -> Dict[str, List[str]]:
        """Get skill bundles for a domain (from domain config legacy support)."""
        return domain_config._raw.get("skill_bundles", {})

    def install_bundle_by_name(
        self,
        bundle_name: str,
        domain_config: "DomainConfig",
        target: str = "claude-code"
    ) -> int:
        """Install a bundle by name.
        
        Prioritizes the new BundleManager, backscalls to domain config.
        """
        # Try new bundle manager first
        bundle = self.bundle_manager.get_bundle(bundle_name)
        if bundle:
            # Need to convert skills to Skill objects to list names?
            # get_bundle returns Bundle obj which has .skills (names)
            # But we might need to resolve dynamic selectors
            
            # NOTE: Getting all skills via registry to resolve dynamic
            # Incompat: registry returns dicts now
            # We need pure Skill objects for bundle resolution
            # registry.discovery.scan() is expensive? registry.load() returns cached list of Skill objects? 
            # Wait, registry.load() returns List[Skill]. registry.get_all_skills() returns List[Dict].
            
            # Let's use registry.discovery.scan()? Or modify registry to expose skills objects?
            # registry._skills holds Skill objects if loaded.
            
            # For efficiency, let's just trigger load() if needed
            self.registry.load()
            all_skills = self.registry._skills # Access protected member? 
            
            resolved = self.bundle_manager.resolve_bundle_skills(bundle_name, all_skills)
            skill_names = [s.name for s in resolved]
            
            # Auto-sync marketplace whenever we use/load bundles to keep it fresh?
            # Perhaps better done explicitly or on init.
            try:
                mp_path = self.registry.root_path / ".claude-plugin" / "marketplace.json"
                self.bundle_manager.sync_to_marketplace(mp_path, all_skills)
            except Exception:
                pass
            
            return self.install_bundle(
                bundle_name=bundle_name,
                skills=skill_names,
                domain=bundle.domain or domain_config.id,
                target=target
            )

        # Fallback to legacy domain config bundles
        bundles = self.get_bundles(domain_config)
        if bundle_name not in bundles:
            available = list(bundles.keys())
            raise ValueError(
                f"Bundle '{bundle_name}' not found. "
                f"Available: {', '.join(available)}"
            )

        skills = bundles[bundle_name]
        return self.install_bundle(
            bundle_name=bundle_name,
            skills=skills,
            domain=domain_config.id,
            target=target
        )
