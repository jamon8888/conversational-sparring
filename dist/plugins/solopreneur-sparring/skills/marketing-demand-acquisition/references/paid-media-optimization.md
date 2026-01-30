# Paid Media Optimization
### 2.1 Channel Strategy Matrix

| Channel            | Best For                    | CAC Benchmark | Conversion Rate | Series A Priority |
| ------------------ | --------------------------- | ------------- | --------------- | ----------------- |
| **LinkedIn Ads**   | B2B, Enterprise, ABM        | $150-$400     | 0.5-2%          | ⭐⭐⭐⭐⭐        |
| **Google Search**  | High-intent, BOFU           | $80-$250      | 2-5%            | ⭐⭐⭐⭐⭐        |
| **Google Display** | Retargeting, awareness      | $50-$150      | 0.3-1%          | ⭐⭐⭐            |
| **Meta (FB/IG)**   | SMB, consumer-like products | $60-$200      | 1-3%            | ⭐⭐⭐            |
| **YouTube**        | Product demos, brand        | $100-$300     | 0.5-1.5%        | ⭐⭐              |
| **Reddit/Twitter** | Technical audiences         | $40-$180      | 0.5-2%          | ⭐⭐              |

### 2.2 LinkedIn Ads Playbook (Primary B2B Channel)

**Campaign Structure**:

```
Account
└─ Campaign Group: [Q2-2025-Enterprise-ABM]
   ├─ Campaign 1: [Awareness - Thought Leadership]
   │  ├─ Ad Set: [CTO/VP Eng, US, Tech Companies]
   │  └─ Creatives: [3 carousel posts, 2 video ads]
   ├─ Campaign 2: [Consideration - Product Education]
   │  ├─ Ad Set: [Engaged audience, retargeting]
   │  └─ Creatives: [2 lead gen forms, 1 landing page]
   └─ Campaign 3: [Conversion - Demo Requests]
      ├─ Ad Set: [Website visitors, content downloaders]
      └─ Creatives: [Direct demo CTA, case study]
```

**Targeting Best Practices**:

