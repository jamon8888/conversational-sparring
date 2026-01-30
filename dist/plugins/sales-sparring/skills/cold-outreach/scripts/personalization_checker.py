import sys

def check_personalization(email_text):
    """
    Checks if personalization tokens are properly filled in cold email.
    """
    issues = []
    score = 100
    
    # Common placeholder patterns
    placeholders = [
        r'\[NAME\]', r'\[COMPANY\]', r'\[TITLE\]', r'\[PRODUCT\]',
        r'\{\{.*?\}\}',  # Handlebars style
        r'<.*?>',  # Angle brackets
        r'\[.*?\]'  # Square brackets
    ]
    
    import re
    found_placeholders = []
    for pattern in placeholders:
        matches = re.findall(pattern, email_text, re.IGNORECASE)
        found_placeholders.extend(matches)
    
    if found_placeholders:
        score = 0
        issues.append(f"Unfilled placeholders detected: {', '.join(set(found_placeholders))}")
    
    # Check for generic greetings
    generic_greetings = ['dear sir/madam', 'to whom it may concern', 'hello there', 'hi team']
    for greeting in generic_greetings:
        if greeting in email_text.lower():
            score -= 30
            issues.append(f"Generic greeting detected: '{greeting}'")
    
    # Check for personalization elements
    personalization_score = 0
    if re.search(r'\b(saw|noticed|read)\b.*\b(your|you)\b', email_text, re.IGNORECASE):
        personalization_score += 20
    if re.search(r'\b(recent|latest|new)\b', email_text, re.IGNORECASE):
        personalization_score += 10
    if len(email_text.split()) < 150:  # Short and focused
        personalization_score += 10
    
    return max(0, min(100, score + personalization_score)), issues

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python personalization_checker.py 'Email text here'")
        sys.exit(1)
    
    email_text = sys.argv[1]
    score, issues = check_personalization(email_text)
    
    print(f"Personalization Score: {score}/100")
    
    if issues:
        print("\nIssues:")
        for issue in issues:
            print(f"⚠️ {issue}")
    else:
        print("✅ Email is well personalized!")
