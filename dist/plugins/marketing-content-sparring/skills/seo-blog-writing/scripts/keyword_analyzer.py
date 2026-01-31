import sys
import re
from collections import Counter

def analyze_keywords(text, target_keyword):
    """
    Analyzes the text for target keyword usage, density, and placement.
    """
    text_lower = text.lower()
    keyword_lower = target_keyword.lower()
    
    word_count = len(text.split())
    keyword_count = text_lower.count(keyword_lower)
    density = (keyword_count / word_count) * 100 if word_count > 0 else 0
    
    # Check placement
    lines = text.split('\n')
    h1_found = False
    first_para_found = False
    
    for line in lines:
        if line.startswith('# ') and keyword_lower in line.lower():
            h1_found = True
        # Rough check for first paragraph (first non-header line)
        if not line.startswith('#') and len(line) > 50 and not first_para_found:
            if keyword_lower in line.lower():
                first_para_found = True
            break
            
    return {
        "word_count": word_count,
        "keyword_count": keyword_count,
        "density": density,
        "h1_found": h1_found,
        "first_para_found": first_para_found
    }

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python keyword_analyzer.py 'Target Keyword' 'File Path'")
        sys.exit(1)
        
    keyword = sys.argv[1]
    file_path = sys.argv[2]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        results = analyze_keywords(content, keyword)
        
        print(f"--- Keyword Analysis: '{keyword}' ---")
        print(f"Word Count: {results['word_count']}")
        print(f"Keyword Count: {results['keyword_count']}")
        print(f"Density: {results['density']:.2f}% (Target: 1-2%)")
        
        print("\nPlacement Checks:")
        print(f"[{'x' if results['h1_found'] else ' '}] In H1 Title")
        print(f"[{'x' if results['first_para_found'] else ' '}] In First Paragraph")
        
        if results['density'] > 2.5:
            print("\n⚠️ Warning: Keyword stuffing detected (>2.5%)")
        elif results['density'] < 0.5:
            print("\n⚠️ Warning: Keyword density too low (<0.5%)")
        else:
            print("\n✅ Density looks good.")
            
    except Exception as e:
        print(f"Error: {e}")
