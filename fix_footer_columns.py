import os
import re

for filename in os.listdir('.'):
    if filename.endswith('.html'):
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        content = content.replace('mt-lg-5 pt-lg-4', '')
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
