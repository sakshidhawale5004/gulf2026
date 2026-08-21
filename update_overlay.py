import re

# Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the image
html = html.replace('src="Expert Support for Your Transfer Pricing Needs-FINAL1.jpg"', 'src="aboutpageimage.jpg"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find and replace all background properties inside .hero-overlay blocks
# Currently it is something like `background: linear-gradient(135deg, rgba(8, 102, 75, 0.4) 0%, rgba(245, 145, 32, 0.3) 100%);`
new_gradient = """background: linear-gradient(
  90deg,
  rgba(0, 82, 70, 0.88) 0%,
  rgba(0, 82, 70, 0.65) 35%,
  rgba(0, 82, 70, 0.25) 65%,
  rgba(0, 82, 70, 0.05) 100%
);"""

css = re.sub(r'background:\s*linear-gradient\([^;]+;', new_gradient, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
