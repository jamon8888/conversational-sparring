# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Attribution & ROI: Measure What Matters in Marketing

## Overview

Marketing attribution is the practice of identifying which marketing touchpoints contribute to revenue outcomes (leads, opportunities, closed deals). ROI measurement quantifies the financial return of marketing investments. For solo entrepreneurs and small teams, attribution answers the critical question: "Which marketing channels should I invest in?" Without attribution, you're flying blind—wasting budget on ineffective channels while underinvesting in winners.

**When to use this skill:**
- You're spending money on multiple marketing channels (ads, content, events)
- Leadership asks "What's our marketing ROI?" and you can't answer confidently
- You need to allocate next quarter's marketing budget
- Sales complains that "marketing leads don't convert"
- You want to prove marketing's contribution to pipeline and revenue
- You're launching a new campaign and need to track performance
- Board or investors ask about CAC, LTV, and payback period
- You're scaling spend and need to identify diminishing returns

**Why attribution and ROI matter:**
- **Budget efficiency:** Shift spending from low-ROI to high-ROI channels
- **Prove marketing value:** Demonstrate marketing's contribution to revenue
- **Strategic decisions:** Know which campaigns to scale vs. kill
- **Sales-marketing alignment:** Shared definition of lead quality and sources
- **Investor confidence:** Show disciplined capital allocation
- **Forecasting:** Predict pipeline impact of marketing investments

**The cost of poor attribution:**
- 30-50% of marketing budget wasted on ineffective channels
- Can't scale winners because you don't know which channels work
- Sales and marketing blame each other for poor performance
- Executives lose confidence in marketing team
- Miss revenue targets due to insufficient pipeline generation

## Multi-Touch Attribution Models

### Understanding Attribution Models

**First-Touch Attribution**
```
DEFINITION:
100% credit to the first touchpoint that introduced the lead

EXAMPLE:
Lead journey: Blog Post → Webinar → Demo → Customer
Credit: 100% to Blog Post

PROS:
- Simple to implement and understand
- Good for measuring brand awareness and top-of-funnel
- Highlights channels that generate new leads

CONS:
- Ignores nurturing and conversion touchpoints
- Overvalues first touch, undervalues sales effort
- Not useful for multi-channel attribution

BEST FOR:
- Content marketing ROI
- Brand awareness campaigns
- Top-of-funnel lead generation focus
```

**Last-Touch Attribution**
```
DEFINITION:
100% credit to the last touchpoint before conversion

EXAMPLE:
Lead journey: Blog Post → Webinar → Demo → Customer
Credit: 100% to Demo

PROS:
- Simple to implement and understand
- Good for measuring conversion effectiveness
- Highlights bottom-of-funnel channels

CONS:
- Ignores all earlier nurturing touchpoints
- Overvalues last touch, ignores brand-building
- Sales-led orgs may see "direct" as last touch

BEST FOR:
- Direct response campaigns
- Conversion-focused measurement
- Short sales cycles (< 30 days)
```

**Linear (Multi-Touch) Attribution**
```
DEFINITION:
Equal credit to all touchpoints in the journey

EXAMPLE:
Lead journey: Blog Post → Webinar → Email → Demo → Customer
Credit: 20% each to all 5 touchpoints

PROS:
- Recognizes all touchpoints contribute
- Fair middle-ground approach
- Good for understanding full journey

CONS:
- May over-credit low-impact touches
- Doesn't differentiate high-value vs low-value touches
- Can dilute insight on what really drives conversions

BEST FOR:
- Long, complex sales cycles
- Multi-channel strategies
- Starting point before customizing model
```

**U-Shaped (Position-Based) Attribution**
```
DEFINITION:
40% credit to first touch, 40% to last touch, 20% split among middle touches

EXAMPLE:
Lead journey: Blog Post → Webinar → Email → Demo → Customer
Credit: 40% Blog, 6.7% Webinar, 6.7% Email, 40% Demo, 6.7% Customer (opp creation)

PROS:
- Balances awareness and conversion
- Recognizes importance of first and last touch
- Still gives credit to nurturing

CONS:
- Somewhat arbitrary weighting
- May not match your actual buyer journey
- Complex to explain to stakeholders

BEST FOR:
- B2B SaaS with defined nurture process
- Balancing brand and demand gen
- 30-90 day sales cycles
```

