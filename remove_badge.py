import re

# 1. Remove the Data Accuracy badge from index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

badge_pattern = r'<!-- Floating Stat Card 1: Data Accuracy -->.*?</div>\s*</div>'
html = re.sub(badge_pattern, '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Removed badge")
