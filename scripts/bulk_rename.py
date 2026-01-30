import os
import re

def bulk_rename(directory):
    replacements = {
        'Sparring': 'Sparring',
        'sparring': 'sparring',
        'Sparring': 'Sparring',
        'sparring': 'sparring'
    }
    
    # Compile regex for case-sensitive matching
    pattern = re.compile('|'.join(re.escape(k) for k in replacements.keys()))
    
    for root, dirs, files in os.walk(directory):
        # Skip .git and other hidden dirs
        if '.git' in dirs:
            dirs.remove('.git')
        if '.gemini' in dirs:
            dirs.remove('.gemini')
            
        for file in files:
            if not file.endswith(('.md', '.py', '.yaml', '.txt')):
                continue
            
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            new_content = pattern.sub(lambda m: replacements[m.group(0)], content)
            
            if new_content != content:
                print(f"Updating {path}")
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)

if __name__ == "__main__":
    target_dir = r"C:\Users\NMarchitecte\Documents\persistent-mind-model-v1.0\conversational-sparring"
    bulk_rename(target_dir)