**W-Shaped Attribution**
```
DEFINITION:
30% to first touch, 30% to lead conversion touch, 30% to opportunity creation, 10% split among other touches

EXAMPLE:
Lead journey: Blog Post → Downloaded eBook (became MQL) → Webinar (became Opp) → Demo → Customer
Credit: 30% Blog, 30% eBook, 30% Webinar, 5% Demo, 5% Close activities

PROS:
- Recognizes key milestone transitions (MQL, Opp)
- Aligns with marketing and sales handoffs
- Good for complex B2B journeys

CONS:
- Requires clear stage definitions
- More complex to implement
- Needs CRM integration and tracking

BEST FOR:
- B2B companies with defined lead stages
- Sales-marketing alignment initiatives
- Understanding which channels drive MQLs vs Opps
```

**Time-Decay Attribution**
```
DEFINITION:
More credit to recent touchpoints, less to older ones (exponential decay)

EXAMPLE:
Lead journey over 60 days: Blog (day 1) → Webinar (day 30) → Demo (day 55) → Customer (day 60)
Credit: 10% Blog, 20% Webinar, 35% Demo, 35% Close touch

PROS:
- Reflects buyer psychology (recency matters)
- Good for measuring bottom-of-funnel impact
- Balances early and late touches naturally

CONS:
- May undervalue brand-building content
- Decay rate is somewhat arbitrary (7 days? 30 days?)
- Complex to calculate manually

BEST FOR:
- Long sales cycles (90+ days)
- Nurture-heavy strategies
- Measuring acceleration of late-stage deals
```

**Custom/Algorithmic Attribution**
```
DEFINITION:
Machine learning analyzes thousands of journeys to determine actual influence of each touchpoint

PROS:
- Most accurate reflection of reality
- Adapts to your specific buyer journey
- Can reveal unexpected insights

CONS:
- Requires significant data (1,000+ conversions)
- Complex to build and maintain
- "Black box" hard to explain to stakeholders
- Requires data science expertise

BEST FOR:
- Large companies with data science teams
- High-volume digital businesses
- Mature attribution programs
```

### Choosing Your Attribution Model

**Decision Framework:**
```
IF sales cycle < 30 days:
  → Use First-Touch or Last-Touch (simple journeys)

IF sales cycle 30-90 days:
  → Use U-Shaped or Linear (balanced approach)

IF sales cycle > 90 days with clear stages:
  → Use W-Shaped (milestone-based)

IF heavy content nurture before conversion:
  → Use Time-Decay (rewards recent engagement)

IF high-volume digital business (ecommerce, PLG SaaS):
  → Use Algorithmic (data-driven optimization)

RECOMMENDATION FOR SMALL TEAMS:
Start with U-Shaped (40/20/40) or Linear, then customize based on insights
```

## Implementing Attribution Tracking

### 1. Technical Setup

**UTM Parameter Strategy**

Consistent UTM tagging for all marketing links:

```
UTM STRUCTURE:
https://yoursite.com/page?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content]&utm_term=[term]

REQUIRED PARAMETERS:
- utm_source: Where traffic comes from (google, linkedin, newsletter, partner-acme)
- utm_medium: Channel type (cpc, social, email, referral, organic)
- utm_campaign: Campaign name (q1-product-launch, webinar-series-2024)

OPTIONAL PARAMETERS:
- utm_content: Variant identifier (ad-variant-a, cta-top, blue-button)
- utm_term: Keyword (for paid search tracking)

NAMING CONVENTIONS (lowercase, hyphens only):
Source: google, linkedin, facebook, twitter, newsletter, partner-[name]
Medium: cpc, display, social, email, referral, organic, affiliate
Campaign: [quarter]-[theme]-[type] (q1-product-launch-webinar)
Content: [variant]-[placement]-[creative] (ad-a-feed-video)
```

**UTM Tagging Examples:**
```
GOOGLE ADS:
utm_source=google&utm_medium=cpc&utm_campaign=q1-brand-search&utm_term=revenue-operations-software

LINKEDIN ORGANIC POST:
utm_source=linkedin&utm_medium=social&utm_campaign=thought-leadership-q1&utm_content=post-attribution-guide

EMAIL NEWSLETTER:
utm_source=newsletter&utm_medium=email&utm_campaign=monthly-feb-2024&utm_content=cta-primary

PARTNER REFERRAL:
utm_source=partner-acme&utm_medium=referral&utm_campaign=partner-program-2024

WEBINAR PROMOTION:
utm_source=linkedin&utm_medium=cpc&utm_campaign=attribution-webinar-jan-2024&utm_content=ad-variant-b

TRADE SHOW:
utm_source=trade-show-b2b-expo&utm_medium=event&utm_campaign=b2b-expo-2024&utm_content=booth-scan
```

**CRM Lead Source Tracking**

Map UTM parameters to CRM fields:

