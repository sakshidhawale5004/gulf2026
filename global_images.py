import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add the new global image styling rule
new_rule = """
/* ==========================================================================
   GLOBAL CONTENT IMAGE STYLING (Padding & Radius)
   ========================================================================== */
img:not(header img):not(nav img):not(footer img):not(.footer img):not([style*="absolute"]):not(.navbar-brand img):not(.hero-section img):not(.hero img):not(.hero-right-img img) {
    border-radius: 20px !important;
    padding: 20px !important;
    background-color: #ffffff !important;
    box-sizing: border-box !important;
    /* Adding a subtle border so the padding frame is visible on white backgrounds */
    border: 1px solid rgba(8, 102, 75, 0.08) !important;
}
"""

if "GLOBAL CONTENT IMAGE STYLING" not in css:
    css += new_rule

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Added global image styling to style.css")
