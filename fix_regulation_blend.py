import codecs
import re

regulation_pages = [
    'uae-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'qatar-transfer-pricing.html',
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html'
]

def update_regulation_hero(content):
    # Regex to capture the url() part
    # Look for background: linear-gradient(...), url(...) center/cover no-repeat;
    # It might have different rgba values currently.
    
    def replacer(match):
        url_part = match.group(1) # The full url('...') string
        return f"background: linear-gradient(rgba(10, 107, 79, 0.85), rgba(10, 107, 79, 0.85)), {url_part} center/cover no-repeat;\n            background-blend-mode: normal;"
    
    # Matches background: linear-gradient(...), url('...') center/cover no-repeat;
    # Or similar
    content = re.sub(r'background:\s*linear-gradient\([^)]+\),\s*([^)]+\)[^)]+\)(?:, [^)]+\))?[^)]*\)),?\s*(url\([^)]+\))\s+center/cover\s+no-repeat;', replacer, content)
    # wait, the regex above is getting messy for nested parenthesis.
    # simpler:
    content = re.sub(r'background:\s*linear-gradient\([^)]+\)[^,]*,?\s*(url\([^)]+\))\s*center/cover\s*no-repeat;', replacer, content)
    # wait, rgba(...) has parenthesis! linear-gradient(rgba(...), rgba(...))
    
    content = re.sub(r"background:\s*linear-gradient\(rgba\([^)]+\),\s*rgba\([^)]+\)\),\s*(url\('[^']+'\))\s*center/cover\s*no-repeat;", replacer, content)
    return content

for f in regulation_pages:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_regulation_hero(content)
        
        # also, just in case background-blend-mode: normal; is already there, don't duplicate it.
        # But this is a simple script, it'll just overwrite.
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f} (Regex might have failed or it's already updated)")
    except Exception as e:
        print(f"Error in {f}: {e}")
