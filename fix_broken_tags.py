import codecs
import re

form_pages = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html'
]

def fix_broken_html(c):
    # Find <class="display-5 fw-bold mb-4 text-white text-uppercase " h1>
    # and replace with <h1 class="display-5 fw-bold mb-4 text-white text-uppercase">
    # Wait, in the output it was:
    # <class="display-5 fw-bold mb-4" h1>Request a GCC Benchmark Search</class="display-5 fw-bold mb-4">
    # Let's fix that.
    
    def replacer(match):
        attrs = match.group(1) # e.g. class="..." 
        tag = match.group(2) # e.g. h1
        inner = match.group(3)
        
        # fix the attrs by adding text-white text-uppercase if needed
        if 'text-white' not in attrs:
            attrs = attrs.replace('class="', 'class="text-white text-uppercase ')
        
        return f"<{tag} {attrs}>{inner}</{tag}>"

    c = re.sub(r'<(class="[^"]*")\s*(h[1-2])>(.*?)</class="[^"]*">', replacer, c)
    return c

for p in form_pages:
    try:
        with codecs.open(p, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        new_content = fix_broken_html(content)
        if new_content != content:
            with codecs.open(p, 'w', encoding='utf-8-sig') as f:
                f.write(new_content)
            print(f"Fixed {p}")
        else:
            print(f"No changes in {p}")
    except Exception as e:
        print(f"Error {p}: {e}")
