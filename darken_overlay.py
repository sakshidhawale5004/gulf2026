import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

old_overlay = """
.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      90deg,
      rgba(0, 35, 30, 0.95) 0%,
      rgba(0, 45, 40, 0.85) 35%,
      rgba(0, 50, 45, 0.55) 65%,
      rgba(0, 55, 55, 0.35) 100%
    ) !important;
}
"""

new_overlay = """
.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      90deg,
      rgba(0, 25, 20, 1.0) 0%,
      rgba(0, 30, 25, 0.95) 45%,
      rgba(0, 35, 30, 0.80) 70%,
      rgba(0, 35, 30, 0.50) 100%
    ) !important;
}
"""

if old_overlay.strip() in css:
    css = css.replace(old_overlay.strip(), new_overlay.strip())
else:
    # Just in case, try a regex replacement
    css = re.sub(r'\.hero-overlay\s*\{\s*position:\s*absolute;\s*inset:\s*0;\s*background:\s*linear-gradient[^}]+\}\s*', new_overlay.strip() + '\n', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
