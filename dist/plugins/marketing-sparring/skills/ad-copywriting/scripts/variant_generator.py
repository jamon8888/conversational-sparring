import sys
import itertools

def generate_variants(headlines, ctas):
    """
    Generates combinations of headlines and CTAs.
    """
    variants = list(itertools.product(headlines, ctas))
    return variants

if __name__ == "__main__":
    # Example usage: python variant_generator.py "Headline 1|Headline 2" "CTA 1|CTA 2"
    if len(sys.argv) < 3:
        print("Usage: python variant_generator.py 'H1|H2|H3' 'CTA1|CTA2'")
        sys.exit(1)
        
    headlines = sys.argv[1].split('|')
    ctas = sys.argv[2].split('|')
    
    variants = generate_variants(headlines, ctas)
    
    print(f"Generated {len(variants)} Variants:\n")
    for i, (h, c) in enumerate(variants, 1):
        print(f"Variant {i}:")
        print(f"  Headline: {h.strip()}")
        print(f"  CTA:      {c.strip()}")
        print("-" * 20)
