# CLAUDE.md

This file provides guidance to Claude Code when working with the Conversational Sparring plugin.

## Project Overview

The Conversational Sparring Partner is a universal, domain-adaptive sparring plugin for Claude Code. It helps users track goals, detect behavioral patterns, and improve workflow across any domain.

**Core Philosophy**: Domain knowledge exists only in YAML configuration, not in code.

## Architecture

```
Commands → Domain Config → Ledger (SQLite) → Analysis
                               ↓
                         Goal Manager
                         Pattern Detector
                         Feedback Generator
                         Metrics Calculator
```

## Key Files

| Component      | File              | Purpose                                               |
| -------------- | ----------------- | ----------------------------------------------------- |
| Ledger         | `lib/ledger.py`   | Append-only SQLite event store with hash chaining     |
| Goals          | `lib/goals.py`    | Goal lifecycle management                             |
| Patterns       | `lib/patterns.py` | Behavioral pattern detection                          |
| Feedback       | `lib/feedback.py` | Domain-aware sparring messages                        |
| Metrics        | `lib/metrics.py`  | Progress and efficiency metrics                       |
| Domains        | `lib/domains/`    | Domain configuration loading                          |
| Domain Configs | `domains/*.yaml`  | Domain definitions (categories, patterns, thresholds) |

## Commands

```bash
/sparring                    # Show sparring dashboard
/sparring goal <desc>        # Set a new goal
/sparring goals              # List active goals
/sparring close <id>         # Complete a goal
/sparring progress           # Show progress summary
/sparring reflect            # Trigger reflection
/sparring patterns           # Show detected patterns
/sparring domains            # List available domains
/sparring --domain=X goal    # Set goal in specific domain
```

## Domain System - Virtual C-Suite

The system operates as a **Virtual Executive Team**, covering 7 key functions:

| Domain        | Role | Focus                                  |
| :------------ | :--- | :------------------------------------- |
| `strategy`    | CEO  | Vision, Decisions, Fundraising, Board  |
| `engineering` | CTO  | Code Quality, Architecture, Shipping   |
| `growth`      | CMO  | Acquisition, Retention, PMF            |
| `product`     | CPO  | Roadmap, User Research, Prioritization |
| `sales`       | CRO  | Pipeline, Closing, Negotiation         |
| `operations`  | COO  | Systems, Legal/Finance, Efficiency     |
| `people`      | CHRO | Hiring, Culture, Performance           |

### Dual-Mode Agents

Every agent adapts to the user's context:

- **Solofounder Mode**: Practical, "in the trenches" help. Co-creation focus.
- **Team Mode**: Executive sparring. Management and delegation focus.

Custom domains: `~/.claude/sparring/domains/`

## Event Types

```python
EVENT_KINDS = [
    "goal_open",        # User sets a goal
    "goal_close",       # Goal completed
    "goal_abandon",     # Goal abandoned
    "reflection",       # Structured reflection
    "struggle",         # Detected blocker
    "intervention",     # Sparring offered help
    "feedback",         # Sparring feedback
    "pattern_detected", # Pattern identified
    "achievement",      # Milestone reached
    "config",           # User preferences
    "session_start",    # Session began
    "session_end",      # Session ended
    "domain_change",    # Domain switched
]
```

## Data Storage

- Database: `~/.claude/sparring/sparring.db`
- Custom domains: `~/.claude/sparring/domains/`
- Agents: `agents/<domain>/<agent>.md` (e.g., `agents/engineering/sparring-mentor.md`)
- Skills: `skills/<domain>/<skill>.md` (e.g., `skills/engineering/sparring-patterns.md`)

## Testing

```bash
cd conversational-sparring
pytest tests/
```

## Plugin Generation

You can generate standalone plugins for each domain:

```bash
python scripts/generate_plugins.py
```

This creates ready-to-use packages in `dist/plugins/` (e.g., `dist/plugins/marketing-sparring`).

## Code Modification Guidelines

