# Attribution Models Framework

## Overview
A comprehensive guide to marketing attribution models and when to use each one.

## Attribution Model Types

### 1. Single-Touch Models

#### First-Touch Attribution
**Definition**: 100% credit to the first touchpoint

**Formula**:
```
Attribution = 100% to first interaction
```

**Best For**:
- Top-of-funnel campaigns
- Brand awareness measurement
- Understanding discovery channels

**Example**:
```
Journey: Google Ad → Email → Demo → Purchase ($10K)
Attribution: Google Ad = $10K
```

**Pros**:
- Simple to implement
- Shows what drives awareness
- Easy to explain

**Cons**:
- Ignores nurture efforts
- Undervalues mid/bottom funnel
- Not accurate for long sales cycles

#### Last-Touch Attribution
**Definition**: 100% credit to the last touchpoint before conversion

**Formula**:
```
Attribution = 100% to final interaction
```

**Best For**:
- Bottom-of-funnel optimization
- Direct response campaigns
- Short sales cycles

**Example**:
```
Journey: Google Ad → Email → Demo → Purchase ($10K)
Attribution: Demo = $10K
```

**Pros**:
- Simple to implement
- Shows what closes deals
- Good for conversion optimization

**Cons**:
- Ignores awareness efforts
- Undervalues early touches
- Misleading for long journeys

### 2. Multi-Touch Models

#### Linear Attribution
**Definition**: Equal credit to all touchpoints

**Formula**:
```
Attribution per touch = Total Revenue / Number of Touches
```

**Best For**:
- Balanced view of journey
- Long sales cycles
- Multiple stakeholders

**Example**:
```
Journey: Google Ad → Email → Webinar → Demo → Purchase ($10K)
Attribution: Each touch = $2,500
```

**Pros**:
- Fair to all channels
- Simple logic
- Encourages full-funnel thinking

**Cons**:
- Treats all touches equally
- Doesn't reflect actual impact
- May overvalue minor touches

#### Time-Decay Attribution
**Definition**: More credit to recent touchpoints

**Formula**:
```
Weight = 2^(position from start)
Attribution = (Weight / Total Weight) × Revenue
```

**Best For**:
- Sales-driven organizations
- Short consideration periods
- Bottom-funnel focus

**Example**:
```
Journey: Ad (Day 0) → Email (Day 5) → Demo (Day 10) → Purchase ($10K)
Weights: 1, 2, 4, 8 (Total: 15)
Attribution:
- Ad: $667 (1/15)
- Email: $1,333 (2/15)
- Demo: $2,667 (4/15)
- Purchase: $5,333 (8/15)
```

**Pros**:
- Values recent interactions
- Reflects buying momentum
- Good for short cycles

**Cons**:
- Undervalues awareness
- May miss long-term impact
- Complex to explain

#### U-Shaped (Position-Based) Attribution
**Definition**: 40% first, 40% last, 20% distributed to middle

**Formula**:
```
First Touch = 40% × Revenue
Last Touch = 40% × Revenue
Middle Touches = 20% × Revenue / (Total Touches - 2)
```

**Best For**:
- Balanced marketing + sales
- Lead generation focus
- Multi-stage funnels

**Example**:
```
Journey: Ad → Email → Webinar → Demo → Purchase ($10K)
Attribution:
- Ad (first): $4,000 (40%)
- Email: $667 (6.67%)
- Webinar: $667 (6.67%)
- Demo: $667 (6.67%)
- Purchase (last): $4,000 (40%)
```

**Pros**:
- Values discovery and conversion
- Balances marketing and sales
- Industry standard

**Cons**:
- Arbitrary 40/40/20 split
- May undervalue middle touches
- Complex to implement

#### W-Shaped Attribution
**Definition**: 30% first, 30% lead creation, 30% opportunity creation, 10% to others

**Best For**:
- B2B SaaS
- Long sales cycles
- Multiple decision makers

**Formula**:
```
First Touch = 30%
Lead Creation = 30%
Opportunity Creation = 30%
Other Touches = 10% distributed
```

