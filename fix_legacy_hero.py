import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all rogue color overrides for .hero-title
# Find `color: white !important;` or `color: #ffffff !important;` inside blocks containing .hero-title
def remove_hero_title_white(match):
    block = match.group(0)
    # Only strip the color and text-shadow rules so we don't break layout
    block = re.sub(r'color:\s*(?:white|#ffffff)\s*!important;', 'color: var(--deep-teal) !important;', block)
    block = re.sub(r'text-shadow:[^;]+;', 'text-shadow: none !important;', block)
    return block

css = re.sub(r'\.hero-title[^\{]*\{[^}]+\}', remove_hero_title_white, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed legacy hero-title overrides")
