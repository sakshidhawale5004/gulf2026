import codecs
import re

files_all = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'ip-licensing-database.html',
    'services-database.html'
]

def update_heading(content):
    # Find <h2 style="...">Ready to Get Started?</h2> and make it <h2 class="text-white" style="...">Ready to Get Started?</h2>
    content = re.sub(r'<h2([^>]*?)>Ready to Get Started\?</h2>', r'<h2 class="text-white"\1>Ready to Get Started?</h2>', content)
    return content

for f in files_all:
    try:
        with codecs.open(f, 'r', encoding='utf-8-sig') as file:
            content = file.read()
        
        new_content = update_heading(content)
        
        if new_content != content:
            with codecs.open(f, 'w', encoding='utf-8-sig') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"No changes in {f}")
    except Exception as e:
        print(f"Error in {f}: {e}")
