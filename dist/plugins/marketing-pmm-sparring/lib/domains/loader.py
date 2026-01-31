"""Domain configuration loader.

Loads domain configurations from YAML files with support for:
- Base configuration inheritance (_base.yaml)
- User custom domains (~/.claude/sparring/domains/)
- Built-in domains (conversational-sparring/domains/)
"""

from __future__ import annotations

from pathlib import Path
from typing import Any, Dict, List, Optional

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None  # type: ignore
    HAS_YAML = False


def _get_builtin_domains_path() -> Path:
    """Return path to built-in domains directory."""
    return Path(__file__).parent.parent.parent / "domains"


def _get_user_domains_path() -> Path:
    """Return path to user custom domains directory."""
    return Path.home() / ".claude" / "sparring" / "domains"


class DomainConfig:
    """Loaded domain configuration with all settings."""

    def __init__(self, config: Dict[str, Any]) -> None:
        """Initialize domain config from parsed YAML dict.

        Args:
            config: Parsed domain configuration dictionary
        """
        domain_info = config.get("domain", {})
        self.id: str = domain_info.get("id", "unknown")
        self.name: str = domain_info.get("name", "Unknown Domain")
        self.description: str = domain_info.get("description", "")

        self.categories: List[Dict[str, Any]] = config.get("categories", [])
        self.patterns: Dict[str, Dict[str, Any]] = config.get("patterns", {})
        self.impact_keywords: Dict[str, List[str]] = config.get("impact_keywords", {})
        self.struggle_indicators: Dict[str, List[str]] = config.get("struggle_indicators", {})
        self.thresholds: Dict[str, Any] = config.get("thresholds", {})
        self.messages: Dict[str, str] = config.get("messages", {})

        # Store raw config for extension
        self._raw = config

    def get_category_keywords(self) -> Dict[str, List[str]]:
        """Return mapping of category ID to keywords."""
        return {
            cat["id"]: cat.get("keywords", [])
            for cat in self.categories
        }

    def get_category_by_keywords(self, text: str) -> str:
        """Detect category from text based on keywords.

        Args:
            text: Text to analyze (e.g., goal description)

        Returns:
            Category ID, defaults to "other" if no match
        """
        text_lower = text.lower()
        for cat in self.categories:
            keywords = cat.get("keywords", [])
            if any(kw in text_lower for kw in keywords):
                return cat["id"]
        return "other"

    def get_category_names(self) -> Dict[str, str]:
        """Return mapping of category ID to display name."""
        return {
            cat["id"]: cat.get("name", cat["id"].title())
            for cat in self.categories
        }

    def get_valid_categories(self) -> List[str]:
        """Return list of valid category IDs."""
        return [cat["id"] for cat in self.categories]

    def get_threshold(self, key: str, default: Any = None) -> Any:
        """Get a threshold value with fallback.

        Args:
            key: Threshold key (e.g., "stalled_goal_days")
            default: Default value if not set

        Returns:
            Threshold value or default
        """
        return self.thresholds.get(key, default)

    def get_message(self, key: str, default: str = "") -> str:
        """Get a customized message with fallback.

        Args:
            key: Message key (e.g., "goal_created")
            default: Default message if not set

        Returns:
            Custom message or default
        """
        return self.messages.get(key, default)

    def get_pattern_definition(self, pattern_name: str) -> Optional[Dict[str, Any]]:
        """Get pattern definition by name.

        Args:
            pattern_name: Pattern identifier

        Returns:
            Pattern definition dict or None
        """
        return self.patterns.get(pattern_name)

    def compute_impact_score(self, text: str) -> int:
        """Compute impact score (1-10) based on keywords.

        Args:
            text: Text to analyze

        Returns:
            Impact score from 1 to 10
        """
        score = 5  # Base score
        text_lower = text.lower()

        # High impact keywords
        high_keywords = self.impact_keywords.get("high", [])
        for word in high_keywords:
            if word in text_lower:
                score += 2

        # Medium impact keywords
        medium_keywords = self.impact_keywords.get("medium", [])
        for word in medium_keywords:
            if word in text_lower:
                score += 1

        # Low impact keywords (reduce score)
        low_keywords = self.impact_keywords.get("low", [])
        for word in low_keywords:
            if word in text_lower:
                score -= 1

        return max(1, min(10, score))

    def detect_struggle_type(self, text: str) -> Optional[str]:
        """Detect struggle type from context text.

        Args:
            text: Context text to analyze

        Returns:
            Struggle type key or None
        """
        text_lower = text.lower()
        for struggle_type, indicators in self.struggle_indicators.items():
            if any(ind in text_lower for ind in indicators):
                return struggle_type
        return None


