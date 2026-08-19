import re

with open('ip-licensing-database.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Tailored IP Licensing Searches (Image Left -> fade-right)
html = re.sub(
    r'(<div class="row content-block align-items-center mb-5">\s*<div class="col-md-5 mb-3 mb-md-0")([^>]*>)(\s*<img src="lifestyle-credit-payment-using-shopping.jpg")',
    r'\1 data-aos="fade-right"\2\3', html)

# Why GulfTP? (Image Right -> fade-left)
html = re.sub(
    r'(<div class="row content-block align-items-center flex-md-row-reverse mb-5">\s*<div class="col-md-5 mb-3 mb-md-0")([^>]*>)(\s*<img src="IP_LicensingIMAGE.jpg")',
    r'\1 data-aos="fade-left"\2\3', html)

with open('ip-licensing-database.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed ip-licensing")
