"""Domain configuration validation schemas.

Provides validation for domain YAML files to catch configuration errors early.
"""

from __future__ import annotations

from typing import Any, Dict, List, Tuple


# Required fields for domain config
REQUIRED_DOMAIN_FIELDS = ["id", "name"]

# Valid severity levels for patterns
VALID_SEVERITIES = ["info", "warning", "concern"]

# Valid impact levels
VALID_IMPACT_LEVELS = ["high", "medium", "low"]


class ValidationError(Exception):
    """Domain configuration validation error."""

    def __init__(self, message: str, path: str = "") -> None:
        self.message = message
        self.path = path
        super().__init__(f"{path}: {message}" if path else message)


def validate_domain_config(config: Dict[str, Any]) -> List[ValidationError]:
    """Validate a domain configuration dictionary.

    Args:
        config: Parsed domain configuration

    Returns:
        List of validation errors (empty if valid)
    """
    errors: List[ValidationError] = []

    # Validate domain section
    domain_errors = _validate_domain_section(config.get("domain", {}))
    errors.extend(domain_errors)

    # Validate categories
    category_errors = _validate_categories(config.get("categories", []))
    errors.extend(category_errors)

    # Validate patterns
    pattern_errors = _validate_patterns(config.get("patterns", {}))
    errors.extend(pattern_errors)

    # Validate impact keywords
    impact_errors = _validate_impact_keywords(config.get("impact_keywords", {}))
    errors.extend(impact_errors)

    # Validate thresholds
    threshold_errors = _validate_thresholds(config.get("thresholds", {}))
    errors.extend(threshold_errors)

    return errors


def _validate_domain_section(domain: Dict[str, Any]) -> List[ValidationError]:
    """Validate the domain info section."""
    errors = []

    if not domain:
        errors.append(ValidationError("Missing 'domain' section", "domain"))
        return errors

    for field in REQUIRED_DOMAIN_FIELDS:
        if field not in domain:
            errors.append(ValidationError(f"Missing required field '{field}'", f"domain.{field}"))
        elif not isinstance(domain[field], str):
            errors.append(ValidationError(f"Field '{field}' must be a string", f"domain.{field}"))
        elif not domain[field].strip():
            errors.append(ValidationError(f"Field '{field}' cannot be empty", f"domain.{field}"))

    # Validate ID format (lowercase, alphanumeric, hyphens)
    domain_id = domain.get("id", "")
    if domain_id and not all(c.isalnum() or c in "-_" for c in domain_id):
        errors.append(ValidationError(
            "Domain ID must be alphanumeric with hyphens/underscores only",
            "domain.id"
        ))

    return errors


def _validate_categories(categories: List[Any]) -> List[ValidationError]:
    """Validate the categories section."""
    errors = []

    if not isinstance(categories, list):
        errors.append(ValidationError("Categories must be a list", "categories"))
        return errors

    seen_ids = set()
    for i, cat in enumerate(categories):
        path = f"categories[{i}]"

        if not isinstance(cat, dict):
            errors.append(ValidationError("Category must be an object", path))
            continue

        # Required: id
        if "id" not in cat:
            errors.append(ValidationError("Category missing 'id'", path))
        else:
            cat_id = cat["id"]
            if not isinstance(cat_id, str):
                errors.append(ValidationError("Category 'id' must be a string", f"{path}.id"))
            elif cat_id in seen_ids:
                errors.append(ValidationError(f"Duplicate category ID: {cat_id}", f"{path}.id"))
            else:
                seen_ids.add(cat_id)

        # Required: name
        if "name" not in cat:
            errors.append(ValidationError("Category missing 'name'", path))

        # Optional: keywords (must be list of strings)
        keywords = cat.get("keywords", [])
        if not isinstance(keywords, list):
            errors.append(ValidationError("Category 'keywords' must be a list", f"{path}.keywords"))
        elif not all(isinstance(k, str) for k in keywords):
            errors.append(ValidationError("All keywords must be strings", f"{path}.keywords"))

    return errors


