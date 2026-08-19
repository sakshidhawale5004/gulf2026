import re

with open('gulf-company-database.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    'src="https://images.unsplash.com/photo-1554224155-8d04cb21cd6c?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80"',
    'src="lifestyle-credit-payment-using-shopping.jpeg"'
)

with open('gulf-company-database.html', 'w', encoding='utf-8') as f:
    f.write(content)
