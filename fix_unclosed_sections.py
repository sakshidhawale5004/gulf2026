import re

for filename in ['about.html', 'our-data-methodology.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove the empty unclosed section
    content = content.replace('    <section data-aos="fade-up" class="section-padding">\n', '')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
