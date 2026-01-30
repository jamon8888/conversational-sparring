# Conversational Sparring Plugin

A universal, domain-adaptive sparring partner plugin for Claude Code that helps users track goals, detect patterns, and improve their workflow across any domain - development, business, marketing, product, and more.

## Overview

The Conversational Sparring Partner provides:

- **Domain Adaptation** - Sparring that adapts to your work context
- **Goal Tracking** - Set, track, and complete goals with domain-specific categories
- **Pattern Detection** - Identify behavioral patterns customized to your domain
- **Progress Metrics** - Track completion rates, streaks, and learning velocity
- **Personalized Feedback** - Get feedback adapted to your history and domain
- **Proactive Sparring** - Agents that detect struggles and offer help

## Skills Library Integration

This plugin is the core engine for the **Claude Skills Library**. It dynamically loads skill bundles from the `skills/` directory, allowing you to:

1.  **Access 48+ Professional Skills** - Marketing, Engineering, Product, etc.
2.  **Use Dynamic Bundles** - Install skills by category or custom groups.
3.  **Sync with Marketplace** - Automatically available as Claude Code plugins.

The `conversational-sparring` package acts as the `skills-engine` that powers dynamic discovery and execution of Python tools found in `skills/`.

## 🏭 Domain Plugin Factory

This repository includes a generator that creates **standalone sparring plugins** for specific domains.

Instead of installing the generic sparring partner, you can generate and install specialized versions:

1.  **Marketing Sparring** (`marketing-sparring`)
2.  **Engineering Sparring** (`engineering-sparring`)
3.  **Solopreneur Sparring** (`solopreneur-sparring`)
4.  And more...

To generate these plugins locally:

```bash
python scripts/generate_plugins.py
```

Resulting plugins are created in `dist/plugins/` and are ready for distribution.

## Installation (Generic)

The generic plugin is designed to work with Claude Code. Place the `conversational-sparring/` directory in your project or reference it in your Claude Code configuration.

**Requirements:** Python 3.9+, PyYAML (for domain configuration)

```bash
pip install pyyaml
```

## Commands

| Command                        | Description                        |
| ------------------------------ | ---------------------------------- |
| `/sparring`                    | Show sparring dashboard            |
| `/sparring goal <description>` | Set a new goal                     |
| `/sparring goals`              | List all active goals              |
| `/sparring close <goal-id>`    | Close/complete a goal              |
| `/sparring progress`           | Show progress summary with metrics |
| `/sparring reflect`            | Trigger structured reflection      |
| `/sparring patterns`           | Show detected behavioral patterns  |
| `/sparring domains`            | List available domains             |

## Domain System

The sparring adapts to any domain through YAML configuration files. No hardcoded ontology - domain knowledge exists only in configuration.

### Available Domains

| Domain        | Description                    | Example Goals                     |
| ------------- | ------------------------------ | --------------------------------- |
| `developer`   | Software development (default) | "Fix login bug", "Implement auth" |
| `business`    | Executive leadership           | "Increase Q2 revenue by 15%"      |
| `marketing`   | Marketing teams                | "Launch Q1 campaign"              |
| `product`     | Product management             | "Ship feature X to users"         |
| `strategy`    | Strategic planning             | "Complete market analysis"        |
| `engineering` | Non-software engineering       | "Complete design review"          |
| `personal`    | Personal development           | "Read 2 books this month"         |

### Using Domains

```bash
# Set a goal with explicit domain
/sparring --domain=business goal "Close partnership with Acme Corp"

# List goals (uses last domain or default)
/sparring goals

# Set default domain
/sparring config domain marketing

# List available domains
/sparring domains
```

### Domain-Specific Features

Each domain provides:

- **Categories** - Domain-specific goal categorization (e.g., "revenue", "operations" for business)
- **Patterns** - Behavioral patterns relevant to the domain
- **Impact Keywords** - Keywords for scoring goal importance
- **Thresholds** - Domain-appropriate timeframes (business goals take longer than dev tasks)
- **Messages** - Customized terminology ("Objective achieved" vs "Shipped")

## Quick Start

```bash
# Developer domain (default)
/sparring goal "Implement user authentication with JWT"
/sparring goals
/sparring close a1b2c3d4
/sparring progress

# Business domain
/sparring --domain=business goal "Secure Series A funding"
/sparring --domain=business progress
```

## Architecture

The plugin is built on an event-sourced architecture inspired by the Persistent Mind Model (PMM):

```
Commands → Domain Config → Ledger (SQLite) → Analysis
                                ↓
                          Goal Manager
                          Pattern Detector
                          Feedback Generator
                          Metrics Calculator
```

### Core Components

| Component | File              | Purpose                         |
| --------- | ----------------- | ------------------------------- |
| Domains   | `lib/domains/`    | Domain configuration loading    |
| Ledger    | `lib/ledger.py`   | Append-only SQLite event store  |
| Goals     | `lib/goals.py`    | Goal lifecycle management       |
| Patterns  | `lib/patterns.py` | Behavioral pattern detection    |
| Feedback  | `lib/feedback.py` | Structured feedback generation  |
| Metrics   | `lib/metrics.py`  | Progress and efficiency metrics |

### Domain Configuration Files

