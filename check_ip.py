with open('ip-licensing-database.html', 'r', encoding='utf-8') as f:
    html = f.read()

import re
match = re.search(r'(<div class="container"[^>]*>.*?</header>)', html, re.DOTALL)
idx = html.find('Overview')
print(html[idx-200:idx+800])
