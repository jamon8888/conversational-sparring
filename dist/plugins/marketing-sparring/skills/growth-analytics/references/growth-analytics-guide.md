# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)

# Growth Analytics & Metrics

## Overview

You can't optimize what you don't measure. This skill teaches solo entrepreneurs how to track, analyze, and act on growth metrics without hiring a data team – from cohort retention to North Star metrics to growth accounting.

**The Measurement Mindset:**
```
Most founders track vanity metrics:
- "We have 10,000 signups!" (but 90% churned)
- "Traffic is up 50%!" (but conversion is down)
- "We added 100 customers!" (but lost 95)

Growth analytics tracks what matters:
- Cohort retention: Do customers stick around?
- Growth accounting: Are we growing or just churning?
- Funnel conversion: Where do users drop off?
- North Star metric: What predicts long-term success?

Result: Data-driven decisions, not gut feelings
```

---

## When to Use This Skill

- You're growing but don't know which metrics to track
- You suspect growth is hiding churn (high signup, high churn)
- You want to find bottlenecks in your funnel
- You need to prove ROI to investors or stakeholders
- You're running experiments and need to measure impact
- Your team debates priorities without data

---

## Why Growth Analytics Matters

**The Hidden Churn Problem:**
```
Scenario: SaaS Company

Month 1: 100 customers, +20 new, -10 churned = 110 total
Month 2: 110 customers, +20 new, -15 churned = 115 total
Month 3: 115 customers, +20 new, -20 churned = 115 total

Surface view: "We're growing! 100 → 115 customers in 3 months"

Reality: Churn is accelerating (10 → 15 → 20)
New customer adds are masking a churn crisis
In 6 months: Churn will exceed new adds → negative growth

Growth accounting reveals:
- New: +20/month (flat)
- Churned: Increasing 10 → 15 → 20 (BAD TREND)
- Net growth: Decreasing (+10 → +5 → 0)

Fix: Address churn NOW, not when growth goes negative
```

---

## The Growth Analytics Stack

### Tier 1: Foundational Metrics (Track These First)

**1. North Star Metric (NSM)**
```
Definition: The ONE metric that best predicts long-term success

Not revenue (lagging)
Not signups (vanity)
But: Leading indicator of value delivered

Examples by Business Model:
- Spotify: Hours of music streamed
- Airbnb: Nights booked
- Slack: Messages sent by teams
- Amazon: Purchases per month
- Netflix: Hours watched

Your NSM Test:
□ Measures value delivered (not just engagement)
□ Predicts revenue (customers who do X → pay more)
□ Actionable (you can influence it)

Example: Email Marketing SaaS
Bad NSM: Signups (doesn't predict retention)
Good NSM: Emails sent per week (predicts upgrade & retention)

Why?
- Users sending >100 emails/week → 80% retain
- Users sending <10 emails/week → 20% retain
Action: Increase emails sent → improve retention
```

---

**2. Growth Accounting (aka The Leaky Bucket)**
```
Formula:
Net Growth = New Customers + Resurrected - Churned

Track monthly:
┌───────────────────────────────────┐
│ Starting Customers: 1,000         │
│ + New: +150                       │
│ + Resurrected: +20 (came back)   │
│ - Churned: -80                    │
│ = Ending Customers: 1,090         │
│                                   │
│ Net Growth: +90 (+9%)             │
└───────────────────────────────────┘

Categories:
- New: First-time customers
- Resurrected: Churned customers who came back
- Retained: Stayed from last month
- Churned: Left this month

Quick Health Check:
✓ Good: New > Churned (net positive growth)
✗ Bad: New < Churned (shrinking)
✗ Terrible: New + Resurrected < Churned (leaky bucket)
```

**Visual:**
```
Growth Accounting Chart (Monthly):

│ +150 New ████████████████
│  +20 Resurrected ███
│  -80 Churned █████████
│  ────────────────────
│  +90 Net Growth ██████████

Month-over-month trend:
Jan: +50 net
Feb: +70 net (accelerating ✓)
Mar: +90 net (accelerating ✓)
Apr: +60 net (decelerating ✗ - investigate!)
```

