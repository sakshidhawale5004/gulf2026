import codecs

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
    'uae-transfer-pricing.html',
    'about.html'
]

def update_background(content):
    # Make the green overlay even darker
    content = content.replace('rgba(4, 45, 33, 0.88)', 'rgba(2, 20, 15, 0.95)')
    # If about.html is in this, it might have a different gradient.
    # We should make sure about.html also has the darker overlay? No they just asked to reduce height.
    # Let's reduce padding in about.html from 80px to 60px to make it even smaller, just in case 80 was still too big.
    content = content.replace('padding: 80px 0;', 'padding: 60px 0;')
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
