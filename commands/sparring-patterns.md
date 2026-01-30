---
description: Show detected behavioral patterns with examples
allowed-tools: Bash(python:*)
---

# Sparring Patterns Command

Display detailed behavioral patterns detected from sparring data.

## Usage

```
/sparring patterns
```

## Instructions

1. Run Python script to analyze patterns:

```python
import sys
sys.path.insert(0, 'conversational-sparring/lib')
from ledger import SparringLedger
from patterns import PatternDetector, PATTERN_DEFINITIONS

ledger = SparringLedger()
detector = PatternDetector(ledger)

patterns = detector.analyze()
gaps = detector.get_knowledge_gaps()
strengths = detector.get_strengths()

for p in patterns:
    print(f"## {p.name}")
    print(f"Severity: {p.severity}")
    print(f"Trend: {p.trend}")
    print(f"Occurrences: {p.occurrences}")
    print(f"Description: {p.description}")
    print(f"Suggestion: {p.suggestion}")
    print(f"Examples: {p.examples}")
    print()

print(f"Knowledge Gaps: {gaps}")
print(f"Strengths: {strengths}")
```

2. Format output with:
   - Each pattern with severity indicator
   - Trend arrow (improving/stable/declining)
   - Specific examples
   - Actionable suggestions
   - Knowledge gaps section
   - Strengths section

## Example Output

```
## Behavioral Patterns Analysis

### Patterns Detected

#### context_switching ⚠️ Warning
Starting new goals before completing existing ones

**Trend:** stable →
**Occurrences:** 5 times

**Examples:**
- Started 'Add caching' with 4 open goals
- Started 'Fix login' with 3 open goals
- Started 'Update docs' with 3 open goals

**Suggestion:** Focus on completing one goal before starting another.
Consider using `/sparring goals` to review and prioritize.

---

#### rushed_completion ℹ️ Info
Closing goals very quickly (< 1 hour)

**Trend:** improving ↑
**Occurrences:** 3 times

**Examples:**
- Completed in 0.5 hours
- Completed in 0.8 hours

**Suggestion:** Quick wins are good! Make sure quality isn't sacrificed.

---

#### reflection_consistency ℹ️ Info
Regular reflection on work progress

**Trend:** improving ↑
**Occurrences:** 8 times

**Suggestion:** Keep reflecting! It helps identify patterns.

---

### Knowledge Gaps

Areas where you've struggled multiple times:
- **async-patterns** (3 struggles) - Consider studying async/await patterns
- **testing-mocks** (2 struggles) - Review mocking strategies

### Strengths

What you're doing well:
- Consistent goal completion
- Strong at feature tasks
- Efficient problem solving

---

**Overall:** 3 patterns detected. 1 needs attention, 2 are informational.

Use `/sparring progress` for full metrics.
```

## Severity Indicators

- ⚠️ **Warning** - Should address soon
- 🔴 **Concern** - Needs immediate attention
- ℹ️ **Info** - Just informational

## Trend Arrows

- ↑ Improving
- → Stable
- ↓ Declining

