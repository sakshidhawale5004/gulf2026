import glob
import re

regulation_new = """Regulation <i class="fa-solid fa-chevron-down ms-1" style="font-size: 0.75rem;"></i></a>
                            <ul class="dropdown-menu" style="min-width: 280px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: none; border-radius: 10px; padding: 12px 0;">
                                <li><a class="dropdown-item" href="uae-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>United Arab Emirates</a></li>
                                <li><a class="dropdown-item" href="saudi-arabia-transfer-pricing-benchmarking.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Kingdom of Saudi Arabia</a></li>
                                <li><a class="dropdown-item" href="kuwait-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Kuwait</a></li>
                                <li><a class="dropdown-item" href="qatar-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Qatar</a></li>
                                <li><a class="dropdown-item" href="bahrain-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Bahrain</a></li>
                                <li><a class="dropdown-item" href="oman-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Oman</a></li>
                                <li><hr class="dropdown-divider" style="margin: 8px 0; opacity: 0.1;"></li>
                                <li><h6 class="dropdown-header" style="font-size: 0.8rem; letter-spacing: 1px; color: #94a3b8; padding: 4px 20px;">WIDER MIDDLE EAST</h6></li>
                                <li><a class="dropdown-item" href="egypt-transfer-pricing.html" style="padding: 10px 20px; font-size: 0.95rem; color: #0a6b4f; font-weight: 500;"><i class="fa-solid fa-location-dot me-3" style="color: #f39223;"></i>Egypt</a></li>
                            </ul>"""

# 1. Update the dropdown for any files that have a different dropdown order
for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We find "Regulation <i..." and replace everything until </ul>
    pattern = re.compile(r'Regulation <i class="fa-solid fa-chevron-down[^>]+></i></a>\s*<ul class="dropdown-menu[^>]*>.*?</ul>', re.DOTALL)
    
    if pattern.search(html):
        html = pattern.sub(regulation_new, html)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)


# 2. Fix .value-card h4 color in style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

css = re.sub(r'(\.value-card h4\s*\{[^}]*)color:\s*#ffffff\s*!important;', r'\1color: var(--deep-teal) !important;', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Fixed dropdowns and value card h4 color")
