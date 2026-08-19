import re

with open("style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Let's remove the block:
css = re.sub(r"h1,\s*h2,\s*h3,\s*\.h1,\s*\.h2,\s*\.h3\s*\{[^}]*\}", "", css)

with open("style.css", "w", encoding="utf-8") as f:
    f.write(css)
