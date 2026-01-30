---
name: lead-qualification
description: Use when qualifying and scoring leads using the FITS model to prioritize your sales pipeline. Trigger when needing to evaluate prospects based on Fit, Intent, Timing, and Size (scripts/lead_scorer.py), identifying high-priority buyer signals, or disqualifying non-ICP leads to optimize team focus.
license: MIT
---

# Lead Qualification

## Quick Start

This skill helps you qualify and score leads systematically. For complete frameworks, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Lead Scorer** (`scripts/lead_scorer.py`):

```bash
python scripts/lead_scorer.py leads.csv
```

Scores leads using FITS model.

## Execution Checklist

### Qualifying a Lead

- [ ] Check Fit (ICP match: industry, size, role)
- [ ] Check Intent (active buyer signals)
- [ ] Check Timing (budget cycle, urgency)
- [ ] Check Size (deal value, potential)
- [ ] Score 1-10 on each dimension
- [ ] Total score >28 = high priority
- [ ] Route to appropriate sales process

## Key Frameworks

- **FITS Model**: Fit + Intent + Timing + Size (score each 1-10)
- **BANT**: Budget + Authority + Need + Timeline
- **Scoring Thresholds**: <20 (disqualify), 20-28 (nurture), >28 (prioritize)

## Quick Wins

- Disqualify non-ICP leads immediately (save time)
- Look for intent signals (downloaded content, visited pricing)
- Ask timing question early ("When are you looking to solve this?")
- Score leads weekly, update priorities

## Resources

- [Complete Guide](references/guide.md)

## Related Skills

### From Sales Toolkit

- [discovery-calls](../discovery-calls/SKILL.md) - Deep qualification
- [cold-outreach](../cold-outreach/SKILL.md) - Target qualified prospects

### From RevOps Toolkit

- [sales-marketing-alignment](../../revenue-operations-toolkit/skills/sales-marketing-alignment/SKILL.md) - MQL/SQL definitions