```
CRM FIELD MAPPING:

Lead Source (dropdown) ← utm_medium
- Organic Search
- Paid Search
- Social Media - Organic
- Social Media - Paid
- Email Marketing
- Referral
- Direct
- Event
- Partner

Lead Source Detail (text) ← utm_source
- Examples: google, linkedin, newsletter, partner-acme

Campaign Name (text) ← utm_campaign
- Examples: q1-product-launch, webinar-series-2024

Ad Content (text) ← utm_content
- Examples: ad-variant-a, cta-top

Search Keyword (text) ← utm_term
- Examples: revenue operations software

Original Referrer (URL) ← HTTP referrer
- Full referring URL (first touch)

Landing Page (URL) ← First page visited
- Full URL of first page

IMPORTANT RULES:
1. Capture on FIRST touch (store in cookie)
2. Never overwrite original source
3. Track both first and last touch
4. Create "Lead Source History" table for all touches
```

**Multi-Touch Journey Tracking**

Store all touchpoints, not just first/last:

```
DATABASE SCHEMA (conceptual):

CONTACT TABLE:
- contact_id
- email
- first_touch_source (from first session)
- first_touch_campaign
- first_touch_date
- last_touch_source (most recent session)
- last_touch_campaign
- last_touch_date

TOUCHPOINT TABLE (many-to-one with CONTACT):
- touchpoint_id
- contact_id (foreign key)
- timestamp
- utm_source
- utm_medium
- utm_campaign
- utm_content
- utm_term
- page_url
- session_id
- referrer

CONVERSION TABLE:
- conversion_id
- contact_id (foreign key)
- conversion_type (MQL, SQL, Opportunity, Customer)
- conversion_date
- conversion_value (deal amount)
- attributed_touchpoints (JSON array or separate table)

EXAMPLE QUERY (simplified):
SELECT contact_id,
       COUNT(*) as touchpoint_count,
       MIN(timestamp) as first_touch,
       MAX(timestamp) as last_touch,
       DATEDIFF(day, MIN(timestamp), MAX(timestamp)) as journey_length_days
FROM touchpoint
WHERE contact_id IN (SELECT contact_id FROM conversion WHERE conversion_type = 'Customer')
GROUP BY contact_id
```

### 2. Tracking Setup by Channel

**Website Analytics (Google Analytics 4)**
```
GOALS TO TRACK:
- Form submissions (demo request, contact us, download)
- Account signups (for freemium/trial)
- Key page views (pricing, case studies)
- Video plays (product demos)
- Time on site (engagement metric)

CUSTOM EVENTS:
- CTA clicks (which CTAs drive conversions)
- Scroll depth (content engagement)
- Button clicks (feature interest)
- File downloads (lead magnets)

CONVERSION PATHS:
- Multi-Channel Funnels (in GA4: Path exploration)
- Time to conversion
- Touchpoint sequence analysis
- Assisted conversions by channel
```

**Email Marketing (HubSpot, Mailchimp, etc.)**
```
TRACK:
- Email opens (engagement signal, not attribution)
- Link clicks (count as touchpoint)
- Unsubscribes (negative signal)
- Replies (high-intent signal)

ATTRIBUTION STRATEGY:
- Use unique UTM per email campaign
- Track email → landing page → conversion
- Segment by email type (newsletter, nurture, promo)
- Calculate email-influenced pipeline

IMPORTANT:
Don't over-attribute email opens (easily inflated)
Focus on clicks and post-click behavior
```

**Paid Advertising (Google Ads, LinkedIn Ads, Facebook Ads)**
```
TRACK:
- Impressions (awareness metric)
- Clicks (engagement)
- Cost per click (efficiency)
- Conversions (goal completions)
- Conversion value (revenue attributed)

AUTO-TAGGING:
- Google Ads: Enable auto-tagging (gclid parameter)
- LinkedIn: Use LinkedIn Insight Tag + conversion tracking
- Facebook: Use Facebook Pixel + Conversions API

MANUAL TRACKING:
- Add UTM parameters to all ad URLs
- Create separate campaigns by audience/creative
- Track offline conversions (from CRM back to ad platform)
```

**Content Marketing (Blog, SEO, Organic Social)**
```
TRACK:
- Organic traffic by page
- Time on page (engagement)
- Scroll depth (content consumption)
- Social shares (reach amplification)
- Conversions by content piece

ATTRIBUTION STRATEGY:
- First-touch: Which content pieces generate new leads?
- Assisted conversions: Which content nurtures leads?
- Content by funnel stage (TOFU, MOFU, BOFU)
- Revenue by content topic

MEASUREMENT:
- Use Google Search Console for keyword attribution
- Track "organic search" as channel
- Segment by content type (blog, case study, ebook)
```

