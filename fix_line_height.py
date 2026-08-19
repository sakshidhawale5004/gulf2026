import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the block
content = content.replace(
'''h1, h2, h3, .h1, .h2, .h3 {
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-weight: 600 !important;
}''',
'''h1, h2, h3, .h1, .h2, .h3 {
    text-transform: uppercase !important;
    letter-spacing: 0.08em !important;
    font-weight: 600 !important;
    line-height: 1.35 !important;
}'''
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
