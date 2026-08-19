import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '''<h1 class="hero-title" style="font-family: 'Cormorant Garamond', serif; font-weight: 500; font-size: 3.8rem; line-height: 1.15; letter-spacing: -1px;">About Us</h1>
            <p class="hero-breadcrumb" style="max-width: 540px; line-height: 1.7; font-family: 'Inter', sans-serif !important; font-weight: 200 !important; font-size: 1.2rem; margin: 0 auto;">Home - About Us</p>''',
    '''<h1 class="hero-title" style="font-family: 'Cormorant Garamond', serif; font-weight: 500; font-size: 3.8rem; line-height: 1.15; letter-spacing: -1px; text-transform: uppercase;">Our Data & Methodology</h1>
            <p class="hero-breadcrumb" style="max-width: 540px; line-height: 1.7; font-family: 'Inter', sans-serif !important; font-weight: 200 !important; font-size: 1.2rem; margin: 0 auto;">Home - Our Data & Methodology</p>'''
)

with open('our-data-methodology.html', 'w', encoding='utf-8') as f:
    f.write(content)
