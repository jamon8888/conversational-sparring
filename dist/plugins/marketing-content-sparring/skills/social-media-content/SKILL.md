---
name: social-media-content
description: Use when creating engaging social media content optimized for platform-specific formats and character limits. Trigger when needing to validate posts for LinkedIn/Twitter (scripts/platform_validator.py), applying Hook-Story-Lesson formulas, or scheduling content during peak engagement times (e.g., 7-9am for LinkedIn).
license: MIT
---

# Social Media Content

## Quick Start

This skill helps you create engaging social media content across LinkedIn, Twitter, Facebook, and Instagram. For complete strategies and post templates, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Platform Validator** (`scripts/platform_validator.py`):

```bash
python scripts/platform_validator.py linkedin "your post content"
```

Validates character counts and format for each platform.

## Execution Checklist

### Creating a Social Media Post

- [ ] Choose platform (LinkedIn, Twitter, Facebook, Instagram)
- [ ] Define goal (engagement, traffic, leads, brand awareness)
- [ ] Write hook (first line grabs attention)
- [ ] Structure for scannability (short paragraphs, line breaks)
- [ ] Add value (educate, entertain, or inspire)
- [ ] Include CTA (comment, share, click link)
- [ ] Add relevant hashtags (3-5 max)
- [ ] Validate format with platform_validator.py
- [ ] Schedule for optimal time
- [ ] Engage with comments within first hour

## Platform Specifications

- **LinkedIn**: 3,000 chars max, 1,300 optimal; Professional tone; 3-5 hashtags
- **Twitter/X**: 280 chars limit; Conversational; 1-2 hashtags; Threads for longer content
- **Facebook**: 40-80 chars optimal for engagement; Visual-first; Ask questions
- **Instagram**: 2,200 chars max, 138-150 optimal; Visual storytelling; 20-30 hashtags

## Content Formulas

- **Hook-Story-Lesson**: Start bold → Share experience → Extract takeaway
- **Problem-Solution**: Identify pain → Offer fix
- **List Post**: "5 ways to...", "3 mistakes...", "7 tips for..."
- **Hot Take**: Controversial opinion + backup reasoning
- **Question**: Ask engaging question to drive comments

## Quick Wins

- Post during peak times (LinkedIn: 7-9am, 5-6pm; Twitter: 12-3pm)
- Use first line as hook (most visible in feed)
- Add line breaks for readability (dense text = scroll past)
- Engage in first hour (algorithm boost)
- Repurpose blog content into bite-sized posts

## Resources

For complete strategies and templates:

- [Complete Guide](references/guide.md)

## Related Skills

### From Marketing Toolkit

- [content-strategy](../content-strategy/SKILL.md) - Plan social content calendar
- [seo-blog-writing](../seo-blog-writing/SKILL.md) - Repurpose blog as social posts
- [email-marketing](../email-marketing/SKILL.md) - Promote email list on social
- [marketing-analytics](../marketing-analytics/SKILL.md) - Track social metrics

### From Sales Toolkit

- [social-selling](../../sales-toolkit/skills/social-selling/SKILL.md) - LinkedIn outreach and engagement
- [cold-outreach](../../sales-toolkit/skills/cold-outreach/SKILL.md) - Social + email combo

### From RevOps Toolkit

- [attribution-roi](../../revenue-operations-toolkit/skills/attribution-roi/SKILL.md) - Track social campaign ROI
