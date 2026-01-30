# Revenue Operations Skills Index

Quick reference guide for AI assistant to match user requests to the right skill.

## Skill Catalog

### 1. Pipeline Forecasting (`pipeline-forecasting/SKILL.md`)
**Use when:** Building revenue forecasts, managing pipeline, tracking deal health, analyzing win rates

**Trigger phrases:**
- "forecast revenue"
- "pipeline management"
- "predict sales"
- "track deals"
- "win rate analysis"
- "pipeline coverage"
- "sales velocity"
- "forecast accuracy"

**What it contains:**
- Revenue forecasting models (Weighted, Deal-by-Deal, Stage-based)
- Pipeline coverage calculations
- Win rate analysis frameworks
- Sales velocity metrics
- Pipeline health diagnostics
- Forecast accuracy tracking

---

### 2. Attribution & ROI (`attribution-roi/SKILL.md`)
**Use when:** Measuring marketing performance, calculating CAC/LTV, proving marketing value

**Trigger phrases:**
- "marketing ROI"
- "attribution model"
- "CAC calculation"
- "LTV calculation"
- "channel performance"
- "campaign ROI"
- "track conversions"
- "prove marketing value"

**What it contains:**
- Multi-touch attribution models (First-Touch, Last-Touch, Linear, U-Shaped, Time-Decay)
- CAC and LTV calculators
- Channel performance frameworks
- UTM tracking strategies
- ROI measurement playbooks
- Marketing dashboard templates

---

### 3. Revenue Analytics (`revenue-analytics/SKILL.md`)
**Use when:** Building dashboards, tracking KPIs, analyzing revenue metrics, creating executive reports

**Trigger phrases:**
- "build dashboard"
- "track KPIs"
- "revenue metrics"
- "MRR and ARR"
- "churn analysis"
- "cohort analysis"
- "executive reporting"
- "performance tracking"

**What it contains:**
- SaaS metrics framework (MRR, ARR, NRR, GRR)
- Cohort analysis templates
- Dashboard design best practices
- Executive reporting formats
- North Star metric selection
- Funnel analytics

---

### 4. CRM Hygiene (`crm-hygiene/SKILL.md`)
**Use when:** Setting up CRM, cleaning data, managing duplicates, standardizing fields

**Trigger phrases:**
- "clean CRM data"
- "CRM setup"
- "duplicate records"
- "data quality"
- "standardize fields"
- "CRM workflows"
- "data governance"
- "contact management"

**What it contains:**
- Data quality audit frameworks
- Duplicate detection and merging
- Field standardization guidelines
- CRM workflow optimization
- Data governance policies
- Automated cleanup scripts

---

### 5. Pricing & Packaging (`pricing-packaging/SKILL.md`)
**Use when:** Setting prices, designing product tiers, testing pricing, building value-based models

**Trigger phrases:**
- "pricing strategy"
- "package products"
- "pricing tiers"
- "test pricing"
- "value-based pricing"
- "pricing objections"
- "monetization strategy"
- "ROI calculator"

**What it contains:**
- Pricing strategy frameworks (Cost-Plus, Competitor-Based, Value-Based)
- Product packaging models (Good-Better-Best)
- Price testing methodologies
- Pricing psychology tactics
- ROI calculator templates
- Objection handling playbooks

---

### 6. Sales-Marketing Alignment (`sales-marketing-alignment/SKILL.md`)
**Use when:** Defining MQL/SQL, creating lead handoff process, building scoring models, establishing SLAs

**Trigger phrases:**
- "MQL definition"
- "SQL criteria"
- "lead handoff"
- "sales and marketing alignment"
- "lead scoring"
- "conversion tracking"
- "SLA definition"
- "feedback loops"

**What it contains:**
- MQL/SQL definition frameworks
- Lead scoring models
- SLA templates
- Lead handoff workflows
- Feedback loop processes
- Alignment meeting agendas

---

