# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# Process Automation: Scale Your Revenue Operations Without Hiring

## Overview

Process automation is the practice of using software to execute repetitive revenue operations tasks automatically—data entry, lead routing, email follow-ups, reporting, and more. For solo entrepreneurs and small teams, automation is the multiplier that allows you to scale revenue operations without proportionally scaling headcount.

**When to use this skill:**
- You're spending 5+ hours per week on repetitive manual tasks
- Data entry errors are causing problems (wrong fields, missing information)
- Leads are falling through the cracks (slow follow-up, no follow-up)
- You need to scale operations but can't afford more headcount
- Reports and dashboards require manual data compilation
- You want to improve response times without working weekends
- Integration between tools requires manual copy-paste
- You're preparing to scale and need repeatable systems

**Why process automation matters:**
- **Time savings:** Reclaim 10-20 hours per week for strategic work
- **Consistency:** Automated processes never forget or skip steps
- **Speed:** Instant execution (lead routing in seconds, not hours)
- **Scalability:** Handle 10x more leads without 10x more people
- **Data accuracy:** Eliminate manual data entry errors
- **Cost efficiency:** $5,000/year in automation vs $50,000+ for a hire
- **Competitive advantage:** Respond faster, deliver better customer experience

**The cost of manual processes:**
- 15-25 hours per week spent on repetitive tasks (at $100/hour = $78K-$130K/year in opportunity cost)
- Slow response times (24+ hours vs. minutes) = 30-50% fewer conversions
- Errors and inconsistencies (data quality issues, missed follow-ups)
- Can't scale without hiring (linear relationship between volume and headcount)
- Burnout from repetitive work (low morale, high turnover)

## The Process Automation Framework

### 1. Identify Automation Opportunities

**The Automation Priority Matrix**

Prioritize processes based on impact and ease:

```
HIGH IMPACT + EASY TO AUTOMATE (DO FIRST):
✓ Lead routing and assignment
✓ Email follow-up sequences
✓ Data enrichment (company/contact info)
✓ Lead scoring and qualification
✓ Calendar scheduling (book meetings)
✓ Slack/email notifications (alerts)
✓ CRM data updates (status changes)

HIGH IMPACT + MODERATE COMPLEXITY (DO SECOND):
✓ Multi-channel campaigns (email + LinkedIn + ads)
✓ Report generation and distribution
✓ Customer onboarding workflows
✓ Renewal reminders and upsell triggers
✓ Deal stage progression tracking
✓ Churn risk detection and alerts

HIGH IMPACT + COMPLEX (DO LATER OR OUTSOURCE):
✓ Predictive lead scoring (machine learning)
✓ Custom integrations (API development)
✓ Advanced analytics and forecasting
✓ Multi-system data sync (data warehouse)

LOW IMPACT (DON'T AUTOMATE YET):
✗ Rarely-used reports (manual is fine)
✗ One-off processes (not worth building)
✗ Tasks requiring high-touch personalization (sales calls, contract negotiation)
```

**Time Audit: Where Are You Spending Time?**

Track your time for one week:

```
AUDIT TEMPLATE:

DAY 1 (Monday):
- 8:00-8:30am: Check email, respond to inquiries (30 min)
- 8:30-9:15am: Manually route new leads to sales reps (45 min) ← AUTOMATE
- 9:15-10:00am: Update deal stages in CRM (45 min) ← AUTOMATE
- 10:00-11:00am: Sales calls (60 min) ✓ Keep
- 11:00-11:30am: Follow-up emails after calls (30 min) ← AUTOMATE
- 11:30am-12:00pm: Data entry from calls into CRM (30 min) ← AUTOMATE
...

WEEKLY TOTAL BY CATEGORY:
- Sales calls/meetings: 15 hours ✓ High-value (keep)
- Data entry: 5 hours ← AUTOMATE (save 5 hours/week)
- Lead routing: 3 hours ← AUTOMATE (save 3 hours/week)
- Follow-up emails: 4 hours ← AUTOMATE (save 4 hours/week)
- Reporting: 2 hours ← AUTOMATE (save 2 hours/week)
- Other admin: 3 hours ← Some automatable

TOTAL AUTOMATABLE: 14+ hours/week
VALUE: 14 hours × 50 weeks × $100/hour = $70,000/year in time savings
```

**ROI Calculation for Each Process:**

```
PROCESS: Lead Routing
Time Spent: 3 hours/week (manual assignment, context checking)
Error Rate: 10% (wrong rep, duplicate assignment)
Value of Automation:
- Time saved: 3 hours × 50 weeks = 150 hours/year = $15,000
- Faster routing: <5 minutes instead of 4+ hours = 30% more conversions = $50,000 revenue impact
- Fewer errors: Eliminate 10% error rate = better customer experience
Total Value: $65,000/year

Cost to Automate:
- CRM workflow setup: 5 hours @ $100/hour = $500 (one-time)
- Ongoing maintenance: 2 hours/year = $200/year
Total Cost: $700 (first year), $200/year (ongoing)

ROI: $65,000 / $700 = 9,186% first year
Payback: <1 week

VERDICT: Automate immediately ✓
```

