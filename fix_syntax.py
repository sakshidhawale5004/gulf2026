for filename in ['interest-rates-database.html', 'services-database.html', 'ip-licensing-database.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    html = html.replace('shadow-sm""', 'shadow-sm"')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
