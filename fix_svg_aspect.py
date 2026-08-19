import os
import re

directory = '.'

for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Add preserveAspectRatio="none" if it's not already there
        if 'preserveAspectRatio="none"' not in content:
            new_content = re.sub(
                r'<svg viewBox="0 0 1440 120"([^>]*?)>',
                r'<svg viewBox="0 0 1440 120"\1 preserveAspectRatio="none">',
                content
            )
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
