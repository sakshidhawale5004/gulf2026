with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('UAE, Saudi Arabia, Qatar, Bahrain, Oman, and Egypt', 'UAE, Saudi Arabia, Kuwait, Qatar, Bahrain, and Oman')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
