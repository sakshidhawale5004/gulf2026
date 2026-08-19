import codecs
import re

policy_pages = [
    'privacy-policy.html',
    'terms-of-use.html'
]

def update_policy_pages(content):
    # 1. Update <h1> in banner
    # It might be <h1>Privacy Policy</h1> or <h1 class="...">...
    def fix_h1(match):
        attrs = match.group(1).replace('class="', '').replace('"', '').strip()
        inner = match.group(2)
        # Ensure it has hero-title and text-white
        classes = attrs.split()
        if 'hero-title' not in classes:
            classes.append('hero-title')
        if 'text-white' not in classes:
            classes.append('text-white')
            
        class_str = ' '.join(classes)
        return f'<h1 class="{class_str}" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500;">{inner}</h1>'
        
    content = re.sub(r'<h1([^>]*)>(.*?)</h1>', fix_h1, content)
    
    # 2. Update <h2>
    def fix_h2(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            if 'Cormorant Garamond' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem; ')
        else:
            attrs += ' style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem;"'
        return f"<h2{attrs}>{inner}</h2>"
        
    content = re.sub(r'<h2([^>]*)>(.*?)</h2>', fix_h2, content)
    
    # 3. Update <h3>
    def fix_h3(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            if 'Cormorant Garamond' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Cormorant Garamond\', serif; font-weight: 600; font-size: 1.6rem; ')
        else:
            attrs += ' style="font-family: \'Cormorant Garamond\', serif; font-weight: 600; font-size: 1.6rem;"'
        return f"<h3{attrs}>{inner}</h3>"
        
    content = re.sub(r'<h3([^>]*)>(.*?)</h3>', fix_h3, content)

    # 4. Explicitly set <p> and <li> text to Inter font
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
    
    def fix_li(match):
        attrs = match.group(1)
        inner = match.group(2)
        if 'style="' in attrs:
            if 'Inter' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Inter\', sans-serif; ')
        else:
            attrs += ' style="font-family: \'Inter\', sans-serif;"'
        return f"<li{attrs}>{inner}</li>"
        
    content = re.sub(r'<li([^>]*)>(.*?)</li>', fix_li, content, flags=re.DOTALL)
    
    return content

for f in policy_pages:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_policy_pages(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
