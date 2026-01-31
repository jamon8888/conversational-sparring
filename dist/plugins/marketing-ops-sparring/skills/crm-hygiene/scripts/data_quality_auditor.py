import sys
import csv
from datetime import datetime

def audit_crm_data(records):
    """
    Audit CRM data quality and identify issues.
    
    Args:
        records: List of dicts representing CRM records
    
    Returns:
        dict: Audit results with issues and scores
    """
    issues = {
        'missing_fields': [],
        'invalid_emails': [],
        'duplicate_records': [],
        'stale_records': [],
        'incomplete_records': []
    }
    
    total_records = len(records)
    quality_score = 100
    
    # Required fields
    required_fields = ['name', 'email', 'company', 'status']
    
    # Track for duplicates
    seen_emails = {}
    
    for i, record in enumerate(records):
        record_id = record.get('id', i)
        
        # Check missing fields
        missing = [field for field in required_fields if not record.get(field)]
        if missing:
            issues['missing_fields'].append({
                'id': record_id,
                'missing': missing
            })
            quality_score -= 1
        
        # Check email validity
        email = record.get('email', '')
        if email and '@' not in email:
            issues['invalid_emails'].append({
                'id': record_id,
                'email': email
            })
            quality_score -= 2
        
        # Check for duplicates
        if email:
            if email in seen_emails:
                issues['duplicate_records'].append({
                    'id': record_id,
                    'duplicate_of': seen_emails[email],
                    'email': email
                })
                quality_score -= 3
            else:
                seen_emails[email] = record_id
        
        # Check for stale records (no activity in 180 days)
        last_activity = record.get('last_activity_date')
        if last_activity:
            try:
                last_date = datetime.strptime(last_activity, '%Y-%m-%d')
                days_since = (datetime.now() - last_date).days
                if days_since > 180:
                    issues['stale_records'].append({
                        'id': record_id,
                        'days_since_activity': days_since
                    })
                    quality_score -= 0.5
            except:
                pass
        
        # Check completeness (optional fields)
        optional_fields = ['phone', 'title', 'industry', 'revenue']
        filled_optional = sum(1 for field in optional_fields if record.get(field))
        if filled_optional < 2:
            issues['incomplete_records'].append({
                'id': record_id,
                'filled_fields': filled_optional
            })
            quality_score -= 0.5
    
    quality_score = max(0, min(100, quality_score))
    
    return {
        'total_records': total_records,
        'quality_score': quality_score,
        'issues': issues,
        'summary': {
            'missing_fields': len(issues['missing_fields']),
            'invalid_emails': len(issues['invalid_emails']),
            'duplicates': len(issues['duplicate_records']),
            'stale_records': len(issues['stale_records']),
            'incomplete_records': len(issues['incomplete_records'])
        }
    }

if __name__ == "__main__":
    # Example usage
    sample_records = [
        {'id': 1, 'name': 'John Doe', 'email': 'john@example.com', 'company': 'Acme', 'status': 'Lead', 'last_activity_date': '2024-01-15'},
        {'id': 2, 'name': 'Jane Smith', 'email': 'jane@example.com', 'company': 'TechCo', 'status': 'Opportunity'},
        {'id': 3, 'name': 'Bob Johnson', 'email': 'invalid-email', 'company': 'StartupXYZ', 'status': 'Lead'},
        {'id': 4, 'name': 'Alice Brown', 'email': 'john@example.com', 'company': 'Acme', 'status': 'Customer'},
    ]
    
    results = audit_crm_data(sample_records)
    
    print("--- CRM Data Quality Audit ---")
    print(f"Total Records: {results['total_records']}")
    print(f"Quality Score: {results['quality_score']:.1f}/100\n")
    
    print("Issues Found:")
    for issue_type, count in results['summary'].items():
        if count > 0:
            print(f"  {issue_type.replace('_', ' ').title()}: {count}")