### 2. CRM Automation (Foundation)

**Lead Routing Automation**

Automatically assign leads to the right rep:

```
WORKFLOW: New Lead Submitted (via form)

TRIGGER:
Contact is created OR Contact property "Lead Status" changes to "New"

CONDITIONS (IF/THEN LOGIC):

IF Company Size ≥ 200 employees AND Lead Score ≥ 80:
  → Set property "Lead Type" = "Enterprise"
  → Assign to Owner: [Enterprise Team] (round-robin rotation)
  → Set property "Priority" = "High"
  → Send Slack notification to #enterprise-leads channel
  → Send email alert to assigned rep
  → Create task: "Contact within 4 hours"

ELSE IF Company Size 50-200 employees AND Lead Score ≥ 60:
  → Set property "Lead Type" = "Mid-Market"
  → Assign to Owner: [Mid-Market Team] (round-robin)
  → Set property "Priority" = "Medium"
  → Add to sequence: "Mid-Market Outreach"
  → Send email alert to assigned rep

ELSE IF Company Size < 50 employees AND Lead Score ≥ 60:
  → Set property "Lead Type" = "SMB"
  → Assign to Owner: [SMB/SDR Team] (round-robin)
  → Set property "Priority" = "Medium"
  → Add to sequence: "SMB Outreach"

ELSE IF Lead Score 40-59:
  → Set property "Lead Type" = "Nurture"
  → Assign to Owner: [Marketing]
  → Enroll in workflow: "Nurture Sequence"
  → No sales notification

ELSE (Lead Score < 40):
  → Set property "Lead Status" = "Unqualified"
  → Assign to Owner: [Marketing]
  → Enroll in workflow: "Long-term Newsletter"

SPECIAL CASES:

IF Lead Source = "Referral":
  → Override routing, assign to referral partner owner
  → Set priority = "High"
  → Send immediate Slack notification

IF Company Name matches Target Account List:
  → Assign to dedicated account owner (not round-robin)
  → Flag as "Target Account"
  → Send notification to sales leader

IMPLEMENTATION:
- HubSpot: Use Workflows (Professional or Enterprise plan)
- Salesforce: Use Flow Builder or Process Builder
- Pipedrive: Use Workflow Automation
- Zoho: Use Workflows
```

**Lead Scoring Automation**

Automatically calculate and update lead scores:

```
WORKFLOW: Lead Scoring Engine

TRIGGER: Contact property changes OR Company property changes OR Website activity

SCORING LOGIC:

FIT SCORE (Company/Contact Properties):
Start with 0, add/subtract points based on:

Company Size:
  IF Employees = "50-200" → +25 points
  IF Employees = "201-500" → +20 points
  IF Employees = "1-10" → -10 points

Industry:
  IF Industry = "B2B SaaS" OR "Technology" → +20 points
  IF Industry = "Professional Services" → +10 points
  IF Industry = "Non-profit" → -20 points

Job Title:
  IF Job Title contains "VP" OR "Director" OR "C-Suite" → +25 points
  IF Job Title contains "Manager" → +15 points
  IF Job Title contains "Coordinator" → +5 points

ENGAGEMENT SCORE (Behavioral):

Website Activity:
  IF Page = "Pricing" → +30 points
  IF Page = "Demo Request" → +50 points
  IF Page = "Case Study" → +15 points
  IF Page = "Blog Post" → +5 points

Email Activity:
  IF Email Opened → +2 points (per open, max 10)
  IF Email Clicked → +5 points (per click, max 20)
  IF Email Replied → +25 points

Form Submissions:
  IF Form = "Demo Request" → +50 points
  IF Form = "Content Download" → +15 points
  IF Form = "Newsletter Signup" → +5 points

DECAY LOGIC:
  IF Last activity > 60 days → Reduce engagement score by 50%
  IF Last activity > 90 days → Reset engagement score to 0

TOTAL SCORE:
  Calculate: Fit Score + Engagement Score = Total Lead Score

UPDATE CRM:
  Set property "Lead Score" = [Calculated Total]
  IF Lead Score ≥ 80 → Set "Lead Grade" = "A"
  IF Lead Score 60-79 → Set "Lead Grade" = "B"
  IF Lead Score 40-59 → Set "Lead Grade" = "C"
  IF Lead Score < 40 → Set "Lead Grade" = "D"

TRIGGER ACTIONS:
  IF Lead Score crosses 60 threshold (C → B or D → C):
    → Create MQL (trigger lead routing workflow)
    → Notify assigned sales rep

  IF Lead Score crosses 80 threshold (B → A):
    → Flag as "Hot Lead"
    → Send urgent Slack notification
    → Create high-priority task
```

**Deal Stage Automation**

Track and automate deal progression:

