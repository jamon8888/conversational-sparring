# Conversational Sparring Plugin - Next Roadmap

## Overview

This roadmap outlines enhancements to the Conversational Sparring plugin based on analysis of the Persistent Mind Model (PMM) architecture. The goal is to evolve the sparring from a simple goal-tracking tool into a sophisticated self-modeling sparring system that learns from user behavior patterns.

## Current State Analysis

### What We Have
- **Event-sourced ledger** (`ledger.py`) - Append-only SQLite storage with hash chaining
- **Goal lifecycle management** (`goals.py`) - Open/close goals with categories
- **Basic pattern detection** (`patterns.py`) - Threshold-based pattern identification
- **Domain configuration** (`domains/`) - YAML-based domain adaptation
- **Feedback generation** (`feedback.py`) - Domain-aware sparring messages
- **Metrics calculation** (`metrics.py`) - Basic progress tracking

### What We're Missing (Learned from PMM)
1. **Projections** - Fast queryable state derived from ledger
2. **Recursive Self-Model (RSM)** - Behavioral tendencies and meta-patterns
3. **Graph structures** - Causal/semantic relationships between events
4. **Autonomy kernel** - Background self-direction and maintenance
5. **Concept bindings** - Semantic tokens linked to events
6. **Policy evolution** - Self-adjusting thresholds based on outcomes

---

## Phase 1: Mirror Projection Layer

**Goal**: Fast, rebuildable state projection for efficient queries

### New Files
- `lib/mirror.py` - In-memory projection of ledger state

### Key Features
```python
class SparringMirror:
    """Rebuildable projection over SparringLedger."""

    def __init__(self, ledger):
        self.open_goals: Dict[str, Dict] = {}  # goal_id -> goal data
        self.stale_flags: Dict[str, bool] = {}  # goal_id -> is_stale
        self.reflection_counts: Dict[str, int] = {}  # source -> count
        self.last_event_id: int = 0
        self.current_domain: str = "developer"

    def rebuild(self, events=None):
        """Rebuild from ledger - deterministic."""

    def sync(self, event):
        """Incrementally update from new event."""
```

### Benefits
- O(1) queries for open goals instead of O(n) ledger scans
- Stale goal detection without repeated computation
- Current domain tracking across sessions

---

## Phase 2: Recursive Self-Model for Sparring

**Goal**: Track behavioral tendencies and meta-patterns over time

### New Files
- `lib/rsm.py` - Recursive Self-Model adapted for sparring

### Key Features
```python
class SparringRSM:
    """Behavioral self-model built from sparring events."""

    BEHAVIORAL_PATTERNS = {
        "goal_completion_rate": (("goal_close",), None),
        "reflection_consistency": (("reflection",), None),
        "domain_switching": (("domain_change",), None),
        "struggle_frequency": (("struggle",), None),
        "quick_wins": (("goal_close",), ("quick_win",)),
    }

    def snapshot(self) -> Dict:
        """Return serialized self-model for feedback."""
        return {
            "behavioral_tendencies": self.behavioral_tendencies,
            "knowledge_gaps": self.knowledge_gaps,
            "sparring_meta_patterns": self.meta_patterns,
        }
```

### New Event Types to Add
```python
# Add to EVENT_KINDS in ledger.py
"rsm_snapshot",      # Periodic self-model checkpoint
"tendency_detected", # New behavioral tendency identified
"meta_pattern",      # Pattern of patterns detected
```

### Behavioral Tendencies to Track
| Tendency | Description | Trigger |
|----------|-------------|---------|
| `completion_momentum` | Consecutive goal completions | goal_close events |
| `reflection_habit` | Regular reflection practice | reflection events |
| `context_discipline` | Staying focused vs switching | domain_change events |
| `struggle_resilience` | Recovery after struggles | struggle → goal_close |
| `quick_start_bias` | Opening goals without completing | goal_open vs goal_close |

---

## Phase 3: Causal Graph (MemeGraph Adaptation)

**Goal**: Track relationships between sparring events

