# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)

# Lead Qualification Mastery

## Overview
Evaluate ICP fit, buying intent, and routing priority for new leads. This skill helps you score prospects, prioritize your pipeline, and focus time on high-value opportunities.

---

## When to Use This Skill

- New inbound or outbound leads need scoring
- Deciding which prospects to pursue first
- Marketing → Sales handoff criteria
- Limited SDR capacity requires prioritization
- Building transparent scoring logic for RevOps

---

## Core Framework: FITS

Score every lead across these four dimensions:

### **F** - Firmographics
**Question:** Does this company match our ICP?

**Criteria to evaluate:**
- Industry (target vs. non-target)
- Company size (employees, revenue)
- Geography (serviceable regions)
- Funding stage / growth trajectory
- Technology stack (for SaaS)

**Scoring:**
- **Strong fit (25 points):** Matches 4-5 criteria perfectly
- **Good fit (15 points):** Matches 3 criteria
- **Weak fit (5 points):** Matches 1-2 criteria
- **No fit (0 points):** Outside ICP entirely

---

### **I** - Intent
**Question:** Are they actively looking for a solution?

**Signals to track:**
- Visiting pricing page
- Downloading comparison guides
- Attending demos or webinars
- Engaging with bottom-of-funnel content
- G2/Capterra research activity
- LinkedIn searches for relevant keywords

**Scoring:**
- **High intent (25 points):** 3+ high-value actions in past 7 days
- **Medium intent (15 points):** 1-2 actions in past 30 days
- **Low intent (5 points):** Top-of-funnel engagement only
- **No intent (0 points):** No engagement tracked

---

### **T** - Timing
**Question:** When do they need a solution in place?

**Questions to ask:**
- "When do you need this solved by?"
- "What's driving the urgency?"
- "What happens if this doesn't get done in the next [timeframe]?"

**Scoring:**
- **Immediate (25 points):** Need solution in <30 days
- **Near-term (15 points):** Need solution in 30-90 days
- **Long-term (5 points):** Exploring for future (>90 days)
- **No timeline (0 points):** "Just researching"

---

### **S** - Solution Match
**Question:** Can we actually solve their problem?

**Criteria:**
- Their pain matches your core value prop
- No technical blockers (integrations, compliance)
- They have resources to implement successfully
- Success metrics are measurable

**Scoring:**
- **Perfect match (25 points):** Core use case, proven playbook
- **Good match (15 points):** Can solve, may need customization
- **Stretch match (5 points):** Edge case, risky fit
- **No match (0 points):** Outside our capabilities

---

## Total Score Thresholds

| Score Range | Classification | Action |
|-------------|---------------|--------|
| **80-100** | Hot Lead | Immediate AE handoff, priority outreach |
| **60-79** | Warm Lead | SDR follow-up within 24 hours, qualify further |
| **40-59** | Cool Lead | Nurture sequence, revisit in 30-60 days |
| **0-39** | Cold Lead | Recycle or disqualify |

---

## Qualification Question Toolkit

### Firmographic Questions
- "Tell me about your company—how big is your team?"
- "What industry are you in?"
- "Where are you based? (for compliance/service regions)"
- "What's your current tech stack?"

### Intent Questions
- "What prompted you to reach out / fill out the form today?"
- "How long have you been looking for a solution like this?"
- "What have you tried so far?"
- "What other solutions are you evaluating?"

### Timing Questions
- "When do you need this in place?"
- "What's driving that timeline?"
- "What happens if you don't solve this by [date]?"
- "Is there a specific event or deadline forcing urgency?"

### Solution Match Questions
- "Walk me through your current process for [X]."
- "What's the biggest problem you're trying to solve?"
- "How are you currently measuring success on this?"
- "What would make this project a success 6 months from now?"

---

## Scoring Worksheet

Use this template to score each lead:

```markdown
# Lead Score: [Company Name]

## Firmographics (max 25 points)
- Industry: [Target/Non-target] - [Points]
- Size: [Employees/Revenue] - [Points]
- Geography: [Region] - [Points]
- Tech stack: [Compatible/Not] - [Points]
**Subtotal:** [X/25]

## Intent (max 25 points)
- Pricing page visit: [Yes/No] - [Points]
- Demo request: [Yes/No] - [Points]
- Content engagement: [High/Med/Low] - [Points]
- Third-party research: [Yes/No] - [Points]
**Subtotal:** [X/25]

## Timing (max 25 points)
- Timeline: [<30 days / 30-90 / 90+ / None] - [Points]
- Urgency driver: [Describe] - [Points]
- Budget cycle: [Q1/Q2/Q3/Q4] - [Points]
**Subtotal:** [X/25]

## Solution Match (max 25 points)
- Primary pain: [Core use case / Edge case] - [Points]
- Technical fit: [Yes / Needs customization / No] - [Points]
- Implementation capacity: [Has resources / Needs help / None] - [Points]
**Subtotal:** [X/25]

---

## TOTAL SCORE: [X/100]
**Classification:** [Hot / Warm / Cool / Cold]
**Recommended Action:** [Action]

## Notes:
[Explainability notes for why this score was assigned]
```

---

## ICP Fit Checklist

Before scoring, verify ICP fit:

**Target Company Profile:**
- [ ] Industry: [List target industries]
- [ ] Size: [X-Y employees OR $X-Y revenue]
- [ ] Geography: [Target regions]
- [ ] Growth stage: [Startup / Scaleup / Enterprise]
- [ ] Tech maturity: [Uses tools like X, Y, Z]

**Target Persona:**
- [ ] Title: [VP Sales, CRO, Sales Ops, etc.]
- [ ] Department: [Sales / Marketing / RevOps]
- [ ] Seniority: [Manager+ / Director+ / VP+]
- [ ] Team size: [Manages X+ people]

**Qualifying Characteristics:**
- [ ] Has budget authority or influence
- [ ] Owns the problem we solve
- [ ] Can champion internally
- [ ] Has pain that maps to our value prop

---

## Routing Logic

Based on score, route leads to appropriate workflows:

### Hot Lead (80-100) → Immediate AE Handoff
**Actions:**
1. Alert AE via Slack/email (SLA: respond within 1 hour)
2. SDR schedules discovery call
3. AE reviews lead profile before call
4. Prioritize above all other leads

**Handoff Requirements:**
- FITS score + notes in CRM
- Intent signals documented
- Recommended talking points
- Next step scheduled

---

### Warm Lead (60-79) → SDR Follow-Up
**Actions:**
1. SDR reaches out within 24 hours
2. Qualify missing FITS dimensions
3. Attempt to elevate to Hot (gather more intent/timing data)
4. If qualified → AE handoff; if not → Nurture

**Follow-Up Sequence:**
- Day 1: Personalized email
- Day 3: LinkedIn connection + message
- Day 7: Phone call
- Day 10: Value-add email (case study/resource)
- Day 14: Final attempt or move to nurture

---

### Cool Lead (40-59) → Nurture Sequence
**Actions:**
1. Add to automated nurture campaign
2. Send monthly value content (blogs, webinars, case studies)
3. Monitor for intent signals (website revisits, content downloads)
4. Re-score quarterly based on new activity

**Nurture Content:**
- Month 1: Industry insights / thought leadership
- Month 2: Customer success story
- Month 3: Product updates / new features
- Month 4: Re-engagement: "Still interested in [X]?"

---

### Cold Lead (0-39) → Recycle or Disqualify
**Actions:**
1. Review for data quality issues (bad email, wrong persona)
2. Disqualify if outside ICP
3. Recycle if timing issue ("Check back in Q3")
4. Remove from active pipeline

---

## Playbook Variations

### Inbound Lead Scoring
**Higher weight on:**
- Intent (they came to you)
- Timing (what prompted action)

**Lower weight on:**
- Firmographics (if intent is strong, stretch ICP acceptable)

---

