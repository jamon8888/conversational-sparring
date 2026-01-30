# Attribution & Reporting
### 5.1 Attribution Models (HubSpot Native)

**Model Selection** (use multi-touch for hybrid motion):

**First-Touch** - Credit to first interaction

- Use case: Awareness campaigns, brand building
- Pro: Shows what drives discovery
- Con: Ignores nurturing influence

**Last-Touch** - Credit to last interaction before conversion

- Use case: Direct response, BOFU campaigns
- Pro: Shows what closes deals
- Con: Ignores earlier touchpoints

**Multi-Touch (W-Shaped)** - Credit to first, last, and middle (40-20-40 split)

- Use case: Hybrid PLG/Sales-Led (recommended for Series A)
- Pro: Full-funnel view
- Con: More complex to explain to stakeholders

**HubSpot Setup**:

- Marketing → Reports → Attribution → Select Model
- Default: Use Multi-Touch for holistic view
- Compare: Run reports side-by-side to see differences

### 5.2 Reporting Dashboard (HubSpot)

**Weekly Performance Dashboard**:

```
Metrics to Track:
1. Traffic: Visits, unique visitors, bounce rate
2. Leads: MQLs, SQLs, conversion rates
3. Pipeline: Opportunities created, value, velocity
4. CAC: Spend ÷ customers acquired
5. Channel Mix: % of leads by source

Dimensions:
- By Channel: Organic, Paid, Email, Social, Referral
- By Campaign: Individual campaign performance
- By Region: US, CA, EU breakdown
- By Stage: TOFU, MOFU, BOFU metrics
```

**Monthly Executive Dashboard**:

```
KPIs:
1. Marketing-Sourced Pipeline: $[X]M (target: $[Y]M)
2. Marketing-Sourced Revenue: $[X]k (target: $[Y]k)
3. Blended CAC: $[X] (target: $[Y])
4. MQL→SQL Rate: [X]% (target: [Y]%)
5. Pipeline Velocity: [X] days (target: [Y] days)
6. ROMI: [X]:1 (target: 3:1+)

Insights:
- Top performing campaigns
- Underperforming channels (kill or optimize)
- New experiments to test next month
- Budget reallocation recommendations
```

### 5.3 Google Analytics Setup

**Events to Track** (GA4):

```
Engagement:
- page_view (auto-tracked)
- scroll (75% depth)
- video_play (product demos)
- file_download (whitepapers, eBooks)

Conversions:
- sign_up (free trial, account created)
- demo_request (calendar booking)
- contact_form (inbound interest)
- pricing_view (pricing page visit)

E-commerce (if applicable):
- add_to_cart
- begin_checkout
- purchase
```

**Custom Dimensions**:

- User Type: Free vs. Paid
- Plan Type: Starter, Pro, Enterprise
- HubSpot Lead Status: MQL, SQL, Customer
- Campaign: HubSpot Campaign ID

**Integration with HubSpot**:

- Use HubSpot tracking code (includes GA4 by default)
- Or: Google Tag Manager for advanced tracking
- Sync: GA4 audiences → HubSpot lists for retargeting

---
