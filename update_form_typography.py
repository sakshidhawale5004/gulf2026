import codecs
import re

files = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html'
]

def process_html(content):
    # 1. Update the main heading: reduce size and font-weight 500 (consistent with index page)
    # The heading currently looks like: <h1 class="text-white text-uppercase display-5 fw-bold mb-4">
    # We want: <h1 class="text-white text-uppercase fs-2 mb-4" style="font-weight: 500;">
    content = re.sub(
        r'<h1 class="([^"]*)display-5\s+fw-bold([^"]*)">',
        r'<h1 class="\1fs-2\2" style="font-weight: 500;">',
        content
    )
    
    # 2. Update the feature/step h6 titles
    # They look like <h6 class="fw-bold mb-1"> or <h6 class="fw-bold mb-0"> or <h6 class="mb-1 fw-bold">
    # Wait, some might already have text-white.
    def replace_h6(match):
        attrs = match.group(1)
        inner_text = match.group(2)
        # We only want to apply this to the specific headings mentioned, but it's safe to apply to all in the left panel.
        # Let's just make all fw-bold h6's inside the left panel use Cormorant + white.
        # The easiest is to just replace 'fw-bold' with 'text-white' (if not present) and add style
        if 'text-white' not in attrs:
            attrs = attrs.replace('fw-bold', 'text-white')
        else:
            attrs = attrs.replace('fw-bold', '').replace('  ', ' ')
            
        style_str = "font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.25rem;"
        if 'style="' in attrs:
            attrs = attrs.replace('style="', f'style="{style_str} ')
        else:
            attrs += f' style="{style_str}"'
            
        return f"<h6 {attrs.strip()}>{inner_text}</h6>"
        
    content = re.sub(r'<h6\s+class="([^"]*fw-bold[^"]*)"[^>]*>(.*?)</h6>', replace_h6, content)
    
    # 3. Update the descriptions <p class="text-white-50..."> or <small class="text-white-50">
    # Add Inter font.
    def replace_desc(match):
        tag = match.group(1)
        attrs = match.group(2)
        inner = match.group(3)
        style_str = "font-family: 'Inter', sans-serif;"
        if 'style="' in attrs:
            attrs = attrs.replace('style="', f'style="{style_str} ')
        else:
            attrs += f' style="{style_str}"'
        return f"<{tag} {attrs.strip()}>{inner}</{tag}>"
        
    content = re.sub(r'<(p|small)\s+class="([^"]*text-white-50[^"]*)"[^>]*>(.*?)</\1>', replace_desc, content)
    
    return content

for f in files:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = process_html(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
