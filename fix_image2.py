import re

with open('gulf-company-database.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('src="lifestyle-credit-payment-using-shopping.jpeg"', 'src="lifestyle-credit-payment-using-shopping.jpg"')

with open('gulf-company-database.html', 'w', encoding='utf-8') as f:
    f.write(content)
