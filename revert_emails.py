import os
import glob

files = glob.glob('*.html') + glob.glob('*.md')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    
    target_str = 'connect@gulftp.com (admin@gulftp.com as parent)'
    replacement_str = 'connect@gulftp.com'
    
    if target_str in content:
        content = content.replace(target_str, replacement_str)
        changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
