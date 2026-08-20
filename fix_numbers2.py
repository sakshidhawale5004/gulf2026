import glob
import re

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The hero section
    content = content.replace('<span style="color: var(--primary-orange);">100,000<span class="text-accent-red">+</span></span>', '<span class="text-gradient-red-orange">100,000+</span>')
    
    # The others
    content = content.replace('100,000<span class="text-accent-red">+</span>', '<span class="text-gradient-red-orange">100,000+</span>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('*.html'):
    fix_file(filepath)
