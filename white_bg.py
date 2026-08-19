import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update value-added-section to plain white
css = re.sub(r'\.value-added-section\s*\{[^}]+\}', """
.value-added-section {
    background-color: #ffffff;
    background-image: none;
    padding: 100px 0;
    position: relative;
    overflow: hidden;
    font-family: 'GT Walsheim', 'Outfit', sans-serif;
}
""", css)

# Update watermark to be faint dark instead of faint white
css = re.sub(r"color:\s*rgba\(255,\s*255,\s*255,\s*0\.02\);", "color: rgba(0, 0, 0, 0.03);", css)

# Update value-card to look good on white background
css = re.sub(r'\.value-card\s*\{[^}]+\}', """
.value-card {
    background: #ffffff;
    border: 1px solid rgba(0, 0, 0, 0.08);
    box-shadow: 0 10px 30px rgba(0,0,0,0.03);
    border-radius: 12px;
    padding: 30px;
    height: 100%;
    position: relative;
    z-index: 1;
    transition: transform 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease;
}
.value-card:hover {
    transform: translateY(-5px);
    border-color: var(--primary-orange);
    box-shadow: 0 15px 35px rgba(0,0,0,0.08);
}
""", css)

# Fix card title color explicitly
if '.value-card h4 {' in css:
    css = re.sub(r'\.value-card h4\s*\{[^}]+\}', """
.value-card h4 {
    color: var(--deep-teal) !important;
    font-size: 1.25rem;
    margin-bottom: 15px;
    font-weight: 600;
}
""", css)
else:
    css += """
.value-card h4 {
    color: var(--deep-teal) !important;
    font-size: 1.25rem;
    margin-bottom: 15px;
    font-weight: 600;
}
"""

# Fix card text color
css = re.sub(r'\.value-card p\s*\{[^}]+\}', """
.value-card p {
    color: #555555 !important;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 20px;
}
""", css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# Update HTML to remove text-white and fix subtitle color
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace <h2 class="text-white mb-3" with <h2 class="mb-3"
html = html.replace('<h2 class="text-white mb-3" style="font-size: 2.5rem; font-weight: 600;">Complete Benchmarking Support</h2>', 
                    '<h2 class="mb-3" style="color: var(--deep-teal); font-size: 2.5rem; font-weight: 600;">Complete Benchmarking Support</h2>')

# Replace the gray subtitle that was meant for dark bg
html = html.replace('<p style="color: #a0aec0;">We provide specialized databases and tools for comprehensive transfer pricing analysis, compliance, and strategic growth.</p>',
                    '<p style="color: #555555;">We provide specialized databases and tools for comprehensive transfer pricing analysis, compliance, and strategic growth.</p>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
