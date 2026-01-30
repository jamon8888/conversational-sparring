---
name: crm-hygiene
description: Use when maintaining CRM data quality, auditing records for duplicates, or establishing data governance standards. Trigger when needing to clean up inconsistent contact information, perform a bulk merge of duplicate records, or schedule a periodic data quality audit (scripts/data_quality_auditor.py) for CRM health.
license: MIT
---

# CRM Hygiene

## Quick Start

This skill helps you maintain clean, reliable CRM data. For complete frameworks, see the [Complete Guide](references/guide.md).

## Tools & Scripts

**Data Quality Auditor** (`scripts/data_quality_auditor.py`):

```bash
python scripts/data_quality_auditor.py crm_export.csv
```

Audits CRM data quality and identifies issues.

## Execution Checklist

### CRM Cleanup Process

- [ ] Audit current data quality
- [ ] Identify duplicates (merge or delete)
- [ ] Standardize fields (naming conventions)
- [ ] Complete missing data (enrich)
- [ ] Archive inactive records
- [ ] Set up validation rules
- [ ] Create data entry guidelines
- [ ] Schedule monthly audits

## Key Standards

- **Required Fields**: Name, Email, Company, Status
- **Standardization**: Consistent formats (phone, date, etc.)
- **Duplicate Rules**: Auto-merge on email match
- **Data Freshness**: Update contacts quarterly

## Quick Wins

- Require fields at creation (prevent bad data)
- Use picklists (enforce standards)
- Merge duplicates weekly
- Archive records inactive >1 year

## Resources

- [Complete Guide](references/guide.md)
- [Data Governance](references/data-governance.md)

## Related Skills

### From RevOps Toolkit

- [pipeline-forecasting](../pipeline-forecasting/SKILL.md) - Clean data = accurate forecasts
- [sales-marketing-alignment](../sales-marketing-alignment/SKILL.md) - Data definitions