**Events and Webinars**
```
TRACK:
- Registrations (captured via form with UTMs)
- Attendance rate (showed up)
- Engagement (Q&A, polls, chat)
- Post-event conversions (demo requests, trials)

ATTRIBUTION:
- Tag event registrations with utm_source=event-[name]
- Track registration → attendance → conversion
- Measure pipeline generated within 30/60/90 days
- Compare virtual vs in-person event ROI

OFFLINE EVENTS:
- Badge scans → CRM with lead source = event name
- Use unique promo codes or links
- Manual data entry with consistent naming
```

### 3. Attribution Reporting

**Attribution Report Structure**

**Report 1: Channel Performance (First-Touch)**
```
COLUMNS:
- Channel (e.g., Organic Search, Paid Social, Referral)
- New Leads (count)
- MQLs (count + conversion rate)
- SQLs (count + MQL→SQL rate)
- Opportunities Created (count + SQL→Opp rate)
- Opportunities Won (count + win rate)
- Revenue (sum of closed-won deals)
- CAC (total channel spend / new customers)
- ROI (revenue / channel spend)

EXAMPLE:
Channel            | Leads | MQLs | SQLs | Opps | Won | Revenue  | Spend   | ROI
Organic Search     | 450   | 120  | 45   | 22   | 8   | $240,000 | $5,000  | 48x
Paid LinkedIn      | 280   | 95   | 38   | 18   | 6   | $180,000 | $25,000 | 7.2x
Content Syndication| 520   | 78   | 12   | 4    | 1   | $30,000  | $8,000  | 3.75x
Referral           | 65    | 52   | 38   | 20   | 12  | $360,000 | $2,000  | 180x

INSIGHTS:
- Referral has highest quality (80% MQL rate) and ROI
- Organic Search is highest volume, strong ROI
- Content Syndication has poor conversion (15% MQL rate)
- Decision: Scale Referral program, maintain Organic, pause Content Syndication
```

**Report 2: Campaign Performance**
```
COLUMNS:
- Campaign Name
- Launch Date
- Status (Active, Paused, Completed)
- Impressions
- Clicks
- CTR (click-through rate)
- Conversions (by type: MQL, SQL, Opp)
- Spend
- Cost per MQL
- Cost per Opportunity
- Pipeline Generated
- Revenue Closed
- ROI

EXAMPLE:
Campaign                    | Clicks | MQLs | Cost/MQL | Opps | Pipeline  | Spend   | ROI
Q1 Product Launch Webinar   | 820    | 156  | $45      | 12   | $360,000  | $7,000  | 51x
ABM Enterprise Outreach     | 340    | 48   | $156     | 8    | $480,000  | $7,500  | 64x
Thought Leadership LinkedIn | 2,400  | 312  | $32      | 18   | $540,000  | $10,000 | 54x

INSIGHTS:
- ABM has highest deal size ($60K avg) despite lower volume
- Webinar has best MQL quality (7.7% MQL→Opp rate)
- LinkedIn has highest volume, good efficiency at scale
```

**Report 3: Multi-Touch Attribution (W-Shaped)**
```
Shows credit distribution across journey stages

EXAMPLE DEAL JOURNEY:
Contact: Acme Corp (Deal: $50,000)

Touchpoints:
1. Blog post (organic search) - Day 1
2. Downloaded ebook - Day 8 (became MQL)
3. Attended webinar - Day 22 (became Opportunity)
4. Demo call - Day 35
5. Pricing page visit - Day 40
6. Sales call - Day 42 (closed-won)

W-SHAPED CREDIT (30/30/30/10):
1. Blog post: 30% = $15,000 attributed revenue
2. Ebook download: 30% = $15,000
3. Webinar: 30% = $15,000
4. Demo + Pricing + Sales: 10% split = $1,667 each

ROLL-UP BY CHANNEL:
- Organic Search (blog): $15,000
- Content Marketing (ebook): $15,000
- Webinar: $15,000
- Sales Activities (demo, pricing, calls): $5,000

INSIGHTS:
- Content and webinars drive most attribution
- Sales activities get credit but less than marketing
- Organic search initiated the journey
```

## Key Marketing ROI Metrics

### Customer Acquisition Cost (CAC)

**Basic CAC Formula:**
```
CAC = Total Sales & Marketing Expenses / Number of New Customers Acquired

EXAMPLE:
Sales & Marketing Spend: $50,000/month
New Customers: 25/month
CAC = $50,000 / 25 = $2,000 per customer

WHAT TO INCLUDE:
Marketing Expenses:
- Advertising spend (paid search, social, display)
- Marketing software (CRM, automation, analytics)
- Content production (writers, designers, video)
- Events and sponsorships
- Agency/contractor fees
- Marketing team salaries + benefits

Sales Expenses:
- Sales team salaries + benefits
- Sales commissions (base, not accelerators)
- Sales software (CRM, sales engagement, dialers)
- Sales training and enablement
- Travel and entertainment

WHAT TO EXCLUDE:
- Customer success costs (post-sale)
- Product development costs
- General overhead (office rent, HR, finance)
```

