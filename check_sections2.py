import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')
stack = []

for i, line in enumerate(lines):
    if '<section' in line:
        stack.append(i + 1)
    if '</section>' in line:
        if stack:
            stack.pop()

print(f"Unclosed sections started on lines: {stack}")
