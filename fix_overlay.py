import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Specifically target .hero-overlay block
# The easiest way is to use regex: \.hero-overlay\s*\{[^}]*\}
# and replace the background inside it.

def replace_overlay(match):
    block = match.group(0)
    new_gradient = """background: linear-gradient(
  90deg,
  rgba(0, 82, 70, 0.88) 0%,
  rgba(0, 82, 70, 0.65) 35%,
  rgba(0, 82, 70, 0.25) 65%,
  rgba(0, 82, 70, 0.05) 100%
);"""
    # Replace the background property within this block
    new_block = re.sub(r'background:\s*linear-gradient\([^;]+;', new_gradient, block)
    return new_block

css = re.sub(r'\.hero-overlay\s*\{[^}]*\}', replace_overlay, css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
