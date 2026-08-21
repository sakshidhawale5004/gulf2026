with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('<img src="Expert Support for Your Transfer Pricing Needs-FINAL1.jpg"Tailored Pricing">', '<img src="Expert Support for Your Transfer Pricing Needs-FINAL1.jpg" alt="Expert Support">')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
