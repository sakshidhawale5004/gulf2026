import codecs
import re

regulation_pages = [
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html',
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]

def update_country_pages(content):
    # 1. Update <h1 class="text-white">
    # We want it to be same as index page: class="hero-title text-white" with weight 500
    content = re.sub(
        r'<h1 class="([^"]*)text-white([^"]*)">',
        r'<h1 class="\1hero-title text-white\2" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500;">',
        content
    )
    
    # 2. Update <h2> tags to ensure they use Cormorant and weight 500, size 2.0rem
    # Be careful not to replace already modified ones if script is run twice
    def fix_h2(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            # Check if font-family is already there
            if 'Cormorant Garamond' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem; ')
        else:
            attrs += ' style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem;"'
        return f"<h2{attrs}>{inner}</h2>"
        
    content = re.sub(r'<h2([^>]*)>(.*?)</h2>', fix_h2, content)
    
    # 3. Update <h3 class="glass-card-title">
    def fix_h3(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            if 'Cormorant Garamond' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Cormorant Garamond\', serif; font-weight: 600; font-size: 1.4rem; ')
        else:
            attrs += ' style="font-family: \'Cormorant Garamond\', serif; font-weight: 600; font-size: 1.4rem;"'
        return f"<h3{attrs}>{inner}</h3>"
        
    content = re.sub(r'<h3([^>]*)>(.*?)</h3>', fix_h3, content)

    # 4. Make sure <p> and <li> and <small> and <span> and <div> that contain text explicitly have Inter font if needed,
    # but style.css already sets body to Inter. However, let's explicitly set it on the glass-card-body and standard text.
    # To avoid breaking angular ng-repeat etc, I'll just set it on the main section container if possible,
    # or just trust the global style.css (which works). Let's explicitly set Inter on <p> and <li> just in case.
    # Actually, the user says "text inter the headings and text be same as index page".
    # I'll just add it to <p> tags in the document body.
    def fix_p(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            if 'Inter' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Inter\', sans-serif; ')
        else:
            attrs += ' style="font-family: \'Inter\', sans-serif;"'
        return f"<p{attrs}>{inner}</p>"
        
    content = re.sub(r'<p([^>]*)>(.*?)</p>', fix_p, content, flags=re.DOTALL)
    
    return content

for f in regulation_pages:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_country_pages(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
