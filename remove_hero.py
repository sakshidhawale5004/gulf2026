import re

filename = 'buy-subscription.html'
with open(filename, 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the entire hero section
html_new = re.sub(r'<section data-aos="fade-up" class="hero-banner">.*?</section>\s*', '', html, flags=re.DOTALL)

with open(filename, 'w', encoding='utf-8') as f:
    f.write(html_new)
print("Removed hero section")