---

**3. Cohort Retention**
```
Definition: % of users from a signup cohort who remain active over time

Example: January 2024 Cohort
┌─────────────────────────────────────────────────┐
│ Month 0 (Jan): 100 signups = 100% active        │
│ Month 1 (Feb): 80 active = 80% retention        │
│ Month 2 (Mar): 70 active = 70% retention        │
│ Month 3 (Apr): 65 active = 65% retention        │
│ Month 4 (May): 63 active = 63% retention        │
│ Month 5 (Jun): 62 active = 62% retention        │
│ Month 6 (Jul): 61 active = 61% retention        │
└─────────────────────────────────────────────────┘

Retention Curve:
100% ●
     │ ●
 80% │   ●
     │     ●
 60% │       ● ● ● ● (flatlines = good!)
     │
 40% │
     └─────────────────────
     M0 M1 M2 M3 M4 M5 M6

Interpretation:
- M0 → M1: 20% drop (onboarding problem)
- M1 → M3: Gradual decline (product fit issues)
- M3+: Flattens at ~60% (core retained users)

Benchmark:
Month 1: 60-80% (SaaS)
Month 6: 40-60% (SaaS)
Month 12: 30-50% (SaaS)

Healthy retention: Curve flattens (not continuous decay)
Unhealthy: Curve never flattens (product doesn't stick)
```

---

### Tier 2: Advanced Metrics (Add These Next)

**4. Funnel Conversion Rates**
```
Track conversion at each stage:

Visitor → Signup → Activation → Payment → Retention

Example SaaS Funnel:
┌─────────────────────────────────────┐
│ Visitors: 10,000                    │
│   ↓ 5% convert                      │
│ Signups: 500 (Free trial)           │
│   ↓ 40% activate                    │
│ Activated: 200 (Sent first email)   │
│   ↓ 25% convert to paid             │
│ Paying: 50 customers                │
│   ↓ 80% retain (Month 1)            │
│ Retained: 40 customers              │
└─────────────────────────────────────┘

Overall conversion: 10,000 visitors → 40 retained = 0.4%

Bottleneck analysis:
- Visitor → Signup: 5% (INDUSTRY AVERAGE)
- Signup → Activation: 40% (BELOW BENCHMARK - FIX THIS)
- Activation → Payment: 25% (GOOD)
- Payment → Retention: 80% (GOOD)

Action: Focus on improving activation (40% → 60% = +100 activated, +25 paying customers)
```

**Funnel Optimization Priorities:**
```
Use ICE Score to prioritize improvements:

Stage | Conversion | Impact | Confidence | Ease | ICE Score
Signup | 5% | 5 | 3 | 2 | 30
Activation | 40% | 10 | 8 | 7 | 560 ← FOCUS HERE
Payment | 25% | 7 | 6 | 5 | 210
Retention | 80% | 9 | 7 | 4 | 252

Activation has highest ICE score → improve this first
```

---

**5. Leading vs. Lagging Indicators**
```
Lagging Indicators (Results, slow to change):
- Revenue
- Churn rate
- Customer count

Leading Indicators (Predict results, fast to change):
- Activation rate (predicts retention)
- Usage frequency (predicts upgrade)
- Feature adoption (predicts expansion)

Example:
Lagging: Monthly churn = 5%
Leading: Users who use <3 features churn at 15%

Action: Improve feature adoption → reduce future churn

Relationship:
High usage (leading) → High retention (lagging)
Low usage (leading) → High churn (lagging)

Track both:
- Lagging: Understand outcomes
- Leading: Predict & prevent problems early
```

---