```
WORKFLOW: Deal Stage Transitions

TRIGGER: Deal stage changes

STAGE 1: DISCOVERY → DEMO

ACTIONS:
- Create task: "Send demo confirmation email" (due: immediately)
- Create task: "Prepare demo environment" (due: 1 day before demo)
- Create task: "Send calendar invite with Zoom link" (due: 2 days before demo)
- Update property "Next Steps" = "Demo scheduled for [date]"
- Set reminder: "Follow up 1 day before demo"
- Send internal Slack notification: "[Rep] booked demo with [Company]"

STAGE 2: DEMO → PROPOSAL

ACTIONS:
- Create task: "Send proposal" (due: within 48 hours)
- Create task: "Follow up on proposal" (due: 3 days after sent)
- Update property "Proposal Sent Date" = Today
- Calculate property "Days in Proposal Stage" (for tracking)
- Send email template: "Proposal Follow-Up" (automated, 2 days after proposal sent)

STAGE 3: PROPOSAL → NEGOTIATION

ACTIONS:
- Create task: "Schedule contract review call" (due: within 24 hours)
- Create task: "Send contract" (due: within 48 hours)
- Update property "Contract Sent Date" = Today
- Notify sales manager: "Deal in negotiation, review needed"
- Set forecast category: "Commit" (high confidence)

STAGE 4: NEGOTIATION → CLOSED-WON

ACTIONS:
- Update deal status: "Closed-Won"
- Update close date: Today
- Create task: "Send welcome email" (due: immediately)
- Create task: "Onboarding kickoff call" (due: within 48 hours)
- Assign to Customer Success: [CS Team]
- Enroll in workflow: "Customer Onboarding"
- Send internal Slack notification: "🎉 [Rep] closed [Company] - $[Amount]!"
- Create invoice (if using billing automation)
- Trigger revenue recognition (if using accounting integration)

STAGE 5: CLOSED-LOST

ACTIONS:
- Update deal status: "Closed-Lost"
- Update close date: Today
- Create task: "Complete win/loss survey" (due: within 24 hours)
- Required field: "Closed Lost Reason" (dropdown)
- IF Closed Lost Reason = "Timing" OR "Budget":
  → Enroll in workflow: "Re-engagement (6 months)"
  → Create task for rep: "Follow up in 6 months"
- IF Closed Lost Reason = "Competitor":
  → Capture competitor name
  → Add to competitive intelligence report
- Remove from active sales sequences

STALE DEAL DETECTION:

IF Deal has been in same stage for 30+ days:
  → Send alert to rep: "Deal stale in [Stage] for 30 days"
  → Create task: "Update deal or move to Closed-Lost"
  → Notify sales manager (for coaching)

IF Deal has been in same stage for 60+ days:
  → Escalate to sales manager
  → Mark as "At Risk"
  → Require rep to update or close
```

### 3. Email Automation and Sequences

**Automated Follow-Up Sequences**

Never forget to follow up:

```
SEQUENCE: MQL Follow-Up (Automated)

TRIGGER: Contact becomes MQL (lead score ≥ 60)

EMAIL 1 (Immediate - within 1 hour):
Subject: Quick question about [Company]'s [pain point]

Hi [First Name],

I noticed you [specific action: downloaded our guide, attended our webinar, visited pricing page].

We help [Company Size] companies in [Industry] solve [Pain Point]. Would it make sense to have a quick 15-minute call to explore if we can help [Company]?

Here's a link to my calendar: [Calendar Link]

[Your Name]
[Title]

---

IF NO RESPONSE AFTER 2 DAYS:

EMAIL 2 (Day 3):
Subject: Re: Quick question about [Company]'s [pain point]

Hi [First Name],

Following up on my note from [Day 1]. I'd love to share how we helped [Similar Company] achieve [Specific Result].

Are you the right person to discuss [solution area] at [Company]? If not, who should I reach out to?

[Your Name]

---

IF NO RESPONSE AFTER 4 MORE DAYS:

EMAIL 3 (Day 7):
Subject: Should I close your file?

Hi [First Name],

I haven't heard back, so I'm guessing now's not the right time.

Should I close your file, or would you like to reconnect in a few months?

Just reply "Close" or "Later" and I'll follow your lead.

[Your Name]

---

IF CLICKS LINK OR REPLIES:
→ Remove from sequence
→ Alert assigned sales rep
→ Create high-priority task: "Contact responded - follow up now"

IF NO RESPONSE AFTER 3 EMAILS:
→ Remove from sequence
→ Add to nurture workflow (long-term education)
→ Re-engage if new high-intent activity

PERSONALIZATION TOKENS:
- {{First Name}}
- {{Company}}
- {{Industry}}
- {{Job Title}}
- {{Specific Action}} (downloaded X, attended Y)
- {{Mutual Connection}} (if referral)

BEST PRACTICES:
✓ Send between 9am-5pm in recipient's time zone
✓ Skip weekends (pause until Monday)
✓ Remove if unsubscribe or replies "not interested"
✓ A/B test subject lines (track open rates)
✓ Personalize beyond first name (reference their company, pain point)
```

