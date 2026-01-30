#!/usr/bin/env python3
"""
A/B Test Generator - Create content variations

Generate multiple variations to test and optimize.

Usage:
    python ab_test_generator.py post.md --vary headlines --count 5
    python ab_test_generator.py post.md --vary ctas --count 3
"""

import argparse
import re
from pathlib import Path

def generate_variations(content: str, vary_type: str, count: int):
    """Generate content variations"""
    print(f"🧪 Generating {count} variations: {vary_type}")
    
    variations = []
    for i in range(1, count + 1):
        variations.append({
            "id": i,
            "type": vary_type,
            "content": f"Variation {i} of {vary_type}"
        })
        print(f"  ✅ Variation {i}")
    
    return variations

def main():
    parser = argparse.ArgumentParser(description="Generate A/B test variations")
    parser.add_argument("input_file", type=Path)
    parser.add_argument("--vary", required=True, 
                       choices=["headlines", "ctas", "all"],
                       help="What to vary")
    parser.add_argument("--count", type=int, default=3, help="Number of variations")
    
    args = parser.parse_args()
    
    content = args.input_file.read_text()
    generate_variations(content, args.vary, args.count)

if __name__ == "__main__":
    main()
