#!/usr/bin/env python3
"""Agent files generator and updater.

Automatically generates and updates agent files based on domain configurations.
When domains/skills change, this script updates agent files accordingly.

Usage:
    python scripts/generate_agents.py              # Preview changes
    python scripts/generate_agents.py --apply      # Apply changes
    python scripts/generate_agents.py --create     # Create missing agent folders
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Any

try:
    import yaml
    HAS_YAML = True
except ImportError:
    yaml = None
    HAS_YAML = False

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DOMAINS_DIR = PROJECT_ROOT / "domains"
AGENTS_DIR = PROJECT_ROOT / "agents"
SKILLS_DIR = PROJECT_ROOT / "skills"

# Standard agent files
AGENT_TYPES = [
    ("sparring-mentor.md", "Mentor and guide for domain expertise"),
    ("sparring-reviewer.md", "Code and work reviewer"),
    ("sparring-planner.md", "Goal planning and strategy"),
    ("sparring-celebrator.md", "Celebrates wins and tracks progress"),
]


def load_domain_config(domain_path: Path) -> Optional[Dict[str, Any]]:
    """Load and parse domain YAML configuration."""
    if not HAS_YAML or yaml is None:
        return None
    
    try:
        with open(domain_path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    except Exception:
        return None


def get_domain_skills(config: Dict[str, Any]) -> List[str]:
    """Extract recommended skills from domain config."""
    skills = config.get("recommended_skills", [])
    return [s for s in skills if isinstance(s, str)]


def get_skill_path(skill_name: str) -> Optional[Path]:
    """Find the path to a skill in the skills directory."""
    if not SKILLS_DIR.exists():
        return None
    
    for category_dir in SKILLS_DIR.iterdir():
        if category_dir.is_dir():
            skill_dir = category_dir / skill_name
            if skill_dir.exists() and (skill_dir / "SKILL.md").exists():
                return skill_dir
    return None


def generate_skills_table(skills: List[str], domain_id: str) -> str:
    """Generate markdown table of available skills for an agent."""
    lines = ["| Need | Skill | Command |", "|------|-------|---------|"]
    
    # Map skills to categories and generate table rows
    skill_commands = {
        "content-creator": ("Content/SEO", "python ../../skills/{cat}/content-creator/scripts/seo_optimizer.py <file>"),
        "product-manager-toolkit": ("Prioritization", "python ../../skills/{cat}/product-manager-toolkit/scripts/rice_prioritizer.py <file>"),
        "marketing-demand-acquisition": ("Marketing", "ls ../../skills/{cat}/marketing-demand-acquisition/scripts/"),
        "aws-solution-architect": ("Infrastructure", "python ../../skills/{cat}/aws-solution-architect/scripts/generate_template.py"),
        "ceo-advisor": ("Strategy", "cat ../../skills/{cat}/ceo-advisor/SKILL.md"),
        "market-analyst": ("Research", "cat ../../skills/{cat}/market-analyst/SKILL.md"),
        "growth-analytics": ("Analytics", "cat ../../skills/{cat}/growth-analytics/SKILL.md"),
        "email-marketing": ("Email", "cat ../../skills/{cat}/email-marketing/SKILL.md"),
        "senior-fullstack": ("Development", "cat ../../skills/{cat}/senior-fullstack/SKILL.md"),
        "opportunity-scorer": ("Opportunities", "cat ../../skills/{cat}/opportunity-scorer/SKILL.md"),
        "lead-qualification": ("Sales", "cat ../../skills/{cat}/lead-qualification/SKILL.md"),
    }
    
    for skill in skills[:10]:  # Limit to top 10
        skill_path = get_skill_path(skill)
        if skill_path:
            category = skill_path.parent.name
            if skill in skill_commands:
                need, cmd_template = skill_commands[skill]
                cmd = cmd_template.replace("{cat}", category)
            else:
                need = skill.replace("-", " ").title()[:15]
                cmd = f"cat ../../skills/{category}/{skill}/SKILL.md"
            
            lines.append(f"| {need} | {skill} | `{cmd}` |")
    
    return "\n".join(lines)


def update_agent_skills_section(content: str, skills: List[str], domain_id: str) -> str:
    """Update the skills table section in an agent file."""
    new_table = generate_skills_table(skills, domain_id)
    
    # Pattern to find and replace skills table
    # Looking for: | Need | Skill | Command | followed by table rows
    pattern = r"(\| Need\s+\| Skill\s+\| Command\s+\|[\s\S]*?)(?=\n\n|\n###|\n##|\n\*\*Note)"
    
    if re.search(pattern, content):
        content = re.sub(pattern, new_table, content)
    
    return content


def update_agent_file(agent_path: Path, config: Dict[str, Any], apply: bool) -> bool:
    """Update an agent file with current domain skills."""
    if not agent_path.exists():
        return False
    
    content = agent_path.read_text(encoding="utf-8")
    original = content
    
    domain_info = config.get("domain", {})
    domain_id = domain_info.get("id", agent_path.parent.name)
    skills = get_domain_skills(config)
    
    if skills:
        content = update_agent_skills_section(content, skills, domain_id)
    
    if content != original:
        if apply:
            agent_path.write_text(content, encoding="utf-8")
            print(f"✓ Updated {agent_path.relative_to(PROJECT_ROOT)}")
        else:
            print(f"⚠️ Would update: {agent_path.relative_to(PROJECT_ROOT)}")
        return True
    
    return False


def create_agent_template(domain_id: str, domain_name: str, agent_type: str, description: str) -> str:
    """Generate a new agent file from template."""
    agent_name = agent_type.replace(".md", "").replace("sparring-", "").title()
    
    return f'''---
model: sonnet
description: {domain_name} {agent_name.lower()} agent
allowed-tools: Bash(python:*), Read, Glob
---

# {domain_name} {agent_name} Agent

You are a {agent_name.lower()} specialized in {domain_name.lower()} domain.

## Hybrid Identity (v5.1)

You operate in two primary cognitive modes based on user needs.

### 1. DECISION MODE

**Trigger**: "Should I?", "Is this worth?", "Which approach?"

- **Goal**: Clear, actionable recommendations
- **Posture**: Confident but open to context
- **Method**: Evaluate options against domain best practices

### 2. LEARNING MODE

**Trigger**: "How do I?", "Explain", "Why?"

- **Goal**: Knowledge transfer
- **Method**: Context-appropriate depth

## Dynamic Capabilities

You are extensible. Skills are in `../../skills/`.

**Discovery Protocol:**
1. Check available skills: `ls -F ../../skills/`
2. Read skill docs: `cat ../../skills/*/SKILL.md`
3. Execute scripts directly

## When to Activate

Trigger this agent for {domain_name.lower()}-related queries.

## Bundled Skills

| Need | Skill | Command |
|------|-------|---------|
| See skills | browse | `ls ../../skills/` |

## Key Phrases

- "Let me help you with that."
- "Based on {domain_name.lower()} best practices..."
- "Here's what I recommend."
'''


def create_missing_agents(apply: bool) -> int:
    """Create agent folders and files for domains without agents."""
    if not DOMAINS_DIR.exists():
        return 0
    
    created = 0
    
    for domain_file in DOMAINS_DIR.glob("*.yaml"):
        if domain_file.name.startswith("_"):
            continue
        
        config = load_domain_config(domain_file)
        if not config:
            continue
        
        domain_info = config.get("domain", {})
        domain_id = domain_info.get("id", domain_file.stem)
        domain_name = domain_info.get("name", domain_id.title())
        
        agent_dir = AGENTS_DIR / domain_id
        
        if not agent_dir.exists():
            if apply:
                agent_dir.mkdir(parents=True)
                print(f"✓ Created agent directory: agents/{domain_id}/")
            else:
                print(f"Would create: agents/{domain_id}/")
            created += 1
            
            # Create agent files
            for agent_type, desc in AGENT_TYPES:
                agent_path = agent_dir / agent_type
                if not agent_path.exists():
                    content = create_agent_template(domain_id, domain_name, agent_type, desc)
                    if apply:
                        agent_path.write_text(content, encoding="utf-8")
                        print(f"  ✓ Created {agent_type}")
    
    return created


def sync_all_agents(apply: bool) -> int:
    """Update all agent files with current domain skills."""
    updated = 0
    
    for domain_file in DOMAINS_DIR.glob("*.yaml"):
        if domain_file.name.startswith("_"):
            continue
        
        config = load_domain_config(domain_file)
        if not config:
            continue
        
        domain_info = config.get("domain", {})
        domain_id = domain_info.get("id", domain_file.stem)
        
        agent_dir = AGENTS_DIR / domain_id
        if not agent_dir.exists():
            continue
        
        for agent_file in agent_dir.glob("*.md"):
            if update_agent_file(agent_file, config, apply):
                updated += 1
    
    return updated


def main():
    parser = argparse.ArgumentParser(description="Generate and update agent files")
    parser.add_argument("--apply", action="store_true", help="Apply changes")
    parser.add_argument("--create", action="store_true", help="Create missing agent folders")
    args = parser.parse_args()
    
    print("Agent Generator & Updater")
    print("=" * 50)
    
    if not HAS_YAML:
        print("⚠️ PyYAML not installed. Install with: pip install pyyaml")
        sys.exit(1)
    
    if args.create:
        created = create_missing_agents(args.apply)
        print(f"\n{'Created' if args.apply else 'Would create'} {created} agent folder(s)")
    
    updated = sync_all_agents(args.apply)
    
    if updated:
        if args.apply:
            print(f"\n✅ Updated {updated} agent file(s)")
        else:
            print(f"\n⚠️ {updated} agent file(s) need updating")
            print("Run with --apply to update")
    else:
        print("\n✅ All agent files in sync")


if __name__ == "__main__":
    main()
