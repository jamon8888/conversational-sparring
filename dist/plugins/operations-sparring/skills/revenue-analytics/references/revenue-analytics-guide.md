# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Revenue Analytics: Turn Data Into Growth Decisions

## Overview

Revenue analytics is the practice of measuring, tracking, and analyzing metrics that directly impact revenue growth. For solo entrepreneurs and small teams, revenue analytics provides the visibility needed to identify what's working, what's broken, and where to focus limited resources for maximum impact.

**When to use this skill:**
- You need to report on business performance to stakeholders or board
- You're making strategic decisions about pricing, hiring, or marketing spend
- Sales leadership asks "How's the pipeline?" and you can't answer quickly
- You want to identify bottlenecks in your sales or marketing funnel
- You're tracking toward a revenue goal and need early warning signals
- Investors or leadership ask about unit economics, growth rate, or burn multiple
- You need to justify marketing budget or headcount increases
- You're preparing for fundraising and need investor-ready metrics

**Why revenue analytics matters:**
- **Strategic clarity:** Know exactly where revenue comes from and where it's going
- **Early problem detection:** Identify issues weeks before they impact results
- **Resource allocation:** Invest time and money in high-impact activities
- **Team alignment:** Shared metrics create focus and accountability
- **Investor confidence:** Data-driven storytelling builds trust with stakeholders
- **Predictability:** Forecast revenue with confidence, plan hiring and spending

**The cost of poor revenue analytics:**
- Flying blind, making decisions based on gut feel instead of data
- Missing revenue targets because problems weren't caught early
- Wasting budget on low-ROI activities that "feel" productive
- Unable to answer board or investor questions confidently
- Sales and marketing teams optimizing for vanity metrics
- Can't prove marketing ROI, leading to budget cuts

## The Revenue Analytics Framework

### 1. Core Revenue Metrics

**Monthly Recurring Revenue (MRR)**
```
DEFINITION:
Predictable revenue that recurs every month from subscriptions

FORMULA:
MRR = Sum of all monthly subscription revenue

EXAMPLE:
- 10 customers paying $500/month = $5,000 MRR
- 5 customers paying $1,000/month = $5,000 MRR
- 2 customers paying $2,500/month = $5,000 MRR
Total MRR = $15,000

FOR ANNUAL CONTRACTS:
If customer pays $12,000/year upfront, count as $1,000 MRR (not $12,000 in month 1)

SEGMENTATION:
Track MRR by:
- Product tier (Starter, Pro, Enterprise)
- Customer segment (SMB, Mid-Market, Enterprise)
- Industry vertical
- Cohort (month/year acquired)
- Sales channel (self-serve, sales-led)
```

**MRR Growth Components:**
```
NEW MRR: Revenue from new customers
+ EXPANSION MRR: Upgrades, add-ons, seat expansions
- CONTRACTION MRR: Downgrades, seat reductions
- CHURNED MRR: Canceled customers
= NET NEW MRR

EXAMPLE (March 2024):
Starting MRR (Feb 28): $100,000

New MRR: +$15,000 (10 new customers)
Expansion MRR: +$3,000 (5 customers upgraded)
Contraction MRR: -$1,000 (2 customers downgraded)
Churned MRR: -$4,000 (3 customers canceled)

Net New MRR = $15,000 + $3,000 - $1,000 - $4,000 = $13,000

Ending MRR (March 31): $113,000

MRR Growth Rate = $13,000 / $100,000 = 13%
```

**Annual Recurring Revenue (ARR)**
```
FORMULA:
ARR = MRR × 12

OR (if you have annual contracts):
ARR = Sum of annualized contract values

EXAMPLE:
Current MRR: $113,000
ARR = $113,000 × 12 = $1,356,000 = $1.36M ARR

WHY IT MATTERS:
- Industry standard metric (easier to compare)
- Used for valuation (SaaS companies valued at 5-15x ARR)
- Simplifies annual planning and forecasting

TRACK BOTH:
- MRR for monthly operations
- ARR for strategic planning and fundraising
```

