#!/usr/bin/env python3
"""
Tone Analyzer - Ensure brand voice consistency

Analyzes tone and checks brand voice alignment.

Usage:
    python tone_analyzer.py draft.md --brand-voice brand-voice.json
    python tone_analyzer.py draft.md --compare
"""

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Dict

def analyze_tone(content: str) -> Dict:
    """Analyze tone of content"""
    # Simple tone analysis based on keywords and patterns
    
    word_count = len(content.split())
    
    # Formality indicators
    formal_words = ["therefore", "thus", "consequently", "furthermore"]
    casual_words = ["like", "stuff", "things", "kinda", "gonna"]
    
    formal_count = sum(content.lower().count(word) for word in formal_words)
    casual_count = sum(content.lower().count(word) for word in casual_words)
    
    # Sentiment indicators
    positive_words = ["great", "excellent", "amazing", "wonderful", "best"]
    negative_words = ["bad", "poor", "worst", "terrible", "awful"]
    
    positive_count = sum(content.lower().count(word) for word in positive_words)
    negative_count = sum(content.lower().count(word) for word in negative_words)
    
    # Calculate scores (0-10)
    formality_score = min(10, (formal_count / max(1, word_count / 100)) * 2)
    casualness_score = min(10, (casual_count / max(1, word_count / 100)) * 2)
    positivity_score = min(10, (positive_count / max(1, word_count / 100)) * 2)
    
    return {
        "word_count": word_count,
        "formality": round(formality_score, 1),
        "casualness": round(casualness_score, 1),
        "positivity": round(positivity_score, 1),
        "tone": "formal" if formality_score > casualness_score else "casual"
    }

def compare_with_brand_voice(tone: Dict, brand_voice: Dict) -> Dict:
    """Compare analyzed tone with brand voice guidelines"""
    mismatches = []
    
    if "attributes" in brand_voice:
        target_tone = brand_voice["attributes"][0] if brand_voice["attributes"] else "professional"
        if target_tone == "professional" and tone["formality"] < 5:
            mismatches.append("Content is too casual for professional brand voice")
        elif target_tone == "casual" and tone["formality"] > 5:
            mismatches.append("Content is too formal for casual brand voice")
    
    return {
        "tone_analysis": tone,
        "brand_requirements": brand_voice.get("attributes", []),
        "mismatches": mismatches,
        "score": 100 - (len(mismatches) * 30)
    }

def main():
    parser = argparse.ArgumentParser(description="Analyze content tone")
    parser.add_argument("input_file", type=Path, help="Input file")
    parser.add_argument("--brand-voice-file", type=Path, help="Brand voice JSON file")
    parser.add_argument("--compare", action="store_true", help="Compare with brand voice")
    
    args = parser.parse_args()
    
    content = args.input_file.read_text()
    tone = analyze_tone(content)
    
    if args.brand_voice_file and args.brand_voice_file.exists():
        brand_voice = json.loads(args.brand_voice_file.read_text())
        result = compare_with_brand_voice(tone, brand_voice.get("brand_voice", {}))
    else:
        result = {"tone_analysis": tone}
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
