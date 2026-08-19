import re

# 1. Left align the hero texts in all inner pages
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add left-alignment rule to the hero containers
css += """
.page-hero .container, .hero-banner .container, .subscription-hero .container, .contact-hero .container {
    text-align: left !important;
    padding-left: 5% !important;
}
.page-hero .container h1, .hero-banner .container .hero-title, .subscription-hero .container h1, .contact-hero .container .contact-heading {
    margin-left: 0 !important;
    text-align: left !important;
}
.page-hero .container .breadcrumb-text, .hero-banner .container .hero-breadcrumb, .subscription-hero .container .breadcrumb-text, .contact-hero .container .breadcrumb-text {
    margin-left: 0 !important;
    text-align: left !important;
}
"""
with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Fix the broken HTML in ip-licensing-database.html and others
def fix_database_page(filepath, first_heading, first_desc, second_heading, second_desc, img1, img2):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Find the start of the content section after the premium feature cards
        start_idx = html.find('<div class="row justify-content-center">')
        if start_idx == -1: start_idx = html.find('<div class="row mb-5 justify-content-center">')
        
        # This is too fragile to regex blindly. Let's find the closing tag of the feature cards section.
        # Actually, let's just use regex to replace everything from the first heading to the end of the second block.
        
        # A simpler approach: The issue in ip-licensing is specific:
        if 'Tailored IP Licensing Searches' in html:
            # Rebuild the bottom section of IP licensing
            new_bottom = f"""
        <div class="row mb-5 justify-content-center">
            <div class="col-lg-10">
                
                <div class="row content-block align-items-center mb-5">
                    <div class="col-md-5 mb-3 mb-md-0">
                        <img src="lifestyle-credit-payment-using-shopping.jpg" alt="Tailored IP Licensing Searches" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 ps-md-4">
                        <h3 class="section-title mb-3">Tailored IP Licensing Searches</h3>
                        <p class="section-desc">Get custom searches from our extensive IP License agreement repository. We find the exact comparables you need with minimal turnaround time.</p>
                    </div>
                </div>

                <div class="row content-block align-items-center flex-md-row-reverse mb-5">
                    <div class="col-md-5 mb-3 mb-md-0">
                        <img src="IP_LicensingIMAGE.jpg" alt="Why GulfTP" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 pe-md-4">
                        <h3 class="section-title mb-3">Why GulfTP?</h3>
                        <p class="section-desc">GulfTP is the premier provider of in-depth, high-quality Transfer Pricing data specifically for the Gulf region. Trusted by over 100 Transfer Pricing service providers across the Middle East, our databases are your go-to source for benchmarking analysis.</p>
                        <p class="section-desc">Access comprehensive data covering company financials, transaction rates, service fees, and loan interest rates. Beyond robust data, we empower your analysis with in-house tools for DEMPE analysis and credit rating estimation.</p>
                        <p class="section-desc">With just one powerful login, you'll have all the essential tools and data you need to confidently navigate the complexities of Transfer Pricing at your fingertips.</p>
                    </div>
                </div>

            </div>
        </div>
            """
            # Replace the broken part in ip-licensing-database.html
            # The broken part starts at <div class="row justify-content-center mb-5 mt-4"> and ends before the footer.
            start_broken = html.find('<div class="row justify-content-center mb-5 mt-4">')
            if start_broken != -1:
                end_broken = html.find('<!-- Footer -->')
                if end_broken != -1:
                    html = html[:start_broken] + new_bottom + "\\n    " + html[end_broken:]
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(html)
                        print(f"Fixed {filepath}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

fix_database_page('ip-licensing-database.html', '', '', '', '', '', '')

# Let's also make sure gulf-company-database.html has the pe-md-4 class on the flex-reverse section text
try:
    with open('gulf-company-database.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<div class="col-md-7 ps-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>', '<div class="col-md-7 pe-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>')
    with open('gulf-company-database.html', 'w', encoding='utf-8') as f:
        f.write(html)
except Exception as e: pass

try:
    with open('interest-rates-database.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<div class="col-md-7 ps-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>', '<div class="col-md-7 pe-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>')
    with open('interest-rates-database.html', 'w', encoding='utf-8') as f:
        f.write(html)
except Exception as e: pass

try:
    with open('services-database.html', 'r', encoding='utf-8') as f:
        html = f.read()
    html = html.replace('<div class="col-md-7 ps-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>', '<div class="col-md-7 pe-md-4">\\n                        <h3 class="section-title mb-3">Why GulfTP?</h3>')
    with open('services-database.html', 'w', encoding='utf-8') as f:
        f.write(html)
except Exception as e: pass

print("Done fixing layouts")
