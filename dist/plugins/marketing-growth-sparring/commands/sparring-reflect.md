---
description: Trigger a structured reflection on recent work
allowed-tools: Bash(python:*)
---

# Sparring Reflect Command

Guide the user through a structured reflection on their recent work.

## Usage

```
/sparring reflect [goal-id]
```

## Reflection Structure

Follow the **Intent → Outcome → Next** format:
1. **Intent**: What were you trying to accomplish?
2. **Outcome**: What actually happened?
3. **Next**: What will you do next?

## Instructions

1. If goal-id provided, fetch that goal's details
2. Ask the user the three reflection questions
3. Record the reflection in the ledger:

```python
import sys
sys.path.insert(0, 'lib')
from ledger import SparringLedger
from feedback import FeedbackGenerator

ledger = SparringLedger()
feedback = FeedbackGenerator(ledger)

# Record reflection
event_id = feedback.record_reflection(
    intent="<USER_INTENT>",
    outcome="<USER_OUTCOME>",
    next_action="<USER_NEXT>",
    goal_id="<GOAL_ID>",  # Optional
)

print(f"Reflection recorded: {event_id}")
```

4. Provide brief feedback based on the reflection

## Interaction Flow

**Step 1 - Prompt for Intent**
```
## Reflection Time

Let's reflect on your recent work.

**What were you trying to accomplish?**
(Describe the goal or task you were working on)
```

**Step 2 - Prompt for Outcome**
```
**What actually happened?**
(What did you achieve? What challenges did you face?)
```

**Step 3 - Prompt for Next**
```
**What will you do next?**
(What's your next step or learning from this?)
```

**Step 4 - Confirm and Provide Feedback**
```
## Reflection Recorded

**Intent:** Implement JWT authentication for the API
**Outcome:** Got token generation working, but refresh flow is incomplete
**Next:** Complete refresh token logic tomorrow, then add tests

---

This reflection shows good progress awareness. The incomplete refresh
flow is a clear next step - consider making it a new goal with
`/sparring goal "Complete JWT refresh token flow"`.

Reflection streak: 3 (Keep it up!)
```

## Quick Reflect Mode

If user provides all info at once:
```
/sparring reflect "Worked on auth, got tokens working, need to add refresh flow"
```

Parse and record without prompts.

