import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix the hero text alignment
old_hero_text = """Unlock Over <br>
                            <span style="color: var(--primary-orange);">100,000+</span><br>
                            Comparable<br>
                            Companies"""
                            
new_hero_text = """Unlock Over<br>
<span style="color: var(--primary-orange);">100,000+</span><br>
Comparable<br>
Companies"""
html = html.replace(old_hero_text, new_hero_text)

# Also fix it just in case the indentation in my string above doesn't perfectly match
html = re.sub(r'Unlock Over\s*<br>\s*<span style="color: var\(--primary-orange\);">100,000\+</span><br>\s*Comparable<br>\s*Companies', new_hero_text, html)

# Fix the image source in the Advanced Technology section
old_img = 'src="homepageimage.webp" alt="Cloud Computing and AI Technology"'
new_img = 'src="data-analytics-tech.jpg" alt="Powered by Cutting-Edge Data Analytics"'
html = html.replace(old_img, new_img)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated index.html")
