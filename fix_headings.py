import codecs
import re

def update_file(filepath, callback):
    try:
        with codecs.open(filepath, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        new_content = callback(content)
        if new_content != content:
            with codecs.open(filepath, 'w', encoding='utf-8-sig') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"No changes for {filepath}")
    except Exception as e:
        print(f"Error for {filepath}: {e}")

# 1. Update contact.html
def update_contact(c):
    c = c.replace(
        '<h1 class="contact-heading">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>',
        '<h1 class="contact-heading text-white text-uppercase">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>'
    )
    return c
update_file('contact.html', update_contact)

# 2. Update the left panel headings in form pages
form_pages = [
    'book-search.html',
    'book-a-demo.html',
    'book-an-appointment.html',
    'update-a-search.html',
    'buy-subscription.html'
]

def update_form_heading(c):
    # Find something like: <h1 class="display-5 fw-bold mb-4">Text</h1>
    # We will add text-white text-uppercase
    
    # regex to match h1 or h2 with display-5 or similar inside premium-left-panel
    # Actually, we can just look for class="display-5 fw-bold mb-4"
    # or class="display-5 fw-bold mb-3" etc.
    def replacer(match):
        attrs = match.group(1)
        tag = match.group(2)
        inner = match.group(3)
        # add text-white text-uppercase if not present
        if 'text-white' not in attrs:
            attrs = attrs.replace('class="', 'class="text-white text-uppercase ')
        return f"<{tag} {attrs}>{inner}</{tag}>"
    
    c = re.sub(r'<(h[1-2])\s+(class="display-\d\s+fw-bold[^"]*")[^>]*>(.*?)</\1>', replacer, c)
    return c

for p in form_pages:
    update_file(p, update_form_heading)
