"""Data models for skills system."""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class Skill:
    """Represents a single skill available in the system."""
    
    name: str
    category: str
    source_path: str  # Relative to repo root
    description: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for index/serialization."""
        return {
            "name": self.name,
            "category": self.category,
            "source": self.source_path,
            "description": self.description,
            **self.metadata
        }


@dataclass
class Bundle:
    """Represents a collection of skills."""
    
    name: str
    domain: str
    description: str
    skills: List[str]  # List of skill names
    selectors: List[Dict[str, Any]] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "name": self.name,
            "domain": self.domain,
            "description": self.description,
            "skills": self.skills,
            "selectors": self.selectors
        }
