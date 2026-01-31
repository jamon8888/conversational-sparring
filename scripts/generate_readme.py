#!/usr/bin/env python3
"""README and Plugin documentation generator.

Automatically generates skill listings and plugin documentation from the
actual skill directories.

Usage:
    python scripts/generate_readme.py              # Preview README updates
    python scripts/generate_readme.py --apply      # Apply changes
    python scripts/generate_readme.py --plugins    # Generate plugin READMEs
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None
    HAS_YAML = False

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
SKILLS_DIR = PROJECT_ROOT / "skills"
DOMAINS_DIR = PROJECT_ROOT / "domains"
DIST_DIR = PROJECT_ROOT / "dist" / "plugins"


def load_skill_info(skill_path: Path) -> Optional[Dict[str, str]]:
    """Load skill metadata from SKILL.md frontmatter."""
    skill_md = skill_path / "SKILL.md"
    if not skill_md.exists():
        return None
    
    content = skill_md.read_text(encoding="utf-8")
    
    # Extract YAML frontmatter
    if content.startswith("---"):
        end = content.find("---", 3)
        if end > 0:
            frontmatter = content[3:end].strip()
            if HAS_YAML and yaml:
                try:
                    meta = yaml.safe_load(frontmatter)
                    return {
                        "name": meta.get("name", skill_path.name),
                        "description": meta.get("description", ""),
                        "id": skill_path.name,
                    }
                except Exception:
                    pass
    
    # Fallback: extract from markdown
    name_match = re.search(r"^#\s+(.+)$", content, re.MULTILINE)
    name = name_match.group(1) if name_match else skill_path.name
    
    return {
        "name": name,
        "description": "",
        "id": skill_path.name,
    }


def get_all_skills() -> Dict[str, List[Dict[str, str]]]:
    """Get all skills organized by category.
    
    Returns:
        Dict mapping category name to list of skill info dicts
    """
    skills_by_category = {}
    
    if not SKILLS_DIR.exists():
        return {}
    
    for category_dir in sorted(SKILLS_DIR.iterdir()):
        if not category_dir.is_dir() or category_dir.name.startswith("."):
            continue
        
        skills = []
        for skill_dir in sorted(category_dir.iterdir()):
            if not skill_dir.is_dir():
                continue
            
            info = load_skill_info(skill_dir)
            if info:
                skills.append(info)
        
        if skills:
            skills_by_category[category_dir.name] = skills
    
    return skills_by_category


def generate_skills_summary() -> str:
    """Generate markdown summary of all skills."""
    skills = get_all_skills()
    
    lines = ["## 📚 Complete Skills Library", ""]
    
    total = sum(len(s) for s in skills.values())
    lines.append(f"**{total} skills** across {len(skills)} categories:")
    lines.append("")
    
    for category, skill_list in skills.items():
        # Format category name
        cat_name = category.replace("-", " ").title()
        lines.append(f"### {cat_name} ({len(skill_list)} skills)")
        lines.append("")
        lines.append("| Skill | Description |")
        lines.append("|-------|-------------|")
        
        for skill in skill_list:
            desc = skill["description"][:60] + "..." if len(skill["description"]) > 60 else skill["description"]
            lines.append(f"| `{skill['id']}` | {desc} |")
        
        lines.append("")
    
    return "\n".join(lines)


def generate_domain_plugins_list() -> str:
    """Generate list of available domain plugins."""
    if not DOMAINS_DIR.exists():
        return ""
    
    lines = ["## 🎯 Available Domain Plugins", ""]
    lines.append("| Domain | Focus | Install |")
    lines.append("|--------|-------|---------|")
    
    for domain_file in sorted(DOMAINS_DIR.glob("*.yaml")):
        if domain_file.name.startswith("_"):
            continue
        
        domain_id = domain_file.stem
        
        if HAS_YAML and yaml:
            with open(domain_file, encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
            
            info = config.get("domain", {})
            name = info.get("name", domain_id.title())
            desc = info.get("description", "")[:40]
        else:
            name = domain_id.title()
            desc = ""
        
        install_cmd = f"`/plugin install {domain_id}-sparring`"
        lines.append(f"| **{name}** | {desc} | {install_cmd} |")
    
    lines.append("")
    return "\n".join(lines)


def generate_plugin_readme(domain_id: str, skills: List[Dict[str, str]]) -> str:
    """Generate README for a specific plugin."""
    # Load domain config
    domain_name = domain_id.replace("-", " ").title()
    domain_desc = ""
    
    if HAS_YAML and yaml:
        domain_file = DOMAINS_DIR / f"{domain_id}.yaml"
        if domain_file.exists():
            with open(domain_file, encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
            info = config.get("domain", {})
            domain_name = info.get("name", domain_name)
            domain_desc = info.get("description", "")
    
    lines = [
        f"# {domain_name} Sparring Plugin",
        "",
        domain_desc if domain_desc else f"Conversational sparring partner for {domain_name}.",
        "",
        "## Installation",
        "",
        "```bash",
        f"/plugin install {domain_id}-sparring@conversational-sparring-marketplace",
        "```",
        "",
        f"## Included Skills ({len(skills)})",
        "",
        "| Skill | Description |",
        "|-------|-------------|",
    ]
    
    for skill in skills:
        desc = skill["description"][:50] + "..." if len(skill["description"]) > 50 else skill["description"]
        lines.append(f"| `{skill['id']}` | {desc} |")
    
    lines.extend([
        "",
        "## Commands",
        "",
        "```",
        f"/sparring --domain={domain_id} goal \"Your goal\"",
        "/sparring goals",
        "/sparring progress",
        "/sparring patterns",
        "```",
        "",
        "## Learn More",
        "",
        "[Main Repository](https://github.com/jamon8888/conversational-sparring)",
    ])
    
    return "\n".join(lines)


def update_main_readme(apply: bool) -> bool:
    """Update main README.md with skill and domain listings."""
    readme_path = PROJECT_ROOT / "README.md"
    if not readme_path.exists():
        print("README.md not found")
        return False
    
    content = readme_path.read_text(encoding="utf-8")
    original = content
    
    # Generate new skills section
    skills_summary = generate_skills_summary()
    
    # Find and replace skills section
    # Look for pattern: ## 📚 Detailed Plugin Capabilities ... (until next ## or end)
    skills_pattern = r"(## 📚 Detailed Plugin Capabilities.*?)(?=\n## [^#]|$)"
    
    if re.search(skills_pattern, content, re.DOTALL):
        # Replace with auto-generated content
        replacement = skills_summary.replace("## 📚 Complete Skills Library", "## 📚 Detailed Plugin Capabilities")
        content = re.sub(skills_pattern, replacement + "\n\n", content, flags=re.DOTALL)
    
    if content != original:
        if apply:
            readme_path.write_text(content, encoding="utf-8")
            print(f"✓ Updated README.md")
        return True
    
    print("README.md already up to date")
    return False


def generate_all_plugin_readmes(apply: bool) -> int:
    """Generate README for each plugin in dist/plugins/."""
    if not DIST_DIR.exists():
        print("No plugins directory found")
        return 0
    
    count = 0
    skills_by_cat = get_all_skills()
    
    for plugin_dir in DIST_DIR.iterdir():
        if not plugin_dir.is_dir():
            continue
        
        # Extract domain from plugin name (e.g., "marketing-sparring" -> "marketing")
        domain_id = plugin_dir.name.replace("-sparring", "")
        
        # Find matching skills
        matching_skills = []
        for cat, skill_list in skills_by_cat.items():
            if domain_id in cat or cat in domain_id:
                matching_skills.extend(skill_list)
        
        if not matching_skills:
            # Use all skills in category that matches
            for cat, skill_list in skills_by_cat.items():
                if domain_id.split("-")[0] == cat.split("-")[0]:
                    matching_skills.extend(skill_list)
        
        readme_content = generate_plugin_readme(domain_id, matching_skills)
        readme_path = plugin_dir / "README.md"
        
        if apply:
            readme_path.write_text(readme_content, encoding="utf-8")
            print(f"✓ Generated {readme_path.relative_to(PROJECT_ROOT)}")
        else:
            print(f"Would generate: {readme_path.relative_to(PROJECT_ROOT)}")
        
        count += 1
    
    return count


def main():
    parser = argparse.ArgumentParser(description="Generate README documentation")
    parser.add_argument("--apply", action="store_true", help="Apply changes")
    parser.add_argument("--plugins", action="store_true", help="Generate plugin READMEs")
    parser.add_argument("--list", action="store_true", help="List all skills")
    args = parser.parse_args()
    
    print("README Generator")
    print("=" * 50)
    
    if args.list:
        # Just list skills
        skills = get_all_skills()
        total = 0
        for cat, skill_list in skills.items():
            print(f"\n{cat.upper()} ({len(skill_list)} skills):")
            for s in skill_list:
                print(f"  - {s['id']}: {s['name']}")
            total += len(skill_list)
        print(f"\nTotal: {total} skills")
        return
    
    if args.plugins:
        count = generate_all_plugin_readmes(args.apply)
        print(f"\n{'Generated' if args.apply else 'Would generate'} {count} plugin READMEs")
    else:
        changed = update_main_readme(args.apply)
        if not args.apply and changed:
            print("\nRun with --apply to update")
    
    print()


if __name__ == "__main__":
    main()
