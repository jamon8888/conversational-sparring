# Complete Guide

> For execution instructions, see [SKILL.md](../SKILL.md)

# User Onboarding Optimization

## Overview

The first mile of your product experience determines whether users stay or churn. This skill teaches you how to design, optimize, and scale user onboarding that gets customers to their "aha moment" fast – turning signups into activated, retained users.

**The Onboarding Impact:**
```
Bad Onboarding:
100 signups → 20 activated (20%) → 10 retained (10% overall)
→ 90% of signups wasted

Good Onboarding:
100 signups → 70 activated (70%) → 56 retained (56% overall)
→ 5.6x more customers from same signups

Value unlocked: Same traffic, 5.6x more customers
Investment: 40 hours to redesign onboarding
ROI: $50K+ ARR improvement (at $100/month ARPU)
```

---

## When to Use This Skill

- Signup-to-activation rate is low (<40%)
- Month 1 retention is poor (<60%)
- Users sign up but never complete setup
- Time-to-value (TTV) is too long (>7 days)
- Support overwhelmed with "how do I…?" questions
- You're launching a self-serve/PLG product

**Warning signs:**
- High signup volume, low activation
- Users abandon during onboarding (analytics show 50%+ drop-off)
- Customers say "I signed up but never really used it"

---

## Why Onboarding Matters

**The Activation Cliff:**
```
User Journey:
Signup → Onboarding → Activation → Retention

Without good onboarding:
100 signups → 20 activate → 16 retain (16% retention)

With optimized onboarding:
100 signups → 70 activate → 56 retain (56% retention)

Difference: 3.5x more retained customers

Why?
- Activation predicts retention (activated users stay)
- Time-to-value predicts activation (fast value = more activation)
- Onboarding determines time-to-value

Therefore: Onboarding → Activation → Retention → Revenue
```

**Retention by Activation Status:**
```
Research across 1,000+ SaaS companies:

Users who activate:
- Month 1 retention: 80%
- Month 12 retention: 60%

Users who don't activate:
- Month 1 retention: 15%
- Month 12 retention: <5%

Activation = 5x better long-term retention
```

---

## The "Aha Moment" Framework

### Defining Your Aha Moment

**What is an Aha Moment?**
```
Definition: The moment when a user first experiences the core value of your product

Not:
- Completing tutorial
- Seeing a demo
- Reading documentation

But:
- Achieving a real outcome
- Solving a real problem
- Experiencing tangible value

Examples:
- Slack: Sent 2,000 team messages (experienced team communication)
- Dropbox: Saved first file (experienced file sync)
- Asana: Completed first task (experienced task management)
- Superhuman: Achieved inbox zero (experienced email speed)
```

**Finding Your Aha Moment:**
```
Step 1: Hypothesize candidate moments
What actions correlate with retention?

Example: Email Marketing Tool
Candidates:
- Sent first email campaign
- Added ≥100 subscribers
- Created first automation
- Integrated with website

Step 2: Analyze retention by action
Run cohort analysis:

Action               | % Who Do It | M1 Retention | M6 Retention
---------------------|-------------|--------------|-------------
Sent campaign        | 60%         | 75%          | 55%
Added ≥100 subs      | 40%         | 85%          | 70% ← WINNER
Created automation   | 25%         | 90%          | 75%
Integrated website   | 15%         | 80%          | 65%

Step 3: Choose based on:
□ High retention correlation (≥80% M1 retention)
□ Achievable by most users (≥30% complete it)
□ Measurable and trackable

Winner: Added ≥100 subscribers
- 85% M1 retention (strong correlation)
- 40% complete it (achievable)
- Easy to track (count subscribers)

Step 4: Make this your activation metric
Activation = User added ≥100 subscribers within 7 days of signup
```

---

### Time-to-Value (TTV) Optimization

**The TTV Imperative:**
```
Time-to-Value = Time from signup to experiencing core value

Benchmark by Product Complexity:
- Simple SaaS (e.g., link shortener): <5 minutes
- Medium SaaS (e.g., email tool): <1 hour
- Complex SaaS (e.g., analytics): <24 hours
- Enterprise SaaS (e.g., ERP): <7 days

Your target: Reduce TTV by 50%

Example:
Current TTV: 3 days (signup → first campaign sent)
Target TTV: 1.5 days
Impact: 2x activation rate (more users reach aha moment faster)
```

**Calculating TTV:**
```
Formula:
TTV = Median time from signup to [aha moment]

Example Data (Email Tool):
User A: Signup → Sent campaign in 2 hours
User B: Signup → Sent campaign in 1 day
User C: Signup → Sent campaign in 3 days
User D: Signup → Sent campaign in 7 days
User E: Never sent campaign

TTV calculation:
Exclude User E (never activated)
Median of [2h, 1d, 3d, 7d] = 2 days

Your TTV: 2 days
```

