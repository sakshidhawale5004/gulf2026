import re

for filename in ['about.html', 'index.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('aboutpageimage.jpg', 'about.imagestarting1.jpg')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
