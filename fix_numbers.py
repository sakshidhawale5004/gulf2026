import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    replacements = [
        ('>100,000+<', '>100,000<span class="text-accent-red">+</span><'),
        ('>100+<', '>100<span class="text-accent-red">+</span><'),
        ('>10+<', '>10<span class="text-accent-red">+</span><'),
        ('>100%<', '>100<span class="text-accent-red">%</span><'),
    ]
    
    for old, new in replacements:
        content = content.replace(old, new)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

for filepath in glob.glob('*.html'):
    fix_file(filepath)