**Average Revenue Per Account (ARPA)**
```
FORMULA:
ARPA = Total MRR / Number of Paying Customers

EXAMPLE:
Total MRR: $113,000
Paying Customers: 226
ARPA = $113,000 / 226 = $500/month

ARPA BY SEGMENT:
SMB: $300/month (120 customers)
Mid-Market: $800/month (80 customers)
Enterprise: $2,500/month (26 customers)

WHY IT MATTERS:
- Indicates pricing power and value delivery
- Segment ARPA reveals where to focus (higher ARPA = higher LTV)
- Track ARPA trends (increasing = good, decreasing = concern)

ARPA IMPROVEMENT STRATEGIES:
- Increase prices (test 10-20% increases)
- Drive expansion (upsells, add-ons)
- Shift mix to higher-value customers
- Introduce higher-tier plans
```

**Revenue Growth Rate**
```
FORMULA:
MoM Growth Rate = (Current Month MRR - Prior Month MRR) / Prior Month MRR × 100%

EXAMPLE:
February MRR: $100,000
March MRR: $113,000
Growth Rate = ($113,000 - $100,000) / $100,000 × 100% = 13%

BENCHMARKS (SaaS):
- 5-10% MoM: Good for mature companies
- 10-20% MoM: Strong growth
- 20%+ MoM: Hyper-growth (unsustainable long-term)

COMPOUND ANNUAL GROWTH RATE (CAGR):
= (Ending ARR / Starting ARR)^(1 / Years) - 1

EXAMPLE:
Year 1 ARR: $500K
Year 3 ARR: $2M (2 years later)
CAGR = ($2M / $500K)^(1/2) - 1 = 4^0.5 - 1 = 2 - 1 = 100% CAGR

WHY IT MATTERS:
- Investors focus on growth rate as key valuation driver
- "Triple Triple Double Double Double" = 3x, 3x, 2x, 2x, 2x growth YoY to reach $100M ARR
```

**Customer Churn Rate**
```
FORMULA (Customer Churn):
Monthly Customer Churn Rate = Customers Lost / Starting Customers × 100%

EXAMPLE:
Starting Customers (March 1): 226
Lost Customers (during March): 8
Customer Churn Rate = 8 / 226 × 100% = 3.5%

FORMULA (Revenue Churn):
Monthly MRR Churn Rate = MRR Lost / Starting MRR × 100%

EXAMPLE:
Starting MRR (March 1): $113,000
Churned MRR (during March): $4,000
MRR Churn Rate = $4,000 / $113,000 × 100% = 3.5%

BENCHMARKS (B2B SaaS):
- <2% monthly: Excellent
- 2-5% monthly: Acceptable
- 5-7% monthly: Concerning (need to improve product/fit)
- >7% monthly: Critical issue

ANNUAL CHURN BENCHMARKS:
- <10% annually: Best-in-class
- 10-20% annually: Healthy
- >30% annually: Unsustainable

WHY CHURN MATTERS:
3% monthly churn = 30.6% annual churn
At 30% churn, you lose 1/3 of customers each year
Must acquire 30+ new customers just to stay flat

"LEAKY BUCKET" PROBLEM:
If churn > growth from new customers, MRR will decline
Fix retention before scaling acquisition
```

**Net Revenue Retention (NRR)**
```
FORMULA:
NRR = (Starting MRR + Expansion - Contraction - Churn) / Starting MRR × 100%

EXAMPLE (cohort-based):
Jan 2023 Cohort: 100 customers, $50,000 MRR

One year later (Jan 2024):
- Still Active: 85 customers (15 churned)
- MRR from Active: $47,000 (includes expansions and contractions)

NRR = $47,000 / $50,000 × 100% = 94%

INTERPRETATION:
94 cents of every dollar remain after 1 year

BENCHMARKS:
- <90%: Weak retention, high churn
- 90-100%: Acceptable, but need expansion motion
- 100-110%: Good, expansion offsets some churn
- 110-120%: Excellent, strong expansion
- >120%: Best-in-class, negative net churn

"NEGATIVE NET CHURN":
NRR > 100% means expansion exceeds churn
You can grow revenue even without new customers
The holy grail of SaaS businesses

WHY IT MATTERS:
Companies with 120%+ NRR can scale efficiently
Expansion revenue is more profitable than new logo acquisition
High NRR = strong product-market fit
```

