"""Domain configuration system for the Conversational Sparring Partner

This module provides domain-agnostic sparring by loading configuration
from YAML files. No hardcoded ontology - domain knowledge exists only
in configuration files.
"""

from .loader import (
    DomainConfig,
    load_domain,
    list_available_domains,
    get_default_domain,
    domain_exists,
)
from .schemas import validate_domain_config

__all__ = [
    "DomainConfig",
    "load_domain",
    "list_available_domains",
    "get_default_domain",
    "domain_exists",
    "validate_domain_config",
]

