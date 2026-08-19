import re

files = ['book-a-demo.html', 'book-an-appointment.html', 'book-search.html', 'buy-subscription.html', 'contact.html', 'update-a-search.html']

for f in files:
    with open(f, encoding='utf-8') as fh:
        content = fh.read()
    names = re.findall(r'name=[\"\']([\w-]+)[\"\']\s', content)
    print(f'{f}: {sorted(set(names))}')
