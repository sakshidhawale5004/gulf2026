import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Make sure the stats text is explicitly white using text-white class
content = content.replace('<h2 class="counter">100,000+</h2>', '<h2 class="counter text-white fw-bold">100,000+</h2>')
content = content.replace('<h2 class="counter">6</h2>', '<h2 class="counter text-white fw-bold">6</h2>')
content = content.replace('<h2 class="counter">100+</h2>', '<h2 class="counter text-white fw-bold">100+</h2>')
content = content.replace('<h2 class="counter">100%</h2>', '<h2 class="counter text-white fw-bold">100%</h2>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
