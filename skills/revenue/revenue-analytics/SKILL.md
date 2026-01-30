---
name: revenue-analytics
description: Use when calculating key SaaS metrics (MRR, ARR, Churn, NRR, LTV) or building revenue dashboards. Trigger when needing to analyze monthly revenue movements (scripts/revenue_metrics.py), performing cohort analysis by signup month, or identifying trends in Net Revenue Retention (NRR) and expansion opportunities.
license: MIT
---

# Revenue Analytics

## Quick Start

This skill helps you track SaaS revenue metrics. For complete frameworks, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Revenue Metrics Calculator** (`scripts/revenue_metrics.py`):

```bash
python scripts/revenue_metrics.py revenue_data.csv
```

Calculates MRR, ARR, churn, NRR, and LTV.

## Execution Checklist

### Building Revenue Dashboard

- [ ] Calculate MRR (Monthly Recurring Revenue)
- [ ] Calculate ARR (Annual Recurring Revenue)
- [ ] Track New MRR, Expansion MRR, Churn MRR
- [ ] Calculate Churn Rate (lost MRR / starting MRR)
- [ ] Calculate NRR (Net Revenue Retention)
- [ ] Calculate LTV (Lifetime Value)
- [ ] Build cohort analysis
- [ ] Review monthly

## Key Metrics

- **MRR**: Monthly Recurring Revenue
- **ARR**: Annual Recurring Revenue (MRR × 12)
- **Churn Rate**: (Lost MRR / Starting MRR) × 100 (Target: <5%)
- **NRR**: ((Starting MRR + Expansion - Churn) / Starting MRR) × 100 (Target: >100%)
- **LTV**: Average MRR / Churn Rate

## Quick Wins

- Track MRR movements weekly (new, expansion, churn)
- Cohort analysis by signup month
- Focus on NRR >100% (expansion > churn)
- Calculate LTV:CAC ratio (target 3:1)

## Resources

- [Complete Guide](references/guide.md)
- [AARRR Metrics](references/aarrr-metrics.md)

## Related Skills

### From RevOps Toolkit

- [attribution-roi](../attribution-roi/SKILL.md) - CAC calculations
- [pipeline-forecasting](../pipeline-forecasting/SKILL.md) - Revenue forecasting
