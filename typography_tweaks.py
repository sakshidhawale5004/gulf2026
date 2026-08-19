import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add typographic refinements for GT Walsheim
typography_tweaks = """
/* Typographic refinements for GT Walsheim / Geometric style */
body {
    letter-spacing: 0.01em;
    line-height: 1.7;
}
h1, h2, h3, h4, h5, h6, .hero-title, .section-title {
    letter-spacing: -0.015em;
    line-height: 1.25;
}
.text-uppercase {
    letter-spacing: 0.08em;
}
p {
    margin-bottom: 1.5rem;
}
"""

css += typography_tweaks

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