**Example**:
```
Journey: Ad → Form Fill (MQL) → Demo (SQL) → Proposal → Purchase ($10K)
Attribution:
- Ad: $3,000 (30% - first)
- Form Fill: $3,000 (30% - MQL)
- Demo: $3,000 (30% - SQL)
- Proposal: $1,000 (10% - other)
```

**Pros**:
- Reflects B2B journey
- Values key milestones
- Aligns with sales stages

**Cons**:
- Complex to implement
- Requires stage tracking
- Arbitrary percentages

### 3. Advanced Models

#### Custom/Algorithmic Attribution
**Definition**: Machine learning determines credit based on conversion probability

**Best For**:
- Large data sets (1000+ conversions/month)
- Complex journeys
- Data-driven organizations

**Requirements**:
- Significant data volume
- Analytics platform (Google Analytics 360, Adobe)
- Data science resources

**Pros**:
- Data-driven
- Adapts to your business
- Most accurate

**Cons**:
- Black box
- Requires expertise
- Needs large data set

## Choosing the Right Model

### Decision Framework

**Question 1: Sales Cycle Length?**
- Short (<30 days) → Last-Touch or Time-Decay
- Medium (30-90 days) → U-Shaped
- Long (>90 days) → W-Shaped or Custom

**Question 2: Data Volume?**
- Low (<100 conversions/month) → Simple (First/Last-Touch)
- Medium (100-1000/month) → Multi-Touch (Linear, U-Shaped)
- High (>1000/month) → Custom/Algorithmic

**Question 3: Primary Goal?**
- Awareness → First-Touch
- Conversion → Last-Touch
- Full Funnel → U-Shaped or W-Shaped

**Question 4: Organizational Maturity?**
- Starting out → Last-Touch (simple)
- Growing → U-Shaped (balanced)
- Advanced → Custom (sophisticated)

## Implementation Guide

### Step 1: Define Touchpoints
```
Touchpoint Categories:
- Paid: Google Ads, LinkedIn Ads, Facebook Ads
- Organic: SEO, Social, Direct
- Email: Campaigns, Nurture, Newsletters
- Sales: Calls, Demos, Proposals
- Events: Webinars, Conferences, Trade Shows
```

### Step 2: Track Journey
```
Required Data:
- Touchpoint timestamp
- Channel/source
- Campaign
- Content
- User ID
- Conversion value
```

### Step 3: Calculate Attribution
```python
# Example: U-Shaped Attribution
def calculate_u_shaped(touchpoints, revenue):
    n = len(touchpoints)
    if n == 1:
        return {touchpoints[0]: revenue}
    elif n == 2:
        return {
            touchpoints[0]: revenue * 0.5,
            touchpoints[1]: revenue * 0.5
        }
    else:
        middle_credit = (revenue * 0.2) / (n - 2)
        return {
            touchpoints[0]: revenue * 0.4,
            **{tp: middle_credit for tp in touchpoints[1:-1]},
            touchpoints[-1]: revenue * 0.4
        }
```

### Step 4: Report and Optimize
```
Metrics to Track:
- Revenue by channel
- ROI by channel
- Cost per acquisition
- Conversion rate by touchpoint
- Average touches to conversion
```

## Common Mistakes

❌ **Using wrong model for cycle**: Last-touch for 6-month sales cycle
✅ **Match model to cycle**: W-shaped for complex B2B

❌ **Not tracking all touchpoints**: Missing offline events
✅ **Complete tracking**: All channels, online and offline

❌ **Changing models frequently**: Can't compare periods
✅ **Consistent methodology**: Stick with one model

❌ **Ignoring data quality**: Garbage in, garbage out
✅ **Clean data**: Dedupe, validate, enrich

## Benchmarks

**Average Touches to Conversion**:
- B2C: 3-5 touches
- SMB B2B: 5-7 touches
- Mid-Market B2B: 7-13 touches
- Enterprise B2B: 13-27 touches

**Channel Performance** (typical attribution %):
- Paid Search: 20-30%
- Organic Search: 15-25%
- Email: 15-20%
- Social: 10-15%
- Direct: 10-15%
- Referral: 5-10%
