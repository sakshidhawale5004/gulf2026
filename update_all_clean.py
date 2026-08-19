import os
import re
import codecs

def update_file(filename, callback):
    try:
        with codecs.open(filename, 'r', encoding='utf-8-sig') as f:
            content = f.read()
        new_content = callback(content)
        if new_content != content:
            with codecs.open(filename, 'w', encoding='utf-8-sig') as f:
                f.write(new_content)
    except Exception as e:
        print(f"Error processing {filename}: {e}")

# 1. Solutions Pages
solutions_pages = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]
def fix_solutions(content):
    content = content.replace(
        'background: linear-gradient(rgba(10, 107, 79, 0.85), rgba(10, 107, 79, 0.85))',
        'background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95))'
    )
    return content

for sp in solutions_pages:
    update_file(sp, fix_solutions)

# 2. Regulations with Gradients
reg_with_grad = [
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html'
]
def fix_reg_grad(content):
    content = content.replace(
        'background: linear-gradient(rgba(10, 107, 79, 0.80), rgba(5, 55, 38, 0.93))',
        'background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95))'
    )
    return content

for rp in reg_with_grad:
    update_file(rp, fix_reg_grad)

# 3. Regulations without Gradients
reg_no_grad = [
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]
def fix_reg_no_grad(content):
    # Only replace the background property inside .page-hero
    # Using regex to target exactly background: url(...)
    def repl(m):
        return f"background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95)), url('{m.group(1)}')"
    return re.sub(r"background:\s*url\('([^']+)'\)", repl, content)

for rp in reg_no_grad:
    update_file(rp, fix_reg_no_grad)

# 4. Contact Page
def fix_contact(content):
    # Fix heading
    content = content.replace(
        '<h1 class="contact-heading" style="font-weight: 300; text-transform: uppercase; text-align: left;">',
        '<h1 class="contact-heading" style="color: white !important; font-weight: 300; text-transform: uppercase; text-align: left;">'
    )
    # Fix emails and whatsapp
    content = content.replace('<h5 class="mb-1">Email us</h5>', '<h5 class="mb-1 text-white">Email us</h5>')
    content = content.replace('<p class="mb-0 text-white-50">admin@gulftp.com</p>', '<p class="mb-0 text-white">admin@gulftp.com</p>')
    content = content.replace('<h5 class="mb-1">WhatsApp us</h5>', '<h5 class="mb-1 text-white">WhatsApp us</h5>')
    content = content.replace('<p class="mb-0 text-white-50">+971 581711600</p>', '<p class="mb-0 text-white">+971 581711600</p>')
    return content

update_file('contact.html', fix_contact)

# 5. About Page
def fix_about(content):
    # Fix padding in .hero-banner
    content = content.replace('padding: 110px 0;', 'padding: 80px 0;')
    # Fix styling
    content = content.replace(
        '<h1 class="hero-title">About</h1>',
        '<h1 class="hero-title" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 3.8rem; line-height: 1.15; letter-spacing: -1px;">About</h1>'
    )
    content = content.replace(
        '<p class="hero-breadcrumb">Home - About</p>',
        '<p class="hero-breadcrumb" style="max-width: 540px; line-height: 1.7; font-family: \'Inter\', sans-serif !important; font-weight: 200 !important; font-size: 1.2rem; margin: 0 auto;">Home - About</p>'
    )
    return content

update_file('about.html', fix_about)

print("Update clean script complete.")
