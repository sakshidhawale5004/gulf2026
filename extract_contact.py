with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re

match = re.search(r'(<section data-aos="fade-up" class="contact-hero">.*?</section>)', html, re.DOTALL)
if match:
    section = match.group(1)
    print("Found section.")
else:
    print("Section not found.")
