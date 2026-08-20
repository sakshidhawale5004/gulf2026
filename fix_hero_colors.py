import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Fix .hero-title
css = re.sub(
    r'\.hero-title\s*\{[^}]*\}',
    r'.hero-title {\n    font-size: clamp(2.5rem, 4vw, 4.5rem);\n    line-height: 1.1;\n    color: var(--deep-teal);\n    margin-bottom: 1.5rem;\n    letter-spacing: -1px;\n}',
    css
)

# Fix .hero-subtitle
css = re.sub(
    r'\.hero-subtitle\s*\{[^}]*\}',
    r'.hero-subtitle {\n    font-size: 1.15rem;\n    color: #475569;\n    line-height: 1.7;\n    margin-bottom: 2.5rem;\n}',
    css
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print("Fixed hero text colors in style.css")
