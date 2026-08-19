import os
import re

files_solutions = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]

for f in files_solutions:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('rgba(10, 107, 79, 0.85), rgba(10, 107, 79, 0.85)', 'rgba(10, 107, 79, 0.98), rgba(10, 107, 79, 0.98)')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

files_regulations_with_grad = [
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html'
]

for f in files_regulations_with_grad:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace('rgba(10, 107, 79, 0.80), rgba(5, 55, 38, 0.93)', 'rgba(10, 107, 79, 0.98), rgba(5, 55, 38, 0.98)')
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

files_regulations_no_grad = [
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]

for f in files_regulations_no_grad:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = re.sub(
        r"background:\s*url\('([^']+)'\)",
        r"background: linear-gradient(rgba(10, 107, 79, 0.98), rgba(10, 107, 79, 0.98)), url('\1')",
        content
    )
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)

# Contact page
with open('contact.html', 'r', encoding='utf-8') as file:
    content = file.read()
content = content.replace(
    '<h1 class="contact-heading" style="font-weight: 300; text-transform: uppercase; text-align: left;">',
    '<h1 class="contact-heading" style="color: white !important; font-weight: 300; text-transform: uppercase; text-align: left;">'
)
with open('contact.html', 'w', encoding='utf-8') as file:
    file.write(content)

# About page
with open('about.html', 'r', encoding='utf-8') as file:
    content = file.read()

# Make heading and text same style as home page
content = content.replace(
    '<h1 class="hero-title">About</h1>',
    '<h1 class="hero-title" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 3.8rem; line-height: 1.15; letter-spacing: -1px;">About</h1>'
)
content = content.replace(
    '<p class="hero-breadcrumb">Home - About</p>',
    '<p class="hero-breadcrumb" style="max-width: 540px; line-height: 1.7; font-family: \'Inter\', sans-serif !important; font-weight: 200 !important; font-size: 1.2rem; margin: 0 auto;">Home - About</p>'
)
with open('about.html', 'w', encoding='utf-8') as file:
    file.write(content)

print("Updates completed successfully.")
