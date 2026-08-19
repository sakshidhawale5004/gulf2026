import codecs
import re

files = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html'
]

def update_form_headings(content):
    # Match <h3 class="fw-bold mb-4" style="color: var(--primary-green);">...</h3>
    # and replace fw-bold with standard weight, size 2.0rem, Cormorant
    def replacer(match):
        attrs = match.group(1)
        inner = match.group(2)
        
        # Remove fw-bold
        attrs = attrs.replace('fw-bold', '').replace('  ', ' ')
        
        # Add explicit font-family, weight 500, size 2.0rem
        if 'style="' in attrs:
            if 'Cormorant Garamond' not in attrs:
                attrs = attrs.replace('style="', 'style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem; ')
        else:
            attrs += ' style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 2.0rem;"'
            
        return f"<h3{attrs}>{inner}</h3>"

    content = re.sub(r'<h3([^>]*)>(.*?)</h3>', replacer, content)
    return content

for f in files:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_form_headings(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
