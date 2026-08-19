import codecs

solutions_pages = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]

def update_background(content):
    # Make the overlay pure black
    content = content.replace('rgba(2, 20, 15, 0.95)', 'rgba(0, 0, 0, 0.7)')
    return content

for f in solutions_pages:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_background(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