**Event-Triggered Emails**

Automate based on customer actions:

```
TRIGGER: Demo No-Show

IF Contact is enrolled in "Demo Scheduled" AND Meeting Status = "No-Show":

IMMEDIATE ACTION:
- Send email: "Sorry we missed you"

  Subject: Missed you on our call today

  Hi [First Name],

  I was looking forward to our call at [Time] today, but it looks like we missed each other.

  Life happens! Want to reschedule? Here's my calendar: [Link]

  Or if now's not the right time, just let me know and I can follow up in a few weeks.

  [Your Name]

- Create task for rep: "Follow up on no-show"
- Reschedule opportunity: Automatically suggest 3 alternative times

---

TRIGGER: Pricing Page Visit (High Intent)

IF Contact visits "/pricing" page 2+ times in 7 days:

ACTION:
- Send email: "Questions about pricing?"

  Subject: Saw you checking out our pricing

  Hi [First Name],

  I noticed you've been looking at our pricing page. Do you have any questions about our plans?

  I'd be happy to walk you through which plan might be the best fit for [Company].

  Want to chat for 10 minutes? [Calendar Link]

  [Your Name]

- Create task for rep: "High-intent pricing visit - follow up"
- Offer: "Book a call and get [incentive: extended trial, discount, free onboarding]"

---

TRIGGER: Trial Expiring Soon

IF Contact has active trial AND Trial End Date = 3 days from today:

ACTION:
- Send email: "Your trial ends in 3 days"

  Subject: Your [Product] trial ends soon

  Hi [First Name],

  Your trial of [Product] expires in 3 days. Have you had a chance to explore [Key Feature]?

  I'd love to help you get the most out of your trial before it ends. Want to jump on a quick call?

  Or if you're ready to upgrade, you can do so here: [Upgrade Link]

  [Your Name]

- Create task for CS: "Trial expiring - check in"
- Offer: "Extend trial for 7 more days if needed"

---

TRIGGER: Contract Renewal Coming

IF Customer AND Renewal Date = 60 days from today:

ACTION:
- Send email to CS rep (not customer yet): "Renewal coming up"
- Create task: "Schedule QBR and discuss renewal"
- Check health score:
  IF Health Score < 60 → Flag as "At Risk" → Escalate to manager
  IF Health Score ≥ 80 → Identify upsell opportunity

30 DAYS BEFORE RENEWAL:
- Send email to customer: "Let's talk about renewal"
- Schedule renewal conversation
- Prepare ROI report (show value delivered)

7 DAYS BEFORE RENEWAL:
- Send contract renewal email with DocuSign link
- Offer: "Renew now and lock in current pricing" (if increasing prices)
```

### 4. Data Enrichment and Hygiene Automation

**Automatic Data Enrichment**

Fill in missing data automatically:

```
WORKFLOW: Contact Enrichment

TRIGGER: New contact created OR Contact updated (email changed)

STEP 1: Email Validation
- Use integration: Clearbit, Apollo, ZeroBounce, or NeverBounce
- Validate email format and deliverability
- Update property "Email Status":
  • Valid ✓
  • Invalid ✗
  • Risky (temporary, disposable) ⚠️
- IF Invalid → Flag for manual review, don't send emails

STEP 2: Company Identification
- Extract domain from email address (@company.com)
- Look up company details (Clearbit, Apollo, HG Insights)
- Auto-populate:
  • Company Name
  • Company Website
  • Industry
  • Employee Count
  • Annual Revenue (estimated)
  • Company LinkedIn URL
  • Company HQ Location

STEP 3: Contact Enrichment
- Look up contact details (Clearbit, Lusha, RocketReach)
- Auto-populate:
  • Job Title
  • Seniority Level (IC, Manager, Director, VP, C-Suite)
  • Department (Sales, Marketing, Engineering, etc.)
  • LinkedIn Profile URL
  • Phone Number (if available)
  • Location (city, state, country)

STEP 4: Firmographic Scoring
- Categorize company size:
  IF 1-10 employees → "Startup"
  IF 11-50 → "Small Business"
  IF 51-200 → "Mid-Market"
  IF 201-500 → "Growth"
  IF 500+ → "Enterprise"

- Categorize revenue range:
  IF < $1M → "Very Small"
  IF $1-10M → "Small"
  IF $10-50M → "Medium"
  IF $50-100M → "Large"
  IF > $100M → "Enterprise"

STEP 5: Technology Detection
- Identify tools used (BuiltWith, HG Insights, Clearbit)
- Auto-populate:
  • CRM Used (Salesforce, HubSpot, Pipedrive, etc.)
  • Marketing Automation (Marketo, Pardot, HubSpot)
  • Analytics (Google Analytics, Mixpanel, Amplitude)
  • Tech Stack (React, AWS, WordPress, etc.)

USE CASES:
- Better lead scoring (company size, tech stack)
- Personalized outreach (reference their CRM, tools)
- Segmentation (target companies using competitor tools)

STEP 6: Social Profile Linking
- Search for LinkedIn profile (if not provided)
- Search for Twitter profile
- Populate social links in CRM

COST:
- Clearbit: $99-$999/month (based on volume)
- Apollo: $49-$149/month
- BuiltWith: $295-$995/month
- Free alternatives: Google search, LinkedIn manual lookup

FALLBACK:
IF enrichment fails (no data found):
  → Flag contact for manual research
  → Create task for SDR: "Research [Name] at [Company]"
  → Set completeness score = low (triggers manual work)
```

