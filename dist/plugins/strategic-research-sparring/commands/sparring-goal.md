---
description: Set a new development goal for tracking
allowed-tools: Bash(python:*)
---

# Sparring Goal Command

Set a new development goal for tracking and sparring.

## Usage

```
/sparring goal <description>
```

## Goal Categories

Goals are automatically categorized based on description:

- **c-level** - Vision, Fundraising, Planning (Executive)
- **product** - Roadmap, specs, user research (Product)
- **engineering** - Architecture, code, devops (Engineering)
- **marketing-growth** - Acquisition, campaigns, experiments (Growth)
- **sales** - Pipeline, closing, outreach (Sales)
- **operations** - Finance, legal, systems (Ops)
- **people** - Hiring, culture, feedback (People)

## Instructions

1. Parse the user's goal description
2. Run the Python script to create the goal:

```python
import sys
sys.path.insert(0, 'lib')
from ledger import SparringLedger
from goals import GoalManager

ledger = SparringLedger()
manager = GoalManager(ledger)

# Create the goal
goal_id = manager.open_goal(
    description="<USER_DESCRIPTION>",
    category=None,  # Auto-detect
)

# Get current state
open_goals = manager.get_open_goals()
print(f"Goal created: {goal_id}")
print(f"Active goals: {len(open_goals)}")
```

3. Report the result to the user:
   - Show goal ID
   - Show detected category
   - Show current active goal count
   - If >5 active goals, warn about context switching

## Example

**User**: `/sparring --domain=marketing-growth goal "Launch localized campaign in DACH"`

**Response**:

```
## Goal Created

ID: `i9j0k1l2`
Category: acquisition
Description: Launch localized campaign in DACH

You now have 3 active goals.

Tip: Focus on completing goals before starting new ones.
Use `/sparring close i9j0k1l2` when done.
```

## Warnings

If user has more than 5 active goals:

```
Warning: You have 6 active goals. Consider closing some before
starting new ones to avoid context switching.

Use `/sparring goals` to review your active goals.
```
