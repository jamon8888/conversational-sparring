# Value-Based Pricing Framework

## Overview
A systematic approach to pricing based on customer value rather than cost-plus or competition.

## The Value Pricing Process

### Step 1: Identify Customer Segments
**Segment by Value Received**:
- Enterprise (high value, complex needs)
- Mid-Market (moderate value, standard needs)
- SMB (lower value, simple needs)

**Example Segmentation**:
```
Enterprise:
- >1000 employees
- Complex workflows
- High customization needs
- Value: $500K+ annually

Mid-Market:
- 100-1000 employees
- Standard workflows
- Some customization
- Value: $50K-$500K annually

SMB:
- <100 employees
- Simple workflows
- Self-service
- Value: $5K-$50K annually
```

### Step 2: Quantify Value Delivered

**Value Drivers**:
1. **Time Savings**: Hours saved × Hourly rate
2. **Cost Reduction**: Current cost - Future cost
3. **Revenue Increase**: Additional revenue generated
4. **Risk Mitigation**: Probability × Cost of risk

**Example Calculation**:
```
Time Savings:
- 20 hours/week saved
- $75/hour labor cost
- Value: 20 × 52 × $75 = $78,000/year

Cost Reduction:
- Replace $50K/year tool
- Value: $50,000/year

Revenue Increase:
- 10% conversion improvement
- $1M annual revenue
- Value: $100,000/year

Total Annual Value: $228,000
```

### Step 3: Determine Value Capture

**Value Capture Rule**: Price at 10-30% of value delivered

**Example**:
```
Total Value: $228,000/year
Value Capture: 20%
Annual Price: $45,600
Monthly Price: $3,800
```

**Considerations**:
- Competitive alternatives
- Customer willingness to pay
- Implementation effort
- Switching costs

### Step 4: Design Pricing Tiers

**Good-Better-Best Structure**:

**Starter** (30% of value):
- Core features
- Self-service
- Community support
- Price: $1,500/month

**Professional** (50% of value):
- All Starter features
- Advanced features
- Email support
- Price: $3,000/month

**Enterprise** (70% of value):
- All Professional features
- Custom integrations
- Dedicated support
- Price: $6,000/month

### Step 5: Test and Optimize

**Price Testing Methods**:
1. **A/B Testing**: Different prices to different segments
2. **Van Westendorp**: Survey willingness to pay
3. **Conjoint Analysis**: Feature/price trade-offs
4. **Pilot Programs**: Test with select customers

## Pricing Models

### 1. Per-User Pricing
**Best For**: Collaboration tools, CRM, productivity software

**Formula**:
```
Price = Base Fee + (# Users × Per-User Fee)
```

**Example**:
```
Base: $100/month
Per User: $25/month
10 Users: $100 + (10 × $25) = $350/month
```

**Pros**: Scales with usage, easy to understand
**Cons**: Discourages adoption, seat-sharing

### 2. Usage-Based Pricing
**Best For**: APIs, infrastructure, data services

**Formula**:
```
Price = Base Fee + (Usage × Unit Price)
```

**Example**:
```
Base: $500/month
API Calls: $0.01 per call
100,000 calls: $500 + (100,000 × $0.01) = $1,500/month
```

**Pros**: Aligns with value, fair pricing
**Cons**: Unpredictable revenue, complex billing

### 3. Tiered Pricing
**Best For**: SaaS, subscriptions, memberships

**Structure**:
```
Tier 1: $0-$99 (0-1,000 units)
Tier 2: $100-$499 (1,001-10,000 units)
Tier 3: $500+ (10,001+ units)
```

**Pros**: Encourages upgrades, clear value ladder
**Cons**: Cliff effects, complexity

### 4. Value Metric Pricing
**Best For**: Outcome-based services

**Examples**:
- Marketing: % of revenue generated
- Recruiting: % of first-year salary
- Consulting: % of cost savings

**Formula**:
```
Price = Value Delivered × Success Fee %
```

**Pros**: Aligns incentives, low risk for customer
**Cons**: Hard to measure, delayed payment

## Packaging Strategy

### Feature Bundling

**Core Features** (in all tiers):
- Essential functionality
- Basic support
- Standard integrations

**Advanced Features** (mid/high tiers):
- Automation
- Advanced analytics
- Priority support
- Custom integrations

**Enterprise Features** (high tier only):
- SSO/SAML
- Dedicated support
- Custom SLAs
- On-premise deployment

### Anchoring Strategy

**Decoy Pricing**:
```
Basic: $99/month (limited features)
Pro: $299/month (best value) ← Target
Enterprise: $999/month (all features)
```

**Most customers choose Pro** (middle option)

## Price Optimization

### Increase Willingness to Pay

**Tactics**:
1. **Social Proof**: "Used by 10,000+ companies"
2. **Scarcity**: "Limited spots available"
3. **Urgency**: "Price increases Jan 1"
4. **Guarantees**: "30-day money-back guarantee"
5. **Framing**: "$10/day" vs "$300/month"

### Reduce Price Sensitivity

**Tactics**:
1. **Annual Billing**: 20% discount for annual vs monthly
2. **Bundling**: Package features together
3. **Add-ons**: Upsell after initial purchase
4. **Freemium**: Free tier drives upgrades

## Pricing Psychology

### Price Anchoring
**High Anchor**:
```
Enterprise: $10,000/month (anchor)
Professional: $3,000/month (seems reasonable)
Starter: $1,000/month (bargain)
```

### Charm Pricing
```
$99 vs $100 (feels significantly cheaper)
$2,997 vs $3,000
```

### Prestige Pricing
```
$5,000 vs $4,999 (premium positioning)
Round numbers signal quality
```

## Common Mistakes

❌ **Cost-Plus Pricing**: Price = Cost × 1.5
✅ **Value-Based**: Price = Value × 0.2

❌ **One-Size-Fits-All**: Single price for all segments
✅ **Segmented Pricing**: Different tiers for different needs

❌ **Feature Parity**: All tiers have same features
✅ **Clear Differentiation**: Obvious value ladder

❌ **Underpricing**: Leaving money on table
✅ **Value Capture**: 10-30% of value delivered

## Benchmarks

**SaaS Pricing**:
- SMB: $50-$500/month
- Mid-Market: $500-$5,000/month
- Enterprise: $5,000-$50,000+/month

**Gross Margin Targets**:
- SaaS: 70-85%
- Services: 40-60%
- E-commerce: 30-50%

**Price Increase Frequency**:
- Annual: 5-10% increase
- New customers: Higher prices
- Existing: Grandfather or migrate
