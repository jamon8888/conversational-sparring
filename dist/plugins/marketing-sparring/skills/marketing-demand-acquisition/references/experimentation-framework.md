# Experimentation Framework
### 6.1 A/B Testing Prioritization (ICE Score)

**Formula**: ICE = (Impact × Confidence × Ease) ÷ 3

Rate each factor 1-10:

- **Impact**: How much will this move the needle?
- **Confidence**: How sure are you it will work?
- **Ease**: How easy is it to implement?

**Example Tests** (sorted by ICE score):

| Test                             | Impact | Confidence | Ease | ICE | Priority |
| -------------------------------- | ------ | ---------- | ---- | --- | -------- |
| CTA button color (red vs. green) | 3      | 8          | 10   | 7.0 | Low      |
| Landing page headline rewrite    | 8      | 7          | 8    | 7.7 | Medium   |
| Pricing page redesign            | 9      | 6          | 4    | 6.3 | Medium   |
| New lead magnet offer            | 9      | 8          | 7    | 8.0 | High     |
| Add live chat to pricing page    | 7      | 9          | 8    | 8.0 | High     |

### 6.2 Test Design & Execution

**Test Template**:

```
Hypothesis: [Adding a case study carousel to the pricing page will increase demo requests by 20% because users need social proof before committing]

Metric: [Demo requests from /pricing page]
Sample Size: [1000 visitors per variant]
Duration: [2 weeks or until significance]
Success Criteria: [20% lift, 95% confidence]

Variant A (Control): [Current pricing page]
Variant B (Treatment): [Pricing page + case study carousel]

Tools: [HubSpot A/B test, or Google Optimize]
```

**Statistical Significance**:

- Minimum: 95% confidence, 1000 visitors/variant
- Use calculator: Optimizely Sample Size Calculator
- Don't stop tests early (false positives)

**Test Velocity** (Series A target):

- 4-6 tests/month across channels
- 70% win rate not realistic (aim for 30-40%)
- Document losers (learnings matter)

### 6.3 Common Experiments

**Landing Page Tests**:

- Headline variations (problem-focused vs. solution-focused)
- CTA copy ("Start Free Trial" vs. "Get Started" vs. "Try Now")
- Form length (5 fields vs. 2 fields)
- Social proof placement (above vs. below fold)
- Hero image (product screenshot vs. people vs. abstract)

**Ad Tests**:

- Creative format (static vs. video vs. carousel)
- Messaging angle (feature-led vs. benefit-led vs. outcome-led)
- Audience targeting (broad vs. narrow)
- Landing page destination (homepage vs. dedicated LP)

**Email Tests**:

- Subject line length (short vs. long)
- Personalization (generic vs. first name vs. company name)
- Send time (morning vs. afternoon vs. evening)
- CTA placement (top vs. middle vs. bottom)

---