def load_domain(domain_id: str) -> DomainConfig:
    """Load domain configuration by ID.

    Search order:
    1. User custom domains (~/.claude/sparring/domains/)
    2. Built-in domains (conversational-sparring/domains/)

    Args:
        domain_id: Domain identifier (e.g., "business", "developer")

    Returns:
        Loaded DomainConfig

    Raises:
        ValueError: If domain not found
        ImportError: If PyYAML not installed
    """
    if not HAS_YAML:
        raise ImportError(
            "PyYAML is required for domain configuration. "
            "Install with: pip install pyyaml"
        )

    # Check user custom domains first
    custom_path = _get_user_domains_path() / f"{domain_id}.yaml"
    if custom_path.exists():
        return _load_from_path(custom_path)

    # Fall back to built-in domains
    builtin_path = _get_builtin_domains_path() / f"{domain_id}.yaml"
    if builtin_path.exists():
        return _load_from_path(builtin_path)

    # List available domains for helpful error
    available = list_available_domains()
    raise ValueError(
        f"Unknown domain: {domain_id}. "
        f"Available domains: {', '.join(available)}"
    )


def _load_from_path(path: Path) -> DomainConfig:
    """Load domain config from a file path.

    Automatically merges with _base.yaml if present.

    Args:
        path: Path to domain YAML file

    Returns:
        Loaded DomainConfig
    """
    # yaml is guaranteed to be available when this is called (checked in load_domain)
    assert yaml is not None, "PyYAML required"

    with open(path, encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    # Merge with base config if not loading base itself
    base_path = path.parent / "_base.yaml"
    if base_path.exists() and path.name != "_base.yaml":
        with open(base_path, encoding="utf-8") as f:
            base = yaml.safe_load(f) or {}
        config = _merge_configs(base, config)

    return DomainConfig(config)


def _merge_configs(base: Dict[str, Any], override: Dict[str, Any]) -> Dict[str, Any]:
    """Deep merge configs with override taking precedence.

    Args:
        base: Base configuration (from _base.yaml)
        override: Domain-specific configuration

    Returns:
        Merged configuration
    """
    result = base.copy()

    for key, value in override.items():
        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            # Deep merge dicts
            result[key] = _merge_configs(result[key], value)
        elif key in result and isinstance(result[key], list) and isinstance(value, list):
            # For lists (like categories), override completely
            result[key] = value
        else:
            result[key] = value

    return result


def list_available_domains() -> List[str]:
    """List all available domain IDs.

    Returns:
        List of domain IDs (sorted)
    """
    domains = set()

    # Check built-in domains
    builtin_path = _get_builtin_domains_path()
    if builtin_path.exists():
        for f in builtin_path.glob("*.yaml"):
            if f.name != "_base.yaml":
                domains.add(f.stem)

    # Check user custom domains
    user_path = _get_user_domains_path()
    if user_path.exists():
        for f in user_path.glob("*.yaml"):
            if f.name != "_base.yaml":
                domains.add(f.stem)

    return sorted(domains)


def get_default_domain() -> str:
    """Get the default domain ID.

    Returns:
        Default domain ID ("personal")
    """
    return "personal"


def domain_exists(domain_id: str) -> bool:
    """Check if a domain exists.

    Args:
        domain_id: Domain identifier to check

    Returns:
        True if domain exists
    """
    custom_path = _get_user_domains_path() / f"{domain_id}.yaml"
    builtin_path = _get_builtin_domains_path() / f"{domain_id}.yaml"
    return custom_path.exists() or builtin_path.exists()

