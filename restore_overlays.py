import os
import codecs
import re

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
def restore_solutions(content):
    content = content.replace(
        'background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95))',
        'background: linear-gradient(rgba(10, 107, 79, 0.85), rgba(10, 107, 79, 0.85))'
    )
    return content

for sp in solutions_pages:
    update_file(sp, restore_solutions)

# 2. Regulations with Gradients
reg_with_grad = [
    'bahrain-transfer-pricing.html',
    'egypt-transfer-pricing.html',
    'oman-transfer-pricing.html'
]
def restore_reg_grad(content):
    content = content.replace(
        'background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95))',
        'background: linear-gradient(rgba(10, 107, 79, 0.80), rgba(5, 55, 38, 0.93))'
    )
    return content

for rp in reg_with_grad:
    update_file(rp, restore_reg_grad)

# 3. Regulations without Gradients
reg_no_grad = [
    'qatar-transfer-pricing.html',
    'saudi-arabia-transfer-pricing-benchmarking.html',
    'uae-transfer-pricing.html'
]
def restore_reg_no_grad(content):
    # Remove the linear-gradient part and just leave the url
    # We added: background: linear-gradient(rgba(5, 55, 38, 0.95), rgba(5, 55, 38, 0.95)), url(...)
    # We want to revert to: background: url(...)
    def repl(m):
        return f"background: url('{m.group(1)}')"
    return re.sub(r"background:\s*linear-gradient\(rgba\(5, 55, 38, 0\.95\),\s*rgba\(5, 55, 38, 0\.95\)\),\s*url\('([^']+)'\)", repl, content)

for rp in reg_no_grad:
    update_file(rp, restore_reg_no_grad)

print("Restoration script complete.")