### Outbound Lead Scoring
**Higher weight on:**
- Firmographics (you're targeting specific ICPs)
- Solution match (prospecting based on known pain)

**Lower weight on:**
- Intent (you're creating demand, not responding to it)

---

### Product-Qualified Lead (PQL) Scoring
**Additional signals to track:**
- Free trial signup
- Feature usage (power users vs. tire-kickers)
- Invite team members
- Hit usage thresholds
- Bumped into paywall / limits

**PQL-specific scoring:**
```
- Trial signup: +10
- Invited 3+ users: +15
- Used core feature 5+ times: +20
- Hit usage limit: +25 (high buying intent)
- Team size >10: +10
```

---

## Intent Signal Decoder

Map intent signals to likely pain points:

| Signal | Likely Pain | Recommended Approach |
|--------|-------------|----------------------|
| Pricing page visit | Budget/ROI evaluation | Send ROI calculator, pricing one-pager |
| Demo request | Actively evaluating | Schedule demo ASAP, high priority |
| Competitor comparison download | Shopping around | Send battlecard, competitive case study |
| G2 reviews research | Vendor selection | Share customer reviews, testimonials |
| Blog: "How to [X]" | Learning mode, early stage | Nurture with educational content |
| Webinar attendance | Engaged, may be mid-funnel | Follow up with case study |
| Job posting for [role] | Scaling, likely pain point | "Saw you're hiring—here's how we help" |

---

## Handoff Checklist (SDR → AE)

Before handing qualified lead to AE, verify:

- [ ] FITS score documented (with explainability notes)
- [ ] CRM fields complete:
  - Company name, size, industry
  - Contact: name, title, email, phone
  - Pain points identified
  - Urgency / timeline
  - Budget status
  - Competition / alternatives
  - Next step scheduled
- [ ] Discovery call booked (or intro email sent)
- [ ] Recommended talking points attached
- [ ] AE notified via Slack/email
- [ ] SLA timer started (AE must respond within [X] hours)

---

## Tips for Accurate Scoring

### Review Weights Quarterly
- Work with RevOps to validate scoring criteria
- Analyze which leads converted → adjust weights
- Update ICP definition as company evolves

### Keep Explainability Notes
- Why did this lead score 85 vs. 65?
- What signals drove the score?
- Helps AEs trust automated scoring

### Pair Scoring with QA Sampling
- Manually review 10% of scored leads
- Catch bad data feeds (wrong company info, spam)
- Identify edge cases to improve model

### Share Top Intent Triggers Weekly
- "This week's top signals: Pricing page visits +40%, demo requests +25%"
- Helps marketing reinforce high-intent channels
- Sales can prioritize accordingly

---

## Qualification Frameworks (Cross-Reference)

This skill uses FITS scoring. For deeper qualification during calls, reference:

- **MEDDICC** → See `discovery-calls.md`
- **BANT** → See `discovery-calls.md`
- **SPIN** → See `discovery-calls.md`

Use FITS for initial scoring, then overlay MEDDICC/BANT during discovery calls.

---

## Common Mistakes to Avoid

**Over-qualifying**
- Problem: Disqualifying good leads too early
- Fix: Err on side of qualifying; let discovery call reveal truth

**Under-qualifying**
- Problem: Wasting AE time on bad-fit leads
- Fix: Use FITS rigorously; don't pass along "maybes"

**Ignoring explainability**
- Problem: AEs don't trust scores, ignore them
- Fix: Always include notes explaining why a lead scored high/low

**Static scoring**
- Problem: Scoring doesn't evolve with business
- Fix: Review quarterly, adjust weights, update ICP

**No feedback loop**
- Problem: Don't know which scores convert best
- Fix: Track conversion rates by score range, optimize

---

## Success Metrics

Track these to validate scoring accuracy:

- **Lead-to-opportunity conversion rate by score:**
  - Hot (80-100): Target 40-60%
  - Warm (60-79): Target 15-25%
  - Cool (40-59): Target 5-10%

- **Speed to contact:**
  - Hot: <1 hour
  - Warm: <24 hours
  - Cool: <7 days

- **AE acceptance rate:**
  - Target: 80%+ of Hot leads accepted by AEs
  - If <80%, scoring criteria needs refinement

---

## Related Skills

- **Discovery Calls** - Deeper qualification during sales calls (MEDDICC/BANT)
- **Cold Outreach** - Targeting high-FITS prospects for outbound
- **Objection Handling** - Converting borderline leads by addressing concerns
- **Social Selling** - Gathering intent signals from LinkedIn activity
