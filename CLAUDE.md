# CLAUDE.md

This file provides guidance to Claude Code when working with the Conversational Sparring plugin (v2.0.0).

## Project Overview

The Conversational Sparring Partner is a universal, domain-adaptive sparring plugin for Claude Code. It acts as a **Cognitive System** that tracks goals, detects behavioral patterns (Decision vs Learning modes), and orchestrates specialized domain agents.

**Core Philosophy**: Domain knowledge lives in YAML and Markdown; logic lives in Python.

## Architecture (v2.0.0)

```
Commands → Domain Config → Ledger (SQLite) → Mirror Projection
                                                 ↓
                                           Cognitive Router
                                           Pattern Detector
                                           Goal Manager
                                           MCP Bridge (Skill Tracking)
                                           Autonomy Kernel
```

## Key Files

| Component      | File                | Purpose                                            |
| -------------- | ------------------- | -------------------------------------------------- |
| **Ledger**     | `lib/ledger.py`     | Append-only event store with hash chaining         |
| **Mirror**     | `lib/mirror.py`     | Fast O(1) state projection (goals, stats)          |
| **Cognitive**  | `lib/cognitive.py`  | Detects Learning (Guide) vs Decision (Challenger)  |
| **Patterns**   | `lib/patterns.py`   | Detects behavioral patterns (e.g., stalling)       |
| **Feedback**   | `lib/feedback.py`   | Generates reflection prompts and status feedback   |
| **Metrics**    | `lib/metrics.py`    | Calculates streaks, completion rates, and insights |
| **MCP Bridge** | `lib/mcp_bridge.py` | Tracks usage of external MCP tools (e.g., Exa)     |
| **Autonomy**   | `lib/autonomy.py`   | Proactive interventions (Reflect, Celebrate)       |
| **Domains**    | `domains/*.yaml`    | Domain definitions (taxonomy, patterns, messages)  |

## Commands

```bash
/sparring                    # Dashboard
/sparring goal <desc>        # Set strategic objective
/sparring reflect            # Structured reflection session
/sparring patterns           # View detected behavioral patterns
/sparring domains            # List active domains
/plugin install <path>       # Install generated plugins
```

## Domain System - Virtual C-Suite

The system covers 10+ specialized domains, acting as a Virtual Executive Team:

| Domain               | Role           | Focus                                      |
| :------------------- | :------------- | :----------------------------------------- |
| `strategy`           | CEO            | Vision, Fundraising, Board Decisions       |
| `marketing-growth`   | Head of Growth | Acquisition, SEO, Experiments, Viral Loops |
| `marketing-content`  | Content Dir.   | specialized Brand Voice, Storytelling      |
| `marketing-pmm`      | PMM Lead       | Launches, Positioning, Sales Enablement    |
| `marketing-ops`      | MOps Mgr       | Automation, Attribution, CRM Hygiene       |
| `strategic-research` | CSO            | Deep Search (Exa), Market Analysis         |
| `engineering`        | CTO            | Architecture, Code Quality, Shipping       |
| `product`            | CPO            | Roadmap, User Research                     |
| `sales`              | CRO            | Pipeline, Closing                          |
| `operations`         | COO            | Systems, Legal/Finance                     |
| `people`             | CHRO           | Hiring, Culture                            |

### Agent Structure (Standardized)

Every domain includes 4 standard agents:

1.  **Mentor**: Strategic advisor (Decision/Learning modes).
2.  **Planner**: Goal setting and roadmap architect.
3.  **Reviewer**: Critic for assets and plans.
4.  **Celebrator**: Recognition of milestones.

**Discovery Protocol**: Agents are trained to check `../../skills/` and use `ls` to find tools.

## Event Types (v2.0)

```python
EVENT_KINDS = [
    "goal_open", "goal_close", "goal_abandon",
    "reflection", "struggle", "intervention",
    "cognitive_mode_switch",    # Learning vs Decision
    "pattern_detected",         # Behavioral pattern
    "skill_use",                # Tool usage (via MCP Bridge)
    "achievement",              # Milestone reached
    "session_start", "session_end"
]
```

## Development Workflow

### 1. Generating Plugins

Use the generator to build standalone plugins from the source components:

```bash
python scripts/generate_plugins.py --clean
python scripts/package_skills.py
```

Artifacts are output to `dist/plugins/`.

### 2. Testing

```bash
pytest tests/
```

### 3. Adding Skills

- Place new skill in `skills/<category>/<skill-name>/SKILL.md`.
- Register in `domains/<domain>.yaml` under `recommended_skills`.
- Regenerate.

## Code Modification Rules

1.  **Determinism**: State must be rebuildable from `ledger.read_all()`.
2.  **No Hardcoded Logic**: Domain rules go in YAML.
3.  **Hash Integrity**: Never modify past ledger entries.

## Recent Updates (Jan 2026)

- **Marketing Split**: Decomposed into 4 personas (Content, Growth, PMM, Ops).
- **Exa/Deep Search**: Integrated `exa-search-expert` into Strategic Research.
- **Cognitive Router**: System automatically detects user intent.
- **MCP Bridge**: External tool usage is now tracked in the specific skill ledger.