### 7. Process Automation (`process-automation/SKILL.md`)
**Use when:** Automating workflows, setting up integrations, building CRM automation, enriching data

**Trigger phrases:**
- "automate workflows"
- "CRM automation"
- "Zapier integration"
- "data enrichment"
- "email automation"
- "task automation"
- "workflow builder"
- "integration setup"

**What it contains:**
- Workflow automation playbooks
- CRM automation templates
- Integration guides (Zapier, Make, native)
- Data enrichment strategies
- Email trigger workflows
- ROI calculation for automation

---

## How to Use This Index

**For the AI Assistant:**
1. When user asks for RevOps help, scan trigger phrases above
2. Silently reference the matched skill file
3. Apply the framework conversationally (don't mention reading files)
4. Generate output using templates and calculators
5. Offer related skills as next steps

**Example:**
```
User: "I need to forecast Q2 revenue"
Assistant: [Reads pipeline-forecasting.md] → Applies forecasting models → Generates forecast template
```

**Cross-References:**
- Pipeline Forecasting → Revenue Analytics (forecast insights → dashboards)
- Attribution & ROI → Revenue Analytics (channel ROI → revenue dashboards)
- CRM Hygiene → Pipeline Forecasting (clean data → accurate forecasts)
- Pricing & Packaging → Revenue Analytics (pricing impact → revenue metrics)
- Sales-Marketing Alignment → Attribution & ROI (lead definitions → ROI tracking)
- Process Automation → All skills (automate workflows across all areas)

---



---



---

## Cross-Toolkit References

**When user needs go beyond revenue operations:**

**→ Sales Toolkit** (`sales-toolkit/skills/`)
- User asks about: "sales process", "deal management", "sales coaching", "quota attainment"
- Skills: discovery-calls, objection-handling, value-propositions, lead-qualification
- Use Case: RevOps builds process → Sales executes it

**→ Marketing Toolkit** (`marketing-toolkit/skills/`)
- User asks about: "lead generation", "campaign optimization", "marketing campaigns"
- Skills: ad-copywriting, email-marketing, landing-page-copy, marketing-analytics
- Use Case: RevOps tracks attribution → Marketing optimizes campaigns

**→ Customer Success Toolkit** (`customer-success-toolkit/skills/`)
- User asks about: "customer retention", "NRR optimization", "churn reduction"
- Skills: churn-prevention, retention-strategies, customer-health-scoring, onboarding
- Use Case: RevOps forecasts renewals → CS drives retention

**→ Content Toolkit** (`content-toolkit/skills/`)
- User asks about: "content ROI", "content analytics", "content performance"
- Skills: content-analytics, content-distribution, storytelling
- Use Case: RevOps measures content impact → Content optimizes strategy

**→ Growth Toolkit** (`growth-toolkit/skills/`)
- User asks about: "experimentation", "growth metrics", "funnel optimization"
- Skills: experiment-design, growth-analytics, product-led-growth
- Use Case: RevOps tracks metrics → Growth runs experiments

**→ Strategic Research Toolkit** (`strategic-research-toolkit/skills/`)
- User asks about: "market analysis", "competitive positioning", "pricing research"
- Skills: market-research, competitive-intelligence, strategic-analysis
- Use Case: RevOps sets pricing → Research validates market position

## Framework Cross-Reference

**AAARRR (Pirate Metrics)** → Use with attribution-roi, revenue-analytics
- Acquisition → Activation → Retention → Revenue → Referral

**Revenue Waterfall** → Use with pipeline-forecasting, sales-marketing-alignment
- Leads → MQLs → SQLs → Opportunities → Closed Won

**Unit Economics** → Use with attribution-roi, pricing-packaging
- CAC, LTV, Payback Period, LTV:CAC ratio

**GTM Efficiency** → Use with attribution-roi, revenue-analytics
- Magic Number, CAC Ratio, Rule of 40, Net Dollar Retention


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