def _validate_patterns(patterns: Dict[str, Any]) -> List[ValidationError]:
    """Validate the patterns section."""
    errors = []

    if not isinstance(patterns, dict):
        errors.append(ValidationError("Patterns must be an object", "patterns"))
        return errors

    for name, definition in patterns.items():
        path = f"patterns.{name}"

        if not isinstance(definition, dict):
            errors.append(ValidationError("Pattern definition must be an object", path))
            continue

        # Validate severity if present
        severity = definition.get("severity")
        if severity is not None and severity not in VALID_SEVERITIES:
            errors.append(ValidationError(
                f"Invalid severity '{severity}'. Must be one of: {VALID_SEVERITIES}",
                f"{path}.severity"
            ))

        # Validate threshold if present
        threshold = definition.get("severity_threshold")
        if threshold is not None:
            if not isinstance(threshold, (int, float)):
                errors.append(ValidationError(
                    "severity_threshold must be a number",
                    f"{path}.severity_threshold"
                ))
            elif threshold < 0:
                errors.append(ValidationError(
                    "severity_threshold must be non-negative",
                    f"{path}.severity_threshold"
                ))

        # Suggestion should be a string
        suggestion = definition.get("suggestion")
        if suggestion is not None and not isinstance(suggestion, str):
            errors.append(ValidationError(
                "Pattern 'suggestion' must be a string",
                f"{path}.suggestion"
            ))

    return errors


def _validate_impact_keywords(impact: Dict[str, Any]) -> List[ValidationError]:
    """Validate the impact_keywords section."""
    errors = []

    if not isinstance(impact, dict):
        errors.append(ValidationError("impact_keywords must be an object", "impact_keywords"))
        return errors

    for level in impact:
        if level not in VALID_IMPACT_LEVELS:
            errors.append(ValidationError(
                f"Invalid impact level '{level}'. Must be one of: {VALID_IMPACT_LEVELS}",
                f"impact_keywords.{level}"
            ))
            continue

        keywords = impact[level]
        if not isinstance(keywords, list):
            errors.append(ValidationError(
                "Impact keywords must be a list",
                f"impact_keywords.{level}"
            ))
        elif not all(isinstance(k, str) for k in keywords):
            errors.append(ValidationError(
                "All impact keywords must be strings",
                f"impact_keywords.{level}"
            ))

    return errors


def _validate_thresholds(thresholds: Dict[str, Any]) -> List[ValidationError]:
    """Validate the thresholds section."""
    errors = []

    if not isinstance(thresholds, dict):
        errors.append(ValidationError("thresholds must be an object", "thresholds"))
        return errors

    # Known numeric thresholds
    numeric_keys = [
        "stalled_goal_days",
        "quick_win_days",
        "max_open_goals",
    ]

    for key in numeric_keys:
        if key in thresholds:
            value = thresholds[key]
            if not isinstance(value, (int, float)):
                errors.append(ValidationError(
                    f"Threshold '{key}' must be a number",
                    f"thresholds.{key}"
                ))
            elif value < 0:
                errors.append(ValidationError(
                    f"Threshold '{key}' must be non-negative",
                    f"thresholds.{key}"
                ))

    # Validate reflection_cadence if present
    cadence = thresholds.get("reflection_cadence")
    valid_cadences = ["daily", "weekly", "biweekly", "monthly", "per-task"]
    if cadence is not None and cadence not in valid_cadences:
        errors.append(ValidationError(
            f"Invalid reflection_cadence '{cadence}'. Must be one of: {valid_cadences}",
            "thresholds.reflection_cadence"
        ))

    return errors


def is_valid_config(config: Dict[str, Any]) -> Tuple[bool, List[str]]:
    """Check if config is valid and return error messages.

    Args:
        config: Domain configuration to validate

    Returns:
        Tuple of (is_valid, list of error messages)
    """
    errors = validate_domain_config(config)
    return (len(errors) == 0, [str(e) for e in errors])

