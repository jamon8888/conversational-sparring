# Content Governance Complete Guide

## Overview

Content governance ensures quality, compliance, and brand consistency through structured approval workflows and automated checks. This guide covers workflow design, compliance requirements, and implementation best practices.

---

## Why Governance Matters

### The Problem

Without governance:
- **Brand inconsistency**: Different voices across team
- **Compliance risks**: GDPR violations, regulatory issues
- **Quality variability**: No quality gates
- **No accountability**: Who approved what, when?

### Enterprise Requirements

Large companies require governance for:
- **Regulatory compliance** (GDPR, CCPA, HIPAA, SOX)
- **Legal protection** (review before publication)
- **Brand protection** (maintain consistent voice)
- **Audit trails** (who did what, when, why)

---

## Approval Workflows

### Standard 4-Stage Workflow

```
Draft → Review → Approve → Publish
```

**Stage 1: Draft (Creator)**
- Creator writes content
- Self-review against brand guidelines
- Runs automated compliance checks
- Submits for review

**Stage 2: Review (Content Manager)**
- Quality check (brand voice, grammar, structure)
- SEO check (keywords, meta, links)
- Compliance pre-screening
- Decision: Approve | Request Changes | Reject

**Stage 3: Approve (Team Lead)**
- Strategic alignment check
- Final quality gate
- Risk assessment
- Decision: Publish | Hold | Reject

**Stage 4: Publish (Publisher)**
- Schedule across channels
- Final formatting
- Distribution coordination
- Mark as published in workflow

**SLA**: 2-3 business days total

---

### Expedited 2-Stage Workflow

```
Draft → Fast Review → Publish
```

**When to Use**:
- Breaking news response
- Timely social media posts
- Urgent announcements
- Hot takes on trends

**Criteria for Expedited**:
- Low compliance risk
- Experienced creator
- Pre-approved topic/format
- Manager available for same-day review

**SLA**: Same day (4-6 hours)

---

### Legal Review 5-Stage Workflow

```
Draft → Content Review → Legal Review → Executive Approval → Publish
```

**When Required**:
- Public company statements
- Financial information
- Regulatory content (healthcare, finance)
- Partnerships/contracts
- Sensitive topics (layoffs, incidents)

**Stage 3: Legal Review** (added):
- Regulatory compliance verification
- Risk assessment
- Language review for legal exposure
- Documentation requirements

**Stage 4: Executive Approval** (added):
- CMO, VP, or C-level sign-off
- Strategic alignment
- Risk acceptance
- Public statement coordination

**SLA**: 5-7 business days

---

## Compliance Checklists

### GDPR Compliance Checklist

**Before Publishing Content**:

- [ ] **Data Processing Mentions**: If describing data processing, include legal basis
- [ ] **Privacy Policy Links**: Any data collection must link to privacy policy
- [ ] **Cookie Consent**: Web content must have proper cookie consent UI
- [ ] **Right to Access**: Contact information for data subject requests
- [ ] **Data Minimization**: Only collect necessary personal data
- [ ] **Consent Language**: Clear, affirmative opt-in language (no pre-checked boxes)
- [ ] **Third-Party Disclosure**: List any third-party data sharing
- [ ] **Retention Policy**: State how long data is kept

**High-Risk Content** (requires legal review):
- Customer testimonials with personal data
- Case studies with company information
- Lead magnets collecting sensitive information

---

### CCPA Compliance Checklist

**California Residents** (if targeting US):

- [ ] **Privacy Notice**: Clear privacy policy accessible
- [ ] **Do Not Sell**: Option to opt-out of data selling
- [ ] **Categories of Data**: List what data is collected
- [ ] **Business Purpose**: Explain why data is collected
- [ ] **Third Parties**: Disclose who data is shared with
- [ ] **Consumer Rights**: Right to access, delete, opt-out

---

### Brand Compliance Checklist

**Voice & Tone**:
- [ ] Matches brand voice (professional, conversational, helpful)
- [ ] Appropriate tone for context (excited, empathetic, authoritative)
- [ ] Consistent terminology (use brand glossary)
- [ ] No off-brand language or slang

