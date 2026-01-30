# Sales Skills Index

Quick reference guide for AI assistant to match user requests to the right skill.

## Skill Catalog

### 1. Cold Outreach (`cold-outreach/SKILL.md`)
**Use when:** Writing cold emails, LinkedIn messages, first-touch outreach, follow-up sequences

**Trigger phrases:**
- "write a cold email"
- "draft LinkedIn message"
- "create outreach sequence"
- "prospect outreach"
- "first touch message"

**What it contains:**
- SPARK framework (Subject, Problem, Action, Result, Keep-it-simple)
- Email templates (7 variations)
- LinkedIn scripts
- Subject line formulas
- Follow-up cadences

---

### 2. Discovery Calls (`discovery-calls/SKILL.md`)
**Use when:** Preparing for sales calls, creating call scripts, qualifying prospects, post-call follow-up

**Trigger phrases:**
- "prepare for discovery call"
- "sales call preparation"
- "what questions should I ask"
- "qualify this prospect"
- "call script"

**What it contains:**
- PREP framework (Purpose, Research, Evidence, Plan)
- Call flow structure
- Question banks by buyer persona
- MEDDICC & BANT scorecards
- Note-taking templates
- Post-call recap format

---

### 3. Objection Handling (`objection-handling/SKILL.md`)
**Use when:** Responding to prospect pushback, handling budget/timing objections, overcoming resistance

**Trigger phrases:**
- "they said [objection]"
- "how do I respond to"
- "handle objection"
- "prospect pushback"
- "overcome resistance"

**What it contains:**
- LACE framework (Listen, Acknowledge, Clarify, Educate)
- Common objection library with responses
- Email & call scripts
- Empathy statements
- Proof points by objection type

---

### 4. Lead Qualification (`lead-qualification/SKILL.md`)
**Use when:** Scoring leads, prioritizing prospects, determining ICP fit, routing decisions

**Trigger phrases:**
- "qualify this lead"
- "is this a good fit"
- "score this prospect"
- "should I pursue"
- "prioritize leads"

**What it contains:**
- FITS model (Firmographics, Intent, Timing, Solution-match)
- Scoring criteria & thresholds
- Qualification questions
- ICP fit checklist
- Routing decision tree

---

### 5. Social Selling (`social-selling/SKILL.md`)
**Use when:** LinkedIn prospecting, social engagement, building relationships, warming up cold prospects

**Trigger phrases:**
- "LinkedIn strategy"
- "social selling approach"
- "engage on LinkedIn"
- "warm up prospect"
- "social touchpoints"

**What it contains:**
- Engagement ladder (monitor → engage → DM → convert)
- LinkedIn DM scripts
- Comment & engagement tactics
- Signal tracking (job changes, posts, events)
- Weekly activity planner

---

### 6. Value Propositions (`value-propositions/SKILL.md`)
**Use when:** Creating proposals, writing ROI narratives, building business cases, executive presentations

**Trigger phrases:**
- "write a proposal"
- "create business case"
- "ROI story"
- "value narrative"
- "executive presentation"

**What it contains:**
- Value story framework
- ROI calculation templates
- Executive one-pager format
- Proof layering structure
- Decision ask templates

---

### 7. Follow-up Sequences (`follow-up-sequences/SKILL.md`)
**Use when:** Planning multi-touch cadences, nurturing cold prospects, re-engaging stalled deals

**Trigger phrases:**
- "follow-up sequence"
- "nurture cadence"
- "multi-touch strategy"
- "re-engage prospect"
- "haven't heard back"

**What it contains:**
- 3-7-14 day cadence framework
- Multi-channel coordination (email + LinkedIn + call)
- Breakup email templates
- Value-add touch examples
- Timing & frequency guidelines

---

## How to Use This Index

