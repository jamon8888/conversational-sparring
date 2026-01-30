# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)


# CRM Hygiene & Data Quality

## Overview
Maintain clean, accurate CRM data that drives reliable reporting, forecasting, and decision-making. This skill helps solo entrepreneurs and small teams build systematic data quality processes without a dedicated operations team.

---

## When to Use This Skill

- Setting up a new CRM
- Cleaning messy CRM data
- Building data entry standards
- Preventing duplicate records
- Automating data maintenance
- Improving forecast accuracy
- Training team on CRM usage

---

## Why CRM Hygiene Matters

**The Cost of Bad Data:**
```
Dirty CRM = Bad decisions

Examples:
• Duplicate contacts → waste time calling same person twice
• Wrong email → marketing bounces, looks unprofessional
• Outdated job titles → pitch wrong person
• Missing fields → can't segment or report
• Old data → chase dead leads

Impact: 30% of CRM data decays annually (people change jobs, companies, emails)
Cost: $15 per bad record × 1,000 records = $15K wasted effort
```

**Clean CRM = Competitive Advantage:**
```
With clean data:
• Marketing: 25% higher open rates (correct emails)
• Sales: 40% faster prospecting (accurate contacts)
• Forecasting: 90%+ accuracy (reliable pipeline data)
• Reporting: Trust your dashboards

ROI: Every $1 spent on data quality → $10 in productivity savings
```

---

## CRM Setup Fundamentals

### Choosing a CRM

**For Solo Entrepreneurs ($0-50/mo):**
- **HubSpot Free CRM**: Best free option, unlimited contacts
- **Pipedrive** ($15/mo): Simple, visual pipeline
- **Streak** (Gmail): $15/mo, lives in Gmail

**For Small Teams ($50-200/mo):**
- **HubSpot Starter** ($50/mo): Marketing + sales
- **Close CRM** ($99/mo): Built for outbound sales
- **Salesforce Essentials** ($25/user/mo): Industry standard

**Selection Criteria:**
```
✓ Ease of use (you'll actually use it)
✓ Integration with email/calendar
✓ Mobile app (update on the go)
✓ Reporting capabilities
✓ Automation features
✓ Price (start small, upgrade later)
```

---

### Essential CRM Objects

**1. Contacts (People)**
```
Required Fields:
□ First Name
□ Last Name
□ Email
□ Phone
□ Company (link to Account)
□ Job Title
□ Owner (who manages this contact)

Optional but Valuable:
□ LinkedIn URL
□ Lead Source
□ Lead Status
□ Last Contacted Date
□ Next Follow-up Date
```

**2. Accounts (Companies)**
```
Required Fields:
□ Company Name
□ Website
□ Industry
□ Company Size (employees)
□ Owner

Optional but Valuable:
□ Annual Revenue
□ Tech Stack
□ Funding Stage
□ Headquarters Location
```

**3. Deals/Opportunities**
```
Required Fields:
□ Deal Name
□ Account (linked)
□ Amount ($)
□ Close Date
□ Stage
□ Owner

Optional but Valuable:
□ Probability (%)
□ Lead Source
□ Next Step
□ Competition
□ Decision Maker (linked Contact)
```

---

## Data Quality Standards

### Field Naming Conventions

**Use consistent formats:**
```
Company Names:
✓ "Acme Corporation" (official name)
✗ "ACME" or "acme corp" or "Acme Co"

Phone Numbers:
✓ "+1-555-123-4567" (international format)
✗ "555.123.4567" or "(555) 123-4567"

Emails:
✓ "john.smith@company.com" (lowercase)
✗ "John.Smith@Company.COM"

Job Titles:
✓ "VP Sales" (standard abbreviations)
✗ "Vice President of Sales" (inconsistent)
```

**Why standards matter:**
- Prevent duplicates
- Enable accurate reporting
- Allow automation
- Make searches work

---

### Required vs. Optional Fields

**Make critical fields required:**
```
Contact Creation:
Required: First Name, Last Name, Email
Optional: Phone, Company, Title

Deal Creation:
Required: Deal Name, Amount, Close Date, Stage
Optional: Probability, Next Step

Why: Balance data quality with ease of entry
```

**Field Validation Rules:**
```
Email: Must contain @ and .
Phone: Must be 10+ digits
Amount: Must be number > 0
Close Date: Must be future date
Website: Must start with http:// or https://
```

---

## Preventing Duplicate Records

### Duplicate Detection Rules

**Contact Duplicates:**
```
Match Rule 1: Exact email match
→ Block creation: "Contact with this email already exists"

Match Rule 2: Same first name + last name + company
→ Warn: "Similar contact found. Are you sure?"

Match Rule 3: Fuzzy company name match
→ Example: "Acme Corp" vs. "Acme Corporation"
→ Suggest merge
```

