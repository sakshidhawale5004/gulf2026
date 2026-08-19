import re

# Read index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Images
# Services Database
html = re.sub(r'<img\s+src="[^"]*"\s+alt="Services Database"[^>]*>', '<img src="Services Database.jpg" alt="Services Database" class="card-img-top">', html)
# Interest Rates
html = re.sub(r'<img\s+src="[^"]*"\s+alt="Interest Rates"[^>]*>', '<img src="Interest Rates.jpg" alt="Interest Rates" class="card-img-top">', html)
# IP Licensing
html = re.sub(r'<img\s+src="[^"]*"\s+alt="IP Licensing"[^>]*>', '<img src="IP Licensing.jpg" alt="IP Licensing" class="card-img-top">', html)

# Expert Support for Your Transfer Pricing Needs
html = re.sub(r'<img\s+src="[^"]*"\s+alt="Transfer Pricing Experts"[^>]*>', '<img src="Expert Support for Your Transfer Pricing Needs.jpg" alt="Transfer Pricing Experts" class="img-fluid rounded shadow-lg">', html)
html = re.sub(r'<img\s+src="[^"]*"\s+alt="Transfer Pricing Data Dashboard"[^>]*>', '<img src="Expert Support for Your Transfer Pricing Needs.jpg" alt="Transfer Pricing Data Dashboard" class="img-fluid rounded shadow-lg">', html)
# Let's just blindly replace the image source near "Expert Support for Your Transfer Pricing Needs" if we don't know the alt tag.
# We will use regex to find the section and replace the img tag.

# Transfer Pricing Implementation Steps
html = re.sub(r'<img\s+src="[^"]*"\s+alt="Transfer Pricing Workflow"[^>]*>', '<img src="Transfer Pricing Implementation Steps.jpg" alt="Transfer Pricing Workflow" class="img-fluid rounded shadow-lg sticky-top" style="top: 100px;">', html)

# 2. Remove "Our data methodology"
# Assuming it's a section. Let's find it.
# We will use regex to remove any section or div containing "Our data methodology" as heading.
html = re.sub(r'<section[^>]*>[\s\S]*?(?:Our data methodology|Data Methodology)[\s\S]*?</section>', '', html, flags=re.IGNORECASE)

# 3. Remove "Update Cadence Quarterly updates..."
html = html.replace('Update Cadence\nQuarterly updates to ensure alignment with shifting regional service costs.', '')
html = re.sub(r'<[^>]+>\s*Update Cadence\s*</[^>]+>\s*<[^>]+>\s*Quarterly updates to ensure alignment with shifting regional service costs.\s*</[^>]+>', '', html, flags=re.IGNORECASE)

# Write index.html
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# Read style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 4. Hero BG Overlay: make it something different (lighter, more vibrant, transparent)
# It was: linear-gradient(135deg, rgba(15, 23, 42, 0.75) 0%, rgba(2, 6, 23, 0.85) 100%)
new_overlay = 'linear-gradient(135deg, rgba(8, 102, 75, 0.4) 0%, rgba(245, 145, 32, 0.3) 100%)' # Soft green to orange transparent
css = re.sub(r'linear-gradient\(135deg,\s*rgba\(15,\s*23,\s*42[^)]+\)\s*0%,\s*rgba\([^)]+\)\s*100%\)', new_overlay, css)

# 5. All headings same color
heading_css = """
/* Consistent Heading Colors */
h1:not(.hero-title), h2, h3, h4, h5, h6, .title, .section-heading .title {
    color: var(--primary-green) !important;
}
.hero-title {
    color: #ffffff !important;
}
"""
if "Consistent Heading Colors" not in css:
    css += heading_css

# 6. 3D Buttons
button_3d_css = """
/* 3D Button Effects */
.btn, .btn-conxora, .btn-orange, .btn-submit, .btn-outline-conxora {
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 0px rgba(8, 102, 75, 0.8) !important;
    transform: translateY(0) !important;
}
.btn-orange {
    box-shadow: 0 4px 0px rgba(200, 100, 10, 0.9) !important;
}
.btn-outline-conxora {
    box-shadow: 0 4px 0px rgba(8, 102, 75, 0.3) !important;
}
.btn:hover, .btn-conxora:hover, .btn-orange:hover, .btn-submit:hover, .btn-outline-conxora:hover {
    box-shadow: 0 6px 0px rgba(0,0,0,0.2) !important;
    transform: translateY(-2px) !important;
}
.btn:active, .btn-conxora:active, .btn-orange:active, .btn-submit:active, .btn-outline-conxora:active {
    box-shadow: 0 0px 0px rgba(0,0,0,0.2) !important;
    transform: translateY(4px) !important;
}
"""
if "3D Button Effects" not in css:
    css += button_3d_css

# Write style.css
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

