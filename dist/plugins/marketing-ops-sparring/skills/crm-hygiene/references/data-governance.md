# Data Governance Framework

## Overview
Standards and processes for maintaining high-quality CRM data.

## Data Quality Dimensions

### 1. Accuracy
**Definition**: Data correctly represents reality

**Standards**:
- Email addresses validated
- Phone numbers formatted correctly
- Addresses complete and verified
- Company names standardized

**Validation Rules**:
```
Email: Must contain @ and valid domain
Phone: (XXX) XXX-XXXX format
Website: Must start with http:// or https://
```

### 2. Completeness
**Definition**: All required fields populated

**Required Fields by Object**:

**Contact**:
- First Name
- Last Name
- Email
- Company
- Title

**Company**:
- Company Name
- Industry
- Employee Count
- Revenue Range
- Website

**Deal**:
- Deal Name
- Amount
- Close Date
- Stage
- Owner

### 3. Consistency
**Definition**: Data formatted uniformly

**Standardization Rules**:
```
Company Names:
- "IBM" not "I.B.M." or "ibm"
- "Salesforce" not "SalesForce" or "SFDC"

Titles:
- "VP Sales" not "Vice President of Sales"
- "CEO" not "Chief Executive Officer"

Industries:
- "Software" not "Software/Technology" or "Tech"
```

### 4. Timeliness
**Definition**: Data is current and up-to-date

**Freshness Standards**:
- Contact info: Updated every 90 days
- Company info: Updated every 180 days
- Deal info: Updated weekly
- Activity logs: Real-time

### 5. Uniqueness
**Definition**: No duplicate records

**Deduplication Rules**:
```
Match Criteria:
- Email (exact match)
- Company + First Name + Last Name (fuzzy match)
- Phone (normalized match)

Merge Priority:
1. Most recently updated
2. Most complete record
3. Owned by active user
```

## Field Standardization

### Picklist Values

**Lead Status**:
```
- New
- Contacted
- Qualified
- Unqualified
- Converted
```

**Deal Stage**:
```
- Prospecting
- Qualification
- Needs Analysis
- Proposal
- Negotiation
- Closed Won
- Closed Lost
```

**Industry**:
```
- Software/SaaS
- Financial Services
- Healthcare
- Manufacturing
- Retail
- Professional Services
- Other
```

### Naming Conventions

**Deals**:
```
Format: [Company Name] - [Product] - [Close Month/Year]
Example: "Acme Corp - Enterprise Plan - Dec 2024"
```

**Campaigns**:
```
Format: [Channel]_[Type]_[Date]_[Description]
Example: "LinkedIn_Webinar_2024Q4_ProductLaunch"
```

**Lists**:
```
Format: [Segment]_[Criteria]_[Date]
Example: "Enterprise_Tech_20241201"
```

## Data Entry Rules

### Contact Creation
```
1. Search for existing record first
2. Check for duplicates (email, name+company)
3. Fill all required fields
4. Use standardized picklist values
5. Add to appropriate lists/campaigns
6. Log initial activity
```

### Company Creation
```
1. Search by domain/website first
2. Use official company name (from website)
3. Verify industry classification
4. Add employee count (LinkedIn)
5. Add revenue range (if available)
6. Link to parent company (if applicable)
```

### Deal Creation
```
1. Link to existing company/contact
2. Use naming convention
3. Set realistic close date
4. Enter qualified amount
5. Assign to correct owner
6. Add to appropriate pipeline
```

## Data Maintenance

### Weekly Tasks
- Review new records for completeness
- Merge obvious duplicates
- Update deal stages
- Clean up unassigned records

### Monthly Tasks
- Run duplicate detection
- Update stale records (180+ days)
- Archive closed/lost deals
- Review data quality metrics

### Quarterly Tasks
- Full data audit
- Update standardization rules
- Review field usage
- Clean up unused fields/values

## Data Quality Metrics

### Completeness Score
```
Formula: (Filled Required Fields / Total Required Fields) × 100

Target: >90%
```

### Accuracy Score
```
Formula: (Valid Records / Total Records) × 100

Validation Checks:
- Email deliverability
- Phone number format
- Website accessibility

Target: >95%
```

### Duplicate Rate
```
Formula: (Duplicate Records / Total Records) × 100

Target: <2%
```

### Staleness Rate
```
Formula: (Records >180 days old / Total Records) × 100

Target: <10%
```

## Roles and Responsibilities

### Data Owner
- Define data standards
- Approve schema changes
- Review quality metrics
- Enforce governance policies

### Data Steward
- Monitor data quality
- Run cleanup campaigns
- Train users on standards
- Report on metrics

### End Users
- Follow entry standards
- Report data issues
- Keep records updated
- Avoid creating duplicates

## Common Issues and Fixes

### Issue: High Duplicate Rate

**Causes**:
- No search before create
- Multiple entry points
- Lack of validation

**Fixes**:
- Mandatory duplicate check
- Single source of truth
- Automated matching rules

### Issue: Incomplete Records

**Causes**:
- Too many required fields
- Lack of training
- No enforcement

**Fixes**:
- Streamline requirements
- User training
- Validation rules

### Issue: Inconsistent Formatting

**Causes**:
- Free text fields
- No standardization
- Multiple users

**Fixes**:
- Convert to picklists
- Standardization rules
- Data normalization

## Automation Opportunities

### Auto-Enrichment
```
Trigger: New contact created
Action: Enrich with Clearbit/ZoomInfo
Fields: Title, Company, Industry, Size
```

### Auto-Deduplication
```
Trigger: Contact created/updated
Action: Check for duplicates
Match: Email, Name+Company
Result: Merge or alert
```

### Auto-Validation
```
Trigger: Field updated
Action: Validate format
Examples:
- Email: Check deliverability
- Phone: Format to standard
- Website: Verify accessibility
```

### Auto-Scoring
```
Trigger: Contact updated
Action: Calculate quality score
Factors:
- Completeness (40%)
- Accuracy (30%)
- Recency (20%)
- Engagement (10%)
```
