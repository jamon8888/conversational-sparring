---
name: follow-up-sequences
description: Use when designing multi-touch sales cadences across email, phone, and LinkedIn. Trigger when needing to plan the optimal timing and sequence of follow-up touches (scripts/cadence_planner.py), creating a 'Value Ladder' for persistence, or implementing 'break-up' emails after 7+ unsuccessful outreach attempts.
license: MIT
---

# Follow-Up Sequences

## Quick Start

This skill helps you design multi-touch follow-up cadences. For complete frameworks and examples, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Cadence Planner** (`scripts/cadence_planner.py`):

```bash
python scripts/cadence_planner.py --touches 5 --days 14
```

Generates optimal follow-up sequence timing.

## Execution Checklist

### Creating a Follow-Up Sequence

- [ ] Define goal (meeting, demo, response)
- [ ] Plan 5-7 touches over 2-3 weeks
- [ ] Vary channels (email, phone, LinkedIn, video)
- [ ] Create value-add content for each touch
- [ ] Schedule touches (days 1, 3, 7, 10, 14, 21)
- [ ] Personalize each message
- [ ] Track response rates per touch
- [ ] Optimize based on data

## Key Frameworks

- **Multi-Touch Cadence**: 7 touches over 21 days (80% of responses)
- **Channel Mix**: Email (60%), Phone (20%), LinkedIn (20%)
- **Value Ladder**: Touch 1 (intro) → Touch 3 (value) → Touch 5 (urgency) → Touch 7 (break-up)
- **Timing**: Days 1, 3, 7, 10, 14, 21 (optimal spacing)

## Quick Wins

- Use "break-up" email on touch 7 ("Should I close your file?")
- Vary value in each touch (article, case study, video)
- Call between emails (breaks pattern, higher response)
- Reference previous touches ("Following up on my note from Tuesday")

## Resources

- [Complete Guide](references/guide.md)
- [Multi-Touch Cadence](references/multi-touch-cadence.md)

## Related Skills

### From Sales Toolkit

- [cold-outreach](../cold-outreach/SKILL.md) - Initial outreach templates
- [discovery-calls](../discovery-calls/SKILL.md) - What to do when they respond
- [social-selling](../social-selling/SKILL.md) - LinkedIn touches in sequence

### From Marketing Toolkit

- [email-marketing](../../marketing-toolkit/skills/email-marketing/SKILL.md) - Email best practices
