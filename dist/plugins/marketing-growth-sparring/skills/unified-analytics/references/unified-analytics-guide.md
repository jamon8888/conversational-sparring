# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Unified Analytics: Complete GTM Performance Measurement

## Overview

A comprehensive analytics system that unifies content performance and marketing metrics into a single dashboard. Track everything from blog post views to campaign ROI, from social engagement to conversion rates, all in one place.

**Merged from**:
- Content Analytics (content performance metrics)
- Marketing Analytics (marketing campaign metrics)

**Key Capabilities**:
- ✅ Content performance tracking (blogs, videos, podcasts, social)
- ✅ Marketing campaign analytics (email, ads, landing pages)
- ✅ Multi-channel attribution
- ✅ Conversion funnel analysis
- ✅ ROI calculation
- ✅ Audience insights
- ✅ Competitor benchmarking
- ✅ Executive reporting

---

## When to Use This Skill

### Primary Use Cases
1. **Content Performance** - Track blog views, engagement, shares
2. **Marketing Campaign ROI** - Measure campaign effectiveness
3. **Multi-Channel Attribution** - Understand customer journeys
4. **Funnel Analysis** - Identify drop-off points
5. **Executive Reporting** - Create comprehensive dashboards
6. **Optimization** - Data-driven decision making

---

## Core Metrics Categories

### Content Metrics
**Blog & Written Content**:
- Page views
- Time on page
- Scroll depth
- Bounce rate
- Social shares
- Comments
- Backlinks

**Video Content**:
- Video views
- Watch time
- Completion rate
- Click-through rate
- Subscriber growth

**Audio Content**:
- Downloads
- Listens
- Completion rate
- Subscriber growth

**Social Content**:
- Impressions
- Reach
- Engagement rate
- Click-through rate
- Follower growth

### Marketing Metrics
**Email Marketing**:
- Open rate
- Click rate
- Conversion rate
- Unsubscribe rate
- Revenue per email

**Paid Advertising**:
- Impressions
- Clicks
- CTR
- CPC
- CPA
- ROAS

**Landing Pages**:
- Visits
- Conversion rate
- Bounce rate
- Time on page
- Form submissions

**Lead Generation**:
- Lead volume
- Lead quality score
- Cost per lead
- Lead-to-customer rate

### Business Metrics
- Traffic sources
- Conversion rate
- Customer acquisition cost (CAC)
- Customer lifetime value (LTV)
- Return on investment (ROI)
- Revenue attribution

---

## Analytics Frameworks

### 1. Content Performance Dashboard

**Top-Level Metrics**:
- Total content pieces published
- Total views/impressions
- Total engagement
- Traffic trend (7, 30, 90 days)

**By Format**:
- Blog posts: Views, engagement, conversions
- Videos: Views, watch time, subscribers
- Podcasts: Downloads, completion rate
- Social: Impressions, engagement rate

**By Channel**:
- Organic search
- Social media
- Email
- Direct
- Referral

### 2. Marketing Campaign Dashboard

**Campaign Performance**:
- Total campaigns
- Active campaigns
- Budget spent
- Revenue generated
- Overall ROI

**By Channel**:
- Email: Open rate, CTR, conversions
- Paid ads: Impressions, CPC, ROAS
- Social: Reach, engagement, conversions
- Organic: Traffic, conversions

**By Stage**:
- Awareness: Impressions, reach
- Consideration: Engagement, CTR
- Conversion: Leads, sales

### 3. Attribution Model

**Multi-Touch Attribution**:
- First touch
- Last touch
- Linear
- Time decay
- U-shaped
- W-shaped

**Customer Journey**:
- Average touchpoints
- Top converting paths
- Assisted conversions
- Time to convert

---

## Analytics Setup