**6. Segmented Analytics**
```
Don't average across all customers – segment by key attributes

Segment by:
- Acquisition channel (organic, paid, referral)
- Customer size (SMB, mid-market, enterprise)
- Use case (e.g., ecommerce vs. SaaS for email tool)
- Geography (US, EU, APAC)

Example: Retention by Channel
┌──────────────────────────────────────────┐
│ Channel    | M1 Retention | M6 Retention │
│─────────────────────────────────────────│
│ Organic    | 75%          | 55%          │
│ Paid Ads   | 60%          | 30%          │
│ Referral   | 85%          | 70%          │
└──────────────────────────────────────────┘

Insight: Referral customers have 2.3x better retention than paid
Action: Invest more in referral program, less in paid ads

Segment by use case:
E-commerce customers: 80% retention
SaaS customers: 60% retention
Action: Focus marketing on e-commerce (better fit)
```

---

## Building Your Growth Dashboard

### Dashboard Design Principles

**1. One Page, One Glance**
```
Bad dashboard:
- 50 metrics (information overload)
- No hierarchy (all metrics equal weight)
- No trends (just current values)

Good dashboard:
- 5-8 key metrics (focused)
- Clear hierarchy (North Star at top)
- Trends visible (up/down arrows, sparklines)
- Actionable (red/green indicators)
```

**2. Metric Hierarchy**
```
Top (Biggest, Most Important):
┌─────────────────────────────────────┐
│ NORTH STAR METRIC                   │
│ Emails Sent per Week: 450           │
│ ↑ +15% vs. last week                │
└─────────────────────────────────────┘

Middle (Supporting Metrics):
┌──────────────┬──────────────┬──────────────┐
│ New Users    │ Activation   │ Retention    │
│ 150          │ 45%          │ 75% (M1)     │
│ ↑ +10%       │ → Flat       │ ↓ -5%        │
└──────────────┴──────────────┴──────────────┘

Bottom (Diagnostic Metrics):
┌──────────────┬──────────────┬──────────────┐
│ Traffic      │ Signup Rate  │ Churn        │
│ 5,000        │ 3%           │ 5%/month     │
└──────────────┴──────────────┴──────────────┘
```

---

### Executive Dashboard Template

```
┌─────────────────────────────────────────────────────────┐
│                     GROWTH DASHBOARD                    │
│                      November 2024                      │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  NORTH STAR METRIC                                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Active Users (weekly):  1,250                    │  │
│  │  ↑ +12% vs. last month                            │  │
│  │  ████████████████░░ 84% of target (1,500)         │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  KEY METRICS                                            │
│  ┌─────────────┬─────────────┬─────────────────────┐   │
│  │ New Users   │ Activation  │ M1 Retention        │   │
│  │ 200         │ 48%         │ 72%                 │   │
│  │ ↑ +15%      │ → Flat      │ ↓ -3% (WATCH)       │   │
│  └─────────────┴─────────────┴─────────────────────┘   │
│                                                         │
│  ┌─────────────┬─────────────┬─────────────────────┐   │
│  │ MRR         │ Churn       │ NRR                 │   │
│  │ $25,000     │ 4.5%        │ 105%                │   │
│  │ ↑ +8%       │ ↑ +0.5% ⚠  │ → Flat              │   │
│  └─────────────┴─────────────┴─────────────────────┘   │
│                                                         │
│  GROWTH ACCOUNTING                                      │
│  ┌───────────────────────────────────────────────────┐  │
│  │  Starting: 500                                    │  │
│  │  + New: +50                                       │  │
│  │  + Resurrected: +5                                │  │
│  │  - Churned: -20                                   │  │
│  │  = Ending: 535 (+7% net growth)                   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                         │
│  ALERTS                                                 │
│  ⚠ Churn increased from 4.0% → 4.5% (investigate!)     │
│  ⚠ Activation rate stuck at 48% for 3 months            │
│                                                         │
│  Last updated: Nov 27, 2024 9:00am                      │
└─────────────────────────────────────────────────────────┘
```

---

### Channel-Specific Dashboard

