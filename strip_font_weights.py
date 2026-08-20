import glob
import re

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # 1. Strip fw-bold, fw-semibold, fw-bolder classes
    html = re.sub(r'\b(fw-bold|fw-semibold|fw-bolder)\b', '', html)
    
    # 2. Replace inline font-weight: 600; font-weight: 700; etc with font-weight: 500;
    html = re.sub(r'font-weight:\s*[6789]00\s*!?', 'font-weight: 500', html)
    html = re.sub(r'font-weight:\s*bold\s*!?', 'font-weight: 500', html)
    
    # Clean up empty class="" attributes just in case
    html = re.sub(r'class="\s+"', '', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Stripped all aggressive font weights from all HTML files")
