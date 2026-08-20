with open('gulf-company-database.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'(<div class="row mb-5 justify-content-center">.*?</section>)', html, re.DOTALL)
if match:
    print(match.group(1)[:1500])
else:
    print("Section not found.")
