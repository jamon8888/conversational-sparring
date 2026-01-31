import sys

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def luminance(r, g, b):
    a = [x / 255.0 for x in (r, g, b)]
    a = [((x + 0.055) / 1.055) ** 2.4 if x > 0.03928 else x / 12.92 for x in a]
    return 0.2126 * a[0] + 0.7152 * a[1] + 0.0722 * a[2]

def contrast_ratio(hex1, hex2):
    """
    Calculates the contrast ratio between two hex colors.
    """
    rgb1 = hex_to_rgb(hex1)
    rgb2 = hex_to_rgb(hex2)
    
    lum1 = luminance(*rgb1)
    lum2 = luminance(*rgb2)
    
    brightest = max(lum1, lum2)
    darkest = min(lum1, lum2)
    
    return (brightest + 0.05) / (darkest + 0.05)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python contrast_checker.py '#FFFFFF' '#000000'")
        sys.exit(1)
        
    c1 = sys.argv[1]
    c2 = sys.argv[2]
    
    try:
        ratio = contrast_ratio(c1, c2)
        print(f"Contrast Ratio: {ratio:.2f}:1")
        
        if ratio >= 4.5:
            print("✅ AA Pass (Normal Text)")
        else:
            print("⚠️ AA Fail (Normal Text)")
            
        if ratio >= 3.0:
            print("✅ AA Pass (Large Text)")
        else:
            print("⚠️ AA Fail (Large Text)")
            
    except Exception as e:
        print(f"Error: {e}")