### New Files
- `lib/sparring_graph.py` - Causal graph for sparring events

### Key Features
```python
class SparringGraph:
    """Directed graph tracking causal relationships."""

    TRACKED_KINDS = {
        "goal_open",
        "goal_close",
        "goal_abandon",
        "reflection",
        "struggle",
        "intervention",
        "feedback",
    }

    EDGE_TYPES = {
        "closes": ("goal_close", "goal_open"),
        "reflects_on": ("reflection", "goal_close"),
        "triggered_by": ("struggle", "goal_open"),
        "resolved_by": ("intervention", "struggle"),
    }
```

### Use Cases
1. **Thread queries**: Get all events related to a goal
2. **Impact analysis**: Which goals led to reflections?
3. **Struggle mapping**: What patterns precede struggles?
4. **Success paths**: What sequences lead to completion?

---

## Phase 4: Autonomy Kernel for Sparring

**Goal**: Background self-direction and proactive sparring

### New Files
- `lib/autonomy.py` - Autonomous sparring decisions

### Key Features
```python
class SparringAutonomy:
    """Deterministic self-direction based on ledger state."""

    DEFAULT_THRESHOLDS = {
        "reflection_prompt_interval": 5,   # Goals completed before prompt
        "stalled_goal_days": 7,            # Days before goal considered stalled
        "max_open_goals": 5,               # Trigger overcommitment warning
        "struggle_intervention_threshold": 2,  # Struggles before intervention
    }

    def decide_next_action(self) -> SparringDecision:
        """Decide proactive sparring action."""
        # Check for stalled goals
        # Check for overcommitment
        # Check for reflection due
        # Check for celebration due
        return SparringDecision(
            decision="reflect" | "intervene" | "celebrate" | "idle",
            reasoning="...",
            evidence=[event_ids],
        )
```

### Autonomous Actions
| Decision | Trigger | Action |
|----------|---------|--------|
| `reflect` | 5+ goals closed without reflection | Prompt reflection |
| `intervene` | 2+ struggles on same goal | Offer help |
| `celebrate` | Streak milestone | Recognition feedback |
| `rebalance` | Too many open goals | Suggest focus |
| `unstall` | Goal idle > threshold | Check-in prompt |

---

## Phase 5: Concept Bindings for Sparring

**Goal**: Semantic tokens linking goals to concepts

### New Files
- `lib/concepts.py` - Concept graph for sparring

### Key Features
```python
class SparringConcepts:
    """Semantic concept bindings for sparring goals."""

    def bind_goal_to_concepts(self, goal_id: str, tokens: List[str]):
        """Bind a goal to semantic concept tokens."""

    def goals_for_concept(self, token: str) -> List[str]:
        """Find all goals related to a concept."""

    def related_concepts(self, token: str) -> List[str]:
        """Find concepts related to a token."""
```

### Concept Categories
- **Skill tokens**: `skill.python`, `skill.leadership`, `skill.communication`
- **Project tokens**: `project.auth`, `project.q2-campaign`
- **Area tokens**: `area.health`, `area.career`, `area.learning`
- **Time tokens**: `time.daily`, `time.weekly`, `time.quarterly`

### Benefits
- Cross-domain goal linking (personal fitness + career energy)
- Pattern detection across concept clusters
- Semantic search for related goals

---

## Phase 6: Policy Evolution

**Goal**: Self-adjusting thresholds based on outcomes

### New Files
- `lib/policy.py` - Adaptive policy management

### Key Features
```python
class SparringPolicy:
    """Evolving policies based on outcome tracking."""

    def suggest_policy_changes(self, outcomes: List[Outcome]) -> List[Suggestion]:
        """Suggest threshold adjustments based on outcomes."""

    def apply_policy_update(self, suggestions: List[Suggestion]):
        """Apply approved policy changes to thresholds."""
```

### Adaptive Behaviors
| Metric | Policy Change |
|--------|---------------|
| High completion rate | Increase max_open_goals |
| Low completion rate | Decrease max_open_goals |
| Quick completions | Shorten quick_win threshold |
| Frequent stalls | Decrease stalled_goal_days |
| Rare reflections | Decrease reflection_prompt_interval |

