import re

# 1. Restore style.css by replacing var(--deep-teal) !important back to white !important
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = css.replace('color: var(--deep-teal) !important;', 'color: #ffffff !important;')

# But wait, earlier I updated .hero-title to color: var(--deep-teal) without !important in my fix_hero_colors.py
# Let's revert that part too if it's there.
# I want .hero-title in style.css to be color: white; so inner pages stay white.
css = re.sub(r'(\.hero-title\s*\{[^}]*)color:\s*var\(--deep-teal\);', r'\1color: #ffffff;', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Modify index.html to override it inline or with text-dark !important using Bootstrap classes
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Add a style block at the top or just inline styles to the hero text
html = html.replace('class="hero-title text-dark mb-4"', 'class="hero-title mb-4" style="color: var(--deep-teal) !important;"')
html = html.replace('class="hero-subtitle text-muted mb-5"', 'class="hero-subtitle mb-5" style="color: #475569 !important; text-shadow: none !important;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Restored style.css for inner pages, applied inline fix to index.html")
