import codecs
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html',
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html',
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]

def update_background(content):
    # Regex to find the background property in .page-hero
    # It might have a linear-gradient already or just a url
    # We will just replace it cleanly.
    # First, let's capture the url
    match = re.search(r"background:\s*(?:linear-gradient\([^)]+\),\s*(?:rgba\([^)]+\),\s*)?)?url\('([^']+)'\)", content)
    if not match:
        # Some don't have linear-gradient but might have other things
        match = re.search(r"background:\s*url\('([^']+)'\)", content)
        
    if match:
        img_url = match.group(1)
        # Construct the new very dark background
        new_bg = f"background: linear-gradient(rgba(4, 45, 33, 0.88), rgba(4, 45, 33, 0.88)), url('{img_url}')"
        # Replace the entire background property value
        # Look for the background property line
        content = re.sub(
            r"background:\s*[^;]+;",
            f"{new_bg} center/cover no-repeat;",
            content,
            count=1 # Only replace the first one which is inside .page-hero
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
