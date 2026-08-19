import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update the value added section colors
css = re.sub(r'\.value-added-section\s*\{[^}]+\}', """
.value-added-section {
    background-color: var(--deep-teal);
    background-image: radial-gradient(circle at center, #0a6b4f 0%, var(--deep-teal) 100%);
    padding: 100px 0;
    position: relative;
    overflow: hidden;
    font-family: 'GT Walsheim', 'Outfit', sans-serif;
}
""", css)

# Update the watermark A to *
css = re.sub(r"content:\s*'A';", "content: '*';", css)

# Update cards
css = re.sub(r'\.value-card\s*\{[^}]+\}', """
.value-card {
    background: rgba(0, 0, 0, 0.2);
    border: 1px solid rgba(245, 154, 22, 0.5);
    border-radius: 12px;
    padding: 30px;
    height: 100%;
    position: relative;
    z-index: 1;
    transition: transform 0.3s ease, border-color 0.3s ease;
}
.value-card:hover {
    transform: translateY(-5px);
    border-color: var(--primary-orange);
}
""", css)

# Update icon circle
css = re.sub(r'\.value-icon-circle\s*\{[^}]+\}', """
.value-icon-circle {
    width: 45px;
    height: 45px;
    background-color: var(--primary-orange);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    color: white;
    font-size: 1.2rem;
    box-shadow: 0 4px 10px rgba(245, 154, 22, 0.3);
}
""", css)

# Update link color
css = re.sub(r'\.value-link\s*\{[^}]+\}', """
.value-link {
    color: var(--primary-orange) !important;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 5px;
}
""", css)
css = re.sub(r'\.value-link:hover\s*\{[^}]+\}', """
.value-link:hover {
    color: #e0890f !important;
}
""", css)

# Update the custom button gradient (Orange to Green)
css = re.sub(r'\.btn-custom-gradient\s*\{[^}]+\}', """
.btn-custom-gradient {
    background: linear-gradient(90deg, var(--primary-orange) 0%, var(--primary-green) 100%);
    color: white !important;
    border-radius: 50px;
    padding: 12px 35px;
    font-weight: 500;
    border: none;
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    text-decoration: none;
}
""", css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Update index.html content
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_html_content = """
    <!-- Value Added Services Section -->
    <section class="value-added-section" data-aos="fade-up">
        <div class="container position-relative" style="z-index: 2;">
            <div class="text-center mb-5">
                <p style="color: var(--primary-orange); font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">// TRANSFER PRICING EXCELLENCE</p>
                <h2 class="text-white mb-3" style="font-size: 2.5rem; font-weight: 600;">Complete Benchmarking Support</h2>
                <p style="color: #a0aec0;">We provide specialized databases and tools for comprehensive transfer pricing analysis, compliance, and strategic growth.</p>
            </div>

            <div class="row g-4">
                <!-- Card 1 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-server"></i></div>
                        <h4>GCC Benchmarking Data</h4>
                        <p>Access the largest repository of verified comparable company data across the UAE, KSA, Qatar, Kuwait, Bahrain, and Oman.</p>
                        <a href="gulf-company-database.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-chart-line"></i></div>
                        <h4>Interest Rates Database</h4>
                        <p>Benchmark intercompany loans, guarantees, and cash pools with highly accurate daily and historical interest rate data.</p>
                        <a href="interest-rates-database.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-lightbulb"></i></div>
                        <h4>IP Licensing Data</h4>
                        <p>Discover royalty rates and licensing agreements to support arm's length pricing for intellectual property and intangibles.</p>
                        <a href="ip-licensing-database.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 4 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-handshake"></i></div>
                        <h4>Intercompany Services</h4>
                        <p>Determine appropriate mark-ups for management fees, IT services, and administrative support across the Middle East.</p>
                        <a href="services-database.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 5 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-magnifying-glass"></i></div>
                        <h4>Custom Searches</h4>
                        <p>Can't find what you need? Request bespoke benchmarking searches tailored to your exact industry and transaction type.</p>
                        <a href="book-search.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 6 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-screwdriver-wrench"></i></div>
                        <h4>DEMPE Analysis Tools</h4>
                        <p>Leverage our built-in tools to allocate returns for Development, Enhancement, Maintenance, Protection, and Exploitation of intangibles.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 7 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-file-invoice"></i></div>
                        <h4>Local & Master File</h4>
                        <p>Export robust data and analysis ready to be integrated seamlessly into your transfer pricing documentation and compliance reports.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 8 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-headset"></i></div>
                        <h4>Expert Analyst Support</h4>
                        <p>Connect directly with our transfer pricing specialists to help navigate complex transactions and defend your positions.</p>
                        <a href="contact.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>

            <div class="text-center mt-5">
                <a href="contact.html" class="btn-custom-gradient">Get In Touch <i class="fa-solid fa-arrow-right ms-2"></i></a>
            </div>
        </div>
    </section>
"""

# Replace the entire existing value-added-section in index.html
start_tag = '<section class="value-added-section"'
end_tag = '</section>'

start_idx = html.find(start_tag)
if start_idx != -1:
    end_idx = html.find(end_tag, start_idx) + len(end_tag)
    html = html[:start_idx] + new_html_content.strip() + html[end_idx:]
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Updated HTML")
else:
    print("Could not find section in HTML")
