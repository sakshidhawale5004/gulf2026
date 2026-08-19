with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('100000', '0')
content = content.replace('100,000', '[XXX,XXX]')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
