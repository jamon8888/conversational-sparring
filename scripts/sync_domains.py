#!/usr/bin/env python3
"""Domain and Skills synchronization script.

Automatically updates all documentation files when new domains, skills,
or plugins are added.

Usage:
    python scripts/sync_domains.py           # Show what would change
    python scripts/sync_domains.py --apply   # Apply changes
    python scripts/sync_domains.py --check   # Exit 1 if out of sync
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DOMAINS_DIR = PROJECT_ROOT / "domains"
SKILLS_DIR = PROJECT_ROOT / "skills"
AGENTS_DIR = PROJECT_ROOT / "agents"
DIST_DIR = PROJECT_ROOT / "dist" / "plugins"


def load_domains() -> List[Dict[str, str]]:
    """Load all domain configurations."""
    try:
        import yaml
    except ImportError:
        print("Error: PyYAML required. Install with: pip install pyyaml")
        sys.exit(1)
    
    domains = []
    for f in sorted(DOMAINS_DIR.glob("*.yaml")):
        if f.name.startswith("_"):
            continue
        
        with open(f, encoding="utf-8") as fp:
            config = yaml.safe_load(fp) or {}
        
        domain_info = config.get("domain", {})
        domains.append({
            "id": domain_info.get("id", f.stem),
            "name": domain_info.get("name", f.stem.title()),
            "description": domain_info.get("description", ""),
        })
    
    return domains


def count_skills() -> Tuple[int, Dict[str, int]]:
    """Count skills per category.
    
    Returns:
        Tuple of (total_count, {category: count})
    """
    total = 0
    by_category = {}
    
    if not SKILLS_DIR.exists():
        return 0, {}
    
    for category_dir in SKILLS_DIR.iterdir():
        if not category_dir.is_dir() or category_dir.name.startswith("."):
            continue
        
        skill_count = 0
        for skill_dir in category_dir.iterdir():
            if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                skill_count += 1
        
        if skill_count > 0:
            by_category[category_dir.name] = skill_count
            total += skill_count
    
    return total, by_category


def count_agents() -> int:
    """Count agent directories."""
    if not AGENTS_DIR.exists():
        return 0
    
    return sum(1 for d in AGENTS_DIR.iterdir() if d.is_dir() and not d.name.startswith("."))


def count_plugins() -> int:
    """Count generated plugins."""
    if not DIST_DIR.exists():
        return 0
    
    return sum(1 for d in DIST_DIR.iterdir() if d.is_dir())


def generate_domain_table(domains: List[Dict[str, str]]) -> str:
    """Generate markdown table of domains."""
    lines = [
        "| Domain | Focus |",
        "|--------|-------|",
    ]
    
    for d in domains:
        desc = d["description"][:50] + "..." if len(d["description"]) > 50 else d["description"]
        if not desc:
            desc = d["name"]
        lines.append(f"| `{d['id']}` | {desc} |")
    
    return "\n".join(lines)


def update_sparring_md(domains: List[Dict[str, str]], apply: bool) -> bool:
    """Update commands/sparring.md with current domains."""
    path = PROJECT_ROOT / "commands" / "sparring.md"
    if not path.exists():
        return False
    
    content = path.read_text(encoding="utf-8")
    original = content
    
    # Find and replace domain table
    table_pattern = r"(\*\*Available domains:\*\*\n)(\| Domain \| Focus \|\n\|[-|]+\|\n(?:\| .+\|\n)+)"
    new_table = generate_domain_table(domains) + "\n"
    
    if re.search(table_pattern, content):
        content = re.sub(table_pattern, r"\1" + new_table, content)
    
    if content != original:
        if apply:
            path.write_text(content, encoding="utf-8")
            print(f"✓ Updated {path.relative_to(PROJECT_ROOT)}")
        return True
    return False


def update_readme(domains: List[Dict[str, str]], skills_total: int, 
                  skills_by_cat: Dict[str, int], apply: bool) -> bool:
    """Update README.md with current stats."""
    path = PROJECT_ROOT / "README.md"
    if not path.exists():
        return False
    
    content = path.read_text(encoding="utf-8")
    original = content
    
    # Update domain count pattern: "X domains"
    content = re.sub(r"(\d+)\s+domains?(?=\b)", f"{len(domains)} domains", content)
    
    # Update skill count pattern: "X skills" or "X+ skills"
    content = re.sub(r"(\d+)\+?\s+skills?(?=\b)", f"{skills_total}+ skills", content)
    
    # Update category counts if present
    for cat, count in skills_by_cat.items():
        pattern = rf"({cat}[^:]*:\s*)(\d+)"
        content = re.sub(pattern, rf"\g<1>{count}", content, flags=re.IGNORECASE)
    
    if content != original:
        if apply:
            path.write_text(content, encoding="utf-8")
            print(f"✓ Updated {path.relative_to(PROJECT_ROOT)}")
        return True
    return False


def update_claude_md(domains: List[Dict[str, str]], skills_total: int,
                     agents_count: int, apply: bool) -> bool:
    """Update CLAUDE.md with current stats."""
    path = PROJECT_ROOT / "CLAUDE.md"
    if not path.exists():
        return False
    
    content = path.read_text(encoding="utf-8")
    original = content
    
    # Update domain count
    content = re.sub(r"(\d+)\s+domains?(?=\b)", f"{len(domains)} domains", content)
    
    # Update skill count
    content = re.sub(r"(\d+)\+?\s+skills?(?=\b)", f"{skills_total}+ skills", content)
    
    # Update agent count
    content = re.sub(r"(\d+)\s+agents?(?=\b)", f"{agents_count} agents", content)
    
    if content != original:
        if apply:
            path.write_text(content, encoding="utf-8")
            print(f"✓ Updated {path.relative_to(PROJECT_ROOT)}")
        return True
    return False


def generate_stats_summary(domains: List[Dict[str, str]], skills_total: int,
                           skills_by_cat: Dict[str, int], agents_count: int,
                           plugins_count: int) -> str:
    """Generate stats summary for display."""
    lines = [
        f"  Domains: {len(domains)}",
        f"  Skills: {skills_total}",
    ]
    
    for cat, count in sorted(skills_by_cat.items()):
        lines.append(f"    - {cat}: {count}")
    
    lines.append(f"  Agents: {agents_count}")
    lines.append(f"  Plugins: {plugins_count}")
    
    return "\n".join(lines)


def check_stale_references(domains: List[Dict[str, str]]) -> List[str]:
    """Check for domain references that don't exist."""
    warnings = []
    valid_ids = {d["id"] for d in domains}
    
    # Known legacy domains to flag
    legacy_domains = {"strategy", "growth", "developer", "business", "writer"}
    
    for md_file in PROJECT_ROOT.rglob("*.md"):
        # Skip legacy/backup directories
        file_path = str(md_file)
        if any(skip in file_path for skip in [".git", "dist", "test", "persistent-mind-model"]):
            continue
        
        try:
            content = md_file.read_text(encoding="utf-8")
        except Exception:
            continue
        
        # Find domain references
        refs = re.findall(r'--domain[=\s]+["\']?(\w[\w-]*)', content)
        refs += re.findall(r'domain["\']?\s*[=:]\s*["\']?(\w[\w-]*)', content)
        
        for ref in refs:
            if ref in legacy_domains and ref not in valid_ids:
                rel_path = md_file.relative_to(PROJECT_ROOT)
                warnings.append(f"{rel_path}: Legacy domain '{ref}'")
    
    return list(set(warnings))


