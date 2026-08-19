import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix the aggressive global heading color rule
css = re.sub(
    r'(h1:not\(\.hero-title\), h2, h3, h4, h5, h6, \.title, \.section-heading \.title\s*\{\s*color:\s*var\(--primary-green\))\s*!important(\s*;\s*\})',
    r'\1\2', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Removed !important from global heading colors")