**Duplicate Detection and Merging**

Prevent and clean up duplicates:

```
WORKFLOW: Duplicate Prevention

TRIGGER: Contact is about to be created (before save)

STEP 1: Check for Duplicates

Search for existing contacts where:
- Email = New Contact Email (exact match) OR
- First Name + Last Name + Company = Match (fuzzy logic) OR
- Phone Number = Match (if provided)

STEP 2: Action Based on Match

IF Exact Email Match:
  → Prevent creation
  → Show alert: "Contact already exists: [Link to existing record]"
  → Offer to update existing record instead

IF Fuzzy Match (Name + Company):
  → Show warning: "Possible duplicate detected: [Link to similar record]"
  → Allow user to confirm: "Create anyway" or "Update existing"

IF No Match:
  → Allow creation ✓

---

WORKFLOW: Periodic Duplicate Cleanup (Weekly)

SCHEDULE: Every Monday at 8am

STEP 1: Identify Duplicates

Run query:
- Find contacts with same email address (2+ records)
- Find contacts with same name + company (fuzzy match)
- Find contacts with same phone number

STEP 2: Automated Merge (Safe Cases)

IF exact email match AND one record is empty:
  → Automatically merge (keep complete record)
  → Log: "Auto-merged duplicate [ID] into [Master ID]"

IF exact email match AND both have data:
  → Flag for manual review
  → Create task for RevOps: "Review and merge duplicates"

STEP 3: Manual Review Queue

Create list view: "Duplicates for Review"
- Shows side-by-side comparison
- Allows one-click merge
- Tracks merge history

STEP 4: Report

Send weekly report:
- Duplicates found: X
- Auto-merged: Y
- Pending manual review: Z
- Duplicate rate: Z / Total Contacts × 100%

BEST PRACTICES:
✓ Merge older record into newer record (preserve recent activity)
✓ Combine all activities, notes, and associations
✓ Keep most complete field values
✓ Add note: "Merged from [Email] on [Date]"
```

### 5. Reporting and Analytics Automation

**Automated Report Generation**

Stop spending hours building reports:

```
REPORT: Weekly Pipeline Report

SCHEDULE: Every Friday at 5pm

DATA SOURCES:
- CRM: Deals, Activities, Win/Loss Reasons
- Marketing Automation: MQLs, Campaigns
- Spreadsheet: Quota and Targets

METRICS TO CALCULATE:

Pipeline Health:
- Total pipeline value (sum of open deals)
- Pipeline by stage (Discovery, Demo, Proposal, Negotiation)
- Weighted pipeline (stage × probability)
- Pipeline coverage ratio (pipeline / quota)

This Week's Activity:
- MQLs generated: X (vs target)
- SQLs created: Y
- Opportunities created: Z
- Deals closed-won: W ($)
- Deals closed-lost: V ($)

Conversion Rates:
- MQL → SQL: ___%
- SQL → Opp: ___%
- Opp → Closed-Won: ___%

Forecast:
- Committed (>80% probability): $___ (% of quota)
- Best Case (>50% probability): $___ (% of quota)
- Pipeline (all open): $___ (% of quota)

Top Performers:
- Rep with most new pipeline: [Name] ($X)
- Rep with most closed deals: [Name] ($X)
- Best-performing campaign: [Campaign] (X MQLs, Y SQLs)

Red Flags:
- Deals stale > 30 days: X deals
- Pipeline coverage < 3x: ⚠️ At risk of missing target
- MQL → SQL conversion < 20%: ⚠️ Lead quality issue

FORMAT:
- Google Slides or PowerPoint (auto-generated)
- PDF sent via email
- Dashboard link (live data)

DISTRIBUTION:
- Email to: Sales Team, Marketing Team, Leadership
- Posted in Slack: #sales-team channel
- Stored in: Google Drive > Reports > Weekly Pipeline Reports

AUTOMATION TOOLS:
- Databox: Pre-built templates, auto-send reports
- Google Data Studio: Live dashboards, scheduled email delivery
- Power BI: Automated report generation
- Zapier: Pull data from CRM, populate Google Slides, send email

TIME SAVED: 3 hours/week → 150 hours/year = $15,000 value
```

**Real-Time Alerts and Notifications**

Stay informed without constantly checking:

