---
description: Automated workflow for creating and syncing new domain plugins with all related files
---

# Domain Plugin Creation Workflow

This workflow automates the creation of new domain plugins and ensures all related files stay synchronized.

## Prerequisites

Ensure you're in the `conversational-sparring` directory:

```bash
cd conversational-sparring
```

## Step 1: Create Domain YAML File

Create the domain configuration in `domains/<domain-id>.yaml`:

```yaml
domain:
  id: new-domain
  name: New Domain Name
  description: Brief description of the domain focus

categories:
  - id: category1
    name: Category 1
    keywords: ["keyword1", "keyword2"]

thresholds:
  stalled_goal_days: 3.0
  max_concurrent_goals: 7

patterns:
  rapid_switching:
    enabled: true
    threshold: 3

messages:
  goal_created: "New goal set in {domain}!"
```

## Step 2: Create Skills Directory (Optional)

If adding skills for this domain:

```bash
mkdir -p skills/<domain-category>/<skill-name>
```

Create `SKILL.md` with YAML frontmatter:

```yaml
---
name: Skill Name
description: Brief skill description
---
# Skill content...
```

// turbo

## Step 3: Run Domain Sync Script

```bash
python scripts/sync_domains.py --apply
```

This automatically updates:

- `commands/sparring.md` (domain table)
- `README.md` (skill/domain counts)
- `CLAUDE.md` (skill/domain/agent counts)

// turbo

## Step 4: Validate Skills Structure

```bash
python scripts/validate_skills.py
```

Checks:

- YAML frontmatter with `name` and `description`
- Required SKILL.md file
- Domain-agent consistency
- Script quality

// turbo

## Step 5: Update README Skill Listings

```bash
python scripts/generate_readme.py --apply
```

// turbo

## Step 6: Validate Domain Tests

```bash
python -m pytest tests/test_domains.py tests/test_csuite_workflow.py -v
```

Expected: All tests pass.

## Step 5: Create Agent Folder (Optional)

If creating domain-specific agents:

```bash
mkdir -p agents/<domain-id>
```

Create agent files:

- `sparring-mentor.md` - Coaching and guidance
- `sparring-reviewer.md` - Code/work review
- `sparring-planner.md` - Goal planning

// turbo

## Step 6: Generate Plugin

```bash
python scripts/generate_plugins.py
```

This creates:

- `dist/plugins/<domain-id>-sparring/`
- Plugin manifest and README

// turbo

## Step 7: Final Sync Check

```bash
python scripts/sync_domains.py --check
```

Expected: `✅ All files in sync`

## Troubleshooting

### Stale Domain References

If sync reports stale references:

1. Check which files need updating:

   ```bash
   python scripts/sync_domains.py -v
   ```

2. Fix legacy domain names:
   - `strategy` → `c-level`
   - `growth` → `marketing-growth`
   - `business` → `personal` or `c-level`

### Test Failures

If domain tests fail:

1. Check domain exists:

   ```bash
   ls domains/<domain-id>.yaml
   ```

2. Verify YAML syntax:
   ```bash
   python -c "import yaml; yaml.safe_load(open('domains/<domain-id>.yaml'))"
   ```

### Plugin Generation Fails

1. Check domain config is valid
2. Check skills have proper SKILL.md files
3. Run with verbose:
   ```bash
   python scripts/generate_plugins.py --verbose
   ```

## Quick Reference

| Task             | Command                                  |
| ---------------- | ---------------------------------------- |
| Sync domains     | `python scripts/sync_domains.py --apply` |
| Check sync       | `python scripts/sync_domains.py --check` |
| List stats       | `python scripts/sync_domains.py -v`      |
| Test domains     | `pytest tests/test_domains.py -v`        |
| Generate plugins | `python scripts/generate_plugins.py`     |

## Domain Naming Convention

| Domain Type      | ID Pattern       | Example          |
| ---------------- | ---------------- | ---------------- |
| Executive        | `c-level`        | c-level          |
| Department       | `<dept>`         | sales, product   |
| Sub-domain       | `<dept>-<focus>` | marketing-growth |
| Cross-functional | `<function>-ops` | revenue-ops      |
