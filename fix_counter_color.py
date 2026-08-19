import re

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Add text-white explicitly to the .counter in the stats section 
# Wait, the best is just to add a rule: .fact-item .counter { color: #ffffff !important; }
content += "\n.fact-item .counter { color: #ffffff !important; }\n"

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
