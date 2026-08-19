import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Remove .contact-hero .container from the half-half gradient
old_half_half = ".page-hero .container, .hero-banner .container, .contact-hero .container, .subscription-hero .container {"
new_half_half = ".page-hero .container, .hero-banner .container, .subscription-hero .container {"
css = css.replace(old_half_half, new_half_half)

# Make sure contact-hero container is white
css += "\n.contact-hero .container { background: #ffffff !important; }\n"

# Remove the newsletter-hero background image
css = re.sub(r'\.newsletter-hero\s*\{[^}]*background:[^}]*newsletter-bg\.jpg[^}]*\}[^}]*\}?', '', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
