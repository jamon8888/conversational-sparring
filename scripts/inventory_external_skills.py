
import os
from pathlib import Path

def inventory_skills():
    PLUGINS_DIR = Path(r"C:\Users\NMarchitecte\Documents\claude-skills\plugins")
    
    if not PLUGINS_DIR.exists():
        print(f"Directory not found: {PLUGINS_DIR}")
        return

    print(f"Scanning {PLUGINS_DIR} for skills...\n")
    
    found_skills = {}
    
    for plugin_dir in PLUGINS_DIR.iterdir():
        if not plugin_dir.is_dir():
            continue
            
        skills_dir = plugin_dir / "skills"
        if skills_dir.exists() and skills_dir.is_dir():
            plugin_name = plugin_dir.name
            found_skills[plugin_name] = []
            
            for skill_dir in skills_dir.iterdir():
                if skill_dir.is_dir() and (skill_dir / "SKILL.md").exists():
                    found_skills[plugin_name].append(skill_dir.name)
    
    # Print results
    total_skills = 0
    for plugin, skills in sorted(found_skills.items()):
        if skills:
            print(f"[{plugin}]")
            for skill in sorted(skills):
                print(f"  - {skill}")
                total_skills += 1
            print()
            
    print(f"Total plugins scanned: {len(found_skills)}")
    print(f"Total valid skills found: {total_skills}")

if __name__ == "__main__":
    inventory_skills()
