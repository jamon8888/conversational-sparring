---
name: content-attribution
description: Use when tracking the impact of content on revenue across multiple touchpoints (First-Touch, Last-Touch, Multi-Touch). Trigger when needing to prove content marketing ROI, identifying which blog posts start customer journeys, or calculating influence scores to justify content budget allocation.
license: MIT
---

# Content Attribution

## Quick Start

Track which content contributes to leads, pipeline, and revenue. Supports three attribution models: first-touch (what content started the journey), last-touch (what content closed the deal), and multi-touch (weighted across all touchpoints).

For complete methodology and dashboard templates, see the [Complete Guide](references/attribution-guide.md).

## Execution Checklist

### Set Up Attribution Tracking

- [ ] Define attribution model (first-touch, last-touch, or multi-touch)
- [ ] Export contact interaction data from CRM (CSV format)
- [ ] Map content IDs to CRM touchpoints
- [ ] Run attribution calculation script
- [ ] Generate attribution report
- [ ] Create executive dashboard
- [ ] Share insights with team

## Key Frameworks

- **First-Touch Attribution**: Credits the first content interaction (discovers which content generates awareness)
- **Last-Touch Attribution**: Credits the last content before conversion (shows what closes deals)
- **Multi-Touch Attribution**: Weighted credit across all touchpoints (full journey understanding)
- **Content Influence Scoring**: Assigns influence score (0-100) to each content piece based on journey position

## Attribution Models

### First-Touch (Top of Funnel Focus)

- **Use when**: You want to know what content generates awareness and starts journeys
- **Best for**: Content strategy decisions, topic planning
- **Example**: Blog post "What is Marketing Automation" gets first-touch credit for 50 leads

### Last-Touch (Bottom of Funnel Focus)

- **Use when**: You want to know what content closes deals
- **Best for**: Sales enablement content optimization
- **Example**: Case study gets last-touch credit for $500K in closed deals

### Multi-Touch (Full Journey)

- **Use when**: You need complete picture of content's role across journey
- **Best for**: Executive reporting, budget justification
- **Weighting**: First (20%), Middle (30%), Last (50%) - customizable

## Quick Wins

- **Start simple**: Begin with first-touch or last-touch before multi-touch
- **Use sample data**: Test with example CSV before real CRM data
- **Weekly reviews**: Track attribution weekly, optimize monthly
- **Focus on patterns**: Look for content types and topics that consistently perform
- **Share wins**: Showcase high-performing content to justify budget

## Resources

- [Complete Attribution Guide](references/attribution-guide.md) - Full methodology and best practices
- [Dashboard Templates](assets/templates/) - Executive and detailed dashboards
- [Sample Data](assets/templates/sample-attribution-data.csv) - Test with example data
- [Attribution Scripts](scripts/) - Python scripts for calculation

## Related Skills

### From Content Marketing Toolkit

- [content-strategy](../content-strategy/SKILL.md) - Use attribution data to inform strategy
- [unified-analytics](../unified-analytics/SKILL.md) - Combine with performance analytics
- [campaign-orchestration](../campaign-orchestration/SKILL.md) - Track campaign-level attribution

### From Revenue Operations Toolkit

- [pipeline-forecasting](../../../revenue-operations-toolkit/skills/pipeline-forecasting/SKILL.md) - Forecast based on content influence
  [revenue-analytics](../../../revenue-operations-toolkit/frameworks/Unit-Economics.md) - Complete revenue picture

### From Sales Toolkit

- [lead-qualification](../../../sales-toolkit/skills/lead-qualification/SKILL.md) - Use content engagement for lead scoring