```
┌─────────────────────────────────────────────────────────┐
│                ACQUISITION CHANNEL METRICS              │
├─────────────────────────────────────────────────────────┤
│                                                         │
│ Channel    │ Traffic │ Signups │ CAC   │ LTV   │ ROI   │
│────────────┼─────────┼─────────┼───────┼───────┼───────│
│ Organic    │ 2,000   │ 100     │ $50   │ $800  │ 16x   │
│ Paid (FB)  │ 1,500   │ 75      │ $300  │ $600  │ 2x    │
│ Referral   │ 500     │ 50      │ $0    │ $1K   │ ∞     │
│ Content    │ 1,000   │ 40      │ $100  │ $700  │ 7x    │
│────────────┴─────────┴─────────┴───────┴───────┴───────│
│                                                         │
│ INSIGHT: Referral has best economics (infinite ROI)     │
│ ACTION: 2x investment in referral program               │
│                                                         │
│ WATCH: Paid FB CAC increasing ($250 → $300 in 3 mo)    │
│ ACTION: Test new ad creative or pause channel           │
└─────────────────────────────────────────────────────────┘
```

---

## Cohort Retention Analysis (Step-by-Step)

### How to Build a Cohort Retention Table

**Step 1: Define Cohorts**
```
Cohort = Group of users who signed up in the same time period

Example: Monthly Cohorts
- Jan 2024 Cohort: All users who signed up in January
- Feb 2024 Cohort: All users who signed up in February
- etc.

Alternative cohort types:
- By channel: "Paid Ads Cohort" vs. "Organic Cohort"
- By feature: "Users who adopted Feature X" vs. "Didn't adopt"
- By size: "Enterprise Cohort" vs. "SMB Cohort"
```

**Step 2: Define "Active"**
```
What counts as "active"?

Bad definition: "Logged in" (they might not use product)
Good definition: "Completed core action"

Examples:
- Email tool: Sent at least 1 email
- Analytics tool: Viewed at least 1 dashboard
- CRM: Added at least 1 contact

Be specific:
Active = [Did action X] in [time period Y]
Example: "Sent ≥1 email in the last 30 days"
```

**Step 3: Build Retention Table**
```
Cohort Retention Table (% of cohort still active):

Cohort    │ M0   │ M1   │ M2   │ M3   │ M4   │ M5   │ M6
──────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────
Jan 2024  │ 100% │ 75%  │ 68%  │ 64%  │ 62%  │ 61%  │ 60%
Feb 2024  │ 100% │ 78%  │ 70%  │ 66%  │ 64%  │ 63%  │ --
Mar 2024  │ 100% │ 80%  │ 72%  │ 68%  │ 66%  │ --   │ --
Apr 2024  │ 100% │ 82%  │ 74%  │ 70%  │ --   │ --   │ --
May 2024  │ 100% │ 83%  │ 76%  │ --   │ --   │ --   │ --
Jun 2024  │ 100% │ 85%  │ --   │ --   │ --   │ --   │ --

Insights:
1. Retention improving over time (Jan M1 = 75%, Jun M1 = 85%)
   → Product improvements are working
2. Curve flattens around M4 (~60-65% retained long-term)
   → Product has found core user base
3. Biggest drop M0 → M1 (15-25% churn)
   → Onboarding is the problem (fix this first)
```

**Color-Coded View:**
```
Use heatmap colors:

🟢 Green (>80%): Excellent retention
🟡 Yellow (60-80%): Good retention
🟠 Orange (40-60%): At-risk
🔴 Red (<40%): Poor retention

Cohort    │ M0   │ M1   │ M2   │ M3   │ M4   │ M5   │ M6
──────────┼──────┼──────┼──────┼──────┼──────┼──────┼──────
Jan 2024  │ 🟢   │ 🟡   │ 🟡   │ 🟡   │ 🟡   │ 🟡   │ 🟡
Feb 2024  │ 🟢   │ 🟡   │ 🟡   │ 🟡   │ 🟡   │ 🟡   │ --
Mar 2024  │ 🟢   │ 🟢   │ 🟡   │ 🟡   │ 🟡   │ --   │ --
Apr 2024  │ 🟢   │ 🟢   │ 🟡   │ 🟡   │ --   │ --   │ --

Quick diagnosis:
- Recent cohorts (Apr-Jun) have better M1 retention → improvements working
- All cohorts stabilize around 60-65% → healthy plateau
```

---

### Calculating Retention in Spreadsheets