def main():
    parser = argparse.ArgumentParser(description="Synchronize domain and skill references")
    parser.add_argument("--apply", action="store_true", help="Apply changes")
    parser.add_argument("--check", action="store_true", help="Exit 1 if out of sync")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show details")
    args = parser.parse_args()
    
    print("Domain & Skills Sync Tool")
    print("=" * 50)
    
    # Gather stats
    domains = load_domains()
    skills_total, skills_by_cat = count_skills()
    agents_count = count_agents()
    plugins_count = count_plugins()
    
    print(f"\n📊 Current Stats:")
    print(generate_stats_summary(domains, skills_total, skills_by_cat, 
                                  agents_count, plugins_count))
    
    if args.verbose:
        print(f"\n📁 Domains:")
        for d in domains:
            print(f"  - {d['id']}: {d['name']}")
    
    print("\n🔄 Checking files...")
    
    changes = []
    
    # Update files
    if update_sparring_md(domains, args.apply):
        changes.append("commands/sparring.md")
    
    if update_readme(domains, skills_total, skills_by_cat, args.apply):
        changes.append("README.md")
    
    if update_claude_md(domains, skills_total, agents_count, args.apply):
        changes.append("CLAUDE.md")
    
    # Check for stale references
    warnings = check_stale_references(domains)
    
    # Report
    print("\n" + "=" * 50)
    
    if changes:
        if args.apply:
            print(f"✅ Updated {len(changes)} file(s)")
        else:
            print(f"⚠️  {len(changes)} file(s) need updating:")
            for f in changes:
                print(f"    - {f}")
            print("\n    Run with --apply to update")
    else:
        print("✅ All files in sync")
    
    if warnings:
        print(f"\n⚠️  {len(warnings)} stale reference(s):")
        for w in warnings[:10]:  # Limit output
            print(f"    - {w}")
        if len(warnings) > 10:
            print(f"    ... and {len(warnings) - 10} more")
    
    # Exit code for CI
    if args.check and (changes or warnings):
        sys.exit(1)
    
    print()


if __name__ == "__main__":
    main()

