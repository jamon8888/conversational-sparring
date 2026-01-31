---
description: Browse, install, and manage skills from the Claude Code marketplace
allowed-tools: Bash(python:*), Read, Glob, Grep
---

# /skills - Claude Code Skills Marketplace

You help users browse, install, and manage skills from the claude-skills repository. This command integrates with the sparring system to track skill usage and provide domain-specific recommendations.

## Usage

```
/skills                          # List recommended skills for current domain
/skills list                     # List all available skills
/skills list --category marketing
/skills search "SEO content"
/skills info <skill-name>        # Show skill details
/skills install <skill-name>     # Install a skill
/skills install @<domain>/<bundle>  # Install a persona bundle
/skills installed                # Show installed skills
/skills usage                    # Show skill usage stats
/skills bundles                  # Show bundles for current domain
```

## Persona Bundles

Bundles provide curated skill sets for specific roles:

### CEO/C-Level Bundles (`@c-level/*`)

| Bundle              | Skills                                                  | Use Case          |
| ------------------- | ------------------------------------------------------- | ----------------- |
| `@c-level/starter`  | ceo-advisor                                             | Getting started   |
| `@c-level/growth`   | ceo-advisor, product-strategist, marketing-strategy-pmm | Scaling company   |
| `@c-level/complete` | Full suite                                              | Executive toolkit |

### CTO/Engineering Bundles (`@engineering/*`)

| Bundle                  | Skills                                | Use Case                  |
| ----------------------- | ------------------------------------- | ------------------------- |
| `@engineering/starter`  | cto-advisor, senior-architect         | Getting started           |
| `@engineering/scaling`  | + senior-devops, tech-stack-evaluator | Scaling team              |
| `@engineering/complete` | + tdd-guide, senior-security          | Full technical leadership |

### CPO/Product Bundles (`@product/*`)

| Bundle               | Skills                                          | Use Case            |
| -------------------- | ----------------------------------------------- | ------------------- |
| `@product/starter`   | product-manager-toolkit, product-strategist     | Getting started     |
| `@product/discovery` | product-manager-toolkit, ux-researcher-designer | User research focus |
| `@product/complete`  | Full product suite                              | Product leadership  |

### CMO/Marketing Bundles (`@marketing/*`)

| Bundle                | Skills                                                | Use Case             |
| --------------------- | ----------------------------------------------------- | -------------------- |
| `@marketing/starter`  | content-creator, marketing-strategy-pmm               | Getting started      |
| `@marketing/demand`   | + marketing-demand-acquisition, social-media-analyzer | Demand gen           |
| `@marketing/complete` | Full marketing suite                                  | Marketing leadership |

### CRO/Sales Bundles (`@sales/*`)

| Bundle            | Skills                                               | Use Case           |
| ----------------- | ---------------------------------------------------- | ------------------ |
| `@sales/starter`  | marketing-demand-acquisition, marketing-strategy-pmm | Getting started    |
| `@sales/pipeline` | marketing-demand-acquisition, content-creator        | Pipeline building  |
| `@sales/complete` | Full sales suite                                     | Revenue leadership |

### COO/Operations Bundles (`@operations/*`)

| Bundle                  | Skills                           | Use Case              |
| ----------------------- | -------------------------------- | --------------------- |
| `@operations/starter`   | senior-pm, scrum-master          | Getting started       |
| `@operations/atlassian` | + jira-expert, confluence-expert | Atlassian stack       |
| `@operations/complete`  | Full operations suite            | Operations leadership |

### CHRO/People Bundles (`@people/*`)

| Bundle             | Skills                          | Use Case          |
| ------------------ | ------------------------------- | ----------------- |
| `@people/starter`  | ceo-advisor                     | Getting started   |
| `@people/culture`  | ceo-advisor, product-strategist | Culture building  |
| `@people/complete` | Full people suite               | People leadership |

### Solopreneur Bundles (`@solopreneur/*`)

| Bundle                       | Skills                                                               | Use Case                  |
| ---------------------------- | -------------------------------------------------------------------- | ------------------------- |
| `@solopreneur/mvp-builder`   | senior-fullstack, product-manager-toolkit                            | Build your MVP            |
| `@solopreneur/growth-hacker` | content-creator, marketing-demand-acquisition, social-media-analyzer | Marketing & growth        |
| `@solopreneur/indie-saas`    | fullstack, product, content, aws                                     | Full SaaS founder toolkit |
| `@solopreneur/complete`      | Everything                                                           | One-person startup        |

## Implementation

When running `/skills`, use the following Python code:

```python
import sys
sys.path.insert(0, 'conversational-sparring/lib')
from skills import SkillsRegistry, SkillsManager, format_skill_list, format_bundle_list
from ledger import SparringLedger
from domains.loader import load_domain

# Initialize
ledger = SparringLedger()
registry = SkillsRegistry()
manager = SkillsManager(ledger, registry)

# Get current domain
domain_id = ledger.get_current_domain() or "personal"
domain = load_domain(domain_id)

# List skills
skills = registry.get_all_skills()
print(f"Total skills: {len(skills)}")

# Get recommended for domain
recommended = manager.get_recommended_skills(domain)
print(f"Recommended for {domain.name}: {[s['name'] for s in recommended]}")

# Get bundles for domain
bundles = manager.get_bundles(domain)
print(f"Available bundles: {list(bundles.keys())}")

# Install a skill
manager.install_skill("ceo-advisor")

# Install a bundle
manager.install_bundle_by_name("starter", domain)

# Check installed
installed = manager.get_installed_skills()
print(f"Installed: {installed}")

# Record usage
manager.record_usage("ceo-advisor", "Strategic planning session")

# Get usage stats
stats = manager.get_skill_usage_stats()
print(f"Usage stats: {stats}")
```

## Integration with Sparring

Skills integrate with your sparring workflow:

- Goals can reference skills used
- Pattern detection tracks skill adoption
- Metrics include skill usage
- Domain-specific recommendations based on your role

## Examples

### CEO Starting Out

```bash
/sparring --domain=c-level
/skills install @c-level/starter
/sparring goal "Prepare board deck for Q1"
```

### Solopreneur Building MVP

```bash
/sparring --domain=solopreneur
/skills install @solopreneur/mvp-builder
/sparring goal "Launch beta by end of month"
```

### CTO Scaling Team

```bash
/sparring --domain=engineering
/skills bundles
/skills install @engineering/scaling
/sparring goal "Implement CI/CD pipeline"
```

## Output Formats

### `/skills list`

```
## Available Skills (42 total)

### c-level (2)
- **ceo-advisor**: Executive leadership guidance...
- **cto-advisor**: Technical leadership guidance...

### engineering (18)
- **senior-architect**: System design and architecture...
- **senior-fullstack**: Full-stack development...
...

### marketing (5)
- **content-creator**: SEO-optimized content...
...
```

### `/skills installed`

```
## Installed Skills (5)

- ceo-advisor [c-level] - installed 2 days ago
- product-strategist [product] - installed 2 days ago
- senior-architect [engineering] - installed 1 day ago

Usage Stats:
- ceo-advisor: 12 uses
- product-strategist: 5 uses
- senior-architect: 3 uses
```

### `/skills bundles`

```
## C-Level Bundles

### @c-level/starter
Skills: ceo-advisor

### @c-level/growth
Skills: ceo-advisor, product-strategist, marketing-strategy-pmm

### @c-level/complete
Skills: ceo-advisor, product-strategist, senior-architect, marketing-strategy-pmm, risk-management-specialist
```
