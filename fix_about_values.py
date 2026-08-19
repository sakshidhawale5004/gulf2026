import re

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace Why Choose GulfTP cards
content = content.replace(
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-lock"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">100% Control Of Your Business</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Full control and ownership of your transfer pricing analysis with a local partner in most sectors.</p>
                            </div>''',
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-map-location-dot"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Unmatched GCC Focus</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Built specifically for the Gulf region, we provide the most relevant comparables tailored to local market conditions, ensuring full compliance with regional authorities.</p>
                            </div>'''
)

content = content.replace(
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-globe"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Get Access To A Global Market</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Strategic access connecting Europe, Asia, and Africa for international trade opportunities.</p>
                            </div>''',
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-database"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Comprehensive Data Coverage</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Access over 100,000 active companies, verified IP licensing agreements, intercompany loan rates, and localized management service benchmarks.</p>
                            </div>'''
)

content = content.replace(
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-bolt"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Fast Company Setup</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Quick and efficient transfer pricing analysis and benchmarking in many jurisdictions.</p>
                            </div>''',
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-shield-halved"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Rigorous Quality Assurance</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Every data point undergoes a multi-stage validation process by seasoned experts, ensuring pristine data integrity and audit-ready reliability.</p>
                            </div>'''
)

content = content.replace(
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-shield"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Complete Confidentiality & Privacy</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Strong legal protections for your business and personal information with secure data handling.</p>
                            </div>''',
    '''<div class="benefit-card">
                                <div class="benefit-icon">
                                    <i class="fa-solid fa-bolt"></i>
                                </div>
                                <h5 style="color: white; font-weight: 700; margin-bottom: 10px;">Intuitive Search Platform</h5>
                                <p style="font-size: 0.95rem; opacity: 0.9;">Streamline your benchmarking workflow with our powerful, user-friendly platform designed to reduce your search time from days to minutes.</p>
                            </div>'''
)

# Replace Our Values header description
content = content.replace(
    '''<p style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8;">Built on integrity, delivered with efficiency. We are committed to providing accessible, affordable, and expert transfer pricing solutions to businesses across the Gulf region.</p>''',
    '''<p style="font-size: 1.1rem; color: var(--text-muted); line-height: 1.8;">We are dedicated to elevating the standard of transfer pricing in the Gulf region. Our core principles drive every feature we build and every data point we verify.</p>'''
)

# Replace Our Values cards
content = content.replace(
    '''<div class="value-icon">
                            <i class="fa-solid fa-handshake"></i>
                        </div>
                        <h5>Integrity</h5>
                        <p>We drive companies forward by balancing sustainability with certainty to emerge stronger. Our commitment to ethical practices ensures trust and reliability in every engagement.</p>''',
    '''<div class="value-icon">
                            <i class="fa-solid fa-bullseye"></i>
                        </div>
                        <h5>Data Accuracy & Precision</h5>
                        <p>We believe that reliable benchmarking starts with pristine data. We meticulously verify every data point so you can confidently defend your transfer pricing policies.</p>'''
)

content = content.replace(
    '''<div class="value-icon">
                            <i class="fa-solid fa-bolt"></i>
                        </div>
                        <h5>Efficiency</h5>
                        <p>We empower businesses to make informed decisions and imagine new possibilities. Our streamlined processes and expert tools deliver results quickly without compromising quality.</p>''',
    '''<div class="value-icon">
                            <i class="fa-solid fa-earth-asia"></i>
                        </div>
                        <h5>Regional Expertise</h5>
                        <p>We are deeply rooted in the Middle East. Our methodologies are tailored specifically to the nuances of GCC economic landscapes and local regulatory frameworks.</p>'''
)

content = content.replace(
    '''<div class="value-icon">
                            <i class="fa-solid fa-eye"></i>
                        </div>
                        <h5>Transparency</h5>
                        <p>We align people with the organization's aspirations to foster innovative approaches and drive leadership. Clear communication and open dialogue guide all our interactions.</p>''',
    '''<div class="value-icon">
                            <i class="fa-solid fa-users-gear"></i>
                        </div>
                        <h5>Client Empowerment</h5>
                        <p>We are committed to democratizing access to institutional-grade financial data. Our platform equips tax professionals with the tools they need to operate independently.</p>'''
)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
