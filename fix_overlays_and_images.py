import re
import glob

# 1. Fix index.html overlays
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove overlay in comparables-data-section
html = re.sub(r'<div class="position-absolute top-0 start-0 w-100 h-100" style="background-color: rgba\(0,0,0,0\.15\); z-index: 1;"></div>', '', html)

# Remove overlay in newsletter-hero
html = re.sub(r'<div style="position: absolute; top:0; left:0; right:0; bottom:0; background: rgba\(0,0,0,0\.62\); z-index: 1;"></div>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix image alignment in all HTML files
html_files = glob.glob('*.html')
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        file_html = f.read()
    
    # Add Bootstrap fluid, 100% width, rounded corners, and shadow to the standalone images
    # We look for <img ... style="max-height: 300px; object-fit: cover;">
    # and ensure it has class="img-fluid w-100 rounded-4 shadow-sm"
    
    def add_classes(match):
        img_tag = match.group(0)
        if 'class="' in img_tag:
            # If it already has classes, append to them
            new_img_tag = re.sub(r'class="([^"]*)"', r'class="\1 img-fluid w-100 rounded-4 shadow-sm"', img_tag)
        else:
            # Add class attribute
            new_img_tag = img_tag.replace('<img ', '<img class="img-fluid w-100 rounded-4 shadow-sm" ')
        return new_img_tag

    updated_html = re.sub(r'<img[^>]*style="max-height: 300px; object-fit: cover;"[^>]*>', add_classes, file_html)
    
    if updated_html != file_html:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(updated_html)

print("Done")
