# Unit Economics Framework

## Overview
The fundamental metrics that determine if your business model is sustainable and scalable.

## Core Metrics

### 1. Customer Acquisition Cost (CAC)

**Formula**:
```
CAC = (Sales + Marketing Costs) / New Customers Acquired
```

**Example**:
```
Sales & Marketing: $100,000/month
New Customers: 20/month
CAC = $100,000 / 20 = $5,000
```

**Benchmarks**:
- B2C SaaS: $100-$500
- SMB B2B SaaS: $1,000-$5,000
- Mid-Market B2B: $5,000-$15,000
- Enterprise B2B: $15,000-$50,000+

### 2. Lifetime Value (LTV)

**Formula**:
```
LTV = ARPU × Gross Margin % / Churn Rate
```

**Example**:
```
ARPU: $500/month
Gross Margin: 80%
Monthly Churn: 5%
LTV = $500 × 0.80 / 0.05 = $8,000
```

**Alternative Formula** (for cohort analysis):
```
LTV = Avg Revenue per Customer × Avg Customer Lifespan × Gross Margin %
```

### 3. LTV:CAC Ratio

**Formula**:
```
LTV:CAC = LTV / CAC
```

**Interpretation**:
- <1:1 = Unsustainable (losing money)
- 1:1-3:1 = Concerning (barely profitable)
- 3:1-5:1 = Healthy (good unit economics)
- >5:1 = Excellent (underinvesting in growth)

**Target**: 3:1 minimum, 5:1 ideal

### 4. Payback Period

**Formula**:
```
Payback Period (months) = CAC / (ARPU × Gross Margin %)
```

**Example**:
```
CAC: $5,000
ARPU: $500/month
Gross Margin: 80%
Payback = $5,000 / ($500 × 0.80) = 12.5 months
```

**Benchmarks**:
- Excellent: <6 months
- Good: 6-12 months
- Acceptable: 12-18 months
- Concerning: >18 months

## Advanced Metrics

### 5. Magic Number

**Formula**:
```
Magic Number = (Current Quarter ARR - Previous Quarter ARR) / Previous Quarter S&M Spend
```

**Interpretation**:
- <0.5 = Poor efficiency
- 0.5-0.75 = Acceptable
- 0.75-1.0 = Good
- >1.0 = Excellent

**Example**:
```
Q1 ARR: $1M
Q2 ARR: $1.2M
Q1 S&M Spend: $200K
Magic Number = ($1.2M - $1M) / $200K = 1.0
```

### 6. CAC Ratio

**Formula**:
```
CAC Ratio = New ARR / S&M Spend
```

**Target**: >1.0 (every dollar spent generates >$1 ARR)

### 7. Rule of 40

**Formula**:
```
Rule of 40 = Revenue Growth Rate % + EBITDA Margin %
```

**Interpretation**:
- <40% = Below benchmark
- 40%+ = Healthy SaaS business
- 60%+ = Exceptional

**Example**:
```
Revenue Growth: 50%
EBITDA Margin: -10%
Rule of 40 = 50% + (-10%) = 40% ✓
```

## Cohort Analysis

### Monthly Cohort LTV

**Track by Signup Month**:
```
Jan 2024 Cohort:
- Month 1: $500 ARPU, 100% retention
- Month 2: $500 ARPU, 95% retention
- Month 3: $500 ARPU, 90% retention
- Month 6: $500 ARPU, 75% retention
- Month 12: $500 ARPU, 60% retention

LTV = Sum of (ARPU × Retention × Gross Margin)
```

### Improving Unit Economics

**Reduce CAC**:
- Improve conversion rates
- Optimize ad spend
- Increase organic channels
- Improve sales efficiency

**Increase LTV**:
- Reduce churn
- Increase ARPU (upsells, cross-sells)
- Improve product value
- Better customer success

**Improve Payback**:
- Annual contracts (vs monthly)
- Upfront payments
- Higher pricing
- Lower CAC

## Calculation Examples

### SaaS Startup Example
```
Metrics:
- MRR: $50,000
- Customers: 100
- ARPU: $500/month
- Monthly Churn: 3%
- Gross Margin: 75%
- S&M Spend: $30,000/month
- New Customers: 15/month

Calculations:
CAC = $30,000 / 15 = $2,000
LTV = $500 × 0.75 / 0.03 = $12,500
LTV:CAC = $12,500 / $2,000 = 6.25:1 ✓
Payback = $2,000 / ($500 × 0.75) = 5.3 months ✓
```

### E-commerce Example
```
Metrics:
- Avg Order Value: $100
- Orders per Customer/Year: 3
- Gross Margin: 40%
- Customer Lifespan: 2 years
- CAC: $50

Calculations:
Annual Revenue per Customer = $100 × 3 = $300
LTV = $300 × 2 years × 0.40 = $240
LTV:CAC = $240 / $50 = 4.8:1 ✓
Payback = $50 / ($300 × 0.40 / 12) = 5 months ✓
```

## Benchmarks by Industry

### B2B SaaS
- LTV:CAC: 3:1 to 5:1
- Payback: 12-18 months
- CAC: $1,000-$15,000
- Churn: 5-7% annually

### B2C SaaS
- LTV:CAC: 3:1 to 4:1
- Payback: 6-12 months
- CAC: $50-$500
- Churn: 3-5% monthly

### E-commerce
- LTV:CAC: 3:1 to 6:1
- Payback: 3-6 months
- CAC: $10-$100
- Repeat Rate: 20-40%

## Common Mistakes

❌ **Ignoring gross margin**: Using revenue instead of profit
✅ **Include margins**: LTV calculation must use gross margin

❌ **Not segmenting**: Treating all customers the same
✅ **Cohort analysis**: Track by segment, channel, product

❌ **Short-term view**: Only looking at first 3 months
✅ **Long-term LTV**: Track 12-24+ months

❌ **Incomplete CAC**: Missing overhead, tools, etc.
✅ **Fully-loaded CAC**: All S&M costs included