### 2. Pipeline and Sales Metrics

**Sales Pipeline Value**
```
FORMULA:
Pipeline = Sum of all open opportunity amounts

EXAMPLE:
- 15 opportunities in "Discovery": $450,000
- 12 opportunities in "Demo": $360,000
- 8 opportunities in "Proposal": $240,000
- 5 opportunities in "Negotiation": $150,000

Total Pipeline: $1,200,000

WEIGHTED PIPELINE:
Multiply by stage-specific probability

Stage Probabilities (example):
- Discovery: 20%
- Demo: 40%
- Proposal: 60%
- Negotiation: 80%

Weighted Pipeline:
= ($450K × 20%) + ($360K × 40%) + ($240K × 60%) + ($150K × 80%)
= $90K + $144K + $144K + $120K
= $498,000

INTERPRETATION:
$1.2M in total opportunities
$498K in weighted pipeline (more realistic forecast)
```

**Pipeline Coverage Ratio**
```
FORMULA:
Pipeline Coverage = Total Pipeline / Quota or Target

EXAMPLE:
Q2 Revenue Target: $400,000
Current Pipeline: $1,200,000
Coverage = $1,200,000 / $400,000 = 3.0x

BENCHMARK:
- 3-4x coverage: Healthy (for 25-30% win rates)
- 2-3x coverage: Marginal (at risk of missing target)
- <2x coverage: Red flag (unlikely to hit target)

WEIGHTED COVERAGE:
Weighted Pipeline / Target = $498,000 / $400,000 = 1.25x

INTERPRETATION:
Need at least 1.0x weighted coverage to hit target
1.25x provides some buffer for deal slippage
```

**Win Rate**
```
FORMULA:
Win Rate = Closed-Won Deals / (Closed-Won + Closed-Lost) × 100%

EXAMPLE (Last Quarter):
Closed-Won: 12 deals
Closed-Lost: 28 deals
Win Rate = 12 / (12 + 28) × 100% = 12 / 40 = 30%

WIN RATE BY STAGE:
Discovery → Demo: 60% (qualified opportunities)
Demo → Proposal: 70%
Proposal → Negotiation: 75%
Negotiation → Closed-Won: 85%
Overall Win Rate: 60% × 70% × 75% × 85% = 26.8%

BENCHMARKS:
- <20%: Poor qualification or weak sales process
- 20-30%: Typical for competitive B2B
- 30-40%: Strong qualification and sales execution
- >40%: Excellent (or under-pricing)

WHY IT MATTERS:
Higher win rate = need less pipeline to hit targets
Improving from 25% to 35% reduces pipeline needs by 28%
Focus on win rate before scaling pipeline generation
```

**Average Sales Cycle Length**
```
FORMULA:
Sales Cycle Length = Average days from Opportunity Created to Closed-Won

EXAMPLE:
Last 10 Closed-Won Deals:
Deal 1: 45 days
Deal 2: 62 days
Deal 3: 38 days
...
Deal 10: 51 days

Average = (45 + 62 + 38 + ... + 51) / 10 = 52 days

BY SEGMENT:
SMB: 30 days
Mid-Market: 60 days
Enterprise: 120 days

WHY IT MATTERS:
Longer sales cycles = more pipeline needed for same result
Need to start pipeline generation earlier
Affects cash flow and forecasting accuracy
```

**Average Contract Value (ACV)**
```
FORMULA:
ACV = Total Contract Value / Contract Length (years)

EXAMPLE:
3-year contract for $90,000
ACV = $90,000 / 3 = $30,000

OR (for subscription):
Customer pays $2,500/month
ACV = $2,500 × 12 = $30,000

AVERAGE ACV (across all deals):
Sum of all ACVs / Number of Deals

EXAMPLE:
Q1 Deals:
- 8 SMB deals @ $12K ACV each = $96K
- 4 Mid-Market @ $30K ACV = $120K
- 2 Enterprise @ $75K ACV = $150K

Total: $366K / 14 deals = $26,143 average ACV

WHY IT MATTERS:
Higher ACV = higher ROI on sales effort
$75K ACV deal vs $12K ACV takes similar effort
Focus sales team on higher ACV segments
```

