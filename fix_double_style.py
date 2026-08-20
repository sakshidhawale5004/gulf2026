import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Merge double style tags
html = re.sub(r'style="([^"]+)"\s+style="([^"]+)"', r'style="\1 \2"', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed double style tags")
