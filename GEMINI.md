# GEMINI.md - Conversational Sparring

## Quick Reference

| Action                | Command                                               |
| --------------------- | ----------------------------------------------------- |
| Sync domains          | `python scripts/sync_domains.py --apply`              |
| Check sync            | `python scripts/sync_domains.py --check`              |
| List skills           | `python scripts/generate_readme.py --list`            |
| Update README         | `python scripts/generate_readme.py --apply`           |
| Gen plugin READMEs    | `python scripts/generate_readme.py --plugins --apply` |
| Generate plugins      | `python scripts/generate_plugins.py`                  |
| Generate agents       | `python scripts/generate_agents.py --apply`           |
| Create missing agents | `python scripts/generate_agents.py --create --apply`  |
| Validate skills       | `python scripts/validate_skills.py`                   |
| Run tests             | `python -m pytest tests/ -v`                          |

## Architecture

```
conversational-sparring/
├── domains/           # YAML domain configs (15)
├── skills/            # Skill packages (135)
├── agents/            # Agent definitions (14)
├── commands/          # Slash command handlers
├── lib/               # Core library (ledger, mirror, goals)
├── scripts/           # Automation scripts
│   ├── sync_domains.py       # Domain sync automation
│   └── generate_plugins.py   # Plugin generator
└── dist/plugins/      # Generated plugins (15)
```

## Automation Workflow

**When adding new domain/plugin:**

1. Create `domains/<id>.yaml`
2. Run: `python scripts/sync_domains.py --apply`
3. Run: `python scripts/validate_skills.py`
4. Run: `python scripts/generate_readme.py --apply`
5. Run: `python scripts/generate_agents.py --create --apply`
6. Run: `python scripts/generate_plugins.py`
7. Test: `pytest tests/test_domains.py -v`

Use workflow: `/domain-plugin`

**Files auto-updated by scripts:**

- `commands/sparring.md` - domain table (sync_domains)
- `README.md` - domain/skill counts (sync_domains, generate_readme)
- `CLAUDE.md` - domain/skill/agent counts (sync_domains)
- `agents/*/` - agent files with skill refs (generate_agents)

## Domain Reference

| Current          | Legacy (don't use) |
| ---------------- | ------------------ |
| c-level          | strategy           |
| marketing-growth | growth             |
| personal         | business           |

## Key Scripts

### sync_domains.py

Updates all files when domains change:

- `commands/sparring.md` - domain table
- `README.md` - counts
- `CLAUDE.md` - counts

### generate_plugins.py

Creates standalone plugins from domain configs.

## Core Modules (`lib/`)

| Module          | Purpose                               |
| --------------- | ------------------------------------- |
| `ledger.py`     | Append-only SQLite event store        |
| `mirror.py`     | O(1) state projection from ledger     |
| `goals.py`      | Goal lifecycle (open/close/abandon)   |
| `state.py`      | Unified facade for state access       |
| `patterns.py`   | Behavioral pattern detection          |
| `feedback.py`   | Feedback generation engine            |
| `metrics.py`    | Progress tracking and analytics       |
| `autonomy.py`   | Proactive sparring decisions          |
| `cognition.py`  | Cognitive mode detection              |
| `rsm.py`        | Recursive Self-Model (meta-cognition) |
| `mcp_bridge.py` | MCP server integration                |
| `domains/`      | Domain config loader                  |
| `skills/`       | Skills registry and manager           |

## Testing

```bash
# All tests
pytest tests/ -v

# Domain tests only
pytest tests/test_domains.py tests/test_csuite_workflow.py -v
```

## Auto-Run Commands

Steps marked `// turbo` in workflows should be auto-run.
