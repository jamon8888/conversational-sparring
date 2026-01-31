
import os
from pathlib import Path

def scaffold_agents():
    # Base path
    AGENTS_DIR = Path(r"C:\Users\NMarchitecte\Documents\claude-skills\conversational-sparring\agents")
    
    # New domains to create
    NEW_DOMAINS = [
        ("marketing-content", "Content Director"),
        ("marketing-growth", "Head of Growth"),
        ("marketing-pmm", "PMM Lead"),
        ("marketing-ops", "Marketing Ops Manager")
    ]
    
    TEMPLATE = """---
name: sparring-mentor
description: Your {role} for strategic sparring
---

# {role}

I am your AI sparring partner for {domain_id}. My goal is to challenge your thinking, not just execute tasks.

## Capabilities

I have access to specific skills in {domain_id}:
- **Mentorship**: I guidance on best practices.
- **Review**: I critique your work against professional standards.
- **Planning**: I help you structure your roadmap.

## How to Interact

> "Review this draft..."
> "Challenge my launch plan..."
> "Help me optimize this funnel..."

"""

    for domain_id, role in NEW_DOMAINS:
        domain_dir = AGENTS_DIR / domain_id
        domain_dir.mkdir(exist_ok=True)
        
        agent_file = domain_dir / "sparring-mentor.md"
        if not agent_file.exists():
            content = TEMPLATE.format(role=role, domain_id=domain_id)
            with open(agent_file, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"Created agent: {domain_id}/sparring-mentor.md")
        else:
            print(f"Agent exists: {domain_id}")

if __name__ == "__main__":
    scaffold_agents()