1. **Preserve determinism**: All state derives from ledger events
2. **Keep projections rebuildable**: Any cached state must rebuild from `ledger.read_all()`
3. **Domain config only**: No hardcoded domain knowledge in Python code
4. **Backward compatibility**: Legacy enums preserved alongside domain config

---

## Development Roadmap

### Current Limitations

The sparring partner currently lacks several PMM architectural patterns:

- No projection layer (Mirror) for fast queries
- No self-model (RSM) for behavioral tracking
- No causal graph for event relationships
- No autonomy kernel for proactive sparring

### Phase 1: Mirror Projection Layer

Add `lib/mirror.py` - Fast, rebuildable state projection:

- O(1) queries for open goals
- Stale goal detection
- Current domain tracking

```python
class SparringMirror:
    open_goals: Dict[str, Dict]
    stale_flags: Dict[str, bool]
    reflection_counts: Dict[str, int]

    def rebuild(self, events=None): ...
    def sync(self, event): ...
```

### Phase 2: Recursive Self-Model (RSM)

Add `lib/rsm.py` - Behavioral self-model:

- Track behavioral tendencies over time
- Detect meta-patterns (patterns of patterns)
- Knowledge gap analysis

Tendencies to track:

- `completion_momentum` - Consecutive completions
- `reflection_habit` - Regular reflection practice
- `context_discipline` - Focus vs switching
- `struggle_resilience` - Recovery after struggles

### Phase 3: Causal Graph

Add `lib/sparring_graph.py` - Event relationships:

- Thread queries (all events for a goal)
- Impact analysis (goals → reflections)
- Struggle mapping (patterns before struggles)

Edge types: `closes`, `reflects_on`, `triggered_by`, `resolved_by`

### Phase 4: Autonomy Kernel

Add `lib/autonomy.py` - Proactive sparring:

- Background self-direction
- Configurable thresholds
- Autonomous decisions

Decisions:

- `reflect` - Prompt reflection after completions
- `intervene` - Offer help after struggles
- `celebrate` - Recognition at milestones
- `rebalance` - Suggest focus when overcommitted

### Phase 5: Concept Bindings

Add `lib/concepts.py` - Semantic tokens:

- Link goals to skill/project/area tokens
- Cross-domain pattern detection
- Semantic search for related goals

### Phase 6: Policy Evolution

Add `lib/policy.py` - Adaptive thresholds:

- Self-adjusting based on outcomes
- Increase/decrease thresholds by success rate

### Phase 7: Enhanced Patterns

Upgrade `lib/patterns.py`:

- Meta-patterns (patterns of patterns)
- Temporal patterns (time-based)
- Cross-domain patterns

### Implementation Priority

1. **High**: Mirror → RSM → Autonomy (foundation)
2. **Medium**: Graph → Enhanced Patterns → Policy (enhancement)
3. **Lower**: Concept Bindings (advanced)

### Technical Constraints (From PMM)

**Must Follow:**

- Determinism: All decisions reproducible from ledger
- Idempotency: Same input = same output
- Rebuildability: All projections derivable from ledger
- No hidden state: Everything in events
- Hash chain integrity: prev_hash linking

**Avoid:**

- Wall-clock dependencies in decisions
- Regex in runtime parsing
- Environment variables for behavior
- Unbounded memory growth

### New Event Types (Future)

```python
NEW_EVENT_KINDS = [
    "rsm_snapshot",       # Self-model checkpoint
    "tendency_detected",  # Behavioral tendency
    "meta_pattern",       # Pattern of patterns
    "concept_bind",       # Goal-concept binding
    "policy_update",      # Threshold adjustment
    "autonomy_decision",  # Sparring decision
    "sparring_prompt",    # Proactive message
]
```

---

## References

- PMM Architecture: `../pmm/core/`
- PMM Autonomy: `../pmm/runtime/autonomy_kernel.py`
- PMM RSM: `../pmm/core/rsm.py`
- Full Roadmap: `ROADMAP.md`
