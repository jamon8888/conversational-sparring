---
name: pricing-packaging
description: Use when designing pricing strategies, creating product tiers (Good-Better-Best), or optimizing margins. Trigger when needing to calculate optimal pricing based on COGS and target margins (scripts/pricing_calculator.py), researching competitor price anchoring, or testing willingness-to-pay for new features.
license: MIT
---

# Pricing & Packaging

## Quick Start

This skill helps you design pricing strategies and product tiers. For complete frameworks, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Pricing Calculator** (`scripts/pricing_calculator.py`):

```bash
python scripts/pricing_calculator.py --cost 100 --target_margin 0.7
```

Calculates optimal pricing based on costs and targets.

## Execution Checklist

### Creating Pricing Strategy

- [ ] Calculate costs (COGS, CAC, support)
- [ ] Research competitor pricing
- [ ] Define customer value (willingness to pay)
- [ ] Choose pricing model (value, cost-plus, competitor)
- [ ] Create 3 tiers (good, better, best)
- [ ] Set anchor price (highest tier first)
- [ ] Test with customers
- [ ] Track conversion by tier

## Key Frameworks

- **Value-Based Pricing**: Price on value delivered, not cost
- **Good-Better-Best**: 3 tiers (most choose middle)
- **Anchoring**: Show highest price first
- **LTV:CAC**: Target 3:1 ratio

## Quick Wins

- Show annual pricing (lower monthly, higher commit)
- Anchor with enterprise tier
- Make middle tier "most popular"
- Test 10-20% price increases (measure impact)

## Resources

- [Complete Guide](references/guide.md)
- [Value-Based Pricing](references/value-based-pricing.md)

## Related Skills

### From Sales Toolkit

- [value-propositions](../../sales-toolkit/skills/value-propositions/SKILL.md) - ROI justification

### From RevOps Toolkit

- [revenue-analytics](../revenue-analytics/SKILL.md) - LTV calculations