**Reducing TTV:**
```
Tactics to reduce time-to-value:

1. Pre-populate data (don't make them start from scratch)
   Before: Empty email list → user must import 100+ subscribers → 3 days
   After: Sample list included → user can send campaign immediately → 10 minutes
   Impact: 3 days → 10 min TTV

2. Progressive disclosure (don't show everything at once)
   Before: 20-step setup wizard → 30 minutes to complete → 60% abandon
   After: 3-step wizard → 5 minutes → 90% complete
   Impact: 1.5x more activations

3. Defaults over decisions (reduce cognitive load)
   Before: "Choose template, colors, fonts, layout…" → decision paralysis
   After: Smart default applied → user can customize later
   Impact: 2x faster completion

4. Defer non-critical setup (get to value first)
   Before: Setup integrations → configure settings → invite team → send campaign
   After: Send campaign first → optional setup later
   Impact: Value in 5 min vs. 30 min
```

---

## Onboarding Flow Design

### The Welcome Flow Framework

**Flow Structure (3 Acts):**
```
Act 1: ORIENT (30 seconds)
→ "What is this product? What can I do here?"

Act 2: ACTIVATE (5-15 minutes)
→ "Get user to aha moment as fast as possible"

Act 3: EXPAND (ongoing)
→ "Discover additional features, invite team, upgrade"

Most products fail by reversing the order:
❌ Wrong: Features tour (Act 3) → Setup (Act 2) → Hope they find value (Act 1)
✓ Right: Show value (Act 2) → Orient (Act 1) → Expand (Act 3)

Always lead with value, not features.
```

---

### Act 1: ORIENT (The Welcome Screen)

**Goal:** Help user understand what they can do in <30 seconds

**Template:**
```
┌─────────────────────────────────────────────────────┐
│  Welcome to [Product Name]!                         │
│                                                     │
│  [Value Prop in 8 words or less]                   │
│  "Send beautiful email campaigns in minutes"        │
│                                                     │
│  Let's get you set up:                              │
│  ☐ Import your email list (5 min)                  │
│  ☐ Design your first campaign (10 min)              │
│  ☐ Send to subscribers (instant)                    │
│                                                     │
│  [Get Started] ──────────────────────────────►      │
│                                                     │
│  ┌────────────────────────────────────────────┐    │
│  │ 💡 Tip: Start with our sample list to      │    │
│  │    send a campaign in under 2 minutes      │    │
│  └────────────────────────────────────────────┘    │
└─────────────────────────────────────────────────────┘

Elements:
1. Value prop (8 words): What outcome do I get?
2. Checklist (3 steps): What do I need to do?
3. Time estimate: How long will this take?
4. CTA: Single, clear next action
5. Shortcut: Fast path to value (sample data)
```

**Best Practices:**
```
✓ One primary CTA (not 5 buttons)
✓ Show progress (3 steps, 5 min each)
✓ Offer shortcut (sample data, template)
✗ Feature tour (save for later)
✗ Video tutorials (99% skip)
✗ "Read our docs" (sends wrong message)
```

---

### Act 2: ACTIVATE (The Aha Moment Flow)

**Goal:** Get user to aha moment in <15 minutes

**Onboarding Flow Types:**

**1. Guided Setup (Wizard)**
```
Best for: Multi-step setup (requires data import, configuration)

Example: Email Marketing Tool

Step 1/3: Import Email List
┌─────────────────────────────────────────────┐
│ Upload CSV  or  Connect Gmail  or  Sample   │
│ [Upload]         [Connect]        [Use Demo]│
└─────────────────────────────────────────────┘

Step 2/3: Choose Template
┌────────────┬────────────┬────────────┐
│ Newsletter │ Promotion  │ Announcement│
│    [Use]   │   [Use]    │    [Use]    │
└────────────┴────────────┴────────────┘

Step 3/3: Send Campaign
┌─────────────────────────────────────────────┐
│ Subject: Welcome to our community!          │
│ Preview: "Thanks for subscribing! Here's…"  │
│                                              │
│ [Send Now] or [Schedule]                     │
└─────────────────────────────────────────────┘

✓ Campaign sent! Check your inbox.

Progress: ▓▓▓▓▓▓▓▓▓▓ 100% Complete

Key elements:
- Linear progression (1 → 2 → 3)
- Progress indicator (know where you are)
- Defaults provided (template, subject line)
- Shortcuts available (sample data)
- Instant gratification (send email, see result)
```

