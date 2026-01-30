#!/usr/bin/env python3
"""
Platform Optimizer - Optimize content for specific platforms

Ensures content meets platform requirements and best practices.

Usage:
    python platform_optimizer.py draft.txt --platform twitter
    python platform_optimizer.py draft.txt --platform linkedin --professional-tone
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List

PLATFORM_SPECS = {
    "twitter": {"max_chars": 280, "max_hashtags": 2, "image_size": "1200x675"},
    "linkedin": {"max_chars": 3000, "optimal_chars": 1500, "max_hashtags": 3},
    "instagram": {"max_chars": 2200, "optimal_chars": 150, "max_hashtags": 30},
    "facebook": {"max_chars": 63206, "optimal_chars": 500},
    "youtube": {"max_chars": 5000, "optimal_chars": 200},
}

def optimize_for_platform(content: str, platform: str, **kwargs) -> Dict:
    """Optimize content for specific platform"""
    if platform not in PLATFORM_SPECS:
        return {"error": f"Unknown platform: {platform}"}
    
    spec = PLATFORM_SPECS[platform]
    issues = []
    suggestions = []
    
    # Check length
    if len(content) > spec["max_chars"]:
        issues.append(f"Content too long: {len(content)} chars (max: {spec['max_chars']})")
        suggestions.append(f"Trim to {spec['max_chars']} characters")
    
    # Check optimal length
    if "optimal_chars" in spec:
        if len(content) < spec["optimal_chars"] * 0.5:
            suggestions.append(f"Consider expanding to {spec['optimal_chars']} chars for better engagement")
    
    # Count hashtags
    hashtag_count = content.count('#')
    if "max_hashtags" in spec and hashtag_count > spec["max_hashtags"]:
        issues.append(f"Too many hashtags: {hashtag_count} (recommended: {spec['max_hashtags']})")
    
    return {
        "platform": platform,
        "length": len(content),
        "spec": spec,
        "issues": issues,
        "suggestions": suggestions,
        "score": 100 - (len(issues) * 20)
    }

def main():
    parser = argparse.ArgumentParser(description="Optimize content for platforms")
    parser.add_argument("input_file", type=Path, help="Input file")
    parser.add_argument("--platform", "-p", required=True, choices=list(PLATFORM_SPECS.keys()))
    parser.add_argument("--check-all-platforms", action="store_true")
    
    args = parser.parse_args()
    
    content = args.input_file.read_text()
    result = optimize_for_platform(content, args.platform)
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
