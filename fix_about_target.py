import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('data-target="0"', 'data-target="100000"')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
