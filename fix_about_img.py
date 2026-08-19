import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'(<div class="story-image-box">[\s\S]*?<img\s+src=")[^"]+("[^>]*>)', r'\g<1>aboutpageimage.jpg\g<2>', html)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
