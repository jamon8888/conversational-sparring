---
description: Close/complete a goal with outcome
allowed-tools: Bash(python:*)
---

# Sparring Close Command

Close a goal and record its outcome.

## Usage

```
/sparring close <goal-id> [outcome]
```

Outcomes:
- `success` (default) - Goal completed successfully
- `partial` - Goal partially completed
- `abandoned` - Goal abandoned

## Instructions

1. Parse goal ID and optional outcome from user input
2. Run Python script to close the goal:

```python
import sys
sys.path.insert(0, 'conversational-sparring/lib')
from ledger import SparringLedger
from goals import GoalManager

ledger = SparringLedger()
manager = GoalManager(ledger)

# Close the goal
success = manager.close_goal(
    goal_id="<GOAL_ID>",
    outcome="<OUTCOME>",  # success, partial, or abandoned
    notes=None,  # Optional notes
)

if success:
    stats = manager.get_goal_stats()
    print(f"Goal closed: {stats['current_streak']} streak")
else:
    print("Goal not found or already closed")
```

3. Report result:
   - Confirm closure
   - Show updated streak
   - Celebrate if applicable

## Example: Success

**User**: `/sparring close a1b2c3d4`

**Response**:
```
## Goal Completed!

Goal `a1b2c3d4` marked as successful.

Duration: 2.3 days
Current Streak: 6 goals!

Keep up the great work! Use `/sparring goal` to set your next objective.
```

## Example: Abandoned

**User**: `/sparring close a1b2c3d4 abandoned`

**Response**:
```
## Goal Closed

Goal `a1b2c3d4` marked as abandoned.

That's okay - not every goal works out. Consider:
- Was the goal too large? Break it into smaller tasks.
- Were there unexpected blockers? Document them for future reference.
- Did priorities change? That's a valid reason to pivot.

Use `/sparring reflect` to capture what you learned.
```

## Error Cases

If goal not found:
```
Goal `xyz12345` not found. Use `/sparring goals` to see active goals.
```

If goal already closed:
```
Goal `a1b2c3d4` is already closed.
```