### Step 1: Connect Data Sources
```
Data Sources to Connect:
- Google Analytics 4
- Social media platforms (Twitter, LinkedIn, Instagram, YouTube)
- Email marketing platform (Mailchimp, ConvertKit, etc.)
- CRM (HubSpot, Salesforce, etc.)
- Advertising platforms (Google Ads, Facebook Ads, LinkedIn Ads)
- Content management system
```

### Step 2: Define KPIs

**Content KPIs**:
- Primary: Traffic, engagement rate, conversion rate
- Secondary: Time on page, bounce rate, social shares
- North Star: Content-attributed revenue

**Marketing KPIs**:
- Primary: CAC, LTV, ROI
- Secondary: Conversion rate, lead quality
- North Star: Marketing-attributed revenue

### Step 3: Build Dashboards

**Dashboard 1: Executive Summary**
- Top-level metrics
- Trends (vs. previous period)
- Key insights
- Action items

**Dashboard 2: Content Performance**
- Content by format
- Top performing pieces
- Engagement trends
- Content ROI

**Dashboard 3: Marketing Campaigns**
- Campaign performance
- Channel breakdown
- Attribution analysis
- Budget vs. performance

**Dashboard 4: Conversion Funnel**
- Stage-by-stage analysis
- Drop-off points
- Conversion paths
- Optimization opportunities

---

## Measurement Templates

### Content Performance Report

```markdown
# Content Performance Report - [Month]

## Executive Summary
- Total content pieces: [#]
- Total views: [#]
- Total engagement: [#]
- Content-attributed revenue: $[#]

## Top Performing Content
1. [Title] - [Views] views, [Engagement]% engagement
2. [Title] - [Views] views, [Engagement]% engagement
3. [Title] - [Views] views, [Engagement]% engagement

## By Format
- Blog Posts: [#] pieces, [#] views, [#]% engagement
- Videos: [#] pieces, [#] views, [#]% engagement
- Podcasts: [#] episodes, [#] downloads
- Social: [#] posts, [#] impressions, [#]% engagement

## Key Insights
- [Insight 1]
- [Insight 2]
- [Insight 3]

## Recommendations
- [Action 1]
- [Action 2]
- [Action 3]
```

### Marketing Campaign Report

```markdown
# Marketing Campaign Report - [Month]

## Executive Summary
- Total campaigns: [#]
- Total spend: $[#]
- Total revenue: $[#]
- Overall ROI: [#]x

## Campaign Performance
| Campaign | Spend | Revenue | ROI | Status |
|----------|-------|---------|-----|--------|
| [Name]   | $[#]  | $[#]    | [#]x| Active |

## Channel Performance
- Email: [#] sends, [#]% open, [#]% CTR, $[#] revenue
- Paid Ads: [#] impressions, $[#] CPC, [#]x ROAS
- Social: [#] impressions, [#]% engagement, $[#] revenue

## Attribution Analysis
- First touch: [#]% of conversions
- Last touch: [#]% of conversions
- Assisted: [#]% of conversions

## Recommendations
- [Action 1]
- [Action 2]
- [Action 3]
```

---

## Analytics Tools & Stack

### Recommended Tools

**Web Analytics**:
- Google Analytics 4 (free, comprehensive)
- Plausible (privacy-focused)
- Fathom (simple, privacy-focused)

**Content Analytics**:
- Google Search Console (SEO data)
- BuzzSumo (content performance)
- Ahrefs (SEO + content)

**Social Analytics**:
- Native platform analytics
- Hootsuite Analytics
- Sprout Social

**Marketing Analytics**:
- HubSpot (all-in-one)
- Google Analytics 4 (free)
- Mixpanel (product analytics)

**Dashboard Tools**:
- Google Data Studio (free)
- Tableau
- Power BI
- Klipfolio

---

## Advanced Analytics

### Cohort Analysis
Track groups of users over time:
```
Month 0: 1,000 users
Month 1: 600 retained (60%)
Month 2: 450 retained (45%)
Month 3: 380 retained (38%)
```

