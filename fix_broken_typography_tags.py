import codecs
import re

files = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html'
]

def fix_broken_tags(content):
    # Fix <h6>
    # We have things like: <h6 text-white mb-1 style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.25rem;">
    # It might be `mb-0` or `text-white` or whatever was originally in the class.
    # The pattern is <h6 (some words) style="...">
    
    def fix_h6(match):
        classes = match.group(1).strip()
        style = match.group(2)
        inner = match.group(3)
        return f'<h6 class="{classes}" {style}>{inner}</h6>'
        
    # Match <h6 something something style="...">
    # Be careful not to match class="something" if it already has class
    content = re.sub(r'<h6\s+([^c>]*?)\s*(style="[^"]*")\s*>(.*?)</h6>', fix_h6, content)
    
    # Fix <p>
    def fix_p(match):
        classes = match.group(1).strip()
        style = match.group(2)
        inner = match.group(3)
        return f'<p class="{classes}" {style}>{inner}</p>'
        
    content = re.sub(r'<p\s+([^c>]*?)\s*(style="[^"]*")\s*>(.*?)</p>', fix_p, content)

    # Fix <small>
    def fix_small(match):
        classes = match.group(1).strip()
        style = match.group(2)
        inner = match.group(3)
        return f'<small class="{classes}" {style}>{inner}</small>'
        
    content = re.sub(r'<small\s+([^c>]*?)\s*(style="[^"]*")\s*>(.*?)</small>', fix_small, content)

    return content

for f in files:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = fix_broken_tags(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Fixed {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
