import re

def fix_layout(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Pattern to match the col-md-3 and col-md-9 structure
    pattern = re.compile(
        r'<div class="col-md-3">\s*(<h4 class="section-title[^>]+>.*?</h4>)\s*</div>\s*<div class="col-md-9">',
        re.DOTALL | re.IGNORECASE
    )

    # Replace with a single col-12
    # Also change mb-3 to mb-4 on the h4 for a bit more spacing below the heading
    def repl(m):
        heading = m.group(1).replace('mb-3', 'mb-4')
        return f'<div class="col-12">\s*                {heading}'

    html_new = pattern.sub(repl, html)

    # Clean up the literal \s* from the replacement string
    html_new = html_new.replace(r'\s*                ', '\n                ')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html_new)

fix_layout('interest-rates-database.html')
fix_layout('services-database.html')
print("Fixed layouts!")
