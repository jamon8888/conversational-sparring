---
name: email-marketing
description: Use when writing high-converting newsletters, promotional campaigns, or welcome series. Trigger when needing to check subject lines for spam triggers (scripts/spam_checker.py), applying the PAS (Problem-Agitate-Solution) framework to email copy, or optimizing open/click rates through mobile-first design and A/B testing.
license: MIT
---

# Email Marketing

## Quick Start

This skill helps you create effective email campaigns. For detailed frameworks and examples, see the [Email Marketing Guide](references/email-marketing-guide.md).

## Tools & Scripts

### Spam Checker

Check subject lines for spam triggers before sending:

```bash
python scripts/spam_checker.py "Your subject line here"
```

### Newsletter Template

Responsive HTML template ready to customize:

```
assets/newsletter_template.html
```

## Execution Checklist

### Writing a Newsletter

- [ ] Define your audience segment
- [ ] Choose newsletter type (value, promotion, update)
- [ ] Write compelling subject line (test with spam checker)
- [ ] Structure email: Personal intro → Value → CTA → P.S.
- [ ] Add one clear call-to-action
- [ ] Test on mobile before sending
- [ ] Track: open rate, click rate, conversions

### Building a Welcome Series

- [ ] Map out 5-email sequence (Days 0, 2, 4, 7, 10)
- [ ] Email 1: Deliver lead magnet + intro
- [ ] Email 2: Your story / credibility
- [ ] Email 3: Best resources
- [ ] Email 4: Social proof / case studies
- [ ] Email 5: Soft pitch / next step
- [ ] Set up automation in ESP
- [ ] Monitor open rates per email

### Creating a Nurture Sequence

- [ ] Identify trigger (behavior, segment, tag)
- [ ] Define sequence goal (educate, convert, re-engage)
- [ ] Map email flow (5-7 emails recommended)
- [ ] Use PAS framework: Problem → Agitate → Solution
- [ ] Include social proof (testimonials, case studies)
- [ ] Clear next step in each email
- [ ] Set appropriate delays between emails
- [ ] Test and optimize based on metrics

### Running a Promotional Campaign

- [ ] Plan 5-7 email sequence (7-10 days)
- [ ] Email 1: Announce what's coming
- [ ] Email 2: Educate why it matters
- [ ] Email 3: Social proof (testimonials)
- [ ] Email 4: Handle objections
- [ ] Email 5: Create urgency (deadline)
- [ ] Email 6: Last chance (24 hours)
- [ ] Email 7: Final reminder (cart closing)
- [ ] Track conversions at each stage

## Key Frameworks

### Email Types

- **Welcome Series**: First 5 emails to new subscribers
- **Newsletter**: Weekly value + promotion (80/20 split)
- **Nurture Sequence**: Behavior-triggered automation
- **Promotional Campaign**: Product launch or sale (5-7 emails)

### Subject Line Formulas

- Curiosity: "This changed how I [do thing]"
- Urgency: "Last chance: [Offer] ends tonight"
- Benefit: "How to [outcome] in [timeframe]"
- Personal: "[Name], question for you"

### Copywriting Pattern (PAS)

1. **Problem**: Identify pain point
2. **Agitate**: Make it worse
3. **Solution**: Present your offer

### Metrics Benchmarks

- **Open Rate**: 20-30% (good), 30%+ (excellent)
- **Click Rate**: 2-5% (good), 5%+ (excellent)
- **Unsubscribe**: <0.5% (healthy)

## Quick Wins

### Improve Open Rates

- Test 3 subject line variations
- Personalize sender name
- Optimize send time (test morning vs. evening)
- Clean list (remove inactive subscribers)

### Improve Click Rates

- Use one clear CTA
- Add urgency ("Limited time")
- Show social proof ("500+ entrepreneurs use this")
- Link to high-value content

### Reduce Unsubscribes

- Set expectations upfront (frequency, content)
- Segment your audience
- Provide preference center (choose topics)
- Maintain 80/20 value-to-promotion ratio

## Resources

For complete strategies, examples, and detailed frameworks:

- [Email Marketing Guide](references/email-marketing-guide.md)
- [Email Conversion Sequence](references/email-conversion-sequence.md)

## Related Skills

### From Marketing Toolkit

- [content-strategy](../content-strategy/SKILL.md) - Plan your email content calendar
- [landing-page-copy](../landing-page-copy/SKILL.md) - Create pages where email clicks lead
- [lead-magnets](../lead-magnets/SKILL.md) - Build your email list with valuable offers
- [social-media-content](../social-media-content/SKILL.md) - Promote your email list on social
- [marketing-analytics](../marketing-analytics/SKILL.md) - Track email performance metrics

### From Sales Toolkit

- [cold-outreach](../../sales-toolkit/skills/cold-outreach/SKILL.md) - Cold email templates and strategies
- [follow-up-sequences](../../sales-toolkit/skills/follow-up-sequences/SKILL.md) - Multi-touch email cadences

### From RevOps Toolkit

- [attribution-roi](../../revenue-operations-toolkit/skills/attribution-roi/SKILL.md) - Track email campaign attribution
- [sales-marketing-alignment](../../revenue-operations-toolkit/skills/sales-marketing-alignment/SKILL.md) - Define MQL criteria for email leads
