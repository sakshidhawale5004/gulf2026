import codecs
import re

file_path = 'about.html'

def process_html(content):
    # Reduce h2 sizes from 2.5, 2.8, 2.2 to 2.0rem
    content = content.replace('font-size: 2.5rem;', 'font-size: 2.0rem;')
    content = content.replace('font-size: 2.8rem;', 'font-size: 2.0rem;')
    content = content.replace('font-size: 2.2rem;', 'font-size: 2.0rem;')
    
    # Reduce h3 sizes from 2rem to 1.8rem
    content = content.replace('font-size: 2rem;', 'font-size: 1.6rem;')
    
    # Change any font-weight: 700 to 500 on h3 to be consistent if needed, 
    # but index page has some 700. I'll leave 700 alone unless it looks bad, wait they said "weight be consistent... same as index page".
    # Index page has section titles at 500. Let's make sure section titles are 500.
    content = content.replace('font-weight: 700; font-size: 1.8rem;', 'font-weight: 500; font-size: 1.6rem;')
    
    return content

try:
    with codecs.open(file_path, 'r', encoding='utf-8-sig') as file:
        content = file.read()
    
    new_content = process_html(content)
    
    if new_content != content:
        with codecs.open(file_path, 'w', encoding='utf-8-sig') as file:
            file.write(new_content)
        print(f"Updated {file_path}")
    else:
        print(f"No changes in {file_path}")
except Exception as e:
    print(f"Error: {e}")
