import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if 'btn-outline-primary' in content:
            # Replace btn-outline-primary with a custom green outlined button style
            content = content.replace('btn-outline-primary', 'btn-outline-custom-green')
            
            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