**Google Sheets Formula:**
```
Setup:
- Sheet 1: User signup data (UserID, SignupDate, LastActiveDate)
- Sheet 2: Retention table

Formula for "M1 Retention" (Jan 2024 Cohort):
=COUNTIFS(SignupDate, ">=2024-01-01", SignupDate, "<=2024-01-31", LastActiveDate, ">=2024-02-01")
 / COUNTIFS(SignupDate, ">=2024-01-01", SignupDate, "<=2024-01-31")

Explanation:
- Numerator: Users who signed up in Jan AND were active in Feb
- Denominator: All users who signed up in Jan
- Result: % of Jan cohort still active in Month 1 (Feb)

Drag formula across to calculate M2, M3, etc.
```

**SQL Query:**
```sql
-- Cohort Retention (M1) for Jan 2024 Cohort
SELECT
  DATE_TRUNC('month', signup_date) AS cohort_month,
  COUNT(DISTINCT user_id) AS cohort_size,
  COUNT(DISTINCT CASE
    WHEN last_active_date >= DATE_ADD(signup_date, INTERVAL 1 MONTH)
    THEN user_id END) AS active_m1,
  ROUND(100.0 * COUNT(DISTINCT CASE
    WHEN last_active_date >= DATE_ADD(signup_date, INTERVAL 1 MONTH)
    THEN user_id END) / COUNT(DISTINCT user_id), 1) AS retention_m1
FROM users
WHERE signup_date >= '2024-01-01' AND signup_date < '2024-02-01'
GROUP BY cohort_month;
```

---

## North Star Metric Framework

### How to Choose Your North Star

**The NSM Test (All Must Be True):**
```
□ Measures value delivered to customer (not just engagement)
□ Predicts revenue (customers who do more X → pay more)
□ Leading indicator (changes before revenue does)
□ Understandable (whole team can explain it)
□ Actionable (you can influence it via product/growth)

Examples That Pass:
✓ Spotify: Hours listened (value = music enjoyment)
✓ Airbnb: Nights booked (value = travel stays)
✓ Slack: Messages sent (value = team communication)

Examples That Fail:
✗ Revenue (lagging, not value-based)
✗ Signups (no value delivered yet)
✗ DAU (vanity, doesn't predict revenue)
```

**Finding Your NSM:**
```
Step 1: List core value props
"Our product helps customers [do what?]"

Example: Email Marketing Tool
Value props:
- Send email campaigns
- Grow email list
- Automate email sequences
- Analyze campaign performance

Step 2: Identify measurable actions
- Emails sent per week
- Subscribers added per month
- Automation workflows created
- Reports viewed per week

Step 3: Correlate with retention/revenue
Run analysis:
- Users sending >100 emails/week → 85% retain, $150 ARPU
- Users sending <10 emails/week → 20% retain, $50 ARPU

Step 4: Choose leading indicator
North Star: Emails sent per week
Why? High email volume predicts high retention and revenue
```

---

### NSM by Business Model

**SaaS:**
```
B2B SaaS: Weekly Active Users (WAU) completing core action
- Asana: Tasks completed per week
- Notion: Pages created/edited per week
- Intercom: Messages sent per week

Consumer SaaS: Value delivered to user
- Netflix: Hours watched
- Duolingo: Lessons completed
```

**Marketplace:**
```
Two-sided marketplaces: Transactions completed
- Uber: Rides completed
- Airbnb: Nights booked
- Upwork: Jobs posted & filled

Why transactions? Shows both sides are engaged (supply + demand)
```

**E-Commerce:**
```
Transactional: Orders per month
- Amazon: Orders per month
- Shopify merchant: Products sold

Subscription: Order frequency
- Dollar Shave Club: Subscription renewals
```

**Media/Content:**
```
Ad-supported: Time spent / Content consumed
- YouTube: Hours watched
- Medium: Stories read

Subscription: Engagement depth
- NY Times: Articles read per week
```

---

## Growth Experiments & A/B Testing

### Statistical Significance Basics

