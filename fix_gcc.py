import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Regulation Dropdown
    old_dropdown = '''                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="uae-transfer-pricing.html">United Arab Emirates</a></li>
                                <li><a class="dropdown-item" href="saudi-arabia-transfer-pricing-benchmarking.html">Kingdom of Saudi Arabia</a></li>
                                <li><a class="dropdown-item" href="qatar-transfer-pricing.html">Qatar</a></li>
                                <li><a class="dropdown-item" href="bahrain-transfer-pricing.html">Bahrain</a></li>
                                <li><a class="dropdown-item" href="egypt-transfer-pricing.html">Egypt</a></li>
                                <li><a class="dropdown-item" href="oman-transfer-pricing.html">Oman</a></li>
                            </ul>'''
    new_dropdown = '''                            <ul class="dropdown-menu">
                                <li><a class="dropdown-item" href="uae-transfer-pricing.html">United Arab Emirates</a></li>
                                <li><a class="dropdown-item" href="saudi-arabia-transfer-pricing-benchmarking.html">Kingdom of Saudi Arabia</a></li>
                                <li><a class="dropdown-item" href="kuwait-transfer-pricing.html">Kuwait</a></li>
                                <li><a class="dropdown-item" href="qatar-transfer-pricing.html">Qatar</a></li>
                                <li><a class="dropdown-item" href="bahrain-transfer-pricing.html">Bahrain</a></li>
                                <li><a class="dropdown-item" href="oman-transfer-pricing.html">Oman</a></li>
                                <li><hr class="dropdown-divider"></li>
                                <li><h6 class="dropdown-header">Wider Middle East</h6></li>
                                <li><a class="dropdown-item" href="egypt-transfer-pricing.html">Egypt</a></li>
                            </ul>'''
    content = content.replace(old_dropdown, new_dropdown)

    # 2. Update Footer Links
    old_footer = '''                    <h5 class="footer-heading">Regulation</h5>
                    <a href="uae-transfer-pricing.html" class="footer-link">UAE</a>
                    <a href="saudi-arabia-transfer-pricing-benchmarking.html" class="footer-link">Saudi Arabia</a>
                    <a href="qatar-transfer-pricing.html" class="footer-link">Qatar</a>
                    <a href="bahrain-transfer-pricing.html" class="footer-link">Bahrain</a>
                    <a href="egypt-transfer-pricing.html" class="footer-link">Egypt</a>
                    <a href="oman-transfer-pricing.html" class="footer-link">Oman</a>'''
    new_footer = '''                    <h5 class="footer-heading">Regulation</h5>
                    <a href="uae-transfer-pricing.html" class="footer-link">UAE</a>
                    <a href="saudi-arabia-transfer-pricing-benchmarking.html" class="footer-link">Saudi Arabia</a>
                    <a href="kuwait-transfer-pricing.html" class="footer-link">Kuwait</a>
                    <a href="qatar-transfer-pricing.html" class="footer-link">Qatar</a>
                    <a href="bahrain-transfer-pricing.html" class="footer-link">Bahrain</a>
                    <a href="oman-transfer-pricing.html" class="footer-link">Oman</a>
                    <h5 class="footer-heading mt-4" style="font-size: 0.9rem;">Wider Middle East</h5>
                    <a href="egypt-transfer-pricing.html" class="footer-link">Egypt</a>'''
    content = content.replace(old_footer, new_footer)

    # 3. Update Contact Form Country Dropdown (contact.html only, maybe others)
    old_select = '''                            <select class="form-select p-3 glass-select" name="country" required>
                                <option value="" disabled selected hidden>GCC Country *</option>
                                <option value="UAE">UAE</option>
                                <option value="Saudi Arabia">Saudi Arabia</option>
                                <option value="Qatar">Qatar</option>
                                <option value="Bahrain">Bahrain</option>
                                <option value="Oman">Oman</option>
                                <option value="Egypt">Egypt</option>
                                <option value="Multiple">Multiple Countries</option>
                            </select>'''
    new_select = '''                            <select class="form-select p-3 glass-select" name="country" required>
                                <option value="" disabled selected hidden>GCC Country *</option>
                                <option value="UAE">UAE</option>
                                <option value="Saudi Arabia">Saudi Arabia</option>
                                <option value="Kuwait">Kuwait</option>
                                <option value="Qatar">Qatar</option>
                                <option value="Bahrain">Bahrain</option>
                                <option value="Oman">Oman</option>
                                <option value="" disabled>--- Wider Middle East ---</option>
                                <option value="Egypt">Egypt</option>
                                <option value="Multiple">Multiple Countries</option>
                            </select>'''
    content = content.replace(old_select, new_select)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