```
ALERT: High-Value Deal Activity

TRIGGER: Deal amount > $50,000 AND Deal stage changes

ACTION:
- Send Slack notification to #revenue-team:
  "🔥 [Rep] moved [Company] ($[Amount]) to [New Stage]"
- Send email to sales manager (if stage = Negotiation or Closed-Won)
- Post to team dashboard (live activity feed)

---

ALERT: Lead Response Time Violation

TRIGGER: MQL created 4+ hours ago AND Lead Status still = "New" (not contacted)

ACTION:
- Send Slack notification to assigned rep:
  "@[Rep] - MQL assigned 4 hours ago, not yet contacted. SLA miss!"
- Send email to sales manager:
  "SLA violation: [Rep] hasn't contacted [Lead] within 4 hours"
- Escalate if 8+ hours: Reassign lead to next available rep
- Track SLA compliance in dashboard (% of leads contacted within SLA)

---

ALERT: Churn Risk Detected

TRIGGER: Customer health score drops below 60

ACTION:
- Send Slack notification to CS manager:
  "⚠️ [Customer] health score dropped to [Score]. At-risk!"
- Send email to assigned CSM:
  "Action needed: [Customer] showing churn risk signals"
- Create task: "Check in with [Customer], understand issues"
- Escalate to executive if customer is Enterprise tier

---

ALERT: Expansion Opportunity

TRIGGER: Customer usage exceeds plan limits by 20%+

ACTION:
- Send Slack notification to CS team:
  "💰 [Customer] exceeding plan limits. Upsell opportunity!"
- Create task for CSM: "Discuss upgrade to [Higher Tier] with [Customer]"
- Auto-generate ROI report (show value they're getting)
- Prepare pricing proposal (upgrade options)

---

ALERT: Competitor Mention

TRIGGER: Deal closed-lost Reason = "Chose competitor" AND Competitor = "[Competitor Name]"

ACTION:
- Send Slack notification to #competitive-intel:
  "Lost deal to [Competitor]: [Company]. Reason: [Details]"
- Add to competitive analysis tracker
- Schedule post-mortem: "Why did we lose to [Competitor]?"
- Update competitive battlecard (if needed)

---

ALERT: Positive Customer Feedback (NPS Promoter)

TRIGGER: Customer NPS score = 9 or 10

ACTION:
- Send Slack notification to #wins:
  "🎉 [Customer] gave us a 10/10 NPS score!"
- Create task for CS: "Request testimonial or case study from [Customer]"
- Create task for Marketing: "Ask [Customer] for G2/Capterra review"
- Send thank-you email to customer (automated or manual)
- Consider referral program outreach

ALERTING BEST PRACTICES:
✓ Don't over-alert (alert fatigue reduces effectiveness)
✓ Only alert on actionable events (not FYI)
✓ Use channels appropriately (Slack for urgent, email for FYI)
✓ Include context (not just "New lead!" but "High-value lead from target account")
✗ Avoid midnight alerts (schedule during work hours)
```

### 6. Integration Automation

**Zapier/Make Workflows**

Connect tools without custom code:

