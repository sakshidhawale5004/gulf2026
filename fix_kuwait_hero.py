import re

with open('kuwait-transfer-pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<title>GulfTP - Oman Transfer Pricing Benchmarking</title>', '<title>GulfTP - Kuwait Transfer Pricing Benchmarking</title>')

# Ensure the hero text is for Kuwait
content = re.sub(r'<h1 class="hero-title"[^>]*>.*?</h1>', '<h1 class="hero-title" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500; font-size: 3.8rem; line-height: 1.15; letter-spacing: -1px;">Kuwait Transfer Pricing</h1>', content)
content = re.sub(r'<p class="hero-breadcrumb"[^>]*>.*?</p>', '<p class="hero-breadcrumb" style="max-width: 540px; line-height: 1.7; font-family: \'Inter\', sans-serif !important; font-weight: 200 !important; font-size: 1.2rem; margin: 0 auto;">Home - Regulation - Kuwait</p>', content)

with open('kuwait-transfer-pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
