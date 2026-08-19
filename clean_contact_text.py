import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace all occurrences of contact-hero .container in the forced white text lists
css = css.replace(', .contact-hero .container .contact-heading', '')
css = css.replace(', .contact-hero .container .breadcrumb-text', '')
css = css.replace(', .contact-hero .container p', '')
css = css.replace(', .contact-hero .container a', '')
css = css.replace('.contact-hero .container p, ', '')

# Ensure we have dark text for contact hero explicitly
css += """
.contact-hero .container {
    color: #333 !important;
}
.contact-hero .container .contact-heading {
    color: var(--primary-green-dark) !important;
}
.contact-hero .container p {
    color: #555 !important;
}
"""

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done cleaning contact-hero white text rules")
