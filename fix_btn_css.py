import os

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

new_css = '''
.btn-outline-custom-green {
    border: 2px solid var(--primary-green) !important;
    color: var(--primary-green) !important;
    background-color: transparent;
    transition: all 0.3s ease;
}
.btn-outline-custom-green:hover {
    background-color: var(--primary-green) !important;
    color: white !important;
}
'''

content += new_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
