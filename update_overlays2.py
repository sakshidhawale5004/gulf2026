import os
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html',
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html',
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]

for f in files_all:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace any existing rgba(10, 107, 79, 0.98) or similar with the darker green
    content = re.sub(
        r"linear-gradient\([^)]+\)",
        "linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95))",
        content
    )
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Contact page
with open('contact.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Make "Email us" etc. white
content = content.replace('<h5 class="mb-1">Email us</h5>', '<h5 class="mb-1 text-white">Email us</h5>')
content = content.replace('<p class="mb-0 text-white-50">admin@gulftp.com</p>', '<p class="mb-0 text-white">admin@gulftp.com</p>')
content = content.replace('<h5 class="mb-1">WhatsApp us</h5>', '<h5 class="mb-1 text-white">WhatsApp us</h5>')
content = content.replace('<p class="mb-0 text-white-50">+971 581711600</p>', '<p class="mb-0 text-white">+971 581711600</p>')

with open('contact.html', 'w', encoding='utf-8') as file:
    file.write(content)

# About page
with open('about.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Change padding from 110px 0 to 80px 0
content = content.replace('padding: 110px 0;', 'padding: 80px 0;')

with open('about.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Updates completed successfully.")
