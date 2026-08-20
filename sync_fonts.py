import os
import glob
import re

# 1. Update style.css to enforce font-weight: 500 on all headings
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add a synchronized font weight rule at the end of style.css
css += """

/* ==========================================================================
   SYNCHRONIZED FONT WEIGHTS FOR ALL PAGES
   ========================================================================== */
h1, h2, h3, h4, h5, h6, 
.title, .section-heading .title, .hero-title,
.hero-title span.highlight,
.navbar-brand, .value-card h4, .benefit-card h5 {
    font-weight: 500 !important;
}
"""
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)


# 2. Strip inline font-weight attributes and fw-bold/fw-bolder/fw-semibold classes 
# from all HTML files to ensure they don't override our synchronized CSS.
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Remove inline font-weight styles from HTML tags
    # matches style="... font-weight: 123; ..."
    html = re.sub(r'(style="[^"]*)font-weight:\s*[^;"]+;?\s*', r'\1', html)
    # clean up empty style tags if any
    html = html.replace('style=""', '')
    
    # Replace bootstrap fw-bold classes
    html = re.sub(r'\bfw-bold\b', 'fw-medium', html)  # fw-medium is 500 in bootstrap 5
    html = re.sub(r'\bfw-bolder\b', 'fw-medium', html)
    html = re.sub(r'\bfw-semibold\b', 'fw-medium', html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Synchronized all font weights!")
