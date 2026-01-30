import sys

def score_lead(firmographics, intent, timing, solution_match):
    """
    Calculate FITS score for lead qualification.
    
    Args:
        firmographics (dict): Company size, industry, revenue
        intent (int): Intent score 0-100
        timing (int): Timing score 0-100
        solution_match (int): Solution fit score 0-100
    
    Returns:
        dict: Scores and qualification level
    """
    # Firmographics scoring
    firm_score = 0
    
    # Company size
    if firmographics.get('employees', 0) >= 100:
        firm_score += 25
    elif firmographics.get('employees', 0) >= 50:
        firm_score += 15
    elif firmographics.get('employees', 0) >= 10:
        firm_score += 10
    
    # Revenue
    if firmographics.get('revenue', 0) >= 10000000:  # $10M+
        firm_score += 25
    elif firmographics.get('revenue', 0) >= 1000000:  # $1M+
        firm_score += 15
    
    # Industry match
    target_industries = ['saas', 'technology', 'software']
    if firmographics.get('industry', '').lower() in target_industries:
        firm_score += 25
    
    # Calculate total FITS score
    total_score = (firm_score + intent + timing + solution_match) / 4
    
    # Qualification level
    if total_score >= 75:
        level = "A - High Priority"
    elif total_score >= 50:
        level = "B - Medium Priority"
    elif total_score >= 25:
        level = "C - Low Priority"
    else:
        level = "D - Disqualified"
    
    return {
        "firmographics_score": firm_score,
        "intent_score": intent,
        "timing_score": timing,
        "solution_match_score": solution_match,
        "total_score": total_score,
        "qualification_level": level
    }

if __name__ == "__main__":
    # Example usage
    firmographics = {
        "employees": 150,
        "revenue": 5000000,
        "industry": "SaaS"
    }
    
    result = score_lead(firmographics, intent=70, timing=80, solution_match=85)
    
    print("--- FITS Lead Score ---")
    print(f"Firmographics: {result['firmographics_score']}/100")
    print(f"Intent: {result['intent_score']}/100")
    print(f"Timing: {result['timing_score']}/100")
    print(f"Solution Match: {result['solution_match_score']}/100")
    print(f"\nTotal Score: {result['total_score']:.1f}/100")
    print(f"Qualification: {result['qualification_level']}")