**Blended vs. Paid CAC:**
```
BLENDED CAC:
= Total Sales & Marketing Spend / New Customers
Includes all channels (organic, paid, referral)

PAID CAC:
= Paid Marketing Spend Only / New Customers from Paid Channels
Isolates paid channel efficiency

EXAMPLE:
Total spend: $50,000
Paid spend: $30,000
New customers: 25 total (15 from paid, 10 from organic/referral)

Blended CAC = $50,000 / 25 = $2,000
Paid CAC = $30,000 / 15 = $2,000

Note: Same CAC, but paid is doing more work than it appears
```

**CAC by Channel:**
```
FORMULA:
Channel CAC = Channel Spend / New Customers Attributed to Channel

EXAMPLE:
Organic Search:
- SEO + Content Spend: $5,000/month
- New Customers: 8
- CAC = $625

Paid LinkedIn:
- Ad Spend: $15,000/month
- New Customers: 6
- CAC = $2,500

Referral Program:
- Program Costs + Rewards: $2,000/month
- New Customers: 4
- CAC = $500

INSIGHT:
Referral and Organic have lowest CAC, but limited scalability
Paid LinkedIn is expensive but scalable
```

**CAC Benchmarks:**
```
B2B SaaS (by ACV):
- <$5K ACV: $500-$1,500 CAC
- $5K-$25K ACV: $1,500-$5,000 CAC
- $25K-$100K ACV: $5,000-$15,000 CAC
- >$100K ACV: $15,000-$50,000+ CAC

RULE OF THUMB:
CAC should be ≤ 1/3 of first-year customer value
Payback period should be < 12 months
LTV:CAC ratio should be ≥ 3:1
```

### Customer Lifetime Value (LTV)

**Basic LTV Formula:**
```
LTV = Average Revenue per Customer × Average Customer Lifespan

OR (for subscriptions):
LTV = ARPA × Gross Margin % / Churn Rate %

EXAMPLE (subscription):
ARPA (average revenue per account): $500/month
Gross Margin: 80%
Monthly Churn: 3%

LTV = ($500 × 0.80) / 0.03 = $400 / 0.03 = $13,333

INTERPRETATION:
Average customer is worth $13,333 in gross profit over their lifetime
```

**Cohort-Based LTV:**
```
More accurate method: Track actual cohort retention and revenue

COHORT EXAMPLE (Jan 2024 cohort):
Month 0: 100 customers, $50,000 MRR ($500 ARPA)
Month 1: 97 customers, $48,500 MRR (3% churn)
Month 2: 94 customers, $47,000 MRR
Month 3: 91 customers, $45,500 MRR
...
Month 24: 45 customers, $22,500 MRR

Total Revenue from Cohort (24 months): $950,000
LTV per Customer = $950,000 / 100 = $9,500

This is more accurate than formula-based LTV
```

**LTV by Segment:**
```
Track LTV by customer segment for better targeting

EXAMPLE:
Enterprise (>200 employees):
- ARPA: $2,000/month
- Churn: 1.5%
- LTV = ($2,000 × 0.80) / 0.015 = $106,667

Mid-Market (50-200 employees):
- ARPA: $800/month
- Churn: 2.5%
- LTV = ($800 × 0.80) / 0.025 = $25,600

SMB (<50 employees):
- ARPA: $300/month
- Churn: 5%
- LTV = ($300 × 0.80) / 0.05 = $4,800

INSIGHT:
Enterprise customers are 22x more valuable than SMB
Should allocate CAC accordingly (can spend $10K+ to acquire Enterprise)
```

### LTV:CAC Ratio

**Formula:**
```
LTV:CAC Ratio = Customer Lifetime Value / Customer Acquisition Cost

EXAMPLE:
LTV: $13,333
CAC: $2,000
Ratio = $13,333 / $2,000 = 6.7:1

INTERPRETATION:
For every $1 spent acquiring customers, you get $6.70 back in lifetime value
```

**Benchmark Targets:**
```
LTV:CAC < 1:1 = Losing money on every customer (unsustainable)
LTV:CAC = 1-3:1 = Breakeven to marginally profitable (underinvesting in growth)
LTV:CAC = 3-5:1 = Healthy, sustainable growth ✓
LTV:CAC > 5:1 = Very efficient (but may be underinvesting in marketing)

SWEET SPOT: 3-4:1 for high-growth companies
```