- **Company Size**: 50-5000 employees (Series A sweet spot)
- **Job Titles**: Director+, VP+, C-level (use LinkedIn's precise targeting)
- **Industries**: Software, SaaS, Tech Services
- **Matched Audiences**: Website retargeting (install Insight Tag), uploaded email lists
- **Budget**: Start $50/day per campaign, scale 20% weekly if CAC < target

**Creative Frameworks**:

1. **Thought Leadership** - Industry insights, no product pitch
2. **Social Proof** - Customer logos, testimonials, case study snippets
3. **Problem-Solution** - Pain point + your solution in 3 seconds
4. **Demo-First** - Show product immediately, skip fluff

**LinkedIn Lead Gen Forms vs. Landing Pages**:

- **Lead Gen Forms**: Higher conversion (2-3x), lower quality, use for TOFU/MOFU
- **Landing Pages**: Lower conversion, higher quality, use for BOFU/demo requests
- **HubSpot Sync**: Connect LinkedIn Lead Gen Forms via native integration

### 2.3 Google Ads Playbook (High-Intent Capture)

**Campaign Types Priority**:

1. **Search - Brand** (highest priority, protect brand terms)
2. **Search - Competitor** (steal market share)
3. **Search - Solution** (problem-aware buyers)
4. **Search - Product Category** (earlier stage)
5. **Display - Retargeting** (re-engage warm traffic)

**Search Campaign Structure**:

```
Campaign: [Search-Solution-Keywords]
├─ Ad Group: [project management software]
│  ├─ Keywords:
│  │  - "project management software" [Phrase]
│  │  - "best project management tool" [Phrase]
│  │  - +project +management +solution [Broad Match Modifier]
│  └─ Ads: [3 responsive search ads with 15 headlines, 4 descriptions]
│
├─ Ad Group: [team collaboration tools]
   ├─ Keywords: [5-10 tightly themed keywords]
   └─ Ads: [3 responsive search ads]
```

**Keyword Strategy**:

- **Brand Terms**: Exact match, bid high, protect brand
- **Competitor Terms**: "[Competitor] alternative", "[Competitor] vs [You]"
- **Solution Terms**: "best [category] software", "top [category] tools"
- **Problem Terms**: "how to [solve problem]"
- **Negative Keywords**: Maintain list of 100+ (free, cheap, jobs, career, reviews)

**Bid Strategy** (2025 best practice):

- New campaigns: Start Manual CPC for control
- After 50+ conversions: Switch to Target CPA
- After 100+ conversions: Test Maximize Conversions with tCPA
- EU markets: Bid 15-20% higher for same quality

**Ad Copy Framework** (Responsive Search Ads):

```
Headlines (15 required):
- H1-3: Value props (Save 10 hours/week, Trusted by 500+ teams)
- H4-6: Features (AI-powered, Real-time sync, Mobile app)
- H7-9: Social proof (4.8★ G2 rating, Used by Microsoft)
- H10-12: CTAs (Start free trial, Book demo, See pricing)
- H13-15: Keywords pinned (Dynamic insertion)

Descriptions (4 required):
- D1: Primary value prop + CTA (30-60 chars)
- D2: Feature list + differentiator (60-90 chars)
- D3: Social proof + urgency (45-90 chars)
- D4: Backup generic (60-90 chars)
```

### 2.4 Meta Ads Playbook (SMB/Lower ACV)

**When to Use Meta**:

- ✅ Product ACV <$10k
- ✅ Visual product (UI, consumer-facing)
- ✅ SMB/prosumer audience
- ✅ Broader awareness campaigns
- ❌ Enterprise/high ACV (use LinkedIn)

**Campaign Setup**:

```
Campaign Objective: [Conversions]
├─ Ad Set 1: [Lookalike - 1% of converters]
│  └─ Placement: [Feed + Stories, Auto]
├─ Ad Set 2: [Interest - Business Software]
│  └─ Placement: [Feed only]
└─ Ad Set 3: [Retargeting - Website 30d]
   └─ Placement: [All placements]
```

**Audience Strategy**:

1. **Core Audiences**: Interests (business tools, productivity, startups)
2. **Lookalike**: 1% of purchasers/high-value leads
3. **Retargeting**: 30-day website visitors, video viewers (75%+)

**Creative Best Practices**:

- Use video (1:1 or 9:16 for Stories)
- First 3 seconds = hook (problem or result)
- Show product UI in action
- Add captions (85% watch muted)
- Test 3-5 creative variants per campaign

### 2.5 Budget Allocation & Scaling

**Initial Budget** (Series A, $30k-50k/month total):

```
Channel            Budget    Expected Results
─────────────────────────────────────────────
LinkedIn Ads       $15k      50 MQLs, 10 SQLs, $1.5k CAC
Google Search      $12k      80 MQLs, 20 SQLs, $600 CAC
Google Display     $5k       120 MQLs, 5 SQLs, $1k CAC
Meta Ads           $5k       100 MQLs, 8 SQLs, $625 CAC
Partnerships       $3k       20 MQLs, 5 SQLs, $600 CAC
─────────────────────────────────────────────
TOTAL              $40k      370 MQLs, 48 SQLs, $833 avg CAC
```

**Scaling Rules**:

1. If CAC <target → Increase budget 20% weekly
2. If CAC >target → Pause, optimize, relaunch
3. If conversion rate drops >20% → Check landing page, offer fatigue
4. Scale winners, kill losers fast (2-week test minimum)

**HubSpot ROI Dashboard**:

- Marketing → Reports → Create Custom Report
- Metrics: Spend, Leads, MQLs, SQLs, CAC, ROAS, Pipeline $
- Dimensions: Campaign, Channel, Region
- Frequency: Daily review, weekly optimization

---