### 3. Marketing Performance Metrics

**Marketing Qualified Leads (MQLs)**
```
DEFINITION:
Leads that meet qualification criteria and are ready for sales follow-up

MQL CRITERIA (example):
- Fits Ideal Customer Profile (ICP)
- Company size: 50-500 employees
- Industry: B2B SaaS, Professional Services, Tech
- Job title: VP+, Director, Manager
- Took high-intent action: Demo request, pricing page view, case study download

MQL VOLUME:
Track MQLs generated per month by channel

EXAMPLE (March 2024):
- Organic Search: 45 MQLs
- Paid LinkedIn: 32 MQLs
- Content Downloads: 28 MQLs
- Webinars: 22 MQLs
Total: 127 MQLs

MQL-TO-SQL CONVERSION RATE:
MQL-to-SQL Rate = SQLs / MQLs × 100%

Example:
127 MQLs → 42 SQLs = 33% conversion rate

BENCHMARK: 25-40% MQL-to-SQL is typical
```

**Cost Per Lead (CPL) and Cost Per MQL**
```
FORMULA:
CPL = Marketing Spend / Total Leads
Cost Per MQL = Marketing Spend / MQLs Generated

EXAMPLE:
March Marketing Spend: $25,000
Total Leads: 520
MQLs: 127

CPL = $25,000 / 520 = $48 per lead
Cost Per MQL = $25,000 / 127 = $197 per MQL

BY CHANNEL:
Organic Search: $5,000 / 45 MQLs = $111 per MQL
Paid LinkedIn: $12,000 / 32 MQLs = $375 per MQL
Webinars: $6,000 / 22 MQLs = $273 per MQL

BENCHMARKS (B2B):
- CPL: $50-$150
- Cost per MQL: $150-$400
- Cost per SQL: $400-$1,200

Vary widely by industry, ACV, and target market
```

**Lead Velocity Rate (LVR)**
```
FORMULA:
LVR = (MQLs This Month - MQLs Last Month) / MQLs Last Month × 100%

EXAMPLE:
February MQLs: 105
March MQLs: 127
LVR = (127 - 105) / 105 × 100% = 21%

WHY IT MATTERS:
LVR is a leading indicator of revenue growth
Growing MQLs today = growing revenue in 60-90 days
Track LVR to predict future pipeline health

BENCHMARK:
10%+ monthly LVR = strong growth trajectory
Negative LVR = pipeline problems ahead
```

**Conversion Rates by Funnel Stage**
```
TRACK:
- Visitor → Lead: ___%
- Lead → MQL: ___%
- MQL → SQL: ___%
- SQL → Opportunity: ___%
- Opportunity → Customer: ___%

EXAMPLE FUNNEL (March 2024):
- 25,000 website visitors
- 520 leads (2.1% conversion)
- 127 MQLs (24.4% lead-to-MQL)
- 42 SQLs (33.1% MQL-to-SQL)
- 18 Opportunities (42.9% SQL-to-Opp)
- 6 Customers (33.3% Opp-to-Customer)

Overall: 25,000 visitors → 6 customers = 0.024% conversion

IDENTIFY BOTTLENECKS:
- Visitor-to-Lead (2.1%) is low → improve landing pages, CTAs
- Lead-to-MQL (24.4%) is low → improve targeting or lead magnets
- Opp-to-Customer (33.3%) is good → sales execution is strong

IMPROVEMENT FOCUS:
Fix top-of-funnel (visitors, leads) before scaling spend
Small improvements compound through funnel
```

### 4. Customer Success Metrics

