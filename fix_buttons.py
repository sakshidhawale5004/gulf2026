import re

def fix_buttons(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the empty col-md-3 and the col-md-9
    pattern = re.compile(
        r'<div class="col-md-3">\s*</div>\s*<div class="col-md-9">',
        re.DOTALL | re.IGNORECASE
    )

    html_new = pattern.sub(r'<div class="col-12">', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_new)

fix_buttons('interest-rates-database.html')
fix_buttons('services-database.html')
print("Fixed buttons layout!")
