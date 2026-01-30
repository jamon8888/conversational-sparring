"""Formatting utilities for skills and bundles."""

from typing import List, Dict, Any

def format_skill_list(skills: List[Dict[str, Any]], verbose: bool = False) -> str:
    """Format a list of skills for display.
    
    Args:
        skills: List of skill dictionaries
        verbose: If True, show full details
        
    Returns:
        Formatted string
    """
    if not skills:
        return "No skills found."
        
    lines = []
    
    if verbose:
        for skill in skills:
            lines.append(f"## {skill.get('name', 'Unknown')}")
            lines.append(f"_{skill.get('description', 'No description')}_")
            lines.append(f"Category: {skill.get('category', 'Uncategorized')}")
            lines.append("")
    else:
        for skill in skills:
            lines.append(f"- **{skill.get('name')}** [{skill.get('category')}]")
            
    return "\n".join(lines)

def format_bundle_list(bundles: Dict[str, List[str]], domain_name: str = "Domain") -> str:
    """Format a dictionary of bundles for display.
    
    Args:
        bundles: Dictionary mapping bundle name to list of skills
        domain_name: Name of the domain for header
        
    Returns:
        Formatted string
    """
    if not bundles:
        return "No bundles available."
        
    lines = [f"## {domain_name} Bundles", ""]
    
    for name, skill_list in bundles.items():
        skills_str = ", ".join(skill_list)
        lines.append(f"- **@{name}**: {skills_str}")
        
    return "\n".join(lines)