**LTV:CAC by Channel:**
```
Calculate for each marketing channel to find winners

EXAMPLE:
Organic Search:
- LTV: $13,333
- CAC: $625
- Ratio: 21:1 (amazing, but hard to scale)

Paid LinkedIn:
- LTV: $13,333
- CAC: $2,500
- Ratio: 5.3:1 (good, scalable)

Paid Google:
- LTV: $8,000 (lower quality, higher churn)
- CAC: $3,500
- Ratio: 2.3:1 (marginal, needs optimization or pause)

INSIGHT:
Organic is most efficient but supply-limited
LinkedIn is scalable with good unit economics
Google needs work (improve targeting or pause)
```

### Payback Period

**Formula:**
```
Payback Period (months) = CAC / (ARPA × Gross Margin %)

EXAMPLE:
CAC: $2,000
ARPA: $500/month
Gross Margin: 80%

Payback = $2,000 / ($500 × 0.80) = $2,000 / $400 = 5 months

INTERPRETATION:
Takes 5 months of subscription revenue to recover customer acquisition cost
```

**Payback Period Benchmarks:**
```
TARGETS (B2B SaaS):
< 6 months: Excellent (can scale aggressively)
6-12 months: Good (healthy, sustainable)
12-18 months: Acceptable (if LTV is strong)
> 18 months: Risky (long time to recover investment)

FACTORS:
- Shorter payback = faster cash recovery = more capital efficient
- Longer payback acceptable if LTV is very high and churn is low
- Venture-backed companies can tolerate longer payback (patient capital)
- Bootstrapped companies need shorter payback (limited cash runway)
```

**Payback Period by Channel:**
```
EXAMPLE:
Referral Program:
- CAC: $500
- ARPA: $500
- Payback = $500 / ($500 × 0.80) = 1.25 months ✓

Paid Ads:
- CAC: $2,500
- ARPA: $400 (lower quality)
- Payback = $2,500 / ($400 × 0.80) = 7.8 months

INSIGHT:
Referral program recovers cost in 1.25 months (prioritize!)
Paid ads take nearly 8 months (need to improve targeting or ARPA)
```

### Marketing-Sourced Pipeline

**Formula:**
```
Marketing-Sourced Pipeline = Total Pipeline Where First Touch = Marketing Channel

EXAMPLE:
Total Pipeline: $2M
- Marketing-sourced first touch: $1.4M (70%)
- Sales-sourced (outbound, referral): $600K (30%)

Marketing-sourced % = 70%
```

**Marketing-Influenced Pipeline:**
```
Marketing-Influenced Pipeline = Total Pipeline Where ANY Touch = Marketing

EXAMPLE:
Total Pipeline: $2M
- Marketing-influenced (any touch): $1.8M (90%)
- Sales-only (no marketing touches): $200K (10%)

Marketing-influenced % = 90%

INTERPRETATION:
Marketing touched 90% of pipeline at some point
Marketing sourced (first touch) 70% of pipeline
```

**Marketing Contribution Metrics:**
```
TRACK BOTH:
1. Marketing-Sourced: Did marketing generate the lead?
2. Marketing-Influenced: Did marketing nurture/assist the deal?

EXAMPLE DASHBOARD:
Q1 2024 Pipeline: $3M total

Marketing-Sourced:
- Organic Search: $800K (27%)
- Paid Ads: $600K (20%)
- Events/Webinars: $400K (13%)
- Content Downloads: $300K (10%)
Total: $2.1M (70% of pipeline)

Marketing-Influenced (assisted):
- Email Nurture: +$400K
- Webinars (not first touch): +$200K
- Case Studies: +$100K
Total Influenced: $2.8M (93% of pipeline)

Sales-Sourced Only: $200K (7%)
```

### Channel ROI

**Formula:**
```
Channel ROI = (Revenue from Channel - Channel Cost) / Channel Cost × 100%

EXAMPLE:
Paid LinkedIn:
- Spend: $25,000
- Revenue attributed (closed-won): $180,000
- ROI = ($180,000 - $25,000) / $25,000 × 100% = 620%

INTERPRETATION:
For every $1 spent on LinkedIn ads, you get $6.20 back in revenue
Net profit: $155,000
```

**Time-Bound ROI:**
```
IMPORTANT: Define time window for attribution

30-Day ROI:
= Revenue from customers acquired within 30 days of channel touch / Channel spend

90-Day ROI:
= Revenue from customers acquired within 90 days / Channel spend

EXAMPLE:
Webinar Spend: $5,000

30-Day Revenue: $25,000 (ROI = 400%)
90-Day Revenue: $85,000 (ROI = 1,600%)
180-Day Revenue: $150,000 (ROI = 2,900%)

INSIGHT:
Long sales cycles (90+ days) make short-term ROI measurement misleading
Use 90-180 day windows for B2B
```

