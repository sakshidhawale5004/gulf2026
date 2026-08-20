import glob
import re

# We will replace the <ul> block for the Regulation dropdown in all HTML files.
regulation_old_pattern = re.compile(
    r'<ul class="dropdown-menu">\s*'
    r'<li><a class="dropdown-item" href="uae-transfer-pricing\.html">United Arab Emirates</a></li>\s*'
    r'<li><a class="dropdown-item" href="saudi-arabia-transfer-pricing-benchmarking\.html">Kingdom of Saudi Arabia</a></li>\s*'
    r'<li><a class="dropdown-item" href="kuwait-transfer-pricing\.html">Kuwait</a></li>\s*'
    r'<li><a class="dropdown-item" href="qatar-transfer-pricing\.html">Qatar</a></li>\s*'
    r'<li><a class="dropdown-item" href="bahrain-transfer-pricing\.html">Bahrain</a></li>\s*'
    r'<li><a class="dropdown-item" href="oman-transfer-pricing\.html">Oman</a></li>\s*'
    r'<li><hr class="dropdown-divider"></li>\s*'
    r'<li><h6 class="dropdown-header">Wider Middle East</h6></li>\s*'
    r'<li><a class="dropdown-item" href="egypt-transfer-pricing\.html">Egypt</a></li>\s*'
    r'</ul>'
)

regulation_new = """<ul class="dropdown-menu" style="min-width: 280px; box-shadow: 0 8px 24px rgba(0,0,0,0.12); border: none; border-radius: 10px; padding: 12px 0;">
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


for filepath in glob.glob('*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace Regulation dropdown
    if regulation_old_pattern.search(html):
        html = regulation_old_pattern.sub(regulation_new, html)
    
    # Also update Solutions dropdown to use border-radius: 10px
    html = html.replace('border-radius: 8px; padding: 12px 0;"', 'border-radius: 10px; padding: 12px 0;"')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated dropdowns")
