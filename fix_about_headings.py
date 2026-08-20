import re

filepath = 'about.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<h2 class="mb-4"', '<h2 class="section-title mb-4"')
content = content.replace('<h2 style=" font-size: 2.0rem;', '<h2 class="section-title" style="font-size: 2.0rem;')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