**Visual Consistency**:
- [ ] Brand colors used correctly
- [ ] Logo placement and sizing correct
- [ ] Typography follows brand guidelines
- [ ] Image style matches brand (photography, illustrations)

**Messaging**:
- [ ] Value proposition consistent
- [ ] Positioning aligned with brand
- [ ] Claims are substantiated
- [ ] No conflicting messages

---

### Industry-Specific Compliance

#### Healthcare (HIPAA)
- [ ] No patient information (PHI) disclosed without consent
- [ ] Health claims are substantiated
- [ ] FDA compliance for medical devices/drugs
- [ ] Proper disclaimers on medical advice

#### Financial Services (SOX, SEC)
- [ ] No forward-looking statements without disclaimers
- [ ] Financial data is accurate and auditable
- [ ] Investment advice includes proper disclosures
- [ ] Material information is not selectively disclosed

#### SaaS/Technology
- [ ] Security claims are accurate
- [ ] Uptime/performance claims substantiated
- [ ] Privacy and data handling accurate
- [ ] No misleading feature claims

---

## Audit Trail Format

### Required Information

```yaml
audit_entry:
  timestamp: "2024-11-30T14:30:00Z"
  actor: "mary@company.com"
  actor_role: "content-manager"
  action: "approved"
  resource: "blog-post-001"
  resource_type: "blog"
  stage: "review"
  decision: "approved"
  comments: "Good quality, SEO optimized, approved for publication"
  next_stage: "approval"
  next_approver: "john@company.com"
```

### Audit Trail Example

```csv
timestamp,actor,action,resource,stage,decision,comments
2024-11-30T10:00:00Z,sarah@co.com,created,blog-001,draft,submitted,Initial draft created
2024-11-30T14:30:00Z,mary@co.com,reviewed,blog-001,review,approved,Good quality approved
2024-11-30T16:00:00Z,john@co.com,approved,blog-001,approval,approved,Published authorized
2024-11-30T16:15:00Z,system,published,blog-001,publish,completed,Published to CMS
```

**Audit Trail Uses**:
- Compliance audits
- Process optimization
- Accountability
- Dispute resolution
- Performance tracking (approval times)

---

## Implementation Guide

### Step 1: Define Your Workflows (1 hour)

**Questions to answer**:
1. How many approval stages do you need? (2-5)
2. Who are the approvers at each stage?
3. What are the SLAs? (hours/days per stage)
4. What triggers legal review?
5. What can be expedited?

**Deliverable**: Workflow diagram with stages, roles, SLAs

---

### Step 2: Create Compliance Checklists (1 hour)

**Based on your needs**:
- Geography: GDPR (EU), CCPA (California), others
- Industry: Healthcare, Finance, Technology
- Brand: Your specific brand guidelines

**Deliverable**: Custom checklist templates

---

### Step 3: Set Up Audit Trail (30 minutes)

**Choose format**:
- CSV for simplicity
- YAML for structure
- JSON for integration

**Tool options**:
- Google Sheets (simple, shareable)
- Git commits (built-in version control)
- Notion database (rich formatting)

**Deliverable**: Audit log template and location

---

### Step 4: Train Team (2 hours)

**Training agenda**:
1. Why governance matters (15min)
2. Workflow walkthrough (30min)
3. How to use compliance checklists (30min)
4. Q&A and edge cases (45min)

**Deliverable**: Trained team, documented Q&A

---

### Step 5: Pilot (1 week)

**Test with**:
- 5-10 content pieces
- Different content types
- Different workflow paths

**Monitor**:
- Approval times
- Bottlenecks
- Confusion points
- Compliance issues

**Deliverable**: Optimized workflow based on pilot

---

## Role Definitions

### Creator
**Responsibilities**:
- Write/create content
- Self-review against guidelines
- Run automated checks
- Submit for review
- Incorporate feedback

**Permissions**: Create, edit own content

### Reviewer (Content Manager)
**Responsibilities**:
- Quality review
- Brand consistency check
- SEO optimization
- Compliance pre-screening
- Approve or request changes

**Permissions**: View all, edit, approve/reject

### Legal Reviewer
**Responsibilities**:
- Regulatory compliance verification
- Risk assessment
- Legal language review
- Approve or block