**ROI by Attribution Model:**
```
SAME CHANNEL, DIFFERENT MODELS:

Content Marketing (Blog + SEO):
Cost: $10,000/month

First-Touch Attribution:
- 30 customers × $5,000 ACV = $150,000 revenue
- ROI = 1,400%

Multi-Touch Attribution (Linear):
- Blog credited with 25% of 80 customers
- 20 customers × $5,000 = $100,000
- ROI = 900%

INSIGHT:
Attribution model choice dramatically changes ROI calculation
Be consistent and transparent about methodology
```

## Campaign ROI Analysis

**Campaign ROI Template:**
```
CAMPAIGN: Q1 Product Launch Webinar Series

COSTS:
Paid Promotion:
- LinkedIn ads: $8,000
- Google ads: $3,000
- Retargeting: $1,500
Subtotal: $12,500

Production:
- Platform (Zoom/Demio): $200
- Design (landing page, emails): $1,000
- Copywriting: $800
- Webinar host time (4 hours × $150): $600
Subtotal: $2,600

Total Cost: $15,100

RESULTS (90-day attribution window):
- Registrants: 840
- Attendees: 378 (45% show-up rate)
- MQLs: 156
- SQLs: 42
- Opportunities: 12
- Closed-Won: 4
- Revenue: $80,000

METRICS:
Cost per Registrant: $15,100 / 840 = $18
Cost per Attendee: $15,100 / 378 = $40
Cost per MQL: $15,100 / 156 = $97
Cost per SQL: $15,100 / 42 = $359
Cost per Opportunity: $15,100 / 12 = $1,258
Cost per Customer: $15,100 / 4 = $3,775
CAC: $3,775 (for this campaign)

ROI:
= ($80,000 - $15,100) / $15,100 × 100%
= $64,900 / $15,100 × 100%
= 430% ROI

PAYBACK:
ACV: $20,000
ARPA: $1,667/month
Gross Margin: 80%
Payback = $3,775 / ($1,667 × 0.80) = 2.8 months

VERDICT: Strong campaign
- 430% ROI within 90 days
- 2.8 month payback
- $1,258 cost per opportunity is reasonable
- 2.7% registrant → customer rate

RECOMMENDATION: Run again, test to improve show-up rate (45% → 55%)
```

## Tools and Technology

**Attribution Platforms:**
- **HubSpot** (free-$800/month): Built-in attribution reporting, multi-touch models
- **Salesforce + Pardot** ($1,250+/month): Enterprise attribution, custom models
- **Bizible/Marketo Measure** ($2,000+/month): Advanced B2B attribution (Adobe)
- **DreamData** ($999+/month): B2B revenue attribution, account-based
- **Ruler Analytics** ($199+/month): Call tracking + marketing attribution
- **Wicked Reports** ($250+/month): Ecommerce attribution + LTV tracking

**Analytics Platforms:**
- **Google Analytics 4** (free): Multi-channel funnels, conversion paths
- **Mixpanel** ($25+/month): Product analytics, user journey tracking
- **Amplitude** ($49+/month): Product analytics + attribution
- **Heap** ($3,600+/year): Auto-capture analytics, retroactive funnels

**Call Tracking (for phone conversions):**
- **CallRail** ($45+/month): Dynamic number insertion, keyword tracking
- **CallTrackingMetrics** ($39+/month): Call attribution + routing
- **Invoca** (enterprise): AI-powered call analytics

**Marketing Dashboards:**
- **Databox** ($49+/month): Pre-built marketing dashboards
- **Klipfolio** ($90+/month): Custom metric dashboards
- **Google Data Studio** (free): Custom dashboards from Google data
- **Supermetrics** ($99+/month): Data connector for dashboards

**Spreadsheet Tools (DIY):**
- **Google Sheets** (free): Manual attribution modeling
- **Excel** (free with Office): Advanced formulas and pivot tables
- **Airtable** ($20+/month): Database + spreadsheet hybrid

## Attribution ROI Calculation

**Investment in Attribution Tracking:**
```
YEAR 1 COSTS:

Tools:
- Marketing automation (HubSpot Marketing): $800/month = $9,600
- Call tracking (CallRail): $45/month = $540
- Attribution platform (DreamData): $999/month = $11,988
Total Tools: $22,128/year

Labor:
- RevOps hire (full-time or fractional): $80,000/year
- Initial setup and integration: $5,000 (one-time)
- Ongoing management: included in RevOps role

Total Year 1: $107,128

YEAR 2+ COSTS (ongoing):
Tools: $22,128/year
Labor: $80,000/year
Total: $102,128/year
```