```
INTEGRATION 1: New Customer → Onboarding

TRIGGER: Deal status changes to "Closed-Won" in CRM

ACTIONS (Multi-Step Zap):

Step 1: Create customer record in billing system (Stripe)
- Customer name
- Email
- Plan tier
- Billing frequency (monthly/annual)

Step 2: Send welcome email (via Gmail or email platform)
- Template: "Welcome to [Product]!"
- Include: Login credentials, getting started guide
- CC: CS team

Step 3: Create Slack channel for customer
- Channel name: #customer-[company-name]
- Add: Account owner, CS manager, support team
- Post welcome message with account details

Step 4: Create project in project management tool (Asana/Trello)
- Project: "[Company] Onboarding"
- Tasks: Kickoff call, setup, training, go-live
- Assign: CS Manager
- Due dates: Based on onboarding timeline

Step 5: Add customer to CS dashboard
- Update customer health score spreadsheet
- Add to "New Customers" report
- Set next check-in date (30 days)

TIME SAVED: 45 minutes per new customer
COST: Zapier Professional: $19.99/month (unlimited Zaps)

---

INTEGRATION 2: Webinar Registration → CRM + Email Sequence

TRIGGER: New webinar registration (Zoom, GoToWebinar, Demio)

ACTIONS:

Step 1: Create or update contact in CRM
- Pull registration data (name, email, company, job title)
- Check for existing contact (by email)
- If exists: Update record, add activity note
- If new: Create contact, set lead source = "Webinar - [Webinar Name]"

Step 2: Add to webinar reminder sequence (email automation)
- Email 1: 24 hours before (confirmation + calendar invite)
- Email 2: 1 hour before (reminder)
- Email 3: 1 hour after (slides + recording, if no-show)

Step 3: Tag in CRM
- Add tag: "Webinar - [Webinar Name]"
- Add to list: "[Webinar Name] Attendees"

Step 4: Notify sales (if high-priority lead)
- IF lead score > 60 OR company on target account list:
  → Send Slack notification: "High-priority webinar registrant: [Name] from [Company]"

Step 5: Post-webinar follow-up
- TRIGGER: Webinar ends
- IF attendee showed up:
  → Update CRM: "Webinar Attended"
  → Add 20 points to lead score
  → Send follow-up email: "Thanks for attending, here's the recording"
  → Create task for sales: "Follow up on webinar attendee"

- IF registered but no-show:
  → Update CRM: "Webinar No-Show"
  → Send email: "Sorry we missed you, here's the recording"
  → Add to nurture sequence

---

INTEGRATION 3: G2/Capterra Review → Slack + CRM

TRIGGER: New review posted (via API or webhook)

ACTIONS:

Step 1: Post to Slack (#customer-love channel)
- "⭐⭐⭐⭐⭐ New 5-star review from [Name] at [Company]!"
- Include review excerpt
- Link to full review

Step 2: Update CRM
- Find customer by company name
- Add note: "Submitted 5-star review on G2"
- Update property: "Review Date" = Today
- IF 5 stars:
  → Add tag: "Promoter"
  → Consider for case study/testimonial
- IF 1-3 stars:
  → Flag for CS follow-up
  → Create task: "Reach out about poor review"

Step 3: Send thank-you email
- Automated email to reviewer
- Thank them for feedback
- Offer incentive (Amazon gift card, product credit)

---

INTEGRATION 4: Support Ticket → CRM Activity

TRIGGER: New support ticket created (Zendesk, Intercom, HelpScout)

ACTIONS:

Step 1: Find customer in CRM (by email)

Step 2: Log activity in CRM
- Activity type: "Support Ticket"
- Subject: [Ticket title]
- Description: [Ticket excerpt]
- Link to ticket (for context)

Step 3: Update health score
- Increment "Support Ticket Count" (last 30 days)
- IF Support Tickets > 5 in 30 days:
  → Flag as "At Risk - High Support Volume"
  → Notify CS Manager

Step 4: Pattern detection
- IF multiple tickets about same feature:
  → Notify Product team
  → Flag for product improvement

POPULAR INTEGRATION TOOLS:
- Zapier ($19.99-$599/month): 5,000+ apps, no code
- Make ($9-$29/month): Advanced logic, similar to Zapier
- Workato ($99+/month): Enterprise integrations
- Tray.io (enterprise): Complex workflow automation
- Native integrations: Most CRMs have built-in integrations (use those first)
```

## Tools and Technology

**Automation Platforms:**
- **Zapier** ($19.99-$599/month): 5,000+ apps, no-code automation
- **Make** ($9-$29/month): Advanced workflows, cheaper than Zapier
- **Workato** ($99+/month): Enterprise-grade automation
- **Microsoft Power Automate** ($15/user/month): Microsoft ecosystem
- **IFTTT** (free-$2.50/month): Simple if-this-then-that automation

**CRM Workflow Automation:**
- **HubSpot Workflows** (Professional: $800/month): No-code CRM automation
- **Salesforce Flow** (included with Salesforce): Enterprise automation
- **Pipedrive Workflow Automation** (included in Advanced plan)
- **Zoho CRM Workflows** (included in Professional+)

**Email Sequence Automation:**
- **HubSpot Sequences** (Sales Hub Professional: $450/month)
- **Outreach** ($100+/user/month): Advanced sales engagement
- **Reply.io** ($60+/user/month): Affordable alternative
- **Mailchimp** ($20+/month): Marketing email automation
- **ActiveCampaign** ($15+/month): Marketing automation + CRM

**Data Enrichment:**
- **Clearbit** ($99-$999/month): Real-time enrichment API
- **Apollo.io** ($49-$149/month): B2B data + enrichment
- **ZoomInfo** (enterprise pricing): Comprehensive B2B data
- **Hunter.io** ($49+/month): Email finding + verification

**Calendar Automation:**
- **Calendly** (free-$10/user/month): Simple scheduling
- **Chili Piper** ($15+/user/month): Advanced routing + scheduling
- **HubSpot Meetings** (free with HubSpot): Basic scheduling
- **Google Calendar + Zapier** (DIY automation)

**Reporting Automation:**
- **Databox** ($49-$135/month): Automated dashboards + reports
- **Klipfolio** ($90-$225/month): Custom metric dashboards
- **Google Data Studio** (free): Free dashboard builder
- **Power BI** ($10+/user/month): Microsoft BI tool

**No-Code Tools:**
- **Airtable** ($20+/user/month): Database + automation
- **Notion** ($10+/user/month): Docs + databases + automation
- **Coda** ($10+/user/month): Docs + automation
- **Retool** ($10+/user/month): Internal tool builder

## Process Automation ROI