### Attribution Modeling
Compare different attribution models:
```
Model          | Conversions | Revenue
---------------|-------------|--------
First Touch    | 120         | $24,000
Last Touch     | 180         | $36,000
Linear         | 150         | $30,000
Time Decay     | 160         | $32,000
```

### Content ROI Calculation
```
Content Piece: "Email Marketing Guide"
- Production cost: $500
- Distribution cost: $100
- Total cost: $600

- Traffic: 5,000 visits
- Conversions: 50 (1% rate)
- Revenue: $5,000
- ROI: 733% ($5,000 / $600)
```

---

## Key Performance Indicators (KPIs)

### Content KPIs
- **Traffic**: Unique visitors, page views
- **Engagement**: Time on page, pages per session, bounce rate
- **Social**: Shares, comments, likes
- **SEO**: Organic traffic, keyword rankings, backlinks
- **Conversion**: Email signups, demo requests, purchases

### Marketing KPIs
- **Acquisition**: Traffic, leads, customers
- **Cost**: CPA, CAC, CPL
- **Revenue**: MRR, ARR, LTV
- **Efficiency**: CAC:LTV ratio, payback period
- **Channel**: ROAS by channel

### Benchmarks
**Blog Content**:
- Avg. time on page: 2-3 minutes
- Bounce rate: 40-60%
- Conversion rate: 1-3%

**Email Marketing**:
- Open rate: 15-25%
- Click rate: 2-5%
- Conversion rate: 1-3%

**Paid Ads**:
- CTR: 1-3%
- Conversion rate: 2-5%
- ROAS: 3-5x

---

## Reporting Cadence

### Daily
- Traffic overview
- Campaign performance
- Critical alerts

### Weekly
- Content performance
- Campaign metrics
- Quick wins identification

### Monthly
- Comprehensive reports
- Trend analysis
- Strategic recommendations

### Quarterly
- Executive summary
- Strategic review
- Goal setting

---

## Related Skills

### Within GTM Content & Marketing Toolkit
- **content-creation-at-scale** - Use analytics to optimize content production
- **seo-geo-blog-writing** - Track SEO performance
- **email-marketing** - Measure email campaign performance
- **ad-copywriting** - Optimize ad creative based on data
- **landing-page-copy** - Improve conversion rates

### Cross-Toolkit References
- **Growth Toolkit** (growth-analytics) - For funnel optimization
- **Revenue Operations Toolkit** (revenue-analytics) - For revenue attribution
- **Strategic Research Toolkit** (competitive-intelligence) - For competitor benchmarking

---

## Tips & Best Practices

### Data Quality
1. **Clean Data** - Remove bot traffic and outliers
2. **Consistent Tracking** - Use UTM parameters consistently
3. **Regular Audits** - Check tracking implementation monthly
4. **Privacy Compliance** - Follow GDPR/CCPA requirements

### Insights Generation
1. **Look for Trends** - Compare periods (WoW, MoM, YoY)
2. **Segment Data** - Analyze by audience, channel, content type
3. **Ask Why** - Don't just report numbers, explain them
4. **Action-Oriented** - Every insight should lead to an action

### Dashboard Design
1. **Top-Down** - Start with executive summary, drill down to details
2. **Visual** - Use charts and graphs, not just tables
3. **Context** - Always show comparison (vs. goal, vs. previous period)
4. **Accessible** - Share dashboards with stakeholders

---

## Troubleshooting

### Common Issues

**Data Discrepancies**:
- Check date ranges match across platforms
- Verify timezone settings
- Understand different tracking methodologies

**Low Engagement**:
- Review content quality
- Check distribution strategy
- Analyze audience match

**Attribution Challenges**:
- Use consistent UTM parameters
- Implement cross-domain tracking
- Consider multi-touch attribution

---

**This unified analytics skill provides comprehensive measurement for all content and marketing activities, enabling data-driven decision making across the entire GTM function.**
