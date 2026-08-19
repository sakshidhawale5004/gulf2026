import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Change text-white to text-dark for hero-title
html = re.sub(r'class="hero-title([^"]*)text-white', r'class="hero-title\1text-dark', html)

# Change hero-subtitle text-white to text-muted
html = re.sub(r'class="hero-subtitle([^"]*)text-white text-opacity-75', r'class="hero-subtitle\1text-muted', html)

# Change hero-badge bg-white bg-opacity-10 text-white to bg-light text-dark border-dark
html = re.sub(r'bg-white bg-opacity-10 text-white px-3 py-2 rounded-pill border border-white border-opacity-25', r'bg-white text-dark px-3 py-2 rounded-pill border shadow-sm', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the dark slate hero-overlay with a clean white/light gradient
new_overlay = 'linear-gradient(135deg, rgba(255, 255, 255, 0.95) 0%, rgba(248, 250, 252, 0.98) 100%)'
css = re.sub(r'linear-gradient\(135deg,\s*rgba\(15,\s*23,\s*42[^)]+\)\s*0%,\s*rgba\([^)]+\)\s*100%\)', new_overlay, css)

# Fix any forced white text on hero
css = re.sub(r'\.hero-title\s*{\s*color:\s*#ffffff\s*!important;\s*}', '.hero-title { color: var(--primary-green) !important; }', css)
css = re.sub(r'\.hero-subtitle\s*{\s*color:\s*rgba\(255,\s*255,\s*255,\s*0\.8\)\s*!important;\s*}', '.hero-subtitle { color: var(--text-muted) !important; }', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
