import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the background image in comparables-data-section
html = re.sub(r'(<section class="comparables-data-section[^>]+)style="background:\s*url\([^)]+\)[^"]+"', r'\1', html)
# Replace the background image in newsletter-section
html = re.sub(r'(<section class="newsletter-section[^>]+)style="background:\s*url\([^)]+\)[^"]+"', r'\1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Remove stock image backgrounds and use premium un-stock deep teal background */
.comparables-data-section, .newsletter-section {
    background-color: var(--deep-teal) !important;
    background-image: radial-gradient(circle at 80% 20%, rgba(0, 107, 87, 0.4) 0%, transparent 60%) !important;
    position: relative;
    overflow: hidden;
}
/* Ensure the inner overlay doesn't darken the deep teal too much */
.comparables-data-section > .position-absolute, .newsletter-section > .position-absolute {
    background-color: transparent !important;
}
""")
