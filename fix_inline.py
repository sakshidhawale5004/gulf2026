import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Fix inline styles in newsletter-hero
html = re.sub(r'(<section class="newsletter-hero[^>]+)style="background:\s*url\([^)]+\)[^"]+"', r'\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Make sure the text on the backgrounds is visible */
.comparables-data-section .text-white, .newsletter-hero .text-white {
    text-shadow: 0 2px 4px rgba(0,0,0,0.5);
}
""")
