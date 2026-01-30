import sys
import re

def check_spam_score(subject_line):
    """
    Analyzes an email subject line for spam triggers and length issues.
    Returns a score (0-100) and a list of warnings.
    """
    score = 100
    warnings = []
    
    # Trigger words (simplified list)
    triggers = [
        "free", "buy now", "act fast", "limited time", "click here", 
        "$$$", "100%", "guarantee", "prize", "winner", "urgent"
    ]
    
    # Check for triggers
    found_triggers = [word for word in triggers if word in subject_line.lower()]
    if found_triggers:
        score -= (len(found_triggers) * 10)
        warnings.append(f"Contains spam trigger words: {', '.join(found_triggers)}")
        
    # Check length
    if len(subject_line) > 50:
        score -= 10
        warnings.append("Subject line is too long (>50 chars). Keep it mobile-friendly.")
    elif len(subject_line) < 10:
        score -= 5
        warnings.append("Subject line is too short. Add more context.")
        
    # Check caps
    if sum(1 for c in subject_line if c.isupper()) / len(subject_line) > 0.5:
        score -= 20
        warnings.append("Too many capital letters. Avoid shouting.")
        
    # Check punctuation
    if "!!!" in subject_line or "??" in subject_line:
        score -= 10
        warnings.append("Excessive punctuation detected.")
        
    return max(0, score), warnings

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python spam_checker.py 'Your Subject Line Here'")
        sys.exit(1)
        
    subject = sys.argv[1]
    score, warnings = check_spam_score(subject)
    
    print(f"Subject: {subject}")
    print(f"Spam Score: {score}/100")
    if warnings:
        print("Warnings:")
        for w in warnings:
            print(f"- {w}")
    else:
        print("✅ Looks good!")
