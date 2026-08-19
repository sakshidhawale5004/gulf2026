import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Make absolutely sure there is no sub-pixel gap
content = content.replace(
    '''.footer-wave svg {
    display: block;
    width: 100%;
    height: 120px;
}''',
    '''.footer-wave svg {
    display: block;
    width: calc(100% + 4px);
    height: 120px;
    margin-left: -2px;
}'''
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
