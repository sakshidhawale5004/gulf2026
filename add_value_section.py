import re

# 1. Update style.css
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

new_styles = """
/* ==========================================================================
   VALUE ADDED SERVICES & CUSTOM BUTTON
   ========================================================================== */
.btn-custom-gradient {
    background: linear-gradient(90deg, #1e549f 0%, #28a745 100%);
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
.btn-custom-gradient:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 20px rgba(40, 167, 69, 0.3);
}

.value-added-section {
    background-color: #021b3d;
    background-image: radial-gradient(circle at center, #042a59 0%, #021b3d 100%);
    padding: 100px 0;
    position: relative;
    overflow: hidden;
    font-family: 'GT Walsheim', 'Outfit', sans-serif;
}

.value-added-section::before {
    content: 'A';
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    font-size: 800px;
    font-weight: 800;
    color: rgba(255,255,255,0.02);
    line-height: 1;
    z-index: 0;
    pointer-events: none;
}

.value-card {
    background: #042a59;
    border: 1px solid #28a745;
    border-radius: 12px;
    padding: 30px;
    height: 100%;
    position: relative;
    z-index: 1;
    transition: transform 0.3s ease;
}
.value-card:hover {
    transform: translateY(-5px);
}
.value-icon-circle {
    width: 45px;
    height: 45px;
    background-color: #28a745;
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    margin-bottom: 20px;
    color: white;
    font-size: 1.2rem;
}
.value-card h4 {
    color: white;
    font-size: 1.25rem;
    margin-bottom: 15px;
    font-weight: 600;
}
.value-card p {
    color: #a0aec0 !important;
    font-size: 0.9rem;
    line-height: 1.6;
    margin-bottom: 20px;
}
.value-link {
    color: #28a745 !important;
    text-decoration: none;
    font-size: 0.9rem;
    font-weight: 500;
    display: flex;
    align-items: center;
    gap: 5px;
}
.value-link:hover {
    color: #218838 !important;
}
"""

if '.btn-custom-gradient' not in css:
    with open('style.css', 'a', encoding='utf-8') as f:
        f.write(new_styles)

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

value_added_html = """
    <!-- Value Added Services Section -->
    <section class="value-added-section" data-aos="fade-up">
        <div class="container position-relative" style="z-index: 2;">
            <div class="text-center mb-5">
                <p style="color: #a0aec0; font-size: 0.85rem; font-weight: 700; letter-spacing: 1px; text-transform: uppercase;">// VALUE ADDED SERVICES</p>
                <h2 class="text-white mb-3" style="font-size: 2.5rem; font-weight: 600;">End-to-End Business Support</h2>
                <p style="color: #a0aec0;">We provide customized business solutions for streamlined setup, compliance, and growth.</p>
            </div>

            <div class="row g-4">
                <!-- Card 1 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-gear"></i></div>
                        <h4>Business Setup</h4>
                        <p>Start your business in UAE with confidence. We handle company formation, trade license registration, and documentation for mainland, free zone, and offshore setups — end to end.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 2 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-building-columns"></i></div>
                        <h4>Corporate Bank Account</h4>
                        <p>Open a UAE corporate bank account with leading local and international banks. We guide you through requirements, documentation, and submission to ensure fast approval.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 3 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-clipboard-check"></i></div>
                        <h4>Visa Assistance</h4>
                        <p>End-to-end UAE visa processing for investors, employees, and dependents — including residency permits, Emirates ID, and visa renewals.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 4 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-id-card"></i></div>
                        <h4>Golden Visa UAE</h4>
                        <p>Secure long-term UAE residency with our Golden Visa support services for investors, entrepreneurs, and qualified professionals. Valid for 5 to 10 years.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 5 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-registered"></i></div>
                        <h4>Trademark Registration</h4>
                        <p>Protect your brand in UAE and internationally with hassle-free trademark registration. We handle filing, approvals, and renewals on your behalf.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 6 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-magnifying-glass-chart"></i></div>
                        <h4>Auditing Services</h4>
                        <p>Licensed audit services to meet UAE regulatory requirements, ensuring financial transparency and compliance for your business.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 7 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-scale-balanced"></i></div>
                        <h4>Legal Advisory</h4>
                        <p>Expert legal consultation on corporate structuring, commercial contracts, and regulatory compliance to protect your business interests in UAE.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 8 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-calculator"></i></div>
                        <h4>Accounting & Tax</h4>
                        <p>Professional accounting, bookkeeping, and UAE corporate tax compliance services to keep your financials accurate and fully compliant.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
            </div>

            <div class="text-center mt-5">
                <a href="contact.html" class="btn-custom-gradient">Get In Touch <i class="fa-solid fa-arrow-right ms-2"></i></a>
            </div>
        </div>
    </section>
"""

# Insert before <footer if not already there
if 'End-to-End Business Support' not in html:
    footer_idx = html.find('<footer')
    if footer_idx != -1:
        html = html[:footer_idx] + value_added_html + '\n    ' + html[footer_idx:]
        with open('index.html', 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Done")