**Permissions**: View all, comment, approve/reject

### Executive Approver
**Responsibilities**:
- Strategic alignment
- Risk acceptance
- Final sign-off on high-stakes content

**Permissions**: View all, approve/reject

### Publisher
**Responsibilities**:
- Final formatting
- Schedule publication
- Cross-channel distribution
- Mark as published

**Permissions**: View approved, publish

---

## Tools & Templates

### Template 1: Standard Workflow YAML

```yaml
workflow:
  name: "Standard Content Approval"
  type: "standard"
  
  stages:
    - stage: "draft"
      approver_role: "creator"
      sla_hours: 48
      
    - stage: "review"
      approver_role: "content-manager"
      sla_hours: 24
      checks:
        - brand_voice
        - seo_compliance
        - grammar_spelling
      
    - stage: "approval"
      approver_role: "team-lead"
      sla_hours: 24
      checks:
        - strategic_alignment
        - risk_assessment
      
    - stage: "publish"
      approver_role: "publisher"
      sla_hours: 4
```

### Template 2: Compliance Checklist YAML

```yaml
compliance_checks:
  gdpr:
    - id: "gdpr-01"
      requirement: "Data processing mentions legal basis"
      severity: "critical"
      status: "not_checked"
      
    - id: "gdpr-02"
      requirement: "Privacy policy linked"
      severity: "critical"
      status: "not_checked"
  
  brand:
    - id: "brand-01"
      requirement: "Voice matches brand guidelines"
      severity: "high"
      status: "not_checked"
      
    - id: "brand-02"
      requirement: "Terminology from approved glossary"
      severity: "medium"
      status: "not_checked"
```

---

## Best Practices

### 1. Balance Speed and Quality

**Don't**: Make workflow so complex that nothing gets published  
**Do**: Match rigor to risk level

**Risk Levels**:
- **Low**: Social posts, blog posts → Standard workflow
- **Medium**: Ebooks, webinars → Standard with extra review
- **High**: Public statements, financial content → Legal review

### 2. Automate What You Can

**Automate**:
- Grammar and spelling checks
- SEO compliance
- Brand terminology validation
- Basic GDPR checks

**Human Review**:
- Strategic alignment
- Complex compliance issues
- Tone and nuance
- Risk assessment

### 3. Clear SLAs

**Example SLAs**:
- Draft submission: Creator's responsibility
- Review stage: 24 hours
- Approval stage: 24 hours
- Legal review: 48-72 hours
- Total cycle time: 3-5 days

**Escalation**: If SLA breached, auto-escalate to next level

### 4. Continuous Improvement

**Monthly Review**:
- Average approval time per stage
- Bottlenecks identified
- Rejection reasons analysis
- Process improvements

---

## Common Scenarios

### Scenario 1: Content Rejected at Review
**Action**: Reviewer provides specific feedback, returns to creator  
**Timeline**: Creator has 24h to revise and resubmit  
**Track**: Log rejection reason for pattern analysis

### Scenario 2: Legal Concern Discovered
**Action**: Immediately escalate to legal review workflow  
**Timeline**: Pauses standard SLA, legal review gets 48h  
**Communication**: Notify all stakeholders of delay

### Scenario 3: Urgent Publication Needed
**Action**: Use expedited workflow  
**Requirements**: Manager must be available for same-day review  
**Limitation**: Max 2 expedited requests per week per creator

---

## Audit Trail Requirements

**What to Log**:
- All state changes (draft → review, etc.)
- All approval decisions (approved, rejected, changes requested)
- All actors (who made decision)
- All timestamps (when decision made)
- All comments (why decision made)

**Retention**:
- Keep for 3 years (GDPR requirement)
- Archive older records
- Secure storage (access controlled)

---

## Next Steps

1. **Choose workflow type** for your team
2. **Customize compliance checklist** for your requirements
3. **Set up audit trail** (spreadsheet or tool)
4. **Pilot with 5-10 pieces** to refine process
5. **Train team** on new workflow
6. **Monitor and optimize** based on data

---

**Result**: Enterprise-grade content governance with compliance, quality control, and complete audit trails.
