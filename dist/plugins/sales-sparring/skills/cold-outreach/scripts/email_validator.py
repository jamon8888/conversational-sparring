import sys
import re

def validate_email(email):
    """
    Validates email address format and checks for common issues.
    """
    issues = []
    score = 100
    
    # Basic format check
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(email_pattern, email):
        issues.append("Invalid email format")
        return 0, issues
    
    # Check for common disposable domains
    disposable_domains = ['tempmail.com', 'guerrillamail.com', 'mailinator.com', '10minutemail.com']
    domain = email.split('@')[1].lower()
    if domain in disposable_domains:
        score -= 50
        issues.append(f"Disposable email domain detected: {domain}")
    
    # Check for role-based emails
    role_prefixes = ['info@', 'admin@', 'support@', 'noreply@', 'sales@', 'contact@']
    if any(email.lower().startswith(prefix) for prefix in role_prefixes):
        score -= 30
        issues.append("Role-based email (lower engagement rates)")
    
    # Check for common typos in domains
    common_typos = {
        'gmial.com': 'gmail.com',
        'gmai.com': 'gmail.com',
        'yahooo.com': 'yahoo.com',
        'hotmial.com': 'hotmail.com'
    }
    if domain in common_typos:
        score -= 20
        issues.append(f"Possible typo: did you mean {common_typos[domain]}?")
    
    return max(0, score), issues

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python email_validator.py 'email@example.com'")
        sys.exit(1)
    
    email = sys.argv[1]
    score, issues = validate_email(email)
    
    print(f"Email: {email}")
    print(f"Validity Score: {score}/100")
    
    if issues:
        print("\nIssues Found:")
        for issue in issues:
            print(f"⚠️ {issue}")
    else:
        print("✅ Email looks good!")
