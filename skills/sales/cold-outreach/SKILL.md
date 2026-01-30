---
name: cold-outreach
description: Use when writing cold emails or LinkedIn messages to prospects, researching personalization angles, or improving response rates. Trigger when needing to find deliverable email addresses (scripts/email_validator.py), checking email personalization scores (scripts/personalization_checker.py), or applying the SPARK framework for outreach campaigns.
license: MIT
---

# Cold Outreach

## Quick Start

This skill helps you write cold emails and LinkedIn messages that get responses. For complete frameworks and templates, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Email Validator** (`scripts/email_validator.py`):

```bash
python scripts/email_validator.py emails.csv
```

Validates email addresses and checks deliverability.

**Personalization Checker** (`scripts/personalization_checker.py`):

```bash
python scripts/personalization_checker.py email.txt
```

Analyzes personalization level and suggests improvements.

## Execution Checklist

### Writing Cold Emails

- [ ] Research prospect (LinkedIn, company site, recent news)
- [ ] Find personalization angle (mutual connection, recent achievement)
- [ ] Write subject line (curiosity or relevance, 30-50 chars)
- [ ] Personalize opening line (reference their work)
- [ ] State value prop (what's in it for them)
- [ ] Keep body to 50-100 words
- [ ] Include ONE clear CTA
- [ ] Add P.S. with social proof or urgency
- [ ] Validate email address
- [ ] Test personalization score
- [ ] Send and track response

## Key Frameworks

- **SPARK**: Subject → Personalize → Agitate → Relevant value → Keep-it-simple CTA
- **Subject Lines**: `[Name], quick question` or `[Trigger event] + [value prop]`
- **Opening**: Reference specific work/achievement
- **Value Prop**: "Help you [achieve X] without [pain Y]"
- **CTA**: One question or one action

## Metrics Benchmarks

- **Reply rate**: 10-15% (excellent), 5-10% (good)
- **Meeting booked**: 25-30% of replies
- **Email length**: 50-100 words optimal
- **Follow-ups**: 80% of responses come after 2-5 touches

## Quick Wins

- Personalize first line (mention their content, company news)
- Keep subject under 50 chars for mobile
- Send Tuesday-Thursday, 8-10am their local time
- Follow up 2-3 times (48 hrs, then 1 week gaps)
- Use "you" more than "I" or "we"

## Resources

For complete templates and frameworks:

- [Complete Guide](references/guide.md)
- [SPARK Framework](references/spark-framework.md)

## Related Skills

### From Sales Toolkit

- [follow-up-sequences](../follow-up-sequences/SKILL.md) - Multi-touch cadences
- [discovery-calls](../discovery-calls/SKILL.md) - What to do when they reply
- [social-selling](../social-selling/SKILL.md) - Warm up prospects on LinkedIn first

### From Marketing Toolkit

- [email-marketing](../../marketing-toolkit/skills/email-marketing/SKILL.md) - Email best practices
- [landing-page-copy](../../marketing-toolkit/skills/landing-page-copy/SKILL.md) - Landing page for email links

### From RevOps Toolkit

- [sales-marketing-alignment](../../revenue-operations-toolkit/skills/sales-marketing-alignment/SKILL.md) - MQL/SQL definitions
