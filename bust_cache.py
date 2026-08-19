import os
import re

files = [
    'about.html', 'contact.html', 'book-search.html', 'book-a-demo.html', 
    'update-a-search.html', 'book-an-appointment.html', 'buy-subscription.html',
    'index.html'
]

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Update the stylesheet link to bust cache
        new_content = re.sub(r'href="style\.css(\?v=[^"]*)?"', 'href="style.css?v=20260627-2"', content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file} cache buster")
    else:
        print(f"File not found: {file}")
