import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove rogue font-weight: 600 or 700 from heading elements.
css = re.sub(r'h3,\s*\.h3\s*\{[^}]*font-weight:\s*700\s*!important;[^}]*\}', '', css)

# Fix duplicate font-weights
css = re.sub(r'font-weight:\s*700;\s*font-weight:\s*500;', 'font-weight: 500;', css)
css = re.sub(r'font-weight:\s*600;\s*font-weight:\s*500;', 'font-weight: 500;', css)

# Make sure .value-card h4 is 500
css = re.sub(r'(\.value-card h4\s*\{[^}]*)font-weight:\s*600;', r'\1font-weight: 500;', css)

# Make sure .glass-card-title is 500
css = re.sub(r'(\.glass-card-title\s*\{[^}]*)font-weight:\s*700;', r'\1font-weight: 500;', css)

# Make sure .section-title is 500
css = re.sub(r'(\.section-title\s*\{[^}]*)font-weight:\s*700;', r'\1font-weight: 500;', css)

# Make sure the synchronized block at the bottom is definitely 500
css = css.replace('font-weight: 600 !important;', 'font-weight: 500 !important;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Synchronized all weights to 500")