**Investment:**
```
TOOLS (monthly):
- Zapier (Professional): $19.99
- HubSpot Marketing + Sales Pro: $800
- Data enrichment (Clearbit): $99
- Calendar scheduling (Calendly): $10
- Reporting (Databox): $49
Total Tools: $978/month = $11,736/year

SETUP TIME:
- Initial automation setup: 60 hours @ $100/hour = $6,000
- Training team: 10 hours = $1,000
- Ongoing maintenance: 3 hours/month = $3,600/year

TOTAL YEAR 1: $22,336
ONGOING (Year 2+): $15,336/year
```

**Value:**
```
SCENARIO: Solo founder + 1 SDR, scaling to $1M ARR

TIME SAVINGS:
- Lead routing: 3 hours/week → 0 hours (automated) = 150 hours/year
- Email follow-ups: 4 hours/week → 1 hour (mostly automated) = 150 hours/year
- Data entry: 5 hours/week → 1 hour (auto-enrichment) = 200 hours/year
- Reporting: 2 hours/week → 0.5 hours (automated) = 75 hours/year
Total Time Saved: 575 hours/year × $100/hour = $57,500 value

REVENUE IMPACT:
- Faster lead response (minutes vs hours) = 30% more conversions
- 100 MQLs/month × 25% SQL rate × 30% lift = +7.5 more SQLs/month
- 7.5 SQLs × 40% Opp rate × 30% win rate × $15K ACV = +$13,500 MRR (eventually)
- Annual revenue impact: ~$160,000

EFFICIENCY GAINS:
- Can handle 3x more leads without hiring = $50K saved (no additional hire needed)
- Improved data quality = better decisions = $25K+ value
- Reduced errors = better customer experience = lower churn

TOTAL VALUE YEAR 1: $290,000+
INVESTMENT: $22,336
ROI: 1,198%
Payback: <1 month
```

## Common Automation Mistakes

**1. Automating Broken Processes**
- **Mistake:** Automating a bad process makes it consistently bad, faster
- **Impact:** Amplifies problems instead of solving them
- **Solution:** Fix the process first, then automate it

**2. Over-Automation**
- **Mistake:** Automating everything, including personal touches
- **Impact:** Feels robotic, customers sense lack of personalization
- **Solution:** Automate repetitive admin, keep human touch on key interactions

**3. No Testing Before Launch**
- **Mistake:** Deploying automation without testing edge cases
- **Impact:** Broken workflows, spam emails, angry customers
- **Solution:** Test with small group first, monitor closely for first week

**4. Set It and Forget It**
- **Mistake:** Building automation and never revisiting it
- **Impact:** Automation becomes outdated, misses new use cases
- **Solution:** Review automations quarterly, update as processes change

**5. Ignoring Error Logs**
- **Mistake:** Automation fails silently, no one notices
- **Impact:** Leads fall through cracks, processes break
- **Solution:** Set up error notifications, review logs weekly

**6. Too Complex Too Soon**
- **Mistake:** Building elaborate multi-step workflows from day 1
- **Impact:** Hard to debug, difficult to maintain, high failure rate
- **Solution:** Start simple (3-5 steps), add complexity gradually

**7. No Documentation**
- **Mistake:** Building automations without documenting how they work
- **Impact:** Team doesn't know what's automated, can't troubleshoot
- **Solution:** Document every automation (trigger, actions, owner, last updated)

**8. Vendor Lock-In Without Backup**
- **Mistake:** Building all automation in one tool with no export capability
- **Impact:** Stuck with expensive tool, can't migrate
- **Solution:** Document logic, use open standards where possible, have migration plan

## Related Skills and Frameworks

**Related Revenue Operations Toolkit Skills:**
- **CRM Hygiene** - Clean data is essential for effective automation
- **Sales-Marketing Alignment** - Automate handoffs between teams
- **Attribution & ROI** - Automate data collection for attribution
- **Pipeline Forecasting** - Automate forecast calculations
- **Revenue Analytics** - Automate report generation and dashboards

**Related Frameworks:**
- **Revenue Waterfall** - Automate stage transitions and tracking
- **AAARRR** - Automate metrics at each funnel stage
- **Unit Economics** - Automate CAC and LTV calculations

**Complementary Skills:**
- **Sales Enablement** - Automate content delivery to sales team
- **Customer Success** - Automate onboarding and health score tracking
- **Lead Management** - Automate scoring, routing, nurturing
- **Email Marketing** - Automate campaigns and sequences

---

**Next Steps:**
1. Complete time audit (track where you spend time for 1 week)
2. Identify top 3 processes to automate (high impact + easy to start)
3. Set up basic lead routing automation in CRM (this week)
4. Implement one email follow-up sequence (use template above)
5. Connect 2-3 tools with Zapier (start simple: form → CRM → Slack)
6. Document what you automate (so team knows what's automatic)

**Remember:** Automation is a force multiplier, not a replacement for strategy. Automate repetitive tasks so you can focus on high-value work: strategy, relationships, and growth. Start small, prove value, then scale. The goal is to build a revenue engine that runs efficiently without requiring constant manual intervention.
