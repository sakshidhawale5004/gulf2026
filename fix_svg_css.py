import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('width: calc(100% + 1.3px);', 'width: 100%;')

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
