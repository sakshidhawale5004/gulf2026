import glob
import re

for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We want to remove color: #333;, color: #666;, color: #1a1a1a; from inline styles in headings.
    # We can just remove `color: #[0-9a-fA-F]{3,6};` from headings, EXCEPT if it's white (#fff, #ffffff).
    # But wait, earlier I also saw color: #0a6b4f (old primary green), let's remove that too so they all use the CSS variable var(--primary-green) perfectly.
    
    def heading_replacer(match):
        tag = match.group(0)
        # Only strip colors that are NOT white.
        # Actually, let's just strip #333, #666, #1a1a1a, #0a6b4f, #000, #333333, #666666
        tag = re.sub(r'color:\s*#(?:333333|333|666666|666|1a1a1a|0a6b4f|000000|000)\s*;?\s*', '', tag, flags=re.IGNORECASE)
        # Clean empty style tags
        tag = tag.replace('style=""', '')
        tag = tag.replace('style=" "', '')
        return tag
    
    html = re.sub(r'<h[1-6][^>]*>', heading_replacer, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Synchronized heading colors by removing dark inline colors")
