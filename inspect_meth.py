import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = content.replace('<title>GulfTP - About Us</title>', '<title>GulfTP - Our Data & Methodology</title>')

# Replace the hero section content
content = re.sub(r'<h1 class="hero-title text-white".*?</h1>', '<h1 class="hero-title text-white" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500;">Our Data & Methodology</h1>', content)
content = re.sub(r'<p class="hero-subtitle text-white-50 mb-0".*?</p>', '<p class="hero-subtitle text-white-50 mb-0" style="font-size: 1.15rem; font-weight: 300;">[TBD by Marketing] Transparent, reliable, and verified transfer pricing data for the GCC region.</p>', content)

# Remove the story section and other about us sections
# We'll just replace everything between <main> and </main> except the hero (which is inside <div class="page-hero"> typically, let's check)
