import re

html = open('index.html', encoding='utf-8').read()
hero_match = re.search(r'<section class="hero-section.*?</section>', html, re.DOTALL)
if hero_match:
    links = re.findall(r'<a[^>]*>.*?</a>', hero_match.group(0))
    for l in links:
        print(l)
else:
    print("No hero")
