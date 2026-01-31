"""MCP to Skill Usage Bridge.

This module provides a bridge between MCP tool calls and skill usage tracking.
Until full MCP middleware integration, this can be called manually to record
tool usage.
"""

from __future__ import annotations

import json
from datetime import datetime, timezone
from typing import Any, Dict, Optional

from .ledger import SparringLedger


# MCP tool name to skill ID mapping
MCP_SKILL_MAPPING = {
    # Exa.ai tools
    "exa_search": "exa-search-expert",
    "exa_find_similar": "exa-search-expert",
    "exa_get_contents": "exa-search-expert",

    # Add other MCP tools as they become available
    # "tavily_search": "tavily-search-expert",
    # "perplexity_search": "perplexity-expert",
}


def record_mcp_tool_use(
    ledger: SparringLedger,
    tool_name: str,
    args: Optional[Dict[str, Any]] = None,
    result: Optional[Any] = None,
    domain: Optional[str] = None,
    goal_id: Optional[str] = None,
) -> bool:
    """Record MCP tool usage as a skill_use event.

    Args:
        ledger: The sparring ledger
        tool_name: MCP tool name (e.g., "exa_search")
        args: Tool arguments
        result: Tool result (optional)
        domain: Current domain (optional)
        goal_id: Related goal ID (optional)

    Returns:
        True if skill_use event was created, False if tool not mapped
    """
    # Check if tool is mapped to a skill
    if tool_name not in MCP_SKILL_MAPPING:
        return False

    skill_id = MCP_SKILL_MAPPING[tool_name]

    # Prepare event data
    content_data = {
        "skill": skill_id,
        "tool": tool_name,
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }

    meta_data = {
        "skill": skill_id,
        "tool": tool_name,
        "success": result is not None,
    }

    # Add optional fields
    if args:
        # Store a summary of args (not full content to avoid bloat)
        if "query" in args:
            content_data["query"] = args["query"]
            meta_data["query"] = args["query"][:100]  # Truncate

    if domain:
        content_data["domain"] = domain
        meta_data["domain"] = domain

    if goal_id:
        content_data["goal_id"] = goal_id
        meta_data["goal_id"] = goal_id

    # Append to ledger
    ledger.append(
        kind="skill_use",
        content=json.dumps(content_data, sort_keys=True),
        meta=meta_data,
    )

    return True


def get_mcp_skill_mapping() -> Dict[str, str]:
    """Get the current MCP tool to skill mapping.

    Returns:
        Dictionary mapping MCP tool names to skill IDs
    """
    return MCP_SKILL_MAPPING.copy()


def add_mcp_skill_mapping(tool_name: str, skill_id: str) -> None:
    """Add a new MCP tool to skill mapping.

    Args:
        tool_name: MCP tool name
        skill_id: Corresponding skill ID
    """
    MCP_SKILL_MAPPING[tool_name] = skill_id


# Convenience function for common tools
def record_exa_search(
    ledger: SparringLedger,
    query: str,
    num_results: Optional[int] = None,
    domain: Optional[str] = None,
    goal_id: Optional[str] = None,
) -> None:
    """Record Exa.ai search usage.

    Args:
        ledger: The sparring ledger
        query: Search query
        num_results: Number of results returned (optional)
        domain: Current domain (optional)
        goal_id: Related goal ID (optional)
    """
    args = {"query": query}
    if num_results is not None:
        args["num_results"] = num_results

    record_mcp_tool_use(
        ledger=ledger,
        tool_name="exa_search",
        args=args,
        result={"count": num_results} if num_results else None,
        domain=domain,
        goal_id=goal_id,
    )