**Customer Health Score**
```
DEFINITION:
Composite score predicting likelihood of renewal or churn

EXAMPLE SCORING MODEL (0-100 scale):

Product Usage (40 points):
- Daily Active Users: 15 points
- Feature adoption: 10 points
- Depth of usage: 10 points
- API calls or integrations: 5 points

Engagement (30 points):
- Support ticket volume: 10 points (fewer = better)
- CSM meeting attendance: 10 points
- Training completion: 5 points
- Community participation: 5 points

Business Outcomes (30 points):
- ROI delivered: 10 points
- Time to value: 10 points
- Expansion opportunity: 5 points
- Executive sponsorship: 5 points

HEALTH SEGMENTATION:
- 80-100: Healthy (low churn risk, expansion candidate)
- 60-79: Stable (moderate risk, needs attention)
- 40-59: At Risk (high churn risk, intervention needed)
- <40: Critical (likely to churn, urgent action)

ACTIONS BY HEALTH:
Healthy: Upsell motion, ask for referral/case study
Stable: Increase engagement, product adoption
At Risk: Executive escalation, success plan
Critical: Retention offer, discount, personalized support
```

**Net Promoter Score (NPS)**
```
QUESTION:
"On a scale of 0-10, how likely are you to recommend [product] to a colleague?"

CALCULATION:
- Promoters (9-10): Loyal enthusiasts
- Passives (7-8): Satisfied but unenthusiastic
- Detractors (0-6): Unhappy, may churn

NPS = % Promoters - % Detractors

EXAMPLE:
Survey 100 customers:
- 50 Promoters (9-10)
- 30 Passives (7-8)
- 20 Detractors (0-6)

NPS = 50% - 20% = 30

BENCHMARKS (B2B SaaS):
- <0: Poor (more detractors than promoters)
- 0-30: Okay (room for improvement)
- 30-50: Good (healthy satisfaction)
- 50-70: Excellent (strong loyalty)
- >70: World-class (exceptional product)

WHY IT MATTERS:
NPS predicts churn, expansion, and word-of-mouth growth
Promoters have 3-10x higher LTV than Detractors
Ask NPS quarterly, track trends
```

**Expansion Revenue Rate**
```
FORMULA:
Expansion Rate = Expansion MRR / Starting MRR × 100%

EXAMPLE (March):
Starting MRR: $100,000
Expansion MRR (upgrades, add-ons): $3,000
Expansion Rate = $3,000 / $100,000 = 3%

ANNUAL EXPANSION RATE:
3% monthly × 12 months = 36% annual expansion

BENCHMARKS:
- 0-10% annual: Low expansion, focus on upsell motion
- 10-20% annual: Decent expansion
- 20-30% annual: Strong expansion
- >30% annual: Exceptional, negative net churn territory

EXPANSION DRIVERS:
- Usage-based pricing (more usage = more revenue)
- Seat-based pricing (team growth)
- Feature-based tiers (upgrade to Pro/Enterprise)
- Add-on products (cross-sell)

WHY IT MATTERS:
Expansion revenue is 4-5x cheaper than new logo acquisition
High expansion offsets churn (enables negative net churn)
```

### 5. Unit Economics Metrics

**Customer Acquisition Cost (CAC)**
```
See Attribution & ROI skill for full details

FORMULA:
CAC = (Sales + Marketing Spend) / New Customers Acquired

QUICK REFERENCE:
- B2B SaaS benchmarks: $1K-$5K for SMB, $5K-$15K for Mid-Market, $15K+ for Enterprise
- Target: CAC ≤ 1/3 of first-year customer value
- Payback period: < 12 months preferred
```

**Lifetime Value (LTV)**
```
See Attribution & ROI skill for full details

FORMULA:
LTV = ARPA × Gross Margin % / Churn Rate

QUICK REFERENCE:
- Target: LTV ≥ 3x CAC
- Improve LTV by: reducing churn, increasing ARPA, driving expansion
```

**Gross Margin**
```
FORMULA:
Gross Margin % = (Revenue - COGS) / Revenue × 100%

COGS (Cost of Goods Sold) for SaaS:
- Hosting (AWS, GCP, Azure)
- Third-party APIs and services
- Customer support team
- Professional services (onboarding, implementation)

EXAMPLE:
MRR: $100,000
COGS: $20,000 (hosting, support, APIs)
Gross Margin = ($100,000 - $20,000) / $100,000 = 80%

BENCHMARKS (SaaS):
- <70%: Low margin (high infrastructure or support costs)
- 70-80%: Typical SaaS
- 80-90%: Excellent (efficient operations)
- >90%: Best-in-class

WHY IT MATTERS:
Gross margin determines how much you can spend on CAC
80% gross margin = $80 of every $100 is "profit" to spend on growth
Used in LTV calculations (LTV based on gross profit, not revenue)
```

