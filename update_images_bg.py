import re

# 1. Replace duplicate image in about.html
with open('about.html', 'r', encoding='utf-8') as f:
    about_html = f.read()

about_html = about_html.replace('about.imagestarting1.jpg?v=2', 'Gulf Company Database-final1234 The Gold Standard in Data.jpg')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(about_html)


# 2. Update background image in style.css for comparables-data-section
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'(\.comparables-data-section\s*\{[^}]*background:\s*url\(")bg\.jpg("\))', r'\1background.jpg\2', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 3. Replace image in index.html for Transfer Pricing Implementation Steps
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the specific image in the tp-implementation-section
tp_idx = index_html.find('Transfer Pricing Implementation Steps Section')
if tp_idx != -1:
    img_idx = index_html.find('<img src="We Provide The Best Transfer Pricing Data in the GCC-2ndimage.webp"', tp_idx)
    if img_idx != -1:
        end_quote = index_html.find('"', img_idx + 10)
        end_quote = index_html.find('"', end_quote + 1)
        index_html = index_html[:img_idx] + '<img src="Transfer Pricing Implementation Steps.jpg"' + index_html[end_quote+1:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

print("Done")