**Value of Attribution:**
```
SCENARIO: $500K marketing budget, no attribution

BEFORE ATTRIBUTION (flying blind):
- Inefficient budget allocation
- 30% waste on low-ROI channels = $150,000 wasted
- Can't scale winners, so overall marketing ROI is 2.5:1
- Revenue from marketing: $1.25M

AFTER ATTRIBUTION (data-driven):
- Reallocate 30% from low-ROI to high-ROI channels
- Identify and scale 3 high-ROI channels
- Overall marketing ROI improves to 4:1
- Revenue from marketing: $2M

INCREMENTAL VALUE:
Revenue lift: $2M - $1.25M = $750,000
Cost of attribution: $107,128
Net benefit: $642,872
ROI: 600%

ADDITIONAL BENEFITS:
- Sales-marketing alignment improves (shared metrics)
- Faster decision-making (kill bad campaigns in weeks, not months)
- Better forecasting (know which channels drive predictable pipeline)
- Executive confidence (data-driven budget allocation)
```

## Common Attribution Mistakes

**1. Only Tracking Last-Touch**
- **Mistake:** Giving 100% credit to last interaction before purchase
- **Impact:** Undervalues brand-building and early-stage content
- **Solution:** Implement multi-touch attribution (U-shaped or W-shaped)

**2. Inconsistent UTM Tagging**
- **Mistake:** Different team members use different naming conventions
- **Impact:** Can't roll up campaign performance, fragmented reporting
- **Solution:** Document UTM standards, use UTM builder tool, audit quarterly

**3. Not Tracking Offline Conversions**
- **Mistake:** Missing phone calls, in-person meetings, offline events
- **Impact:** Underreporting marketing contribution by 20-40%
- **Solution:** Implement call tracking, manual lead source entry, event badge scans

**4. Ignoring Dark Social**
- **Mistake:** Not tracking private shares (Slack, WhatsApp, dark social)
- **Impact:** Appears as "Direct" traffic, undervalues content/social ROI
- **Solution:** Use branded short links, ask "How did you hear about us?" on forms

**5. Short Attribution Windows**
- **Mistake:** Only measuring 30-day conversions for 90+ day sales cycle
- **Impact:** Undervalues top-of-funnel activities and long-term brand building
- **Solution:** Use 90-180 day windows for B2B, track cohort progression

**6. Not Accounting for Gross Margin**
- **Mistake:** Calculating ROI based on revenue instead of gross profit
- **Impact:** Overstates profitability, especially for low-margin products
- **Solution:** Always use gross profit for LTV and ROI calculations

**7. Forgetting to Include Full CAC**
- **Mistake:** Only counting ad spend, ignoring salaries and software
- **Impact:** CAC appears artificially low, over-allocate to expensive channels
- **Solution:** Fully-loaded CAC includes all sales + marketing expenses

**8. Attribution Without Action**
- **Mistake:** Building fancy dashboards but not changing budget allocation
- **Impact:** Wasted effort, no ROI improvement
- **Solution:** Monthly budget reviews, reallocate 10-20% per quarter based on data

## Related Skills and Frameworks

**Related Revenue Operations Toolkit Skills:**
- **CRM Hygiene** - Clean lead source data is essential for attribution
- **Revenue Analytics** - Attribution feeds into executive dashboards
- **Pipeline Forecasting** - Channel mix affects pipeline predictability
- **Sales-Marketing Alignment** - Shared attribution model prevents disputes
- **Process Automation** - Automate lead source capture and enrichment

**Related Frameworks:**
- **AAARRR (Pirate Metrics)** - Attribution by funnel stage (Acquisition → Revenue)
- **Unit Economics** - CAC and LTV are core unit economics metrics
- **GTM Efficiency** - CAC payback feeds into efficiency scoring
- **Revenue Waterfall** - Attribution by pipeline stage

**Complementary Skills:**
- **A/B Testing** - Test campaigns to improve ROI
- **Conversion Rate Optimization** - Improve conversion at each funnel stage
- **Marketing Mix Modeling** - Statistical attribution for large-scale marketing
- **Incrementality Testing** - Measure true lift from marketing spend

---

**Next Steps:**
1. Implement UTM tracking standards across all campaigns (this week)
2. Set up lead source tracking in CRM (map UTMs to fields)
3. Choose an attribution model (recommend U-shaped or Linear to start)
4. Build your first attribution report (channel performance by stage)
5. Calculate CAC, LTV, and payback period for each channel
6. Reallocate budget: add 20% to highest-ROI channel, cut 20% from lowest

**Remember:** Attribution is not about perfect accuracy—it's about directionally correct decisions. Start simple, improve over time, and always take action on the insights.