**Magic Number (Sales Efficiency)**
```
FORMULA:
Magic Number = Net New ARR (this quarter) / Sales & Marketing Spend (last quarter)

EXAMPLE:
Q1 Sales & Marketing Spend: $150,000
Q2 Net New ARR: $120,000
Magic Number = $120,000 / $150,000 = 0.8

INTERPRETATION:
For every $1 spent on sales & marketing last quarter, you generated $0.80 in new ARR this quarter

BENCHMARKS:
- <0.5: Inefficient, burning cash (may need to reduce spend)
- 0.5-0.75: Acceptable, but room for improvement
- 0.75-1.0: Good efficiency
- >1.0: Excellent (generating more ARR than spend)

WHY IT MATTERS:
Magic Number tells you if you should scale spend
>0.75 = green light to scale
<0.5 = fix efficiency before scaling
```

**CAC Payback Period**
```
See Attribution & ROI skill for full details

FORMULA:
Payback Period (months) = CAC / (ARPA × Gross Margin %)

BENCHMARK:
<12 months preferred, <6 months excellent
```

## Building Revenue Dashboards

### Executive Dashboard (Board/Leadership)

**Key Metrics to Display:**
```
REVENUE SECTION:
- MRR (current + trend graph)
- MRR Growth Rate (MoM %)
- ARR (current + YoY growth %)
- Revenue by Segment (pie chart)

GROWTH SECTION:
- Net New MRR (New + Expansion - Contraction - Churn)
- MRR Growth Components (waterfall chart)
- New Customer Adds (count + trend)
- Customer Count (total active)

RETENTION SECTION:
- Customer Churn Rate (%)
- MRR Churn Rate (%)
- Net Revenue Retention (NRR %)
- Expansion Rate (%)

UNIT ECONOMICS:
- ARPA (current + trend)
- LTV (calculated)
- CAC (blended)
- LTV:CAC Ratio
- CAC Payback Period (months)
- Gross Margin (%)

PIPELINE (forward-looking):
- Sales Pipeline Value
- Pipeline Coverage Ratio
- Weighted Pipeline
- Forecast vs Target (progress bar)

UPDATE FREQUENCY: Monthly (with weekly snapshots for critical metrics)
```

### Sales Dashboard

**Key Metrics:**
```
PIPELINE HEALTH:
- Total Pipeline Value (by stage)
- Pipeline by Sales Rep
- Pipeline Coverage Ratio
- Weighted Pipeline vs Quota

CONVERSION METRICS:
- Win Rate (overall + by stage)
- Average Sales Cycle Length
- Conversion Rates by Stage
- Opportunities Created (trend)

PERFORMANCE:
- Closed-Won Deals (count + value)
- Quota Attainment (% by rep)
- Average Contract Value (ACV)
- Revenue by Product/Tier

ACTIVITY:
- Calls/Emails Sent (by rep)
- Meetings Booked
- Demos Completed
- Proposals Sent

UPDATE FREQUENCY: Daily or real-time (in CRM)
```

### Marketing Dashboard

**Key Metrics:**
```
LEAD GENERATION:
- Total Leads (by channel)
- MQLs (by channel)
- Lead Velocity Rate (LVR)
- Cost per MQL (by channel)

CONVERSION:
- Visitor-to-Lead Rate (%)
- Lead-to-MQL Rate (%)
- MQL-to-SQL Rate (%)
- MQL-to-Customer Rate (%)

PIPELINE CONTRIBUTION:
- Marketing-Sourced Pipeline ($)
- Marketing-Influenced Pipeline ($)
- Opportunities from Marketing
- Closed-Won from Marketing

ROI:
- Marketing Spend (by channel)
- Revenue Attributed (by channel)
- Channel ROI (%)
- CAC by Channel

CONTENT:
- Top Performing Content (by conversions)
- Traffic by Source
- Engagement Metrics

UPDATE FREQUENCY: Weekly (with real-time campaign monitoring)
```

