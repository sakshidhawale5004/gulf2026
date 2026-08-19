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

def update_text_white(content):
    # 1. Update <h1> to <h1 class="text-white">
    # Note: some might already have a class, some might not.
    # Let's match <h1> inside .page-hero
    content = re.sub(r'<h1>', '<h1 class="text-white">', content)
    
    # If they already have class="text-white", we don't want to duplicate. But none of them do currently.
    
    # 2. Update breadcrumb text to be white
    # <div class="breadcrumb-text"> -> <div class="breadcrumb-text text-white">
    content = re.sub(r'class="breadcrumb-text"', 'class="breadcrumb-text text-white"', content)
    
    # 3. Update breadcrumb link to be white
    # <a href="index.html">Home</a> -> <a href="index.html" class="text-white">Home</a>
    # We will do this specifically inside the breadcrumb div to be safe.
    # Just replacing href="index.html" in the breadcrumb:
    content = re.sub(r'(<div class="breadcrumb-text text-white">\s*)<a href="index.html">', r'\1<a href="index.html" class="text-white">', content)

    # Let's just blindly make sure all a href="index.html" inside page-hero are text-white
    # Not needed, the regex above handles it.
    
    return content

for f in files_all:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_text_white(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
