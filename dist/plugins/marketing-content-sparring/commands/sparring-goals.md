---
description: List all active goals with status information
allowed-tools: Bash(python:*)
---

# Sparring Goals Command

List all currently active goals with status information.

## Usage

```
/sparring goals
```

## Instructions

1. Run the Python script to fetch goals:

```python
import sys
sys.path.insert(0, 'lib')
from ledger import SparringLedger
from goals import GoalManager

ledger = SparringLedger()
manager = GoalManager(ledger)

goals = manager.get_open_goals()
stats = manager.get_goal_stats()

for goal in goals:
    print(f"{goal['id']} | {goal['category']:12} | {goal['age_days']:.1f}d | {goal['description'][:50]}")
    if goal['is_stalled']:
        print(f"  ^ STALLED - no activity for {goal['age_days']:.1f} days")

print(f"\nStats: {stats['open_count']} open | {stats['completion_rate']}% completion | {stats['current_streak']} streak")
```

2. Format output as a table showing:
   - Goal ID
   - Category
   - Age (days since opened)
   - Description (truncated)
   - Stalled indicator if applicable

3. Show summary stats at the bottom

## Example Output

```
## Active Goals

| ID       | Category    | Age   | Description                              |
|----------|-------------|-------|------------------------------------------|
| a1b2c3d4 | feature     | 2.3d  | Implement user authentication with JWT   |
| b2c3d4e5 | bug         | 0.5d  | Fix login redirect issue                 |
| c3d4e5f6 | refactor    | 5.1d  | Clean up API response handlers           |
                           ^ STALLED

**Summary:** 3 open | 75.0% completion rate | 5 goal streak

Tip: Goal c3d4e5f6 has been stalled for 5+ days.
Consider closing it or breaking it into smaller tasks.
```

## If No Goals

```
## No Active Goals

You have no active goals right now.

Use `/sparring goal <description>` to set a new objective.

Recent completions: 5 goals completed with 80% success rate.
```

