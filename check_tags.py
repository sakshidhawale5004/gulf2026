import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

div_open = len(re.findall(r'<div\b[^>]*>', content))
div_close = len(re.findall(r'</div\s*>', content))
section_open = len(re.findall(r'<section\b[^>]*>', content))
section_close = len(re.findall(r'</section\s*>', content))

print(f"divs: +{div_open} -{div_close}")
print(f"sections: +{section_open} -{section_close}")
