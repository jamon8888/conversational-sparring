"""Skill discovery and indexing."""

from __future__ import annotations

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .models import Skill

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None  # type: ignore
    HAS_YAML = False


class SkillDiscovery:
    """Discovers skills from the file system."""

    def __init__(self, root_path: Path) -> None:
        """Initialize discovery.

        Args:
            root_path: Repository root path containing 'skills' directory
        """
        self.root_path = root_path
        self.skills_path = root_path / "skills"

    def scan(self) -> List[Skill]:
        """Scan repository for skills.

        Returns:
            List of discovered Skill objects
        """
        if not self.skills_path.exists():
            return []

        skills: List[Skill] = []

        # Walk through the skills directory
        for root, _, files in os.walk(self.skills_path):
            if "SKILL.md" in files:
                skill_path = Path(root)
                skill = self._parse_skill(skill_path)
                if skill:
                    skills.append(skill)

        return skills

    def _parse_skill(self, skill_dir: Path) -> Optional[Skill]:
        """Parse a skill directory.

        Args:
            skill_dir: Path to skill directory containing SKILL.md

        Returns:
            Skill object or None if parsing fails
        """
        skill_file = skill_dir / "SKILL.md"
        
        try:
            content = skill_file.read_text(encoding="utf-8")
            frontmatter = self._extract_frontmatter(content)
            
            if not frontmatter:
                return None

            # Calculate path relative to repo root
            # Example: skills/marketing/content-creator
            try:
                rel_path = skill_dir.relative_to(self.root_path)
                source_path = str(rel_path).replace("\\", "/")
            except ValueError:
                # Fallback if path manipulation fails
                source_path = str(skill_dir)

            # Determine category from parent directory if not in metadata
            category = frontmatter.get("category")
            if not category:
                # Try to infer from path: skills/marketing/content-creator -> marketing
                try:
                    # rel_path is skills/marketing/content-creator
                    # parts: ('skills', 'marketing', 'content-creator')
                    parts = rel_path.parts
                    if len(parts) >= 3 and parts[0] == "skills":
                        category = parts[1]
                except Exception:
                    pass
            
            if not category:
                category = "other"

            # Filter known fields to keep metadata clean
            known_fields = {"name", "description", "category"}
            metadata = {k: v for k, v in frontmatter.items() if k not in known_fields}

            return Skill(
                name=frontmatter.get("name", skill_dir.name),
                category=category,
                source_path=source_path, # Fixed argument name
                description=frontmatter.get("description", ""),
                metadata=metadata
            )

        except Exception as e:
            # print(f"Error parsing skill at {skill_dir}: {e}")
            return None

    def _extract_frontmatter(self, content: str) -> Dict[str, Any]:
        """Extract YAML frontmatter from markdown content."""
        if not content.startswith("---"):
            return {}
        
        try:
            # Split on ---
            parts = content.split("---", 2)
            if len(parts) < 3:
                return {}
            
            yaml_content = parts[1]
            if HAS_YAML:
                return yaml.safe_load(yaml_content) or {}
            else:
                # Basic parser fallback if yaml not installed
                return self._basic_yaml_parse(yaml_content)
        except Exception:
            return {}

    def _basic_yaml_parse(self, content: str) -> Dict[str, Any]:
        """Very basic YAML parser for name/description/category."""
        result = {}
        for line in content.splitlines():
            line = line.strip()
            if ":" in line:
                key, value = line.split(":", 1)
                result[key.strip()] = value.strip().strip('"\'')
        return result

    def export_to_codex_index(self, output_path: Path) -> None:
        """Export discovered skills to a Codex-compatible index JSON.
        
        Args:
            output_path: Path to write skills-index.json
        """
        import json
        
        skills = self.scan()
        
        # Aggregate categories
        categories = {}
        for skill in skills:
            if skill.category not in categories:
                categories[skill.category] = {
                    "count": 0,
                    "source": str(Path(skill.source_path).parent).replace("\\", "/").replace("skills/", "../../skills/"), # Approximation
                    "description": f"{skill.category.title()} skills"
                }
            categories[skill.category]["count"] += 1

        index = {
            "version": "1.0.0",
            "name": "claude-code-skills",
            "description": "Auto-generated index from dynamic scan",
            "total_skills": len(skills),
            "skills": [s.to_dict() for s in skills],
            "categories": categories
        }
        
        # Ensure directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)
        
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(index, f, indent=2)
