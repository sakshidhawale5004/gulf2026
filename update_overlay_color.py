import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the existing .hero-overlay block entirely
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
      rgba(18, 102, 77, 1.0) 0%,
      rgba(18, 102, 77, 0.95) 45%,
      rgba(18, 102, 77, 0.85) 75%,
      rgba(18, 102, 77, 0.50) 100%
    ) !important;
    z-index: 1 !important;
}
"""

css = re.sub(r'/\* Super Dark Hero Overlay \*/\s*\.hero-overlay\s*\{[^}]+\}', new_overlay.strip(), css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
