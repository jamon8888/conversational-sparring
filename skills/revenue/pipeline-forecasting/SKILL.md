---
name: pipeline-forecasting
description: Use when building revenue forecasts, managing sales pipeline health, or analyzing stage-based win rates. Trigger when needing to calculate weighted pipeline value (scripts/pipeline_forecaster.py), identifying stale deals with no activity, or measuring pipeline coverage against quarterly targets.
license: MIT
---

# Pipeline Forecasting

## Quick Start

This skill helps you forecast revenue and manage pipeline health. For complete forecasting models and examples, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Pipeline Forecaster** (`scripts/pipeline_forecaster.py`):

```bash
python scripts/pipeline_forecaster.py pipeline.csv --method weighted
```

Calculates weighted pipeline forecast by stage.

## Execution Checklist

### Building a Forecast

- [ ] Calculate average sales cycle length
- [ ] Calculate win rate by stage
- [ ] Assign probability to each stage (10%, 20%, 40%, 70%, 90%)
- [ ] Calculate weighted pipeline value
- [ ] Check pipeline coverage (3-5x target)
- [ ] Review deal age (flag deals >30 days in stage)
- [ ] Disqualify stale deals (no activity)
- [ ] Create 3 scenarios (conservative, realistic, stretch)
- [ ] Update forecast weekly

### Weekly Pipeline Review

- [ ] Review closed wins/losses (learn why)
- [ ] Identify deals closing this week
- [ ] Move deals forward or disqualify
- [ ] Calculate pipeline coverage
- [ ] Update probabilities based on new info
- [ ] Check for pipeline gaps (need more top-of-funnel)

## Key Metrics

- **Pipeline Coverage**: Total Pipeline / Quarterly Target (Target: 3-5x)
- **Win Rate**: Closed-Won / (Won + Lost) (Benchmark: 20-30%)
- **Sales Cycle**: Days from Opportunity → Closed-Won (Track average)
- **Sales Velocity**: (# Opps × Deal Size × Win Rate) / Cycle Length

## Forecasting Methods

- **Stage-Based**: Assign % to each stage (simplest)
- **Historical Win Rate**: Use actual past performance (accurate)
- **Deal-by-Deal**: Evaluate each deal individually (best for small pipelines)

## Quick Wins

- Weekly pipeline reviews (Monday mornings, 30 min)
- Disqualify deals >90 days old with no activity
- Track forecast accuracy monthly (improve over time)
- Use "Commit" vs "Best Case" vs "Pipeline" categories
- Always be filling top of funnel (maintain 3x+ coverage)

## Resources

- [Complete Guide](references/guide.md)
- [Revenue Waterfall](references/revenue-waterfall.md)

## Related Skills

### From Sales Toolkit

- [lead-qualification](../lead-qualification/SKILL.md) - Qualify opportunities
- [discovery-calls](../discovery-calls/SKILL.md) - Move deals through stages

### From RevOps Toolkit

- [revenue-analytics](../../revenue-operations-toolkit/skills/revenue-analytics/SKILL.md) - MRR, ARR tracking
- [crm-hygiene](../../revenue-operations-toolkit/skills/crm-hygiene/SKILL.md) - Clean pipeline data
- [sales-marketing-alignment](../../revenue-operations-toolkit/skills/sales-marketing-alignment/SKILL.md) - Lead definitions
