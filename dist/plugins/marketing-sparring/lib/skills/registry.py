"""Skills registry."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional

from .discovery import SkillDiscovery
from .models import Skill


class SkillsRegistry:
    """Registry of available skills discoverable in the repository."""

    def __init__(self, root_path: Optional[Path] = None) -> None:
        """Initialize registry.

        Args:
            root_path: Repository root path (defaults to auto-detection)
        """
        if root_path is None:
            # Default to repo root assuming this file is in conversational-sparring/lib/skills/
            root_path = Path(__file__).parent.parent.parent.parent
            
        self.root_path = root_path
        self.discovery = SkillDiscovery(root_path)
        self._skills: List[Skill] = []
        self._loaded = False
        
        # Path for the cached index file (for Codex compatibility)
        self.index_path = root_path / ".codex" / "skills-index.json"

    def load(self, force_rescan: bool = False) -> List[Skill]:
        """Load skills from discovery.

        Args:
            force_rescan: Whether to force scanning the file system

        Returns:
            List of loaded skills
        """
        if self._loaded and not force_rescan:
            return self._skills
            
        # Perform fresh scan
        self._skills = self.discovery.scan()
        self._loaded = True
        
        # Auto-sync to Codex index when loading
        self.sync_codex_index()
        
        return self._skills
        
    def sync_codex_index(self) -> None:
        """Sync discovered skills to .codex/skills-index.json."""
        try:
            self.discovery.export_to_codex_index(self.index_path)
        except Exception:
            pass

    def get_all_skills(self) -> List[Dict[str, Any]]:
        """Return all available skills as dicts (compatibility mode).

        Returns:
            List of skill dictionaries
        """
        return [s.to_dict() for s in self.load()]

    def get_skill(self, name: str) -> Optional[Dict[str, Any]]:
        """Get skill by name (compatibility mode).

        Args:
            name: Skill name

        Returns:
            Skill dictionary or None if not found
        """
        for skill in self.load():
            if skill.name == name:
                return skill.to_dict()
        return None

    def get_by_category(self, category: str) -> List[Dict[str, Any]]:
        """Filter skills by category.

        Args:
            category: Category name

        Returns:
            List of skills in that category
        """
        return [
            s.to_dict() for s in self.load()
            if s.category == category
        ]

    def search(self, query: str) -> List[Dict[str, Any]]:
        """Search skills by keyword.

        Args:
            query: Search query

        Returns:
            List of matching skills
        """
        query_lower = query.lower()
        results = []
        for skill in self.load():
            if (query_lower in skill.name.lower() or
                query_lower in skill.description.lower() or
                query_lower in skill.category.lower()):
                results.append(skill.to_dict())
        return results

    def get_total_skills(self) -> int:
        """Get total number of skills."""
        return len(self.load())
