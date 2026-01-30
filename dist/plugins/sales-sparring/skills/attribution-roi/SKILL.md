---
name: attribution-roi
description: Use when calculating marketing attribution across channels, analyzing campaign ROAS, or optimizing marketing spend. Trigger when needing to identify high-performing customer acquisition channels, calculating LTV:CAC ratios, or requesting a multi-touch attribution model (scripts/attribution_calculator.py) for budget allocation.
license: MIT
---

# Attribution & ROI

## Quick Start

This skill helps you track marketing attribution and calculate ROI. For complete models, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Attribution Calculator** (`scripts/attribution_calculator.py`):

```bash
python scripts/attribution_calculator.py conversions.csv --model multi-touch
```

Calculates attribution using various models.

## Execution Checklist

### Setting Up Attribution

- [ ] Implement UTM tracking on all campaigns
- [ ] Set up conversion pixels (ads, CRM)
- [ ] Choose attribution model (first, last, or multi-touch)
- [ ] Connect data sources (analytics, CRM, ads)
- [ ] Calculate CAC by channel
- [ ] Calculate ROAS by campaign
- [ ] Optimize budget allocation
- [ ] Report monthly

## Key Metrics

- **CAC**: Marketing Spend / New Customers
- **ROAS**: Revenue / Ad Spend (Target: 3-5x)
- **LTV:CAC**: Lifetime Value / CAC (Target: 3:1)
- **Payback Period**: CAC / Monthly Recurring Revenue

## Attribution Models

- **First-Touch**: Credit to first interaction
- **Last-Touch**: Credit to final interaction
- **Multi-Touch**: Distributed across touchpoints
- **Time-Decay**: More credit to recent touches

## Quick Wins

- Use UTM parameters consistently
- Track conversions, not just clicks
- Calculate CAC by channel monthly
- Cut channels with CAC > LTV/3

## Resources

- [Complete Guide](references/guide.md)
- [Attribution Models](references/attribution-models.md)
- [Unit Economics](references/unit-economics.md)

## Related Skills

### From Marketing Toolkit

- [marketing-analytics](../../marketing-toolkit/skills/marketing-analytics/SKILL.md) - Marketing dashboards

### From RevOps Toolkit

- [revenue-analytics](../revenue-analytics/SKILL.md) - MRR, ARR, LTV
- [sales-marketing-alignment](../sales-marketing-alignment/SKILL.md) - Lead definitions