| File                       | Purpose                               |
| -------------------------- | ------------------------------------- |
| `domains/_base.yaml`       | Universal patterns (inherited by all) |
| `domains/developer.yaml`   | Software development                  |
| `domains/business.yaml`    | Business sparring                     |
| `domains/marketing.yaml`   | Marketing teams                       |
| `domains/product.yaml`     | Product management                    |
| `domains/strategy.yaml`    | Strategic planning                    |
| `domains/engineering.yaml` | Non-software engineering              |
| `domains/personal.yaml`    | Personal development                  |

### Agents

| Agent                 | Purpose                             |
| --------------------- | ----------------------------------- |
| `sparring-planner`    | Pre-work goal setting and planning  |
| `sparring-reviewer`   | Post-work feedback and review       |
| `sparring-mentor`     | Struggle detection and intervention |
| `sparring-celebrator` | Achievement recognition             |

## Data Storage

All data is stored locally at `~/.claude/sparring/sparring.db`

Custom domains can be placed at `~/.claude/sparring/domains/`

### Event Types

```python
EVENT_KINDS = [
    "goal_open",        # User sets a goal
    "goal_close",       # Goal completed successfully
    "goal_abandon",     # Goal abandoned
    "reflection",       # Structured reflection
    "struggle",         # Detected struggle/blocker
    "intervention",     # Sparring offered help
    "feedback",         # Sparring feedback given
    "pattern_detected", # Behavioral pattern identified
    "achievement",      # Milestone reached
    "config",           # User preferences
    "session_start",    # Sparring session began
    "session_end",      # Sparring session ended
    "domain_change",    # Domain changed during session
]
```

## Creating Custom Domains

Create a YAML file at `~/.claude/sparring/domains/` to define a custom domain:

```yaml
# ~/.claude/sparring/domains/research.yaml
domain:
  id: research
  name: Research & Academia
  description: Academic research and publication sparring

categories:
  - id: literature
    name: Literature Review
    keywords: [literature, papers, review, citations]
  - id: writing
    name: Writing
    keywords: [paper, manuscript, draft, publication]
  - id: grants
    name: Grants
    keywords: [grant, funding, proposal, budget]

patterns:
  publication_pressure:
    description: Taking shortcuts due to publication deadlines
    severity_threshold: 2
    severity: warning
    suggestion: Quality over quantity - reviewers notice rushed work

impact_keywords:
  high: [critical, deadline, reviewer, submission]
  medium: [important, chapter, revision]
  low: [minor, polish, optional]

thresholds:
  stalled_goal_days: 14 # Research takes time
  quick_win_days: 3
  max_open_goals: 8
  reflection_cadence: weekly

messages:
  goal_created: "Research objective set"
  goal_completed: "Objective achieved"
  streak_message: "{count} consecutive completions"
```

## Behavioral Patterns

Patterns are loaded from domain configuration. Base patterns (inherited by all domains):

| Pattern                  | Description                                   | Severity |
| ------------------------ | --------------------------------------------- | -------- |
| `context_switching`      | Starting new goals before completing old ones | Warning  |
| `goal_abandonment`       | Frequently abandoning goals                   | Concern  |
| `rushed_completion`      | Completing goals very quickly                 | Info     |
| `stalled_work`           | Goals sitting idle                            | Warning  |
| `reflection_consistency` | Regular reflection habits                     | Info     |

Domain-specific patterns (examples):

- **Developer:** `test_avoidance`, `review_skipping`, `technical_debt_accumulation`
- **Business:** `stakeholder_misalignment`, `resource_overcommitment`
- **Product:** `scope_creep`, `metric_myopia`, `user_disconnection`

## Metrics

Tracked metrics include:

- **Goal Completion Rate** - Percentage of goals completed successfully
- **Average Goal Duration** - Time from open to close
- **Struggle Frequency** - Struggles per goal
- **Reflection Rate** - Reflections per goal
- **Learning Velocity** - Improvement rate over time
- **Streaks** - Consecutive successful completions

## Integration with PMM

This plugin adapts several components from the Persistent Mind Model:

| PMM Component               | Sparring Adaptation                 |
| --------------------------- | ----------------------------------- |
| Concept Token Layer         | Domain config system                |
| `event_log.py`              | `ledger.py` - Event store           |
| `commitment_manager.py`     | `goals.py` - Goal management        |
| `reflection_synthesizer.py` | `feedback.py` - Feedback generation |
| `rsm.py`                    | `patterns.py` - Pattern detection   |
| `efficiency_metrics.py`     | `metrics.py` - Progress tracking    |

## Privacy

- All data is stored locally on your machine
- No data is sent to external services
- Custom domains are never uploaded
- Delete `~/.claude/sparring/` to reset all data

## Development

### Running Tests

```bash
cd conversational-sparring
python tests/test_sparring.py
```

### Extending

**To add new patterns:**

1. Add pattern definition to domain YAML file
2. Or extend `PATTERN_DEFINITIONS` in `lib/patterns.py` for global patterns
3. Add detection logic in `_process_event()` if needed

**To add new domains:**

1. Create YAML file in `domains/` directory
2. Define categories, patterns, thresholds, and messages
3. Test with `/sparring --domain=your-domain goal "Test goal"`

**To add new commands:**

1. Create markdown file in `commands/`
2. Define frontmatter with description and allowed-tools
3. Document usage and examples

## License

MIT License - See LICENSE file for details.

## Credits

Inspired by the Persistent Mind Model (PMM) cognitive architecture.