**Account Duplicates:**
```
Match Rule 1: Same website domain
→ Block: "Account with this domain already exists"

Match Rule 2: Similar company name (Levenshtein distance)
→ "Acme Inc" vs. "Acme Incorporated"
→ Suggest merge

Match Rule 3: Same address
→ Warn: "Company at this address exists"
```

---

### Deduplication Process

**Monthly Deduplication Routine:**

**Step 1: Find Duplicates**
```
CRM Report: Contacts with same email
Sort by: Email
Review: Merge or keep separate?

Common scenarios:
• Same person, multiple entries → MERGE
• Different people, shared email (e.g., info@company.com) → KEEP SEPARATE
• Old vs. new record → MERGE, keep newest
```

**Step 2: Merge Records**
```
Merge Process:
1. Identify "master" record (most complete)
2. Copy missing data from duplicate to master
3. Reassign activities (emails, calls) to master
4. Delete duplicate

Tools:
• HubSpot: Built-in merge tool
• Salesforce: Duplicate Management
• Manual: Export, dedupe in spreadsheet, reimport
```

**Step 3: Prevent Future Duplicates**
```
Actions:
□ Enable duplicate detection rules
□ Train team on search-before-create
□ Use browser extension (e.g., HubSpot Chrome extension shows if contact exists)
□ Set up import matching rules (match on email)
```

---

## Data Enrichment

### What to Enrich

**Contact-Level:**
```
Add automatically:
• Job title (from LinkedIn)
• Company (from email domain)
• Location (from IP address)
• Social profiles (LinkedIn, Twitter)
```

**Company-Level:**
```
Add automatically:
• Industry
• Company size (employees)
• Revenue
• Funding stage
• Tech stack
```

**Tools for Enrichment:**
- **Clearbit** ($99/mo): Email → full profile
- **ZoomInfo** ($$$): B2B database
- **Hunter.io** ($49/mo): Email finder
- **Built-in**: HubSpot enrichment (free tier)

---

### Enrichment Workflows

**Automated Enrichment (Ideal):**
```
Trigger: New contact created
Action: Look up company via Clearbit
Result: Auto-fill company name, industry, size, revenue

Trigger: New company created
Action: Scrape website for tech stack
Result: Tag with technologies used

Time saved: 5 minutes per record × 100 records/month = 8 hours/month
```

**Manual Enrichment (Budget Option):**
```
Weekly Task (30 min):
1. Export contacts missing key fields
2. Look up on LinkedIn
3. Update in batch
4. Reimport

Focus on:
• High-value prospects (>$10K opportunity)
• Existing customers (for upsell targeting)
```

---

## Data Decay & Maintenance

### Understanding Data Decay

**Decay Rates:**
```
Contact data decays at:
• 30% annually (people change jobs)
• 2.5% monthly

1,000 contacts today:
• 300 will be outdated in 12 months
• 25 are already outdated this month

Action: Regular data hygiene or data becomes worthless
```

**Signs of Decay:**
```
• Email bounces (hard bounce = bad email)
• Phone numbers disconnected
• People no longer at company
• Job title changes
• Company acquired/closed
```

---

### Data Maintenance Schedule

**Weekly (15 min):**
```
□ Review bounced emails (mark invalid or update)
□ Update contacts from recent conversations
□ Flag records missing critical fields
```

**Monthly (1 hour):**
```
□ Run duplicate detection & merge
□ Review stale contacts (no activity 90+ days)
□ Update job titles for key accounts
□ Clean up misspellings/formatting issues
```

**Quarterly (4 hours):**
```
□ Deep clean: export, review, batch update
□ Verify key accounts (top 20%)
□ Re-enrich important contacts
□ Archive dead leads (no response 12+ months)
```

**Annually (8 hours):**
```
□ Full audit of all fields
□ Update field standards
□ Retrain team on data entry
□ Review automation rules
```

---

## CRM Workflow Automation

### Automated Data Entry

**Example Workflows:**

**Workflow 1: Auto-create contact from email**
```
Trigger: Receive email from unknown sender
Action: Create new contact
Fields populated:
• Email (from sender)
• First name (parsed from signature)
• Last name (parsed from signature)
• Lead source: "Inbound email"

Tool: HubSpot, Salesforce, Pipedrive all support this
```

**Workflow 2: Auto-update last contacted**
```
Trigger: Email sent to contact
Action: Update "Last Contacted Date" to today

Why: Track engagement automatically
```

**Workflow 3: Auto-assign owner**
```
Trigger: New lead created
Condition: Lead source = "Website form"
Action: Assign to sales rep (round-robin)

Why: Ensure fast follow-up
```

---

### Data Validation Automation

**Email Verification:**
```
Trigger: New contact created
Action: Verify email via API (e.g., NeverBounce)
Result: Tag as "Valid" or "Invalid"

If invalid: Alert owner, don't add to marketing lists
```

**Phone Validation:**
```
Trigger: Phone number added
Action: Format to standard (+1-555-123-4567)
Result: Consistent format for all records
```

---

## CRM Reporting & Dashboards