### Customer Success Dashboard

**Key Metrics:**
```
HEALTH & ENGAGEMENT:
- Customers by Health Score (Healthy/Stable/At Risk/Critical)
- NPS (overall + trend)
- Support Ticket Volume
- Product Adoption Rate (%)

RETENTION:
- Customer Churn Rate (%)
- MRR Churn Rate (%)
- Net Revenue Retention (%)
- Renewal Rate (%)

EXPANSION:
- Expansion MRR (trend)
- Expansion Rate (%)
- Upsell Pipeline
- Cross-sell Pipeline

AT-RISK ACCOUNTS:
- Accounts with Health Score < 60
- Accounts with Declining Usage
- Accounts with High Support Tickets
- Renewal Risk ($)

UPDATE FREQUENCY: Weekly (with daily monitoring of at-risk accounts)
```

## Tools and Technology

**Business Intelligence (BI) Tools:**
- **Google Data Studio** (free): Easy dashboards, connects to Google Analytics, Sheets
- **Tableau** ($70+/user/month): Powerful visualization, enterprise-grade
- **Power BI** ($10+/user/month): Microsoft ecosystem, affordable
- **Looker** (enterprise pricing): Advanced data modeling, embedded analytics
- **Metabase** (open source): Self-hosted, developer-friendly BI

**Revenue Analytics Platforms:**
- **ChartMogul** ($100+/month): SaaS metrics (MRR, churn, LTV, cohorts)
- **Baremetrics** ($108+/month): SaaS analytics for Stripe, Braintree
- **ProfitWell** (free + paid): Free SaaS metrics, paid cohort analysis
- **Geckoboard** ($49+/month): Simple dashboards, KPI tracking
- **Klipfolio** ($90+/month): Custom metrics, multi-source dashboards

**CRM Analytics:**
- **HubSpot** (built-in): Sales, marketing, customer dashboards
- **Salesforce Reports & Dashboards** (built-in): Enterprise reporting
- **Pipedrive Insights** (built-in): Simple sales analytics

**Data Warehouses:**
- **BigQuery** (Google): Pay-per-query, scales infinitely
- **Snowflake** ($40+/month): Modern data warehouse, separate compute/storage
- **Redshift** (AWS): AWS-native data warehouse
- **PostgreSQL** (free): Self-hosted, open-source database

**ETL/Data Integration:**
- **Fivetran** ($1+/month per connector): Auto-sync data to warehouse
- **Stitch** ($100+/month): ETL for common sources
- **Airbyte** (open source): Self-hosted data integration
- **Zapier** ($29.99+/month): Simple integrations, no-code

**Spreadsheet Tools:**
- **Google Sheets** (free): Formulas, pivot tables, charts
- **Excel** (free with Office): Advanced analytics, Power Query
- **Airtable** ($20+/month): Database + spreadsheet, relational data

## Revenue Analytics ROI

**Investment:**
```
TOOLS (monthly):
- SaaS metrics platform (ChartMogul): $100
- BI tool (Power BI): $50 (5 users × $10)
- Data warehouse (BigQuery): $50 (small usage)
- ETL (Fivetran): $100 (2 connectors)
Total: $300/month = $3,600/year

LABOR:
- Initial setup: 40 hours @ $100/hour = $4,000 (one-time)
- Ongoing maintenance: 10 hours/month @ $100/hour = $12,000/year

TOTAL YEAR 1: $19,600
ONGOING (year 2+): $15,600/year
```

