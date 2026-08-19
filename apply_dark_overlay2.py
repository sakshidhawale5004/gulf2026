import codecs
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html',
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html'
]

def update_background(content):
    # We want to replace the background property inside .page-hero
    # Let's find the URL first
    match = re.search(r"\.page-hero\s*\{[^}]*url\('([^']+)'\)", content)
    if match:
        img_url = match.group(1)
        new_bg = f"background: linear-gradient(rgba(4, 45, 33, 0.88), rgba(4, 45, 33, 0.88)), url('{img_url}') center/cover no-repeat;"
        
        # Now replace the background line in .page-hero
        content = re.sub(
            r"(\.page-hero\s*\{[^}]*?)background:\s*[^;]+;",
            rf"\g<1>{new_bg}",
            content,
            count=1
        )
    return content

for f in files_all:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_background(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
