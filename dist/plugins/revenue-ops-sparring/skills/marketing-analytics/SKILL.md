---
name: marketing-analytics
description: Use when tracking marketing performance, measuring campaign ROI, or building growth dashboards. Trigger when needing to calculate CAC (Customer Acquisition Cost) and ROAS (scripts/roi_calculator.py), setting up UTM parameter tracking, or attributing revenue to specific marketing channels (First/Last/Multi-Touch).
license: MIT
---

# Marketing Analytics

## Quick Start

This skill helps you track marketing performance and calculate ROI. For complete frameworks and dashboards, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**ROI Calculator** (`scripts/roi_calculator.py`):

```bash
python scripts/roi_calculator.py --spend 5000 --revenue 25000
```

Calculates marketing ROI, CAC, and ROAS.

## Execution Checklist

### Building a Marketing Dashboard

- [ ] Define key metrics (leads, MQLs, SQLs, revenue, ROI)
- [ ] Set up tracking (UTM parameters, conversion pixels)
- [ ] Connect data sources (Google Analytics, CRM, ad platforms)
- [ ] Create dashboard (Google Sheets, Data Studio, or BI tool)
- [ ] Set benchmarks for each metric
- [ ] Schedule weekly review meetings
- [ ] Optimize based on data

### Calculating Marketing ROI

- [ ] Track total marketing spend
- [ ] Attribute revenue to campaigns (first-touch, last-touch, multi-touch)
- [ ] Calculate ROI: `(Revenue - Cost) / Cost × 100`
- [ ] Calculate CAC: `Marketing Spend / New Customers
- [ ] Calculate ROAS: `Revenue / Ad Spend`
- [ ] Compare across channels
- [ ] Double down on winners, cut losers

## Key Metrics

- **ROI**: (Revenue - Cost) / Cost × 100 (Target: 300-500%)
- **CAC**: Total Spend / New Customers (Target: <33% of LTV)
- **ROAS**: Revenue / Ad Spend (Target: 3-5x)
- **Conversion Rate**: Conversions / Visitors × 100 (Target: 2-5%)
- **MQL→SQL**: Marketing Qualified → Sales Qualified (Target: 30-50%)

## Quick Wins

- Set up UTM parameters for all campaigns (source, medium, campaign)
- Use conversion pixels (Facebook, Google, LinkedIn)
- Create weekly dashboard review ritual
- Focus on revenue metrics, not just traffic
- Calculate payback period (how long to recoup CAC)

## Resources

For complete dashboards and frameworks:

- [Complete Guide](references/guide.md)

## Related Skills

### From Marketing Toolkit

- [email-marketing](../email-marketing/SKILL.md) - Track email campaign ROI
- [seo-blog-writing](../seo-blog-writing/SKILL.md) - Measure blog performance
- [landing-page-copy](../landing-page-copy/SKILL.md) - Track conversion rates
- [social-media-content](../social-media-content/SKILL.md) - Analyze social metrics

### From Sales Toolkit

- [lead-qualification](../../sales-toolkit/skills/lead-qualification/SKILL.md) - MQL/SQL definitions

### From RevOps Toolkit

- [attribution-roi](../../revenue-operations-toolkit/skills/attribution-roi/SKILL.md) - Multi-touch attribution
- [revenue-analytics](../../revenue-operations-toolkit/skills/revenue-analytics/SKILL.md) - MRR, ARR, churn
- [sales-marketing-alignment](../../revenue-operations-toolkit/skills/sales-marketing-alignment/SKILL.md) - SLAs and definitions
