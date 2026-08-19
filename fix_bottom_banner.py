import codecs
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]

def update_bottom_banner(content):
    # Find the specific div with the green background gradient and replace it with black
    target = r'background: linear-gradient\(rgba\(10, 107, 79, 0\.7\), rgba\(10, 107, 79, 0\.7\)\)'
    replacement = r'background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7))'
    content = re.sub(target, replacement, content)
    return content

for f in files_all:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_bottom_banner(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
