#!/usr/bin/env python3
"""
Domain Plugin Generator

This script automates the creation of standalone Claude Code plugins for each domain
defined in `domains/`.

Usage:
    python scripts/generate_plugins.py [--clean] [--dist-dir DIR]
"""

import os
import sys
import yaml
import json
import shutil
import argparse
from pathlib import Path
from typing import Dict, List, Any

# Constants
DEFAULT_DIST_DIR = "dist/plugins"
COACH_DIR = "."  # Modified for standalone repo
SKILLS_DIR = "skills"

def load_yaml(path: Path) -> Dict[str, Any]:
    with open(path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def setup_plugin_structure(plugin_path: Path, coach_lib: Path):
    """Create basic plugin directory structure and copy core lib."""
    if plugin_path.exists():
        shutil.rmtree(plugin_path)
    
    plugin_path.mkdir(parents=True)
    
    # Create subdirectories
    (plugin_path / "config").mkdir()
    (plugin_path / "skills").mkdir()
    
    # Copy core library
    if coach_lib.exists():
        shutil.copytree(coach_lib, plugin_path / "lib")
    else:
        print(f"Warning: Library path {coach_lib} not found")

def copy_skills(plugin_skills_dir: Path, skill_names: List[str], repo_root: Path):
    """Copy requested skills into the plugin's skills directory."""
    
    # Map of skill name to its path in skills/
    # We scan the skills directory to find them
    skill_map = {}
    skills_root = repo_root / SKILLS_DIR
    
    if not skills_root.exists():
        print(f"Warning: Skills root {skills_root} not found")
        return

    for category_dir in skills_root.iterdir():
        if category_dir.is_dir():
            for skill_dir in category_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    skill_map[skill_dir.name] = skill_dir

    for skill_name in skill_names:
        if skill_name in skill_map:
            src = skill_map[skill_name]
            dst = plugin_skills_dir / skill_name
            # Copy specific skill
            shutil.copytree(src, dst)
            print(f"  + Included skill: {skill_name}")
        else:
            print(f"  ! Warning: Skill '{skill_name}' not found in library")

def patch_file_content(file_path: Path, changes: List[tuple]):
    """Apply text replacements to a file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for old, new in changes:
        if old in content:
            content = content.replace(old, new)
            modified = True
            
    if modified:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

def copy_and_patch_commands(plugin_path: Path, coach_root: Path):
    """Copy commands and patch imports for standalone structure."""
    src_cmds = coach_root / "commands"
    dst_cmds = plugin_path / "commands"
    
    if not src_cmds.exists():
        print("  ! Warning: No commands directory found")
        return

    shutil.copytree(src_cmds, dst_cmds)
    
    # Patch imports in all markdown files
    # Inrepo: sys.path.insert(0, 'conversational-sparring/lib')
    # Plugin: sys.path.insert(0, 'lib')
    for cmd_file in dst_cmds.glob("*.md"):
        patch_file_content(cmd_file, [
            ("conversational-sparring/lib", "lib"),
            ("conversational-coach/lib", "lib") # Safety catch
        ])
    print("  + Included commands")

def copy_and_patch_agents(plugin_path: Path, coach_root: Path, domain_id: str):
    """Copy domain agents and patch imports."""
    # Source: agents/<domain>/
    src_agents = coach_root / "agents" / domain_id
    # Dest: agents/
    dst_agents = plugin_path / "agents"
    
    if src_agents.exists() and src_agents.is_dir():
        shutil.copytree(src_agents, dst_agents)
        
        # Patch imports
        for agent_file in dst_agents.glob("*.md"):
            patch_file_content(agent_file, [
                ("conversational-sparring/lib", "lib"),
                ("../../skills/", "../skills/"), # Fix relative skill paths if needed
                ("conversational-coach/lib", "lib")
            ])
        print(f"  + Included agents for domain '{domain_id}'")
    else:
        # Fallback: Check if there are generic agents or just warn
        print(f"  ~ Note: No specific agents found for '{domain_id}'")

def generate_manifest(plugin_path: Path, domain_config: Dict[str, Any], domain_id: str):
    """Generate manifest.json for the plugin."""
    
    manifest = {
        "name": f"{domain_id}-sparring",
        "version": "1.0.0",
        "description": domain_config.get("domain", {}).get("description", f"Sparring partner for {domain_id}"),
        "commands": [
            {
                "name": "sparring",
                "description": "Start sparring session or manage goals",
                "usage": "/sparring [command]"
            }
        ],
        "permissions": ["filesystem"],
    }
    
    with open(plugin_path / "manifest.json", 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2)

def generate_readme(plugin_path: Path, domain_config: Dict[str, Any], domain_id: str):
    """Generate a specific README for the domain plugin."""
    
    name = domain_config.get("domain", {}).get("name", domain_id.title())
    desc = domain_config.get("domain", {}).get("description", "")
    
    content = f"""# {name} Sparring Partner

{desc}

## Overview
This is a specialized Claude Code plugin designed for the **{name}** domain.
It helps you track goals, detect patterns, and improve your workflow.

## Installation

```bash
/plugin install {domain_id}-sparring@claude-code-skills
```

## Features

- **Domain-Specific**: Optimized for {domain_id} workflows.
- **Goal Tracking**: Set and track {domain_id} goals.
- **Pattern Detection**: Identifies patterns like {', '.join(list(domain_config.get('patterns', {}).keys())[:3])}.

## Usage

```bash
/sparring goal "My new objective"
/sparring progress
```
"""
    with open(plugin_path / "README.md", 'w', encoding='utf-8') as f:
        f.write(content)

def main():
    parser = argparse.ArgumentParser(description="Generate domain plugins")
    parser.add_argument("--clean", action="store_true", help="Clean dist directory first")
    parser.add_argument("--dist-dir", default=DEFAULT_DIST_DIR, help="Output directory")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.resolve()
    coach_root = repo_root / COACH_DIR
    domains_dir = coach_root / "domains"
    dist_dir = repo_root / args.dist_dir
    
    if args.clean and dist_dir.exists():
        shutil.rmtree(dist_dir)
        
    dist_dir.mkdir(parents=True, exist_ok=True)
    
    print(f"Generating plugins in {dist_dir}...")
    
    # Iterate over domains
    for domain_file in domains_dir.glob("*.yaml"):
        if domain_file.name.startswith("_"):
            continue
            
        domain_id = domain_file.stem
        domain_config = load_yaml(domain_file)
        
        plugin_name = f"{domain_id}-sparring"
        plugin_path = dist_dir / plugin_name
        
        print(f"\\nBuilding plugin: {plugin_name}")
        
        # 1. Setup Structure & Copy Core Lib
        setup_plugin_structure(plugin_path, coach_root / "lib")
        
        # 2. Copy specific domain config
        shutil.copy(domain_file, plugin_path / "config/domain.yaml")
        
        # 3. Copy Commands (New)
        copy_and_patch_commands(plugin_path, coach_root)

        # 4. Copy Agents (New)
        copy_and_patch_agents(plugin_path, coach_root, domain_id)
        
        # 5. Bundle Skills
        skills_to_include = set()
        
        if "recommended_skills" in domain_config:
            skills_to_include.update(domain_config["recommended_skills"])
            
        if "skill_bundles" in domain_config:
            for bundle in domain_config["skill_bundles"].values():
                if isinstance(bundle, list):
                    skills_to_include.update(bundle)
                    
        if skills_to_include:
            print(f"  Bundling {len(skills_to_include)} skills...")
            copy_skills(plugin_path / "skills", list(skills_to_include), repo_root)
            
        # 6. Generate Metadata
        generate_manifest(plugin_path, domain_config, domain_id)
        generate_readme(plugin_path, domain_config, domain_id)
        
    print("\\nGeneration complete!")

if __name__ == "__main__":
    main()