### Essential Reports

**Report 1: Data Quality Dashboard**
```
Metrics:
• % contacts with email: 95% (target: 100%)
• % contacts with phone: 60% (target: 80%)
• % contacts with company: 85% (target: 95%)
• # duplicate contacts: 12 (target: 0)
• % stale contacts (90+ days no activity): 40%

Action: Fix lowest-scoring metric each month
```

**Report 2: Activity Report**
```
Last 30 days:
• Emails sent: 150
• Calls logged: 45
• Meetings held: 20
• New contacts added: 35
• Contacts updated: 120

Use: Ensure team using CRM consistently
```

**Report 3: Lead Source Performance**
```
Lead Source    | # Leads | # Opps | # Closed | Win Rate | Avg Deal
---------------|---------|--------|----------|----------|----------
Website        | 50      | 15     | 5        | 33%      | $8K
Referral       | 20      | 12     | 6        | 50%      | $12K
Outbound       | 100     | 20     | 4        | 20%      | $6K
LinkedIn       | 30      | 8      | 3        | 38%      | $10K

Insight: Referrals = best source (high win rate, high deal size)
Action: Build referral program
```

---

## Common CRM Hygiene Mistakes

### ❌ No Data Entry Standards

**Problem:** Every rep enters data differently
**Result:** Can't search, report, or automate
**Fix:** Document standards, train team, enforce with validation

### ❌ Optional Fields Everywhere

**Problem:** Nothing is required, so nothing gets filled
**Result:** 50% of records missing key data
**Fix:** Make critical fields required (email, company, deal amount)

### ❌ No Deduplication Process

**Problem:** Duplicates pile up (5-15% of database)
**Result:** Confusing reports, wasted effort
**Fix:** Monthly deduplication, prevention rules

### ❌ Letting Data Decay

**Problem:** Never update old records
**Result:** 30% of data is wrong within a year
**Fix:** Quarterly data refresh, verify key accounts

### ❌ No CRM Training

**Problem:** Team doesn't know how to use CRM
**Result:** Inconsistent usage, poor data
**Fix:** Onboarding training + monthly refreshers

---

## CRM Hygiene Checklist

**Daily (5 min):**
- [ ] Log all customer interactions (emails, calls, meetings)
- [ ] Update deal stages after conversations
- [ ] Check for duplicate contacts before creating new

**Weekly (15 min):**
- [ ] Review and update deals closing this week
- [ ] Fix bounced emails (update or mark invalid)
- [ ] Fill missing data on high-value prospects

**Monthly (1 hour):**
- [ ] Run duplicate detection and merge
- [ ] Archive stale leads (no activity 90+ days)
- [ ] Review data quality dashboard
- [ ] Update key account information

**Quarterly (4 hours):**
- [ ] Deep clean top 20% of accounts
- [ ] Re-enrich contact data (job titles, companies)
- [ ] Review and update field standards
- [ ] Train team on best practices

**Annually (8 hours):**
- [ ] Full CRM audit
- [ ] Update all standard fields
- [ ] Review automation workflows
- [ ] Celebrate clean data! 🎉

---

## CRM Hygiene Tools

**Free/Built-In:**
- HubSpot: Duplicate detection, enrichment
- Salesforce: Duplicate management
- Pipedrive: Deduplication tools

**Data Enrichment ($):**
- Clearbit ($99/mo): Auto-enrich contacts
- ZoomInfo ($$$): B2B database
- Hunter.io ($49/mo): Email finder

**Data Cleaning ($):**
- Insycle ($99/mo): Automated CRM cleaning
- Validity BriteVerify: Email verification
- NeverBounce: Bulk email verification

**Deduplication:**
- Duplicate Check (Salesforce AppExchange)
- HubSpot Merge Tool (built-in)
- Excel VLOOKUP (manual but free)

---

## CRM Hygiene ROI

**Time Investment:**
```
Setup: 8 hours (standards, validation rules, automation)
Ongoing: 1 hour/week (maintenance, deduplication)

Annual: ~60 hours
```

**Impact:**
```
Before CRM hygiene:
• 30% data inaccurate
• 10% duplicates
• 5 hours/week wasted on bad data
• Unreliable reports
• Missed opportunities (wrong contact info)

After CRM hygiene:
• 95% data accurate
• <1% duplicates
• Save 4 hours/week (no wasted effort)
• Trust your reports
• Never miss opportunity due to bad data

Value saved: 4 hours/week × $100/hour × 52 weeks = $20,800/year
ROI: 346x time invested
```

---

## Related Skills

- **pipeline-forecasting.md** - Clean data = accurate forecasts
- **revenue-analytics.md** - Dashboards require clean data
- **sales-marketing-alignment.md** - Data standards enable handoffs
- **process-automation.md** - Automation needs quality data

## Related Frameworks

- **Revenue Waterfall** - Track stage conversions accurately
- **GTM Efficiency** - Calculate metrics with confidence
