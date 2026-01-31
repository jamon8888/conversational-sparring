import sys

def validate_post(platform, content):
    """
    Validates content against platform-specific constraints.
    """
    platform = platform.lower()
    length = len(content)
    warnings = []
    
    limits = {
        "twitter": 280,
        "linkedin": 3000,
        "instagram": 2200,
        "facebook": 63206
    }
    
    if platform not in limits:
        return False, [f"Unknown platform: {platform}"]
        
    max_len = limits[platform]
    
    if length > max_len:
        warnings.append(f"Content exceeds {platform} limit ({length}/{max_len} chars).")
    
    # Platform specific checks
    if platform == "twitter":
        if content.count("#") > 3:
            warnings.append("Consider using fewer hashtags (2-3 max) for better engagement.")
    
    if platform == "linkedin":
        if length < 100:
            warnings.append("LinkedIn posts perform better with more depth (>100 chars).")
        if "http" in content and "link in comments" not in content.lower():
            warnings.append("Consider putting links in comments to boost reach.")
            
    return len(warnings) == 0, warnings

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python platform_validator.py [Platform] [Content]")
        sys.exit(1)
        
    platform = sys.argv[1]
    content = sys.argv[2]
    
    is_valid, warnings = validate_post(platform, content)
    
    print(f"--- Validating for {platform.capitalize()} ---")
    print(f"Length: {len(content)} chars")
    
    if is_valid:
        print("✅ Content is valid.")
    else:
        print("⚠️ Issues found:")
        for w in warnings:
            print(f"- {w}")
