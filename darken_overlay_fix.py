import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove all existing .hero-overlay blocks
css = re.sub(r'\.hero-overlay\s*\{[^}]+\}', '', css)

# Add the final super dark one
new_overlay = """
/* Super Dark Hero Overlay */
.hero-overlay {
    position: absolute !important;
    top: 0 !important;
    left: 0 !important;
    right: 0 !important;
    bottom: 0 !important;
    background: linear-gradient(
      90deg,
      rgba(0, 20, 15, 1.0) 0%,
      rgba(0, 25, 20, 0.95) 45%,
      rgba(0, 30, 25, 0.85) 75%,
      rgba(0, 35, 30, 0.50) 100%
    ) !important;
    z-index: 1 !important;
}
"""

css += new_overlay

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
