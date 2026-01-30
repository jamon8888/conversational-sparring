import sys

def format_checklist(text):
    """
    Converts lines of text into a Markdown checklist.
    """
    lines = text.strip().split('\n')
    formatted = []
    
    for line in lines:
        line = line.strip()
        if not line:
            continue
        if line.startswith('- [ ]') or line.startswith('- [x]'):
            formatted.append(line)
        elif line.startswith('- ') or line.startswith('* '):
            formatted.append(f"- [ ] {line[2:]}")
        else:
            formatted.append(f"- [ ] {line}")
            
    return "\n".join(formatted)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python checklist_formatter.py 'Line 1\\nLine 2'")
        sys.exit(1)
        
    # Handle multiline input from args or stdin? 
    # For simplicity, let's assume arg 1 is the block of text
    text = sys.argv[1]
    print(format_checklist(text))
