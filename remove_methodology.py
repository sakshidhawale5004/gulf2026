import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Remove navigation links to our-data-methodology.html
    # It might be in an <li> tag
    content = re.sub(r'<li class="nav-item">\s*<a class="nav-link" href="our-data-methodology\.html">[^<]*</a>\s*</li>', '', content)
    # Or just an <a> tag in footer
    content = re.sub(r'<li>\s*<a href="our-data-methodology\.html" class="footer-link">[^<]*</a>\s*</li>', '', content)
    # Also the banner in some pages:
    # <div class="col-12 mt-4 text-center">...<a href="our-data-methodology.html" ...>...</a>...</div>
    content = re.sub(r'<!-- Methodology Link Banner -->[\s\S]*?(?:</div>\s*</div>\s*</div>\s*</div>|<!-- End Methodology Link Banner -->)', '', content)
    # Let's just remove any link to our-data-methodology.html if it's wrapped in something simple, or just the <a> tag
    content = re.sub(r'<a[^>]*href="our-data-methodology\.html"[^>]*>[\s\S]*?</a>', '', content)
    
    # Remove Update Cadence block
    content = re.sub(r'<div class="d-flex">\s*<i class="fa-solid fa-clock-rotate-left[^>]*></i>\s*<div>\s*<h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>\s*<p class="text-muted small mb-0">Quarterly updates to ensure alignment with shifting regional service costs.</p>\s*</div>\s*</div>', '', content)

    # In case the exact spacing is different:
    content = re.sub(r'<h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>\s*<p class="text-muted small mb-0">Quarterly updates to ensure alignment with shifting regional service costs.</p>', '', content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
