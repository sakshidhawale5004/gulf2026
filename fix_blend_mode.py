import codecs
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]

def update_hero_style(content):
    target = r"background: linear-gradient\(rgba\(0, 0, 0, 0\.7\), rgba\(0, 0, 0, 0\.7\)\), url\('([^']+)'\) center/cover no-repeat;"
    replacement = r"background: linear-gradient(rgba(0, 0, 0, 0.7), rgba(0, 0, 0, 0.7)), url('\1') center/cover no-repeat;\n            background-blend-mode: normal;"
    content = re.sub(target, replacement, content)
    return content

for f in files_all:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_hero_style(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
