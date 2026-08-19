import re
import glob

# 1. Fix about.html duplicate image
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The second storytelling section has Expert Support
story_sec_2_idx = html.find('Expert Support for Your Transfer Pricing Needs')
if story_sec_2_idx != -1:
    # Find the image tag right after this
    img_idx = html.find('<img src="about.imagestarting1.jpg"', story_sec_2_idx)
    if img_idx != -1:
        end_quote = html.find('"', img_idx + 10)
        end_quote = html.find('"', end_quote + 1)
        old_img = html[img_idx:end_quote+1]
        html = html[:img_idx] + '<img src="Expert Support for Your Transfer Pricing Needs.jpg"' + html[end_quote+1:]
        
with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)


# 2. Fix layout in database pages (gulf, interest, services, ip-licensing)
pages = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'services-database.html',
    'ip-licensing-database.html'
]

for page in pages:
    try:
        with open(page, 'r', encoding='utf-8') as f:
            html = f.read()
        
        # We have multiple <div class="row content-block align-items-center...
        # We want to alternate them. The first is normal, the second should be flex-md-row-reverse
        # Also improve image heights
        
        blocks = list(re.finditer(r'<div class="row content-block align-items-center(.*?)"', html))
        if len(blocks) >= 2:
            # Modify the second block to have flex-md-row-reverse
            second_block = blocks[1]
            old_class = second_block.group(0)
            if 'flex-md-row-reverse' not in old_class:
                new_class = old_class.replace('align-items-center', 'align-items-center flex-md-row-reverse')
                html = html[:second_block.start()] + new_class + html[second_block.end():]
                
        # Improve all image styles inside content-blocks
        html = re.sub(r'max-height:\s*300px;', 'min-height: 350px; max-height: 450px;', html)
        
        with open(page, 'w', encoding='utf-8') as f:
            f.write(html)
            
    except FileNotFoundError:
        print(f"Skipping {page}, not found.")

print("Done")