**Value:**
```
SCENARIO: $1M ARR company without revenue analytics

BEFORE:
- Can't identify which marketing channels drive revenue (waste 30% of budget)
- Don't track churn by cohort (miss early warning signs)
- No sales pipeline visibility (miss quota by 15%)
- Can't prove ROI to investors (difficulty raising next round)

AFTER (with analytics):
- Reallocate marketing spend from 2.5:1 ROI channels to 5:1 ROI channels
  → +$100K revenue

- Identify at-risk customers 60 days earlier, reduce churn by 25%
  → Reduce annual churn from $120K to $90K = +$30K MRR = +$360K ARR

- Improve pipeline visibility, identify bottlenecks, increase win rate from 25% to 30%
  → +20% more closed deals = +$200K revenue

- Investor-ready metrics enable faster fundraising at better terms
  → $50K saved in dilution/terms

TOTAL VALUE: $710K in Year 1
INVESTMENT: $19,600
ROI: 3,524%
```

## Common Analytics Mistakes

**1. Tracking Vanity Metrics**
- **Mistake:** Focusing on website traffic, social followers, raw leads
- **Impact:** Team optimizes for metrics that don't correlate with revenue
- **Solution:** Focus on revenue, pipeline, CAC, LTV, and conversion rates

**2. Inconsistent Definitions**
- **Mistake:** Sales and marketing define "qualified lead" differently
- **Impact:** Misalignment, blame game, inaccurate reporting
- **Solution:** Document clear definitions, get cross-functional alignment

**3. Not Segmenting Data**
- **Mistake:** Reporting on "average" customer without segmentation
- **Impact:** Miss critical insights (e.g., SMB churns at 50%, Enterprise at 5%)
- **Solution:** Segment by customer type, ACV, industry, cohort

**4. Short Time Horizons**
- **Mistake:** Only looking at this month's results
- **Impact:** Miss long-term trends, react to noise instead of signal
- **Solution:** Track trends over 6-12 months, use cohort analysis

**5. Building Reports, Not Taking Action**
- **Mistake:** Creating beautiful dashboards that nobody uses
- **Impact:** Wasted effort, no improvement
- **Solution:** Weekly review meetings, assign owners to metrics, track action items

**6. No Data Governance**
- **Mistake:** Dirty CRM data, inconsistent tracking
- **Impact:** "Garbage in, garbage out" - reports are unreliable
- **Solution:** Implement CRM hygiene practices (see CRM Hygiene skill)

**7. Over-Reliance on Lagging Indicators**
- **Mistake:** Only tracking revenue (lagging indicator)
- **Impact:** Problems detected too late to fix
- **Solution:** Track leading indicators (pipeline, MQLs, lead velocity rate)

**8. Analysis Paralysis**
- **Mistake:** Spending weeks on perfect attribution models
- **Impact:** Delays decision-making, misses opportunities
- **Solution:** Start simple (80/20 rule), iterate based on decisions needed

## Related Skills and Frameworks

**Related Revenue Operations Toolkit Skills:**
- **Pipeline Forecasting** - Uses revenue analytics data for predictions
- **CRM Hygiene** - Clean data is foundation for accurate analytics
- **Attribution & ROI** - Detailed channel-level ROI analysis
- **Sales-Marketing Alignment** - Shared metrics and dashboards
- **Pricing & Packaging** - ARPA and expansion metrics inform pricing

**Related Frameworks:**
- **AAARRR (Pirate Metrics)** - Funnel-based analytics framework
- **Revenue Waterfall** - Stage-by-stage pipeline metrics
- **Unit Economics** - CAC, LTV, payback period calculations
- **GTM Efficiency** - Efficiency metrics (Magic Number, Burn Multiple)

**Complementary Skills:**
- **Cohort Analysis** - Track customer performance by acquisition date
- **Funnel Optimization** - Improve conversion rates at each stage
- **Forecasting** - Predict future revenue based on trends
- **Data Visualization** - Communicate insights effectively

---

**Next Steps:**
1. Audit your current metrics: What are you tracking today?
2. Choose your North Star Metric (the ONE metric that matters most)
3. Build a simple dashboard (start with MRR, churn, pipeline, CAC)
4. Set up weekly metric review meetings (30 minutes, consistent time)
5. Assign metric owners (who's responsible for improving each metric?)
6. Track 2-3 leading indicators (pipeline, MQLs, LVR) for early warnings

**Remember:** Analytics is only valuable if it drives action. Track fewer metrics, review them consistently, and make decisions based on data. Start simple, improve over time.
