import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Remove letter-spacing: -1px;
        content = re.sub(r'letter-spacing:\s*-1px;?', '', content)
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
