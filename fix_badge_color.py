import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

content += "\n.experience-badge h2, .experience-badge p { color: #ffffff !important; }\n"

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