**Why Sample Size Matters:**
```
Bad experiment:
- Variant A: 10 users, 5 conversions = 50% conversion
- Variant B: 10 users, 7 conversions = 70% conversion
- Winner? Can't tell (sample too small, likely random noise)

Good experiment:
- Variant A: 1,000 users, 500 conversions = 50% conversion
- Variant B: 1,000 users, 700 conversions = 70% conversion
- Winner: Variant B (95% confidence, statistically significant)

Rule: Need ~350+ conversions per variant for significance
```

**P-Value Explained:**
```
P-value = Probability that result is due to random chance

p < 0.05 = 95% confident result is real (industry standard)
p < 0.01 = 99% confident (more stringent)

Example:
Variant A: 10% conversion
Variant B: 12% conversion
P-value: 0.03

Interpretation: 3% chance this is random luck, 97% chance B is truly better → Ship Variant B
```

---

## Common Analytics Mistakes

### ❌ Mistake #1: Tracking Vanity Metrics

**Problem:** Focus on metrics that look good but don't predict success

**Vanity Metrics:**
- Total signups (includes churned users)
- Page views (doesn't mean engagement)
- Social media followers (doesn't mean revenue)

**Actionable Metrics:**
- Active users (exclude churned)
- Activation rate (predicts retention)
- Customer LTV (predicts profitability)

---

### ❌ Mistake #2: Not Segmenting

**Problem:** Average across all customers, miss key insights

**Fix:** Segment by:
- Channel (organic vs. paid)
- Customer size (SMB vs. enterprise)
- Use case
- Geography

Example: "Average retention is 60%" could hide:
- Enterprise: 85% retention
- SMB: 45% retention
Action: Focus on enterprise, fix SMB onboarding

---

### ❌ Mistake #3: Ignoring Leading Indicators

**Problem:** Only track revenue (lagging), miss warning signs

**Fix:** Track leading indicators:
- Usage frequency → predicts churn
- Feature adoption → predicts expansion
- Support tickets → predicts dissatisfaction

---

## Analytics Tools for Solo Entrepreneurs

**Free/Low-Cost:**
- **Google Analytics** (Free): Website traffic, funnels
- **Mixpanel** ($0-89/month): Product analytics, cohorts
- **Amplitude** (Free tier): User analytics, retention
- **PostHog** (Free tier): Product analytics, self-hosted

**Mid-Tier:**
- **Heap** ($599/month): Auto-capture analytics
- **Segment** ($120/month): Data routing, CDP
- **Baremetrics** ($108/month): SaaS metrics (MRR, churn, LTV)

**Spreadsheets (DIY):**
- Google Sheets (Free): Cohort tables, dashboards
- Airtable ($20/month): Database + reporting
- Excel (Free/Office 365): Pivot tables, charts

---

## Growth Analytics Checklist

**Daily (5 min):**
- [ ] Check North Star Metric (trend up/down/flat?)
- [ ] Review new signups (spike or drop?)
- [ ] Check for anomalies (alerts, errors)

**Weekly (30 min):**
- [ ] Review growth accounting (new, churned, net growth)
- [ ] Check funnel conversion rates (any drops?)
- [ ] Segment analysis (which channels/cohorts performing best?)

**Monthly (2 hours):**
- [ ] Build cohort retention table (are newer cohorts improving?)
- [ ] Deep-dive on underperforming segments
- [ ] Update growth dashboard for stakeholders
- [ ] Set experiments for next month based on data

**Quarterly (4 hours):**
- [ ] Full metrics audit (are we tracking the right things?)
- [ ] Benchmark against industry standards
- [ ] Review North Star Metric (still the right one?)
- [ ] Long-term trend analysis (6-12 month view)

---

## Related Skills

- **experiment-design.md** - Use data to run experiments
- **user-onboarding.md** - Improve activation metrics
- **referral-programs.md** - Track referral attribution
- **product-led-growth.md** - PQL scoring and metrics

## Related Frameworks

- **AAARRR.md** - Pirate Metrics funnel
- **ICE-RICE.md** - Prioritize metric improvements
- **PQL-Framework.md** - Product usage scoring
