# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Experiment Design: Build a Data-Driven Growth Engine

## Overview

Experiment design is the systematic approach to testing growth hypotheses, measuring impact, and making data-driven decisions. For solo entrepreneurs and small teams, proper experiment design transforms random tactics into a repeatable growth playbook. This skill teaches you to structure tests with clear hypotheses, metrics, guardrails, and analysis frameworks.

**When to use this skill:**
- You have multiple growth ideas but unsure which to prioritize
- You need to prove (or disprove) assumptions about your customers
- Leadership wants data-driven decisions, not gut feelings
- You're scaling a tactic and need to optimize conversion rates
- You want to build a culture of experimentation
- You're wasting resources on unvalidated ideas
- You need to accelerate learning velocity (fail fast, scale winners)

**Why experiment design matters:**
- **Reduce risk:** Test before scaling (avoid $50K mistakes)
- **Faster learning:** Validate assumptions in weeks, not months
- **Compound growth:** Small wins (2-5% lifts) compound to 50-100% annual growth
- **Team alignment:** Shared framework for evaluating ideas
- **Resource efficiency:** Focus on high-impact experiments
- **Institutional knowledge:** Document what works (and doesn't)

**The cost of poor experiment design:**
- 70% of growth experiments fail - but poor design means you don't learn why
- Waste 30-50% of growth budget on unvalidated tactics
- Ship changes that hurt metrics (because you didn't measure guardrails)
- Slow decision-making (unclear success criteria = endless debates)
- Miss opportunities (don't know which winners to scale)

---

## The Experiment Canvas

### Core Components

Every experiment needs these five elements:

**1. Problem Statement**
```
What customer problem or business challenge are we solving?

GOOD EXAMPLE:
"40% of trial users never complete onboarding. We believe the 8-step setup is overwhelming."

BAD EXAMPLE:
"Onboarding needs improvement."

WHY GOOD IS BETTER:
- Specific metric (40% incompletion rate)
- Clear hypothesis about root cause (8 steps)
- Testable and measurable
```

**2. Hypothesis**
```
STRUCTURE:
If we [CHANGE] for [AUDIENCE], we expect [METRIC] to [DIRECTION] because [ASSUMPTION].

EXAMPLES:

Onboarding:
"If we reduce onboarding from 8 steps to 3 steps for all trial users, we expect onboarding completion rate to increase from 60% to 75% because users get overwhelmed by too many steps."

Pricing:
"If we add a $49/month tier between Free and $99/month for SMB customers, we expect free-to-paid conversion to increase from 12% to 18% because current pricing gap is too large."

Email:
"If we send a mid-trial check-in email on day 7 for trial users who haven't logged in, we expect trial-to-paid conversion to increase from 15% to 20% because early engagement predicts conversion."
```

**3. Success Metrics**
```
PRIMARY METRIC (North Star):
The one metric that defines success

Examples:
- Trial-to-paid conversion rate (15% → 20%)
- Revenue per visitor ($2.50 → $3.00)
- Activation rate (completed setup within 7 days)
- NPS score (35 → 45)

SECONDARY METRICS (Supporting):
Metrics that explain how you moved the primary metric

Examples:
- Email open rate, click rate
- Time to complete onboarding
- Feature adoption rate
- Session duration

GUARDRAIL METRICS (Must not hurt):
Metrics you monitor to ensure you're not breaking things

Examples:
- Churn rate (must stay <3%)
- Support ticket volume (must not increase >10%)
- Page load time (must stay <2 seconds)
- Revenue per customer (must not decrease)
```

**4. Variants**
```
CONTROL (A):
Current experience (baseline)

VARIANT B:
Single change to test

VARIANT C (optional):
Alternative approach

EXAMPLE (Pricing Page):
Control A: Current pricing page (3 tiers: Free, $49, $99)
Variant B: 4 tiers (Free, $29, $69, $149)
Variant C: 2 tiers (Free, $79 all-inclusive)

BEST PRACTICE:
Test one variable at a time (unless doing multivariate testing)
Don't test 5 variants at once (reduces statistical power)
```

**5. Sample Size & Duration**
```
MINIMUM SAMPLE SIZE:
Use statistical calculator to determine sample needed

Example calculation:
- Baseline conversion: 15%
- Expected lift: +5 percentage points (to 20%)
- Statistical significance: 95%
- Statistical power: 80%
- Result: Need 1,482 users per variant (2,964 total)

DURATION:
How long to run experiment?

Factors:
- Traffic volume (1,000 visitors/day = 3 days, 100 visitors/day = 30 days)
- Business cycles (B2B: run for full week, Ecommerce: include weekend)
- Minimum 1-2 full business cycles (capture day-of-week variance)

EXAMPLE:
Traffic: 500 trial users/week
Sample needed: 1,482 per variant
Duration: 3 weeks (1,500 users per variant)
```

---

## ICE/RICE Prioritization Framework

### ICE Scoring (Simple Prioritization)

**Formula:**
```
ICE Score = (Impact × Confidence × Ease) / 3

IMPACT (1-10):
How much will this move your North Star metric?
1 = Minimal impact (<1% lift)
5 = Moderate impact (2-5% lift)
10 = Massive impact (>10% lift)

CONFIDENCE (1-10):
How confident are you this will work?
1 = Total guess (no data)
5 = Some evidence (qualitative feedback)
10 = Strong evidence (quantitative data, proven elsewhere)

EASE (1-10):
How easy is this to implement?
1 = Extremely difficult (3+ months, full eng team)
5 = Moderate effort (2-4 weeks, 1 developer)
10 = Very easy (1-2 days, no-code or simple change)

EXAMPLE SCORING:

Experiment: Simplify onboarding (8 steps → 3 steps)
- Impact: 8 (expect 60% → 75% completion = +25% relative lift)
- Confidence: 7 (user research shows frustration, similar companies saw lifts)
- Ease: 6 (requires front-end work, but straightforward)
- ICE Score: (8 + 7 + 6) / 3 = 7.0

Experiment: Add live chat to pricing page
- Impact: 4 (might help some hesitant buyers, but small % of traffic)
- Confidence: 5 (mixed results in case studies)
- Ease: 9 (install Intercom widget, 1 hour)
- ICE Score: (4 + 5 + 9) / 3 = 6.0

DECISION: Prioritize onboarding simplification (7.0 > 6.0)
```

**ICE Scoring Template:**
```
| Experiment | Impact | Confidence | Ease | ICE Score | Priority |
|------------|--------|------------|------|-----------|----------|
| Onboarding reduction | 8 | 7 | 6 | 7.0 | 1 |
| Pricing tier addition | 7 | 6 | 5 | 6.0 | 2 |
| Email nurture sequence | 6 | 7 | 8 | 7.0 | 1 (tie) |
| Live chat on pricing | 4 | 5 | 9 | 6.0 | 2 |
| Referral program launch | 9 | 4 | 3 | 5.3 | 3 |
```

### RICE Scoring (Advanced Prioritization)

**Formula:**
```
RICE Score = (Reach × Impact × Confidence) / Effort

REACH (number):
How many users will this affect per time period (month/quarter)?
Example: 500 trial users per month

IMPACT (0.25, 0.5, 1, 2, 3):
Massive impact = 3
High impact = 2
Medium impact = 1
Low impact = 0.5
Minimal impact = 0.25

CONFIDENCE (%):
100% = Proven (you've tested this before or have strong data)
80% = High confidence (strong evidence)
50% = Medium confidence (some evidence)
20% = Low confidence (educated guess)

EFFORT (person-weeks):
How many weeks of work (1 person full-time)?
Examples:
- No-code change: 0.25 weeks (few hours)
- Simple feature: 1 week
- Medium feature: 4 weeks
- Large project: 12+ weeks

EXAMPLE SCORING:

Experiment: Email nurture sequence (5 emails for inactive trials)
- Reach: 200 inactive trials per month
- Impact: 2 (high impact, expect 10-15% conversion from 0%)
- Confidence: 80% (proven tactic, we have content ready)
- Effort: 1 week (write emails, set up automation)
- RICE Score: (200 × 2 × 0.80) / 1 = 320

Experiment: Referral program with rewards
- Reach: 50 customers per month (assume 30% participate)
- Impact: 3 (massive, could drive 20-30% of new signups)
- Confidence: 50% (works for some companies, not all)
- Effort: 6 weeks (build referral system, design rewards)
- RICE Score: (50 × 3 × 0.50) / 6 = 12.5

DECISION: Prioritize email nurture (320 >> 12.5)
```

**RICE Scoring Template:**
```
| Experiment | Reach | Impact | Conf % | Effort | RICE Score | Priority |
|------------|-------|--------|--------|--------|------------|----------|
| Email nurture | 200 | 2 | 80% | 1 | 320 | 1 |
| Onboarding reduction | 500 | 2 | 70% | 3 | 233 | 2 |
| Add pricing tier | 150 | 1 | 60% | 2 | 45 | 3 |
| Referral program | 50 | 3 | 50% | 6 | 12.5 | 4 |
```

---

## Hypothesis Testing Framework

### Writing Strong Hypotheses

**Bad Hypotheses:**
```
❌ "We should improve the onboarding flow."
Why bad: No change specified, no metric, no target

❌ "Adding testimonials will increase conversions."
Why bad: Where? For whom? By how much?

❌ "Users want more features."
Why bad: Not testable, vague, no success criteria
```

**Good Hypotheses:**
```
✅ "If we add customer testimonials to the pricing page for visitors from paid ads, we expect trial sign-up rate to increase from 8% to 10% because paid traffic is cold and needs social proof."

✅ "If we send a welcome email with a setup checklist within 5 minutes of sign-up for all trial users, we expect onboarding completion rate to increase from 60% to 75% because users need guidance on what to do first."

✅ "If we change the CTA from 'Start Free Trial' to 'Get Started Free' on the homepage for all visitors, we expect click-through rate to increase from 12% to 15% because 'trial' implies credit card requirement."
```

### Assumption Mapping

**Every hypothesis contains assumptions. Surface them:**

```
HYPOTHESIS:
"If we add a $49/month tier for SMB customers, we expect free-to-paid conversion to increase from 12% to 18%."

ASSUMPTIONS:
1. Current $99/month tier is too expensive for SMBs
2. SMBs represent 60%+ of our trial user base
3. $49 tier won't cannibalize $99 tier (downgrades)
4. $49 tier has sufficient margins (>70% gross margin)
5. Feature set for $49 tier provides enough value
6. SMBs will stay long enough to recover CAC at $49/month

VALIDATION:
- Assumption 1: Survey trials (asking about price objections)
- Assumption 2: Analyze trial data (company size distribution)
- Assumption 3: Model cannibalization risk (how many $99 customers fit $49 profile?)
- Assumption 4: Calculate unit economics (hosting costs, support load)
- Assumption 5: User interviews (what features are must-haves?)
- Assumption 6: Cohort analysis (retention by customer segment)
```

---

## Statistical Significance & Sample Size

### Understanding Statistical Significance

**Significance Level (Alpha):**
```
Alpha = 5% (95% confidence) is standard
Means: 5% chance the result is due to random chance

INTERPRETATION:
p-value < 0.05: Result is statistically significant (likely real)
p-value > 0.05: Result is not significant (could be random chance)

EXAMPLE:
Control: 15% conversion (150 conversions / 1,000 users)
Variant: 18% conversion (180 conversions / 1,000 users)
p-value: 0.03 (3%)

CONCLUSION: Statistically significant (p < 0.05)
Variant B is likely better than Control A
```

**Statistical Power:**
```
Power = 80% is standard
Means: 80% chance of detecting a real difference if it exists

Low power (50-70%): Might miss real differences (false negatives)
High power (80-90%): Reliably detects real differences
```

**Minimum Detectable Effect (MDE):**
```
MDE = Smallest change you care about detecting

EXAMPLE:
Baseline: 15% conversion
MDE: 2 percentage points (to 17%)

Sample size calculator:
- Baseline: 15%
- MDE: 2 percentage points
- Significance: 95%
- Power: 80%
- Result: Need 3,842 users per variant

IF you only expect small lifts (0.5 percentage points), you need MUCH larger samples:
- MDE: 0.5 percentage points (to 15.5%)
- Result: Need 61,475 users per variant (impractical for small companies)

RECOMMENDATION:
Set MDE to 15-25% relative lift (easier to detect)
15% baseline × 20% lift = 18% target (3 percentage points)
```

### Sample Size Calculation

**Use online calculators:**
- Evan's Awesome A/B Tools: https://www.evanmiller.org/ab-testing/sample-size.html
- Optimizely Sample Size Calculator
- VWO A/B Test Duration Calculator

**Example Calculation:**
```
INPUT:
Baseline conversion rate: 10%
Minimum detectable effect: 2 percentage points (to 12%)
Statistical significance: 95%
Statistical power: 80%

OUTPUT:
Sample size needed: 2,863 users per variant (5,726 total)

SCENARIO:
Traffic: 500 visitors/day
Duration: 5,726 / 500 = 11.5 days (round to 14 days for full 2 weeks)

CONCLUSION:
Run experiment for 2 weeks to reach statistical significance
```

**Sample Size by Expected Lift:**
```
For 10% baseline conversion:

+1 percentage point (10% → 11%): 15,000+ users per variant
+2 percentage points (10% → 12%): 2,863 users per variant
+3 percentage points (10% → 13%): 1,240 users per variant
+5 percentage points (10% → 15%): 459 users per variant

INSIGHT:
Larger lifts require smaller samples (easier to detect)
Small lifts require massive samples (need high traffic)

FOR LOW-TRAFFIC SITES:
Focus on high-impact experiments (expect 20-50% lifts)
Don't waste time on tiny optimizations (1-2% lifts need too much traffic)
```

---

## Guardrail Metrics: Prevent Unintended Consequences

### What Are Guardrails?

**Definition:** Metrics you monitor to ensure your experiment doesn't break other parts of the business.

**Example Scenario:**
```
EXPERIMENT:
Reduce trial from 30 days to 14 days (create urgency)

PRIMARY METRIC:
Trial-to-paid conversion rate

WHAT COULD GO WRONG:
- Users don't have enough time to evaluate
- Conversion rate increases, but churn rate spikes (low-quality conversions)
- Support tickets increase (rushed decisions)

GUARDRAIL METRICS:
1. Churn rate (first 90 days): Must stay <5%
2. Support tickets per customer: Must not increase >10%
3. NPS score: Must stay >30
4. Activation rate (completed setup): Must not decrease

IF GUARDRAILS TRIP:
Pause or rollback experiment, even if primary metric improved
```

### Common Guardrail Metrics

**Revenue Guardrails:**
```
- Revenue per customer (ARPA): Ensure you're not attracting lower-value customers
- Average contract value (ACV): Monitor deal size
- MRR/ARR: Overall revenue shouldn't drop
- Gross margin %: Ensure costs don't spike
```

**Retention Guardrails:**
```
- Churn rate (monthly): Must not increase
- Customer lifetime (months): Should stay stable or increase
- Net Revenue Retention (NRR): Should stay >100%
- 90-day retention rate: Early indicator of long-term retention
```

**Engagement Guardrails:**
```
- Daily/weekly active users: Engagement shouldn't drop
- Session duration: Quality of engagement
- Feature usage rate: Core features still being used
- Time to value: How fast users get value
```

**Quality Guardrails:**
```
- Customer satisfaction (CSAT/NPS): User sentiment
- Support ticket volume: Indicator of friction or bugs
- Page load time: Performance shouldn't degrade
- Error rate: Technical quality
```

**Example Guardrail Dashboard:**
```
EXPERIMENT: Reduce onboarding from 8 steps to 3 steps

PRIMARY METRIC:
Onboarding completion rate: 60% → 75% ✅ +25% (statistically significant)

GUARDRAIL METRICS:
✅ Churn rate (Month 1): 3.2% (was 3.0%) - within acceptable range (+0.2pp)
✅ Feature adoption rate: 68% (was 65%) - stable
⚠️ Support tickets: 45/week (was 35/week) - increased +29%
✅ NPS: 42 (was 40) - stable

ANALYSIS:
Primary metric improved significantly
Support tickets increased (users skipping important setup steps)

DECISION:
Modify experiment: Keep 3-step onboarding, but add contextual help tooltips
Re-test with guardrails in place
```

---

## Experiment Lifecycle

### Phase 1: Design (Week 1)

**Checklist:**
- [ ] Write problem statement (what are we solving?)
- [ ] Write hypothesis (If/For/Expect/Because format)
- [ ] Define primary metric, secondary metrics, guardrails
- [ ] Design variants (control, variant B, variant C)
- [ ] Calculate sample size and duration needed
- [ ] Get stakeholder alignment (engineering, product, leadership)
- [ ] Document experiment brief (Notion, Confluence, Google Doc)

**Experiment Brief Template:**
```
EXPERIMENT: [Name]
OWNER: [Your name]
STATUS: Design
PRIORITY: [ICE/RICE score]

PROBLEM:
[1-2 sentences describing the problem]

HYPOTHESIS:
If we [change] for [audience], we expect [metric] to [direction] because [assumption].

VARIANTS:
- Control A: [Description]
- Variant B: [Description]
- Variant C: [Description]

METRICS:
- Primary: [Metric] (baseline: X%, target: Y%)
- Secondary: [Metric 1], [Metric 2]
- Guardrails: [Metric 1] (must not exceed Z%), [Metric 2]

SAMPLE SIZE & DURATION:
- Sample needed: X users per variant
- Expected duration: Y days/weeks
- Launch date: [Date]
- Analysis date: [Date]

ASSUMPTIONS:
1. [Assumption 1]
2. [Assumption 2]

DEPENDENCIES:
- Engineering: [What needs to be built?]
- Design: [What needs to be designed?]
- Data: [What tracking needs to be added?]

SUCCESS CRITERIA:
- Primary metric improves by >X% (statistically significant, p<0.05)
- No guardrail metrics trip
```

### Phase 2: Build (Week 2)

**Checklist:**
- [ ] Design mockups/wireframes (if UI changes)
- [ ] Write copy variations
- [ ] Set up tracking (events, goals, analytics)
- [ ] Build variants (engineering work)
- [ ] QA test all variants (ensure they work)
- [ ] Set up experiment in tool (Optimizely, Google Optimize, LaunchDarkly)
- [ ] Validate data is flowing correctly (spot-check analytics)

**Instrumentation Checklist:**
```
EVENTS TO TRACK:
- Variant exposed (user saw control vs variant B)
- Primary conversion event (e.g., trial signup, purchase)
- Secondary events (e.g., button clicks, form starts)
- Guardrail events (e.g., support ticket submitted, churn event)

TRACKING TOOLS:
- Google Analytics 4 / Mixpanel / Amplitude (product analytics)
- Segment (event pipeline)
- Custom database (user-level experiment assignments)

VALIDATION:
- Test each variant manually
- Confirm events fire in analytics tool
- Verify user is assigned to single variant (no cross-contamination)
```

### Phase 3: Launch (Day 1)

**Checklist:**
- [ ] Soft launch to 10% of traffic (validate tracking)
- [ ] Monitor for first 24 hours (ensure no errors)
- [ ] Scale to 50% of traffic (if all looks good)
- [ ] Scale to 100% of traffic (full experiment running)
- [ ] Announce to team (Slack message with experiment link)

**Launch Announcement Template:**
```
🧪 EXPERIMENT LAUNCHED: [Name]

Hypothesis: [One sentence]
Primary Metric: [Metric] (baseline X%, target Y%)
Duration: [X weeks]
Expected End Date: [Date]

Dashboard: [Link to analytics dashboard]
Experiment Doc: [Link to brief]

We'll analyze results on [Date] and share findings.
```

### Phase 4: Monitor (Daily During Experiment)

**Checklist:**
- [ ] Check dashboard daily (or set up automated alerts)
- [ ] Monitor guardrail metrics (ensure nothing breaking)
- [ ] Watch for statistical significance (don't peek too early!)
- [ ] Document any anomalies (holidays, outages, external events)

**Monitoring Dashboard:**
```
DAILY CHECK:
Date: [Today]

Sample Size Progress:
- Control A: 1,200 / 1,500 (80% to target)
- Variant B: 1,180 / 1,500 (79% to target)
- Days remaining: 3

Primary Metric:
- Control A: 15.2% conversion
- Variant B: 17.8% conversion (+17% lift)
- Statistical significance: p = 0.08 (not yet significant, need more data)

Guardrails:
- Churn rate: 3.1% (stable)
- Support tickets: 42/week (stable)
- NPS: 41 (stable)

Status: On track, continue running
```

### Phase 5: Analyze (Week After Completion)

**Checklist:**
- [ ] Confirm experiment reached sample size target
- [ ] Run statistical significance test (p-value < 0.05?)
- [ ] Analyze primary metric (winner? how much lift?)
- [ ] Analyze secondary metrics (explain why primary moved)
- [ ] Check guardrails (anything break?)
- [ ] Segment analysis (did it work for all segments or just one?)
- [ ] Document findings (write experiment summary)
- [ ] Share results with team (Slack, email, meeting)

**Analysis Template:**
```
EXPERIMENT RESULTS: [Name]

HYPOTHESIS:
[Restate hypothesis]

RESULTS:
✅ WINNER: Variant B
Primary Metric: 15% → 18% (+20% relative lift)
Statistical Significance: p = 0.02 (statistically significant)
Sample Size: 1,500 per variant (reached target)

SECONDARY METRICS:
- Email open rate: 45% → 52% (+15%)
- Click-through rate: 12% → 15% (+25%)
- Time to conversion: 8 days → 6 days (-25%)

GUARDRAILS:
✅ Churn rate: 3.0% (stable, no change)
✅ Support tickets: 38/week (stable)
✅ NPS: 42 (stable)

SEGMENT ANALYSIS:
- SMB customers: +25% lift (strongest)
- Enterprise customers: +10% lift (moderate)
- Free users: No impact

INSIGHTS:
1. Email engagement drove the lift (open rate increased)
2. Faster conversion time suggests stronger urgency
3. SMB segment most responsive (consider SMB-specific experiments next)

DECISION:
✅ SHIP IT - Roll out Variant B to 100% of users
💡 NEXT TEST: Test SMB-specific messaging (since they responded best)
```

### Phase 6: Ship or Kill (Week After Analysis)

**Decision Framework:**
```
SHIP IT ✅ IF:
- Primary metric improved (statistically significant)
- No guardrails tripped
- Lift is meaningful (>10% relative improvement)
- Works across key segments (or acceptable trade-offs)

ITERATE 🔄 IF:
- Primary metric improved slightly (not significant)
- Some guardrails tripped (need to refine approach)
- Works for one segment but not others (personalize by segment)

KILL IT ❌ IF:
- Primary metric didn't improve (or got worse)
- Guardrails tripped (caused harm)
- Not worth the engineering effort (tiny lift)
```

---

## Common Experiment Types

### 1. Messaging & Copy Experiments

**Examples:**
- CTA button text ("Start Free Trial" vs "Get Started Free")
- Headline variations (feature-focused vs benefit-focused)
- Value proposition (product features vs outcomes)
- Email subject lines (curiosity vs value)

**Best Practices:**
- Test one element at a time (button text, not entire page redesign)
- Ensure variants are meaningfully different (not "Sign Up" vs "Sign Up Now")
- Consider brand voice (don't test copy that's off-brand)

### 2. Design & UI Experiments

**Examples:**
- Button color (green vs blue vs orange)
- Form length (5 fields vs 2 fields)
- Page layout (sidebar left vs right, above vs below fold)
- Image vs video on landing page

**Best Practices:**
- Use heatmaps to understand where users look (Hotjar, Crazy Egg)
- Test across devices (mobile vs desktop behavior differs)
- Consider accessibility (color contrast, readability)

### 3. Pricing & Monetization Experiments

**Examples:**
- Pricing tiers (3 tiers vs 4 tiers)
- Price points ($49 vs $59 vs $69)
- Billing frequency (monthly vs annual discount)
- Free trial length (14 days vs 30 days)

**Best Practices:**
- Monitor lifetime value, not just conversion (don't attract bad-fit customers)
- Grandfather existing customers (don't change pricing mid-contract)
- Test on new customers first (lower risk)

### 4. Onboarding & Activation Experiments

**Examples:**
- Onboarding steps (8 steps vs 3 steps)
- Onboarding content (video tutorial vs interactive checklist)
- Welcome email timing (immediate vs 24 hours later)
- Setup wizard vs self-guided

**Best Practices:**
- Measure time to "Aha Moment" (when user sees value)
- Track feature adoption (ensure users learn core features)
- Balance speed vs quality (faster onboarding doesn't always mean better)

### 5. Retention & Engagement Experiments

**Examples:**
- Email cadence (weekly vs bi-weekly newsletter)
- Re-engagement campaigns (win-back emails for churned users)
- In-app notifications (usage tips vs feature announcements)
- Gamification (streaks, badges, leaderboards)

**Best Practices:**
- Monitor long-term metrics (30/60/90-day retention)
- Don't over-message (email fatigue hurts engagement)
- Segment by engagement level (power users vs casual users need different cadences)

---

## Post-Experiment Analysis

### Segmentation Analysis

**Why segment results?**
Averages hide insights. An experiment might work great for one segment and fail for another.

**Key Segments to Analyze:**
```
CUSTOMER SEGMENTS:
- Company size (SMB, mid-market, enterprise)
- Industry vertical (SaaS, ecommerce, healthcare)
- Geography (US, EU, APAC)
- New vs returning customers
- Free vs paid users

BEHAVIORAL SEGMENTS:
- High-engagement vs low-engagement users
- Power users vs casual users
- Mobile vs desktop users
- Organic vs paid acquisition source

DEMOGRAPHIC SEGMENTS:
- User role (founder, manager, individual contributor)
- Company age (startup, scaleup, mature)
```

**Example Segmentation:**
```
OVERALL RESULTS:
Control: 15% conversion
Variant B: 17% conversion (+13% lift)

SEGMENT ANALYSIS:
SMB (<50 employees):
- Control: 18% conversion
- Variant B: 24% conversion (+33% lift) ✅ Strong winner

Enterprise (>200 employees):
- Control: 12% conversion
- Variant B: 11% conversion (-8% lift) ❌ Lost

INSIGHT:
Variant B works great for SMB but hurts Enterprise conversion
Decision: Ship Variant B only to SMB segment (personalized experience)
```

### Learning Documentation

**Why document learnings?**
Build institutional knowledge. Teams forget what they tested 6 months ago.

**Experiment Knowledge Base Structure:**
```
EXPERIMENT LOG (Notion, Confluence, Airtable):

Experiment #47: Reduce onboarding steps (8 → 3)
Date: Jan 15 - Feb 5, 2024
Status: Shipped
Owner: Sarah (Growth PM)

Hypothesis: Simplifying onboarding will increase completion rate
Result: ✅ Win (+25% completion rate, 60% → 75%)
Impact: +500 activated users per month
Learnings: Users prefer speed over comprehensive setup. Can add advanced setup later in-app.
Rollout: Shipped to 100% on Feb 12, 2024

Related Experiments:
- #52: Add setup tooltips (follow-up)
- #38: Welcome email with checklist (tested previously)

Tags: onboarding, activation, product-led-growth
```

**Quarterly Experiment Review:**
```
Q1 2024 EXPERIMENT SUMMARY

Total Experiments Run: 12
- Wins: 5 (42%)
- Losses: 4 (33%)
- Inconclusive: 3 (25%)

Top Wins:
1. Onboarding simplification: +25% completion rate
2. Pricing tier addition: +30% free-to-paid conversion
3. Email nurture sequence: +18% trial engagement

Top Learnings:
1. SMB segment responds better to self-serve changes
2. Enterprise segment needs human touch (automation didn't work)
3. Messaging experiments (copy, design) had smaller impact than expected

Q2 2024 Focus:
- Double down on SMB activation (segment responded well)
- Test Enterprise-specific onboarding (human-assisted)
- Larger bets (10+ experiments that might have 50%+ impact)
```

---

## Experimentation Best Practices

### Do This ✅

**Start small, scale winners:**
- Run 10 small experiments, find 2-3 winners, scale those
- Don't bet everything on one big idea

**Focus on high-leverage areas:**
- Optimize your biggest bottlenecks first (see AAARRR framework)
- 80/20 rule: Fix the 20% of funnel that impacts 80% of results

**Involve the team:**
- Experiment ideas come from everyone (support, sales, product)
- Share results transparently (wins AND losses)

**Document everything:**
- Future you will forget what you tested
- New team members need context

**Be patient:**
- Don't peek at results early (let experiment run to completion)
- Statistical significance requires sample size

### Don't Do This ❌

**Don't test everything:**
- Prioritize ruthlessly (use ICE/RICE scoring)
- Say no to low-impact ideas

**Don't ignore statistical significance:**
- p = 0.12 is NOT significant (even if primary metric improved)
- You need p < 0.05 (or accept higher risk of false positives)

**Don't ship without checking guardrails:**
- A "win" that increases churn 2x is a loss
- Monitor quality metrics, not just conversion

**Don't run multiple overlapping experiments:**
- Experiments should be independent (testing different parts of funnel)
- Testing homepage AND pricing page at same time = confounded results

**Don't give up after one loss:**
- 50-70% of experiments fail - that's normal
- Losses teach you what doesn't work (valuable!)

---

## Experiment Design Tools

### Planning & Prioritization
- **Notion / Confluence** (free-$10/user/month): Experiment briefs, documentation
- **Airtable** ($20/seat/month): Experiment database, prioritization scoring
- **Miro / FigJam** (free-$8/user/month): Brainstorming, hypothesis mapping
- **Google Sheets / Excel** (free): Simple prioritization tables

### A/B Testing Platforms
- **Google Optimize** (free, sunset in 2023 - migrate to Optimizely or VWO)
- **Optimizely** ($50K+/year): Enterprise A/B testing
- **VWO** ($199+/month): Mid-market A/B testing
- **Convert** ($99+/month): Privacy-first A/B testing
- **LaunchDarkly** ($75+/month): Feature flags + experimentation
- **Statsig** (free tier, $50+/month): Experimentation platform for product teams

### Analytics & Tracking
- **Google Analytics 4** (free): Website analytics, goal tracking
- **Mixpanel** ($25+/month): Product analytics, funnel analysis
- **Amplitude** ($49+/month): Advanced product analytics
- **Heap** ($3,600+/year): Auto-capture analytics
- **Segment** ($120+/month): Event tracking infrastructure

### Statistical Calculators
- **Evan Miller's A/B Tools** (free): https://www.evanmiller.org/ab-testing/sample-size.html
- **Optimizely Sample Size Calculator** (free)
- **VWO A/B Test Duration Calculator** (free)
- **AB Testguide** (free): https://abtestguide.com/calc/

### Heatmaps & Session Recording
- **Hotjar** ($39+/month): Heatmaps, session recordings, surveys
- **Crazy Egg** ($29+/month): Heatmaps, scroll maps
- **FullStory** ($199+/month): Session replay, analytics
- **Microsoft Clarity** (free): Heatmaps, session recordings

---

## ROI of Experimentation

**Time Investment:**
```
Per Experiment:
- Design: 4-8 hours (write brief, get alignment)
- Build: 10-40 hours (depends on complexity)
- Monitor: 1-2 hours/week (during experiment)
- Analyze: 4-6 hours (statistical analysis, write-up)
- Total: 20-60 hours per experiment

Annual Investment (running 12 experiments/year):
- 240-720 hours (3-9 months of full-time work)
- OR: 1 growth PM full-time + engineering support
```

**Impact:**
```
CONSERVATIVE SCENARIO:
- Run 12 experiments per year
- 5 wins (42% win rate)
- Average lift per win: 15%
- Compounding effect: 1.15^5 = 2.01x growth

Example:
- Starting MRR: $50,000
- After 5 wins: $100,500 MRR (+$50,500)
- Investment: $80,000 (1 growth PM salary)
- ROI: 63% (first-year payback)

AGGRESSIVE SCENARIO:
- Run 24 experiments per year
- 10 wins (42% win rate)
- Average lift per win: 20%
- Compounding effect: 1.20^10 = 6.19x growth

Example:
- Starting MRR: $50,000
- After 10 wins: $309,500 MRR (+$259,500)
- Investment: $150,000 (growth team)
- ROI: 173% (massive payback)

NOTE: Compounding is key. Each experiment builds on previous wins.
```

---

## Common Mistakes

### ❌ Peeking at Results Early
**Problem:** Checking statistical significance every day (p-value fluctuates)
**Impact:** False positives (shipping experiments that didn't actually win)
**Fix:** Decide sample size upfront, analyze only when reached

### ❌ Testing Too Many Things at Once
**Problem:** Changing headline, CTA, image, and form in one experiment
**Impact:** Can't tell which change drove the result
**Fix:** Test one variable at a time (or use multivariate testing properly)

### ❌ Ignoring External Factors
**Problem:** Running experiments during holidays, product launches, outages
**Impact:** Results are confounded by external events
**Fix:** Avoid testing during anomalous periods, or note them in analysis

### ❌ No Minimum Sample Size
**Problem:** Declaring winner after 50 conversions (too small)
**Impact:** False positives, wrong decisions
**Fix:** Calculate required sample size upfront using calculator

### ❌ Shipping Marginal Winners
**Problem:** Shipping experiment with +2% lift (p = 0.045, barely significant)
**Impact:** Tiny wins don't compound, engineering effort wasted
**Fix:** Set minimum acceptable lift (e.g., 10%+) before shipping

### ❌ Not Learning from Losses
**Problem:** Killing experiments without understanding why they failed
**Impact:** Repeat same mistakes, miss deeper insights
**Fix:** Analyze losses as rigorously as wins (why didn't this work?)

---

## Related Skills and Frameworks

**Related Growth Toolkit Skills:**
- **growth-analytics.md** - Track experiment metrics, build dashboards
- **product-led-growth.md** - Activation and onboarding experiments
- **viral-mechanics.md** - Test referral and viral growth tactics
- **user-onboarding.md** - Onboarding flow experiments

**Related Frameworks:**
- **ICE-RICE.md** - Prioritization framework for choosing experiments
- **AAARRR.md** - Identify which funnel stage to experiment on
- **Viral-Loop-Canvas.md** - Design viral growth experiments

**Complementary Skills:**
- **Conversion Rate Optimization (CRO)** - Landing page and funnel optimization
- **Funnel Analysis** - Understand where users drop off
- **Cohort Analysis** - Measure retention impact of experiments

---

**Next Steps:**

1. **This Week:** Choose one high-impact area to experiment on (use AAARRR to find bottleneck)
2. **Day 1:** Write experiment brief (hypothesis, metrics, variants)
3. **Day 2-3:** Calculate sample size, set up tracking
4. **Week 1:** Build variants, QA test
5. **Week 2-4:** Launch experiment, monitor daily
6. **Week 5:** Analyze results, ship or kill
7. **Week 6:** Document learnings, start next experiment

**Remember:** The goal isn't to run 100 experiments. The goal is to find 5-10 big wins per year that compound into exponential growth. Quality over quantity.
