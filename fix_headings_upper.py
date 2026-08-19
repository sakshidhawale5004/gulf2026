import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old uppercase rule
content = re.sub(r'h1, h2, h3, \.h1, \.h2, \.h3\s*\{[^}]*\}', '', content)

# Add a much more polished version
new_rule = '''
h1, h2, h3, .h1, .h2, .h3 {
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-weight: 600 !important;
}

/* Ensure sub-headings don't get too overwhelmingly large */
h3, .h3 {
    letter-spacing: 0.06em !important;
    font-weight: 700 !important;
}
'''
content += new_rule

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
