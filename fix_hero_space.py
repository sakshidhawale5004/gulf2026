with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the class and style
old_str = 'class="hero-section position-relative overflow-hidden bg-white" style="min-height: 90vh;"'
new_str = 'class="hero-section position-relative overflow-hidden bg-white align-items-start" style="min-height: 80vh; padding-top: 3rem;"'

if old_str in html:
    html = html.replace(old_str, new_str)
    print("Replaced!")
else:
    print("Not found.")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
