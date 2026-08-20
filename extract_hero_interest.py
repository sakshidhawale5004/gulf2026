with open('interest-rates-database.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'(<section[^>]*class="[^"]*page-hero[^"]*".*?</section>)', html, re.DOTALL)
if match:
    print(match.group(1)[:1500])
else:
    print("Section not found.")
