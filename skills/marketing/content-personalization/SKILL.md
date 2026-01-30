---
name: content-personalization
description: Use when creating personalized content variations based on audience segments, firmographics, or behavioral data. Trigger when needing dynamic content adaptation (scripts/variant_generator.py), setting up A/B testing frameworks for segment-specific messaging, or implementing a personalization pyramid to improve conversion rates (15-80% lift).
license: MIT
---

# Content Personalization

## Quick Start

Generate personalized content variations for different audience segments. Define segments, create personalization rules, test variations, and track performance to optimize conversion rates.

For complete personalization strategies and testing frameworks, see the [Complete Guide](references/personalization-guide.md).

## Execution Checklist

### Personalize Your Content

- [ ] Define audience segments (persona, industry, company size, behavior)
- [ ] Create segment-specific content variations
- [ ] Set up A/B testing framework
- [ ] Implement personalization rules
- [ ] Deploy variations to channels
- [ ] Track performance by segment
- [ ] Optimize based on data

## Key Frameworks

- **Segmentation Strategy**: Divide audience by persona, firmographics, behavior, lifecycle stage
- **Dynamic Content Rules**: If/then logic for showing different content to different segments
- **A/B Testing Methodology**: Test one variable at a time, run until statistical significance
- **Personalization Pyramid**: Basic (name) → Intermediate (industry) → Advanced (behavior-based)

## Personalization Levels

### Level 1: Basic (Name & Company)

- "Hi [First Name]"
- "[Company] can benefit from..."
- **Conversion lift**: 5-10%

### Level 2: Firmographic (Industry, Size, Geography)

- Industry-specific examples
- Company size-appropriate pricing
- Regional references
- **Conversion lift**: 15-25%

### Level 3: Behavioral (Actions & Engagement)

- Content based on previous views
- Product recommendations based on behavior
- Lifecycle stage-specific messaging
- **Conversion lift**: 30-50%

### Level 4: Predictive (AI-Driven)

- ML-predicted preferences
- Next-best content recommendations
- Personalized journey orchestration
- **Conversion lift**: 50-80%

## Quick Wins

- **Start with firmographics** - Industry and company size are easy and effective
- **Test headlines first** - 80% of impact comes from headline personalization
- **One variable at a time** - Don't change 10 things, test systematically
- **Document learnings** - Track what works for each segment
- **Scale winners** - Apply winning personalization patterns across content

## Resources

- [Complete Personalization Guide](references/personalization-guide.md) - Full methodology
- [Segment Templates](assets/templates/) - Pre-defined audience segments
- [A/B Testing Framework](assets/templates/ab-testing-template.yaml) - Testing methodology
- [Personalization Scripts](scripts/) - Variant generation tools

## Related Skills

### From Content Marketing Toolkit

- [content-strategy](../content-strategy/SKILL.md) - Segment-based content planning
- [landing-page-copy](../landing-page-copy/SKILL.md) - Personalized landing pages
- [email-marketing](../email-marketing/SKILL.md) - Segment-based email campaigns
- [unified-analytics](../unified-analytics/SKILL.md) - Performance by segment

### From Sales Toolkit

- [lead-qualification](../../../sales-toolkit/skills/lead-qualification/SKILL.md) - Segment leads for personalization
