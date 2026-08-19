import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the previous deep-teal background rule with the specific images requested
old_rule = r'\.comparables-data-section, \.newsletter-section\s*\{[^}]+\}'
new_rule = """
/* Backgrounds requested by user */
.comparables-data-section {
    background: url("bg.jpg") center/cover no-repeat !important;
    position: relative;
    overflow: hidden;
}

.newsletter-section {
    background: url("background (2).jpg") center/cover no-repeat fixed !important;
    position: relative;
    overflow: hidden;
}
"""

if re.search(old_rule, css):
    css = re.sub(old_rule, new_rule, css, count=1)
else:
    # Append if not found
    css += "\n" + new_rule

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done updating CSS with new background images.")