**2. Empty State (Show, Don't Tell)**
```
Best for: Simple products (low setup friction)

Example: Task Management Tool

Empty Dashboard:
┌─────────────────────────────────────────────┐
│  No tasks yet. Add your first task!         │
│                                             │
│  [+ Add Task] ─────────────────►            │
│                                             │
│  💡 Try: "Design onboarding flow"          │
└─────────────────────────────────────────────┘

After adding first task:
┌─────────────────────────────────────────────┐
│  ☐ Design onboarding flow                   │
│  [+ Add Another Task]                       │
│                                             │
│  🎉 Nice! Now invite your team:            │
│  [Invite Team] ─────────────────►           │
└─────────────────────────────────────────────┘

Key elements:
- Zero setup (start using immediately)
- Contextual prompts (guide next action)
- Positive reinforcement (celebrate wins)
- Progressive disclosure (introduce features as needed)
```

**3. Personalized Setup (Role-Based)**
```
Best for: Products with multiple use cases

Example: Analytics Tool

Step 1: What's your goal?
┌───────────────┬───────────────┬───────────────┐
│ Track website │ Measure email │ Analyze sales │
│   traffic     │   campaigns   │   funnel      │
│   [Select]    │   [Select]    │   [Select]    │
└───────────────┴───────────────┴───────────────┘

User selects "Track website traffic"

Step 2: Connect your website
┌─────────────────────────────────────────────┐
│ Add this code to your website:              │
│ <script>… tracking code …</script>          │
│                                             │
│ Or install via:                             │
│ [WordPress Plugin] [Shopify App] [GTM]      │
└─────────────────────────────────────────────┘

Step 3: See your first data
┌─────────────────────────────────────────────┐
│ ✓ Tracking active! Here's your dashboard:   │
│                                             │
│ Visitors today: 47                          │
│ Top pages: /home, /pricing, /features       │
│                                             │
│ [View Full Dashboard]                        │
└─────────────────────────────────────────────┘

Key elements:
- Customized to user goal (not generic)
- Filtered features (show only relevant options)
- Faster time-to-value (skip irrelevant setup)
```

---

### Progress Indicators & Motivation

**The Progress Bar Effect:**
```
Psychological principle: People hate incomplete progress

Without progress bar:
- Users don't know how long setup takes
- Abandon at 50% (no idea they're halfway)

With progress bar:
- Users see "2 of 3 steps done"
- Complete remaining step (don't want to waste effort)
- 2x higher completion rate

Example:
Profile Setup: ▓▓▓▓▓▓▓▓▓░ 90% Complete
→ "Just one more step!" (high completion rate)

vs.

Profile Setup: ▓▓░░░░░░░░ 20% Complete
→ "This will take forever" (high abandon rate)
```

**Gamification & Celebration:**
```
Celebrate micro-wins to build momentum:

After each step:
✓ Email list imported! 🎉
✓ Campaign designed! 🚀
✓ First email sent! 💌

Impact:
- Dopamine hit (feels good)
- Positive reinforcement (keep going)
- Sense of progress (building towards goal)

Avoid:
❌ Generic "Success!" (boring)
❌ No feedback (did anything happen?)
❌ Only celebrate at end (no momentum)
```

---

## Act 3: EXPAND (Feature Discovery)

### Progressive Feature Introduction

**Don't Show Everything at Once:**
```
Bad approach (feature overload):
Day 1: Show all 50 features in sidebar
→ User overwhelmed, ignores 95% of features

Good approach (progressive disclosure):
Day 1: Show 5 core features (email, contacts, campaigns)
Day 7: Unlock automation (after sending 3 campaigns)
Day 14: Unlock A/B testing (after 10 campaigns)
Day 30: Unlock advanced reporting (after first month)

Result:
- Less overwhelm (focus on essentials first)
- Contextual discovery (introduce when relevant)
- Higher adoption (features appear when needed)
```

**Feature Adoption Ladder:**
```
Tier 1 (Core - 100% adopt):
- Send email campaign
- Add contacts
- View stats

Tier 2 (Power - 50% adopt):
- Email automation
- Segmentation
- A/B testing

Tier 3 (Advanced - 10% adopt):
- Custom fields
- API access
- Advanced reports

Introduce features as users climb the ladder:
- Don't show Tier 3 to Tier 1 users (not ready)
- Unlock Tier 2 after mastering Tier 1
- Gate advanced features behind usage milestones
```

---

### Onboarding Email Sequences

**Purpose:**
- Reinforce product value
- Guide users to next actions
- Prevent abandonment

**Email 1: Welcome (Immediate)**
```
Subject: Welcome to [Product]! Here's what to do first 👋

Hi [Name],

Thanks for signing up!

Here's your quick-start guide:

1️⃣ Import your email list (5 min)
   → [Upload CSV] or connect [Gmail/Mailchimp]

2️⃣ Send your first campaign (10 min)
   → Use our templates or design from scratch

3️⃣ Track your results (instant)
   → See opens, clicks, and conversions in real-time

[Get Started →]

Need help? Reply to this email (I read every one!)

Cheers,
[Founder Name]
P.S. Pro tip: Use our sample list to send a test campaign in under 2 minutes

Timing: Send immediately after signup
Goal: Get user to take first action (import list)
```

**Email 2: Nudge (Day 2, if not activated)**
```
Subject: Quick question about [Product]

Hi [Name],

I noticed you signed up for [Product] but haven't sent a campaign yet.

Everything okay? Stuck on anything?

Common blockers:
- Don't have email list ready → [Use sample list]
- Not sure what to send → [Browse templates]
- Need help setting up → [Book 15-min call]

Whatever it is, I'm here to help. Just reply to this email!

Cheers,
[Founder Name]

Timing: Day 2 (only if user hasn't activated)
Goal: Identify and remove blockers
```

**Email 3: Value Reinforcement (Day 7)**
```
Subject: 3 quick wins for [Product] users

Hi [Name],

You've sent your first campaign – nice! 🎉

Here's how to get even more value:

1. Automate welcome emails (save 10 hours/month)
   → [Set up automation]

2. Segment your list (2x your open rates)
   → [Create segments]

3. A/B test subject lines (increase clicks by 25%)
   → [Start A/B test]

Each takes <15 minutes. Pick one to try today!

Cheers,
[Founder Name]

Timing: Day 7 (for activated users)
Goal: Drive feature adoption (Tier 2 features)
```

**Email 4: Case Study (Day 14)**
```
Subject: How [Customer] grew their list 10x with [Product]

Hi [Name],

I thought you'd like this:

[Customer], a company just like yours, used [Product] to grow their email list from 500 → 5,000 subscribers in 3 months.

Here's how they did it:
- Ran weekly lead magnets
- Automated welcome sequence
- Segmented by interest

[Read full case study →]

Want similar results? I can help you set this up.

Cheers,
[Founder Name]

Timing: Day 14
Goal: Inspire with social proof, show ROI
```

**Email 5: Upgrade Prompt (Day 30, for free users)**
```
Subject: Ready to unlock [Premium Feature]?

Hi [Name],

You've been using [Product] for a month – congrats! 🎉

You've sent 15 campaigns and grown your list to 1,200 subscribers. Awesome progress.

Ready to unlock:
✓ Automation (save 10 hours/month)
✓ Advanced segmentation (2x engagement)
✓ Priority support (get help in <2 hours)

[Upgrade to Pro ($49/month) →]

Or stick with the free plan – it's yours forever, no pressure!

Cheers,
[Founder Name]

Timing: Day 30 (for engaged free users)
Goal: Convert to paid (with value-based pitch)
```

---

## In-App Messaging & Tooltips

### When to Use In-App Messages

**Good use cases:**
- Announce new feature (after user completes related action)
- Guide to next step (after completing onboarding step)
- Celebrate milestone (sent 10th campaign)
- Offer help (user stuck on a step for >5 minutes)

**Bad use cases:**
- Generic announcements (not personalized)
- Constant interruptions (every page load)
- Sales pitches (upgrade now!)

---

### Tooltip Design

**Types of Tooltips:**

**1. Feature Callout**
```
┌────────────────────────────────────┐
│ 💡 New Feature: Automation         │
│                                    │
│ Automate your email sequences      │
│ and save 10 hours/month.           │
│                                    │
│ [Try It Now]  [Dismiss]            │
└────────────────────────────────────┘
   ↓
[Automation Button]

When to show: After user sends 5+ campaigns (ready for automation)
Dismissible: Yes (don't force it)
```

**2. Contextual Help**
```
    [Segmentation (?)] ← Hover shows tooltip
         ↓
┌────────────────────────────────────┐
│ Segmentation: Group subscribers    │
│ by interests, behavior, or tags    │
│ to send targeted campaigns.        │
│                                    │
│ Example: "VIP Customers" segment   │
└────────────────────────────────────┘

When to show: On hover (not intrusive)
Always available: Yes (persistent help)
```

**3. Progressive Disclosure**
```
Step 1: User creates first email
   ↓
Tooltip appears: "💡 Want to schedule this for later? Click [Schedule]"

Step 2: User schedules email
   ↓
Tooltip appears: "🎉 Scheduled! Want to set up recurring sends? Click [Automate]"

Pattern: Introduce advanced features AFTER mastering basics
```

---

## Onboarding Metrics & Optimization

### Key Onboarding Metrics

**1. Activation Rate**
```
Formula: (Users who reach aha moment) / (Total signups)

Example:
100 signups → 45 sent first campaign = 45% activation rate

Benchmark:
- Good: 40-60%
- Great: 60-80%
- Excellent: 80%+

Calculation period: Within 7 days of signup
```

**2. Time-to-Value (TTV)**
```
Formula: Median time from signup to aha moment

Example:
User A: 2 hours
User B: 1 day
User C: 3 days
User D: 7 days

Median TTV: 2 days

Benchmark:
- Simple product: <5 min
- Medium product: <1 hour
- Complex product: <24 hours
```

**3. Onboarding Completion Rate**
```
Formula: (Users who complete setup) / (Users who start setup)

Example:
100 users start onboarding → 70 complete = 70% completion

Benchmark: 70-90% (if lower, flow is too long/complex)
```

**4. Step Drop-Off Analysis**
```
Track where users abandon:

Step 1 (Import list): 100 users → 80 complete (80%)
Step 2 (Design email): 80 users → 60 complete (75%)
Step 3 (Send campaign): 60 users → 45 complete (75%)

Overall: 100 → 45 = 45% activation

Bottleneck: Step 1 (20% drop-off)
Action: Simplify list import (add sample data option)
```

---

### Onboarding A/B Tests

**What to Test:**

**1. Flow Length**
- Variant A: 5-step wizard
- Variant B: 3-step wizard (defer non-critical steps)
- Hypothesis: Shorter flow = higher completion

**2. Defaults vs. Customization**
- Variant A: User chooses template, colors, fonts
- Variant B: Smart defaults applied, user can customize later
- Hypothesis: Defaults reduce decision fatigue

**3. Sample Data**
- Variant A: Empty state (user must import list)
- Variant B: Sample list pre-loaded (user can send immediately)
- Hypothesis: Sample data reduces TTV, increases activation

**4. Email Timing**
- Variant A: Send nudge email on Day 1 (if not activated)
- Variant B: Send nudge email on Day 3
- Hypothesis: Day 3 gives more time to activate organically

---

## Common Onboarding Mistakes

### ❌ Mistake #1: Feature Tour Overload

**Problem:** 10-minute product tour on Day 1
**Result:** 90% skip, learn nothing

**Fix:** Skip the tour. Use:
- Empty states (show value, not features)
- Contextual tooltips (when user encounters feature)
- Optional product tour (for those who want it)

---

### ❌ Mistake #2: Asking Too Many Questions

**Problem:** 20-field signup form
**Result:** 50% abandon before completing

**Fix:** Ask minimum:
- Email (required)
- Password (required)
- Everything else: Optional or defer to later

---

### ❌ Mistake #3: No Clear Next Action

**Problem:** Dashboard after signup with no guidance
**Result:** Users don't know what to do, leave

**Fix:** Clear CTA:
- "Add your first task"
- "Import your email list"
- "Connect your website"

---

## Onboarding Optimization Checklist

**Pre-Launch:**
- [ ] Define aha moment (what action predicts retention?)
- [ ] Measure current TTV (how long to reach aha moment?)
- [ ] Map onboarding flow (all steps from signup to aha moment)
- [ ] Identify bottlenecks (where do users drop off?)

**Flow Design:**
- [ ] Reduce signup friction (email + password only)
- [ ] Provide sample data (let users explore without setup)
- [ ] Use defaults (reduce decisions)
- [ ] Show progress (step 2 of 3)
- [ ] Celebrate wins (positive reinforcement)

**Post-Signup:**
- [ ] Send welcome email (immediate)
- [ ] Send nudge email (Day 2, if not activated)
- [ ] Send value email (Day 7, show wins)
- [ ] In-app messages (contextual, not intrusive)

**Measurement:**
- [ ] Track activation rate (weekly)
- [ ] Track TTV (weekly)
- [ ] Track step drop-offs (identify bottlenecks)
- [ ] Run A/B tests (optimize flow)

---

## Related Skills

- **product-led-growth.md** - Self-serve onboarding at scale
- **growth-analytics.md** - Measure activation metrics
- **experiment-design.md** - A/B test onboarding flows
- **viral-mechanics.md** - Onboarding for network-effect products

## Related Frameworks

- **AAARRR.md** - Activation in Pirate Metrics
- **PQL-Framework.md** - Product-qualified lead scoring
- **ICE-RICE.md** - Prioritize onboarding improvements
