# FITS Lead Qualification Model

## Overview
FITS is a modern lead scoring framework that goes beyond traditional BANT to include intent signals and solution fit.

## The FITS Components

### F - Firmographics
**Goal**: Assess if company matches ICP

**Criteria**:
- Company size (employees, revenue)
- Industry/vertical
- Geography
- Growth stage
- Technology stack

**Scoring**:
```
25 points: Perfect ICP match
15 points: Good fit with minor gaps
10 points: Acceptable fit
0 points: Outside ICP
```

**Questions to Ask**:
- "How many employees do you have?"
- "What's your annual revenue range?"
- "What industry are you in?"
- "What tools are you currently using?"

### I - Intent
**Goal**: Measure buying signals and engagement

**Signals**:
- Website visits (frequency, pages viewed)
- Content downloads
- Demo requests
- Pricing page views
- Competitor research
- Job postings for relevant roles

**Scoring**:
```
High Intent (75-100): Active buying process
Medium Intent (50-74): Researching solutions
Low Intent (25-49): Passive interest
No Intent (0-24): Cold outreach
```

**Questions to Ask**:
- "What prompted you to reach out now?"
- "Are you evaluating other solutions?"
- "What's driving this initiative?"

### T - Timing
**Goal**: Understand urgency and timeline

**Factors**:
- Budget cycle
- Contract renewal dates
- Project deadlines
- Trigger events (funding, hiring, launch)
- Executive mandates

**Scoring**:
```
Immediate (75-100): Buying within 30 days
Near-term (50-74): 1-3 months
Mid-term (25-49): 3-6 months
Long-term (0-24): 6+ months
```

**Questions to Ask**:
- "When do you need this in place?"
- "What's driving the timeline?"
- "Is there a specific deadline?"
- "When does your current contract end?"

### S - Solution Match
**Goal**: Assess fit between their needs and your solution

**Criteria**:
- Problem alignment
- Feature requirements
- Use case match
- Success criteria
- Implementation complexity

**Scoring**:
```
Perfect Match (75-100): Solution built for this
Good Match (50-74): Solves core problems
Partial Match (25-49): Some gaps
Poor Match (0-24): Not a fit
```

**Questions to Ask**:
- "What are your top 3 requirements?"
- "What does success look like?"
- "What's your biggest pain point?"
- "Have you used similar solutions before?"

## FITS Scoring Matrix

### Total Score Calculation
```
Total FITS Score = (F + I + T + S) / 4
```

### Qualification Levels

**A-Level (75-100)**:
- Perfect ICP fit
- High intent
- Immediate timeline
- Strong solution match
- **Action**: Prioritize, fast-track

**B-Level (50-74)**:
- Good ICP fit
- Medium intent
- Near-term timeline
- Good solution match
- **Action**: Standard sales process

**C-Level (25-49)**:
- Acceptable fit
- Low intent
- Mid-term timeline
- Partial solution match
- **Action**: Nurture, educate

**D-Level (0-24)**:
- Poor fit
- No intent
- Long timeline
- Poor solution match
- **Action**: Disqualify or long-term nurture

## Example Scoring

**Lead: SaaS Company**
```
Firmographics: 75/100
- 150 employees ✓
- $10M revenue ✓
- SaaS industry ✓
- US-based ✓

Intent: 85/100
- Requested demo ✓
- Viewed pricing 3x ✓
- Downloaded case study ✓
- Researching competitors ✓

Timing: 70/100
- Need solution in 60 days
- Budget approved
- Q4 initiative

Solution Match: 90/100
- Perfect use case
- All requirements met
- Similar customer success

Total: (75+85+70+90)/4 = 80/100
Qualification: A-Level Lead
```

## Integration with Other Frameworks

### FITS + BANT
Use FITS for initial scoring, BANT for qualification:
1. FITS score determines priority
2. BANT confirms qualification
3. Combined score for forecasting

### FITS + MEDDICC
Use FITS for lead scoring, MEDDICC for enterprise deals:
1. FITS qualifies the account
2. MEDDICC qualifies the opportunity
3. Both inform deal strategy

## Automation

**Data Sources**:
- CRM (firmographics)
- Marketing automation (intent)
- Sales engagement (timing)
- Product usage (solution match)

**Scoring Rules**:
```
IF company_size >= 100 AND industry = "SaaS" THEN firmographics_score = 75
IF demo_requested = TRUE THEN intent_score += 30
IF timeline <= 30_days THEN timing_score = 90
IF use_case_match = "perfect" THEN solution_score = 85
```

## Success Metrics

**Healthy FITS Implementation**:
- 80%+ of A-level leads convert
- 50%+ of B-level leads convert
- <20% of C-level leads convert
- D-level leads disqualified early

**Red Flags**:
- High scores but low conversion (scoring too generous)
- Low scores but high conversion (scoring too strict)
- No correlation between score and outcome (criteria wrong)
