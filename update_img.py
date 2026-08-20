with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_str = 'src="Transfer Pricing Implementation Steps.jpg"Transfer Pricing Professional Analysis"'
new_str = 'src="tp-implementation-steps.jpg" alt="Transfer Pricing Professional Analysis"'

html = html.replace(old_str, new_str)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated image src")
