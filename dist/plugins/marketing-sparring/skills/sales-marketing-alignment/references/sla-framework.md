# SLA Framework (Sales-Marketing Alignment)

## Overview
Service Level Agreements between sales and marketing to ensure alignment and accountability.

## Core SLAs

### 1. Lead Response Time

**Marketing Commitment**:
- Route MQLs to sales within 5 minutes
- Provide complete lead context
- Include lead score and source

**Sales Commitment**:
- Contact MQL within 24 hours (business days)
- Attempt contact minimum 3 times
- Log all activities in CRM

**Metrics**:
```
Response Time:
- <1 hour: Excellent
- 1-24 hours: Good
- >24 hours: Poor

Contact Attempts:
- Minimum: 3 attempts
- Optimal: 5-7 attempts over 14 days
```

### 2. Lead Quality

**Marketing Commitment**:
- MQL-to-SQL conversion: >30%
- Lead scoring accuracy: >70%
- Complete required fields: 100%

**Sales Commitment**:
- Review MQL within 24 hours
- Accept/reject with reason
- Provide feedback on quality

**Metrics**:
```
MQL Quality Score:
- Excellent: >40% SQL conversion
- Good: 30-40% SQL conversion
- Poor: <30% SQL conversion

Sales Acceptance Rate:
- Target: >70% of MQLs accepted
```

### 3. Lead Volume

**Marketing Commitment**:
- Deliver X MQLs per month
- Maintain consistent flow
- Forecast 30 days ahead

**Sales Commitment**:
- Follow up on 100% of MQLs
- Convert Y% to SQLs
- Close Z% to customers

**Example**:
```
Monthly Targets:
- Marketing: 200 MQLs
- Sales: 60 SQLs (30% conversion)
- Sales: 12 Closed Won (20% win rate)
```

### 4. Feedback Loop

**Marketing Commitment**:
- Weekly performance report
- Monthly attribution analysis
- Quarterly strategy review

**Sales Commitment**:
- Daily CRM updates
- Weekly win/loss feedback
- Monthly ICP refinement

**Meeting Cadence**:
```
Daily: Slack updates on hot leads
Weekly: Pipeline review (30 min)
Monthly: Strategy alignment (60 min)
Quarterly: Planning session (half day)
```

## Lead Definitions

### Marketing Qualified Lead (MQL)
**Criteria**:
- Demographic fit (title, company size, industry)
- Behavioral engagement (score >60)
- Explicit interest (form fill, demo request)

**Scoring**:
```
Demographics (50 points):
- VP+ title: 25 points
- Target industry: 15 points
- Company size >100: 10 points

Behavior (50 points):
- Pricing page: 20 points
- Demo request: 30 points
- Email engagement: 10 points

MQL = 60+ points
```

### Sales Accepted Lead (SAL)
**Criteria**:
- MQL reviewed by sales
- Contact info verified
- No immediate disqualifiers
- Assigned to rep

**Disqualifiers**:
- Competitor
- Student/academic
- Wrong geography
- No budget authority

### Sales Qualified Lead (SQL)
**Criteria** (BANT):
- Budget: Has or can get budget
- Authority: Decision maker identified
- Need: Clear pain point
- Timing: Buying within 90 days

**Qualification**:
- Discovery call completed
- BANT scorecard filled
- Next steps agreed

## Performance Metrics

### Marketing Metrics
```
Lead Volume:
- MQLs delivered: 200/month (target: 200) ✓
- MQL growth: +15% MoM (target: +10%) ✓

Lead Quality:
- MQL → SQL: 35% (target: >30%) ✓
- SQL → Opp: 25% (target: >20%) ✓
- Opp → Won: 30% (target: >25%) ✓

Lead Velocity:
- MQL → SQL: 7 days (target: <10 days) ✓
- SQL → Opp: 14 days (target: <21 days) ✓
```

### Sales Metrics
```
Response Time:
- <1 hour: 60% (target: >50%) ✓
- <24 hours: 95% (target: >90%) ✓

Contact Attempts:
- Avg attempts: 5.2 (target: >5) ✓
- 3+ attempts: 100% (target: 100%) ✓

Conversion:
- MQL → SQL: 35% (target: >30%) ✓
- SQL → Opp: 25% (target: >20%) ✓
- Opp → Won: 30% (target: >25%) ✓
```

## Lead Routing Rules

### Round Robin
```
Rule: Distribute leads evenly across reps
Logic: Next available rep in rotation
Use Case: Equal opportunity, skill parity
```

### Territory-Based
```
Rule: Route by geography or account
Logic: Rep owns specific territories
Use Case: Field sales, regional teams
```

### Skill-Based
```
Rule: Route by product or vertical
Logic: Rep specialization
Use Case: Complex products, industry expertise
```

### Account-Based
```
Rule: Route to account owner
Logic: Existing relationship
Use Case: Expansion, upsells
```

## Dispute Resolution

### MQL Quality Disputes

**Process**:
1. Sales rejects MQL with reason
2. Marketing reviews within 48 hours
3. Joint decision on scoring adjustment
4. Update criteria if needed

**Common Reasons**:
- Wrong title/seniority
- Outside target industry
- No budget authority
- Competitor/student

### Volume Shortfall

**Process**:
1. Marketing misses target by >10%
2. Root cause analysis
3. Recovery plan created
4. Additional resources if needed

**Remedies**:
- Increase ad spend
- Launch new campaigns
- Activate dormant leads
- Partner with sales on outbound

## Reporting

### Weekly Dashboard
```
LEAD FLOW
- MQLs: 50 (target: 50) ✓
- SALs: 35 (70% acceptance)
- SQLs: 18 (51% conversion)
- Opps: 5 (28% conversion)

RESPONSE TIME
- <1 hour: 30 leads (60%)
- 1-24 hours: 18 leads (36%)
- >24 hours: 2 leads (4%)

QUALITY
- MQL → SQL: 36% (target: >30%) ✓
- Sales acceptance: 70% (target: >70%) ✓
```

### Monthly Review
```
VOLUME
- MQLs: 200 (target: 200) ✓
- SQLs: 70 (target: 60) ✓
- Closed Won: 14 (target: 12) ✓

QUALITY
- MQL → SQL: 35% (↑5% MoM)
- SQL → Won: 20% (→ flat)

VELOCITY
- MQL → SQL: 7 days (↓2 days)
- SQL → Won: 45 days (↑5 days)

TOP SOURCES
1. Google Ads: 30% of MQLs, 40% SQL conversion
2. Organic: 25% of MQLs, 35% SQL conversion
3. LinkedIn: 20% of MQLs, 30% SQL conversion
```

## Common Issues

### Issue: Low MQL Acceptance
**Symptom**: Sales rejects >30% of MQLs
**Root Cause**: Scoring misalignment
**Fix**: Recalibrate scoring, tighten criteria

### Issue: Slow Follow-Up
**Symptom**: >50% of MQLs contacted after 24 hours
**Root Cause**: Capacity or prioritization
**Fix**: Hire SDRs, automate routing, set alerts

### Issue: Poor Conversion
**Symptom**: MQL → SQL <20%
**Root Cause**: Quality or sales process
**Fix**: Improve qualification, sales training

### Issue: Lack of Feedback
**Symptom**: Sales doesn't update CRM
**Root Cause**: Process or tooling
**Fix**: Simplify CRM, automate updates, enforce SLA
