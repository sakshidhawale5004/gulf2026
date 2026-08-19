import re

# 1. Fix contact.html glass styling
with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace white glass styling with dark styling
html = html.replace('border: 1px solid rgba(255, 255, 255, 0.5);', 'border: 1px solid rgba(0, 0, 0, 0.15);')
html = html.replace('.glass-input {\n        background: transparent;\n        border: 1px solid rgba(0, 0, 0, 0.15);\n        color: white;', '.glass-input {\n        background: transparent;\n        border: 1px solid rgba(0, 0, 0, 0.15);\n        color: #333;')
html = html.replace('.glass-input::placeholder {\n        color: rgba(255, 255, 255, 0.7);\n    }', '.glass-input::placeholder {\n        color: rgba(0, 0, 0, 0.5);\n    }')
html = html.replace('background: rgba(255, 255, 255, 0.1);', 'background: rgba(0, 0, 0, 0.05);')
html = html.replace('border-color: white;', 'border-color: var(--primary-green);')
html = html.replace('.glass-input:focus {\n        background: rgba(0, 0, 0, 0.05);\n        border-color: var(--primary-green);\n        color: white;', '.glass-input:focus {\n        background: rgba(0, 0, 0, 0.05);\n        border-color: var(--primary-green);\n        color: #333;')
html = html.replace('.glass-select {\n        background: transparent;\n        border: 1px solid rgba(0, 0, 0, 0.15);\n        color: white;', '.glass-select {\n        background: transparent;\n        border: 1px solid rgba(0, 0, 0, 0.15);\n        color: #333;')
html = html.replace('background: rgba(255, 255, 255, 0.2);', 'background: rgba(0, 107, 87, 0.1); color: var(--primary-green);')

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix MORE DARK TEAL in hero-overlay (index.html hero)
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the hero-overlay gradient
old_overlay = """.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      90deg,
      rgba(0, 55, 55, 0.85) 0%,
      rgba(0, 55, 55, 0.65) 35%,
      rgba(0, 35, 35, 0.35) 65%,
      rgba(0, 20, 20, 0.15) 100%
    ) !important;
}"""

new_overlay = """.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      90deg,
      rgba(0, 35, 30, 0.95) 0%,
      rgba(0, 45, 40, 0.85) 35%,
      rgba(0, 50, 45, 0.55) 65%,
      rgba(0, 55, 55, 0.35) 100%
    ) !important;
}"""

if old_overlay in css:
    css = css.replace(old_overlay, new_overlay)
else:
    # If it was slightly different, just append to override
    css += "\n" + new_overlay

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
