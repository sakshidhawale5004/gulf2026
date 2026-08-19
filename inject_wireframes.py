import re

# Remove the old buggy ::after CSS
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'/\* ==+[^=]+3D WIREFRAME OBJECT.*?(?=\Z|/\*)', '', css, flags=re.DOTALL)

# Add the new robust pure CSS 3D object
new_css = """
/* ==========================================================================
   3D WIREFRAME OBJECT FOR INNER HEROES
   ========================================================================== */
.hero-3d-wireframe {
    position: absolute;
    right: 5%;
    top: 50%;
    transform: translateY(-50%);
    width: 250px;
    height: 250px;
    pointer-events: none;
    z-index: 1;
}

.hero-3d-wireframe .shape {
    position: absolute;
    top: 0; left: 0; right: 0; bottom: 0;
    border: 3px solid #0a6b4f;
    border-radius: 60px;
    animation: spinShape linear infinite;
}

.hero-3d-wireframe .shape:nth-child(1) {
    animation-duration: 20s;
    opacity: 0.8;
}

.hero-3d-wireframe .shape:nth-child(2) {
    animation-duration: 25s;
    animation-direction: reverse;
    opacity: 0.6;
    border-width: 2px;
    transform: rotate(45deg);
}

.hero-3d-wireframe .shape:nth-child(3) {
    animation-duration: 30s;
    opacity: 0.4;
    border-width: 1px;
    border-radius: 80px;
    transform: rotate(20deg);
}

@keyframes spinShape {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

.page-hero .container, .hero-banner .container, .subscription-hero .container {
    position: relative;
    overflow: hidden;
}
"""

css += new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Inject the HTML via a Python script across all HTML files
import glob

html_files = glob.glob('*.html')
for html_file in html_files:
    if html_file in ['index.html', 'contact.html']:
        continue # Skip home and contact pages as requested
        
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # We want to insert <div class="hero-3d-wireframe"><div class="shape"></div><div class="shape"></div><div class="shape"></div></div>
    # right inside the container of the hero section.
    
    # Let's find <div class="container"> or <div class="container hero-content"> inside hero sections
    hero_pattern = r'(<section[^>]*class="[^"]*(?:page-hero|hero-banner|subscription-hero)[^"]*"[^>]*>\s*(?:<div class="hero-overlay"></div>\s*)?<div class="container[^"]*">)'
    
    # Replacement string
    wireframe_html = r'\1\n        <div class="hero-3d-wireframe"><div class="shape"></div><div class="shape"></div><div class="shape"></div></div>'
    
    # Apply
    new_html = re.sub(hero_pattern, wireframe_html, html)
    
    if new_html != html:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(new_html)

print("Done injecting HTML wireframes")
