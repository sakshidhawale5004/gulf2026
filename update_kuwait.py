with open('kuwait-transfer-pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Oman with Kuwait
content = content.replace('Oman', 'Kuwait')
content = content.replace('oman', 'kuwait')
# Be careful with uppercase OMAN if it exists
content = content.replace('OMAN', 'KUWAIT')

with open('kuwait-transfer-pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
