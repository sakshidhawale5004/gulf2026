import glob
import os
import shutil
import re

# 1. Copy favicon-final.jpeg to favicon.png, favicon.jpeg, favicon.ico so all direct requests work
if os.path.exists('favicon-final.jpeg'):
    shutil.copy2('favicon-final.jpeg', 'favicon.png')
    shutil.copy2('favicon-final.jpeg', 'favicon.jpeg')
    shutil.copy2('favicon-final.jpeg', 'favicon.ico')
    print("Copied favicon-final.jpeg to favicon.png, favicon.jpeg, and favicon.ico")

# 2. Update all HTML and PHP files in root
root_files = glob.glob('*.html') + glob.glob('*.php')
for file in root_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    # Replace existing favicon link if present, removing any duplicate tags
    if '<link rel="icon"' in content or '<link rel=\'icon\'' in content:
        parts = re.split(r'<link\s+rel=["\']icon["\'][^>]*>\s*', content)
        content = parts[0] + '    <link rel="icon" type="image/jpeg" href="favicon-final.jpeg">\n' + ''.join(parts[1:])
    elif '</head>' in content:
        content = content.replace('</head>', '    <link rel="icon" type="image/jpeg" href="favicon-final.jpeg">\n</head>')
        
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated root file: {file}")

# 3. Update all PHP files in admin/
if os.path.exists('admin'):
    admin_files = glob.glob('admin/*.php')
    for file in admin_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        original = content
        if '<link rel="icon"' in content or '<link rel=\'icon\'' in content:
            parts = re.split(r'<link\s+rel=["\']icon["\'][^>]*>\s*', content)
            content = parts[0] + '    <link rel="icon" type="image/jpeg" href="../favicon-final.jpeg">\n' + ''.join(parts[1:])
        elif '</head>' in content:
            content = content.replace('</head>', '    <link rel="icon" type="image/jpeg" href="../favicon-final.jpeg">\n</head>')
            
        if content != original:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated admin file: {file}")
