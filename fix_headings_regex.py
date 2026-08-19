import os
import re

files = [
    'about.html', 'contact.html', 'book-search.html', 'book-a-demo.html', 
    'update-a-search.html', 'book-an-appointment.html', 'buy-subscription.html'
]

def clean_style_attr(m):
    full_attr = m.group(0)
    style_content = m.group(1)
    
    decls = [d.strip() for d in style_content.split(';') if d.strip()]
    new_decls = []
    for decl in decls:
        if ':' not in decl:
            new_decls.append(decl)
            continue
        prop, val = [part.strip() for part in decl.split(':', 1)]
        prop_lower = prop.lower()
        val_lower = val.lower()
        
        if prop_lower in ['font-family', 'font-weight']:
            continue
        if prop_lower == 'color':
            # keep white colors
            if val_lower in ['white', '#fff', '#ffffff']:
                new_decls.append(decl)
            continue
        
        new_decls.append(decl)
        
    if new_decls:
        return 'style="' + '; '.join(new_decls) + ';"'
    return ''

def clean_class_attr(m):
    full_attr = m.group(0)
    class_content = m.group(1)
    
    classes = class_content.split()
    new_classes = []
    
    exclude_classes = ['text-dark', 'text-success', 'text-primary', 'text-info', 'text-warning', 'text-danger', 'text-secondary', 'text-muted']
    
    for c in classes:
        if c.startswith('fw-') or c in exclude_classes:
            continue
        new_classes.append(c)
        
    if new_classes:
        return 'class="' + ' '.join(new_classes) + '"'
    return ''

def process_heading_tag(m):
    tag = m.group(0)
    
    # Process style
    tag = re.sub(r'style="([^"]*)"', clean_style_attr, tag)
    tag = re.sub(r"style='([^']*)'", clean_style_attr, tag)
    
    # Process class
    tag = re.sub(r'class="([^"]*)"', clean_class_attr, tag)
    tag = re.sub(r"class='([^']*)'", clean_class_attr, tag)
    
    # Clean up extra spaces
    tag = re.sub(r'\s+', ' ', tag).replace(' >', '>')
    
    return tag

for file in files:
    if os.path.exists(file):
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all h1-h6 opening tags and process them
        new_content = re.sub(r'<h[1-6][^>]*>', process_heading_tag, content)
        
        if new_content != content:
            with open(file, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file}")
    else:
        print(f"File not found: {file}")
