import re
import glob

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the Google Fonts import
old_import = r"@import url\('https://fonts\.googleapis\.com/css2\?family=Manrope[^']+'\);"
new_import = "@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700;800&display=swap');"
if re.search(old_import, css):
    css = re.sub(old_import, new_import, css)
else:
    css = new_import + "\n" + css

# Replace all font-family definitions in CSS
css = re.sub(r"font-family:\s*['\"]?(?:Manrope|Plus Jakarta Sans|Inter|Cormorant Garamond)[^;]+;", "font-family: 'GT Walsheim', 'Outfit', sans-serif;", css)

# Make sure body has the new font
css = re.sub(r"font-family:\s*sans-serif;", "font-family: 'GT Walsheim', 'Outfit', sans-serif;", css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Update all HTML files to remove inline font-families
html_files = glob.glob('*.html')
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace inline styles like font-family: 'Inter', sans-serif !important;
    html = re.sub(r"font-family:\s*['\"]?(?:Manrope|Plus Jakarta Sans|Inter|Cormorant Garamond)[^;]+;?", "font-family: 'GT Walsheim', 'Outfit', sans-serif;", html)
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Done updating fonts globally")
