import sys
import re

def count_syllables(word):
    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count

def calculate_readability(text):
    """
    Calculates Flesch Reading Ease score.
    """
    sentences = max(1, len(re.split(r'[.!?]+', text)))
    words = max(1, len(text.split()))
    syllables = sum(count_syllables(word) for word in text.split())
    
    score = 206.835 - 1.015 * (words / sentences) - 84.6 * (syllables / words)
    return score

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python readability_scorer.py 'Text to analyze'")
        sys.exit(1)
        
    text = sys.argv[1]
    score = calculate_readability(text)
    
    print(f"Flesch Reading Ease Score: {score:.1f}")
    
    if score >= 90:
        print("Level: Very Easy (5th grade)")
    elif score >= 80:
        print("Level: Easy (6th grade)")
    elif score >= 70:
        print("Level: Fairly Easy (7th grade)")
    elif score >= 60:
        print("Level: Standard (8th-9th grade) - Recommended for Landing Pages")
    elif score >= 50:
        print("Level: Fairly Difficult (10th-12th grade)")
    elif score >= 30:
        print("Level: Difficult (College)")
    else:
        print("Level: Very Difficult (College Graduate)")
