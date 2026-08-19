import codecs
import re

files = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html'
]

def update_left_panel_headings(content):
    # Change font-weight: 600 to 500, and font-size: 1.25rem to 1.15rem
    target = r"font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.25rem;"
    replacement = r"font-family: 'Cormorant Garamond', serif; font-weight: 500; font-size: 1.15rem;"
    content = content.replace(target, replacement)
    
    # Also check for "Need direct assistance?" which might be h6 fw-bold
    # In book-a-demo.html it was: <h6 class="mb-1 fw-bold text-white">Need direct assistance?</h6>
    # Let's just make sure any remaining fw-bold in h5/h6 gets updated.
    
    def replace_h6_fwbold(match):
        attrs = match.group(1).replace('fw-bold', '').strip()
        inner = match.group(2)
        return f'<h6 class="{attrs}" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 1.15rem;">{inner}</h6>'
    
    content = re.sub(r'<h6 class="([^"]*fw-bold[^"]*)"[^>]*>(.*?)</h6>', replace_h6_fwbold, content)
    
    return content

for f in files:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_left_panel_headings(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
