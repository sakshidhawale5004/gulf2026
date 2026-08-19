import os

for filename in ['about.html', 'our-data-methodology.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('fill="#0b1120"', 'fill="var(--primary-green)"')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