---

## Phase 7: Enhanced Pattern Detection

**Goal**: Sophisticated pattern detection using PMM techniques

### Enhancements to `lib/patterns.py`
```python
class EnhancedPatternDetector:
    """Advanced pattern detection with meta-patterns."""

    def detect_meta_patterns(self) -> List[MetaPattern]:
        """Detect patterns of patterns."""
        # e.g., "struggles_trigger_reflections"
        # e.g., "monday_goals_complete_friday"

    def detect_temporal_patterns(self) -> List[TemporalPattern]:
        """Detect time-based patterns."""
        # e.g., "morning_person" (goals set before 9am complete faster)

    def detect_domain_patterns(self) -> List[DomainPattern]:
        """Detect cross-domain patterns."""
        # e.g., "personal_goals_affect_work_performance"
```

---

## Implementation Priority

### High Priority (Foundation)
1. **Mirror projection** - Enables all other features
2. **RSM adaptation** - Core value proposition
3. **Autonomy kernel** - Proactive sparring

### Medium Priority (Enhancement)
4. **Causal graph** - Rich analytics
5. **Enhanced patterns** - Better insights
6. **Policy evolution** - Self-improvement

### Lower Priority (Advanced)
7. **Concept bindings** - Semantic search
8. **Cross-ledger references** - Multi-context sparring

---

## Migration Path

### Phase 1: Non-Breaking Additions
- Add Mirror, RSM, Graph as optional components
- Existing commands continue to work
- New `/sparring insights` command for RSM data

### Phase 2: Enhanced Commands
- `/sparring patterns` uses RSM + Graph
- `/sparring progress` includes behavioral tendencies
- `/sparring reflect` guided by autonomy decisions

### Phase 3: Autonomous Features
- Background sparring prompts
- Proactive interventions
- Adaptive thresholds

---

## Event Schema Evolution

### New Event Kinds
```python
NEW_EVENT_KINDS = [
    "rsm_snapshot",       # Periodic self-model checkpoint
    "tendency_detected",  # New behavioral tendency
    "meta_pattern",       # Pattern of patterns
    "concept_bind",       # Goal-concept binding
    "policy_update",      # Threshold adjustment
    "autonomy_decision",  # Autonomous sparring decision
    "sparring_prompt",    # Proactive sparring message
]
```

### Backward Compatibility
- All new event kinds are additive
- Existing events unchanged
- Mirror/RSM rebuild gracefully handles old events

---

## Success Metrics

### User-Facing
- Goal completion rate improvement
- Reflection frequency increase
- Struggle-to-resolution time decrease
- User engagement with insights

### System-Facing
- Projection rebuild time < 100ms
- Autonomy decision determinism (replay tests)
- Event append latency unchanged
- Memory usage bounded (window-based RSM)

---

## Technical Constraints (From PMM)

### Must Follow
1. **Determinism**: All decisions reproducible from ledger
2. **Idempotency**: Same input = same output
3. **Rebuildability**: All projections derivable from ledger
4. **No hidden state**: Everything in events
5. **Hash chain integrity**: prev_hash linking

### Should Avoid
1. Wall-clock dependencies in decisions
2. Regex in runtime parsing
3. Environment variables for behavior
4. Unbounded memory growth

---

## Next Steps

1. **Implement Mirror** - Start with basic projection
2. **Add RSM** - Behavioral tendency tracking
3. **Test determinism** - Replay tests for all new code
4. **Integrate with commands** - Surface insights in CLI
5. **Add autonomy** - Proactive sparring decisions

---

## References

- PMM `mirror.py` - Projection pattern
- PMM `rsm.py` - Recursive Self-Model
- PMM `meme_graph.py` - Causal graph
- PMM `autonomy_kernel.py` - Self-direction
- PMM `concept_graph.py` - Semantic bindings
- PMM CONTRIBUTING.md - Core invariants

