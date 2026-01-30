---
description: Show progress summary with metrics and insights
allowed-tools: Bash(python:*)
---

# Sparring Progress Command

Display a comprehensive progress summary with metrics, patterns, and insights.

## Usage

```
/sparring progress
```

## Instructions

1. Run Python script to gather all metrics:

```python
import sys
sys.path.insert(0, 'lib')
from ledger import SparringLedger
from goals import GoalManager
from patterns import PatternDetector
from metrics import calculate_metrics, get_progress_summary

ledger = SparringLedger()
manager = GoalManager(ledger)
detector = PatternDetector(ledger)

# Get metrics
metrics = calculate_metrics(ledger)
summary = get_progress_summary(ledger)
patterns = detector.analyze()
gaps = detector.get_knowledge_gaps()
strengths = detector.get_strengths()

# Output data
print(f"Status: {summary['status']} - {summary['status_message']}")
print(f"Completion Rate: {metrics.goal_completion_rate}%")
print(f"Avg Duration: {metrics.avg_goal_duration_days} days")
print(f"Current Streak: {metrics.streak_current}")
print(f"Best Streak: {metrics.streak_best}")
print(f"Learning Velocity: {metrics.learning_velocity}%")

print(f"\nPatterns: {len(patterns)}")
for p in patterns[:3]:
    print(f"  - {p.name}: {p.description} ({p.occurrences}x)")

print(f"\nKnowledge Gaps: {gaps}")
print(f"Strengths: {strengths}")
print(f"Insights: {summary['insights']}")
```

2. Format output with sections:
   - Overall Status
   - Key Metrics
   - Behavioral Patterns (top 3)
   - Knowledge Gaps (if any)
   - Strengths
   - Personalized Insights

## Example Output

```
## Progress Summary

### Status: Good - Solid progress!

### Key Metrics
| Metric              | Value      |
|---------------------|------------|
| Completion Rate     | 78.5%      |
| Avg Goal Duration   | 1.8 days   |
| Current Streak      | 4          |
| Best Streak         | 7          |
| Learning Velocity   | +12.3%     |

### Behavioral Patterns

**context_switching** (warning)
Starting new goals before completing existing ones
_Occurrences: 5 | Trend: stable_
> Suggestion: Focus on completing one goal before starting another

**reflection_consistency** (info)
Regular reflection on work progress
_Occurrences: 8 | Trend: improving_
> Great job maintaining reflection habits!

### Knowledge Gaps
- async-patterns (struggled 3 times)
- testing-mocks (struggled 2 times)

### Strengths
- Consistent goal completion
- Strong at feature tasks
- Efficient problem solving

### Insights
- Building momentum: 4-goal streak
- Clear improvement trend - fewer struggles over time
- Great reflection habits!

---
Use `/sparring patterns` for detailed pattern analysis.
Use `/sparring reflect` to capture learnings.
```