**For the AI Assistant:**
1. When user asks for sales help, scan trigger phrases above
2. Silently reference the matched skill file
3. Apply the framework conversationally (don't mention reading files)
4. Generate output using templates
5. Offer related skills as next steps

**Example:**
```
User: "I need to write a cold email to a VP of Sales"
Assistant: [Reads cold-outreach.md] → Applies SPARK → Generates email
```

**Cross-References:**
- Cold Outreach → Social Selling (multi-channel)
- Discovery Calls → Lead Qualification (scoring)
- Objection Handling → Value Propositions (ROI proof)
- Follow-up Sequences → Cold Outreach (templates)


---



---

## Cross-Toolkit References

**When user needs go beyond sales:**

**→ Marketing Toolkit** (`marketing-toolkit/skills/`)
- User asks about: "generate leads", "marketing campaigns", "content marketing", "SEO"
- Skills: ad-copywriting, email-marketing, landing-page-copy, lead-magnets, seo-blog-writing
- Use Case: Sales needs leads → Marketing generates them

**→ Customer Success Toolkit** (`customer-success-toolkit/skills/`)
- User asks about: "onboarding", "customer health", "retention", "upselling post-sale"
- Skills: onboarding, customer-health-scoring, upselling-expansion, retention-strategies
- Use Case: Sales closes → CS onboards and expands

**→ Revenue Operations Toolkit** (`revenue-operations-toolkit/skills/`)
- User asks about: "sales forecasting", "pipeline management", "CRM hygiene", "sales ops"
- Skills: pipeline-forecasting, crm-hygiene, sales-marketing-alignment, revenue-analytics
- Use Case: Sales executes → RevOps optimizes process

**→ Content Toolkit** (`content-toolkit/skills/`)
- User asks about: "sales enablement content", "case studies", "demo videos"
- Skills: storytelling, video-marketing, webinars, content-repurposing
- Use Case: Sales needs content → Content creates sales assets

**→ Growth Toolkit** (`growth-toolkit/skills/`)
- User asks about: "product-led sales", "freemium conversion", "self-serve funnel"
- Skills: product-led-growth, user-onboarding, growth-analytics
- Use Case: Traditional sales → PLG motion

**→ Strategic Research Toolkit** (`strategic-research-toolkit/skills/`)
- User asks about: "ICP definition", "market sizing", "competitive intelligence"
- Skills: market-research, competitive-intelligence, customer-discovery
- Use Case: Sales strategy → Research informs targeting


---

## Document Skills

### DOCX - Word Documents (docx/SKILL.md)
**Purpose:** Create, edit, and analyze Word documents (.docx) with support for tracked changes, comments, and complex formatting.

**Key capabilities:**
- Create new Word documents from scratch using JavaScript/TypeScript
- Edit existing documents with tracked changes (redlining)
- Extract and analyze document content
- Handle comments, formatting, and embedded media
- Professional document review workflows

**When to use:**
- Creating reports, proposals, and professional documents
- Reviewing and editing documents with tracked changes
- Converting documents between formats
- Extracting content for analysis

**Tools:** docx-js, pandoc, Python OOXML library

---

### PDF - PDF Forms (pdf/SKILL.md)
**Purpose:** Work with PDF forms, extract data, fill fields, and convert PDFs to images.

**Key capabilities:**
- Extract form field information from PDFs
- Fill PDF forms programmatically
- Convert PDFs to images for visual analysis
- Check and validate form fields
- Handle fillable PDF documents

**When to use:**
- Processing PDF forms automatically
- Extracting data from PDF documents
- Creating visual representations of PDFs
- Validating PDF form structure

**Tools:** Python PDF libraries, pdftoppm, form processing scripts

---

### PPTX - PowerPoint Presentations (pptx/SKILL.md)
**Purpose:** Create, edit, and analyze PowerPoint presentations (.pptx) with professional layouts and formatting.

**Key capabilities:**
- Create new presentations from scratch
- Edit existing presentations
- Extract and analyze slide content
- Handle complex layouts, charts, and images
- Apply professional themes and formatting

**When to use:**
- Creating pitch decks and business presentations
- Automating slide generation
- Extracting content from presentations
- Updating presentations at scale

**Tools:** python-pptx, OOXML scripts, HTML to PPTX conversion

---

### XLSX - Excel Spreadsheets (xlsx/SKILL.md)
**Purpose:** Create, manipulate, and analyze Excel spreadsheets (.xlsx) with formulas, formatting, and data validation.

**Key capabilities:**
- Create complex Excel workbooks with multiple sheets
- Write formulas and data validation rules
- Apply formatting and styling
- Handle large datasets efficiently
- Generate financial models and reports

**When to use:**
- Creating financial models and reports
- Building data analysis tools
- Automating spreadsheet generation
- Processing and transforming data

**Tools:** openpyxl, pandas, Excel formula libraries

---