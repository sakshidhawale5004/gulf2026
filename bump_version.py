import glob
import re

def bump_version(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Look for style.css?v=...
    content = re.sub(r'style\.css\?v=[0-9\-a-zA-Z]+', 'style.css?v=20260820-1', content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('*.html'):
    bump_version(filepath)
