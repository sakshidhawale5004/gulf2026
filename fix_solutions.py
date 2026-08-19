import re

def fix_gulf_company():
    with open('gulf-company-database.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Bespoke Subscription Models (Image left -> fade-right)
    # The image is inside <div class="col-md-5 mb-3 mb-md-0">
    html = re.sub(
        r'(<div class="row content-block align-items-center mb-5">\s*<div class="col-md-5 mb-3 mb-md-0")([^>]*>)(\s*<img src="homepageimage.webp")',
        r'\1 data-aos="fade-right"\2\3', html)

    # Why GulfTP? (Image right -> fade-left)
    html = re.sub(
        r'(<div class="row content-block align-items-center flex-md-row-reverse mb-5">\s*<div class="col-md-5 mb-3 mb-md-0")([^>]*>)(\s*<img src="We Provide The Best Transfer Pricing Data in the GCC-2ndimage.webp")',
        r'\1 data-aos="fade-left"\2\3', html)

    with open('gulf-company-database.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Fixed gulf-company")

def fix_interest_rates():
    # Let's completely rebuild the bottom content of interest-rates-database.html
    # using exactly the text it has, but with proper row structures.
    with open('interest-rates-database.html', 'r', encoding='utf-8') as f:
        html = f.read()
    
    new_content = """
        <div class="row mb-5 justify-content-center">
            <div class="col-lg-10">
                
                <!-- Block 1: Salient features (Image Right -> flex-reverse, fade-left) -->
                <div class="row content-block align-items-center flex-md-row-reverse mb-5">
                    <div class="col-md-5 mb-3 mb-md-0" data-aos="fade-left">
                        <img src="IP_Licensing-NEW.jpg" alt="Interest Rates Database" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 pe-md-4">
                        <h3 class="section-title mb-3">Salient features</h3>
                        <ul class="feature-list mt-4">
                            <li class="mb-2">High-quality comparable loan agreements that are compliant with country-specific Transfer Pricing regulations and the OECD Transfer Pricing guidelines.</li>
                            <li class="mb-2">Latest semi-variable/non-standard financing agreements.</li>
                            <li class="mb-2">In-depth analysis of comparability factors such as interest rates, key terms and conditions, currency, repayment schedule, etc.</li>
                            <li class="mb-2">Credit rating assigned by credit rating agencies.</li>
                            <li class="mb-2">Credit rating tool for estimating credit rating of borrowing entity.</li>
                        </ul>
                    </div>
                </div>

                <!-- Block 2: Why GulfTP? (Image Left, fade-right) -->
                <div class="row content-block align-items-center mb-5">
                    <div class="col-md-5 mb-3 mb-md-0" data-aos="fade-right">
                        <img src="IP_LicensingIMAGE.jpg" alt="Why GulfTP" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 ps-md-4">
                        <h3 class="section-title mb-3">Why GulfTP?</h3>
                        <p class="section-desc">GulfTP is the premier provider of in-depth, high-quality Transfer Pricing data specifically for the Gulf region. Trusted by over 100 Transfer Pricing service providers across the Middle East, our databases are your go-to source for benchmarking analysis.</p>
                        <p class="section-desc">Access comprehensive data covering company financials, transaction rates, service fees, and loan interest rates. Beyond robust data, we empower your analysis with in-house tools for DEMPE analysis and credit rating estimation.</p>
                        <p class="section-desc">With just one powerful login, you'll have all the essential tools and data you need to confidently navigate the complexities of Transfer Pricing at your fingertips.</p>
                    </div>
                </div>

            </div>
        </div>
"""
    # Replace from `<div class="row mb-5 justify-content-center">` to `<!-- Footer -->`
    start_idx = html.find('<div class="row mb-5 justify-content-center">')
    end_idx = html.find('<footer')
    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + new_content.strip() + "\n    " + html[end_idx:]
        with open('interest-rates-database.html', 'w', encoding='utf-8') as f:
            f.write(html)
            print("Fixed interest-rates")

def fix_services():
    # Same for services-database.html
    with open('services-database.html', 'r', encoding='utf-8') as f:
        html = f.read()

    new_content = """
        <div class="row mb-5 justify-content-center">
            <div class="col-lg-10">
                
                <!-- Block 1: Salient Features (Image Right -> flex-reverse, fade-left) -->
                <div class="row content-block align-items-center flex-md-row-reverse mb-5">
                    <div class="col-md-5 mb-3 mb-md-0" data-aos="fade-left">
                        <img src="about.imagestarting1.jpg" alt="Services Database" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 pe-md-4">
                        <h3 class="section-title mb-3">Salient Features</h3>
                        <ul class="feature-list mt-4">
                            <li class="mb-2">High-quality comparable service agreements compliant with country-specific transfer pricing regulations and the OECD Transfer Pricing guidelines.</li>
                            <li class="mb-2">Diverse service types, including R&D, distribution, management, agency, and procurement.</li>
                            <li class="mb-2">Multiple remuneration models including commission, management, and agent fees.</li>
                            <li class="mb-2">Multitudinous fee bases, including sales, cost pools, etc.</li>
                        </ul>
                    </div>
                </div>

                <!-- Block 2: Tailored Service Fee Searches (Image Left, fade-right) -->
                <div class="row content-block align-items-center mb-5">
                    <div class="col-md-5 mb-3 mb-md-0" data-aos="fade-right">
                        <img src="IP_Licensing-NEW.jpg" alt="Tailored Service Fee Searches" class="img-fluid w-100 rounded-4 shadow-sm" style="min-height: 350px; max-height: 450px; object-fit: cover;">
                    </div>
                    <div class="col-md-7 ps-md-4">
                        <h3 class="section-title mb-3">Tailored Service Fee Searches</h3>
                        <p class="section-desc">Our database provides a meticulously crafted search agreement repository finding the most comparable service fee structures based on your unique operations.</p>
                    </div>
                </div>

                <!-- Block 3: Why GulfTP? (Image Right -> flex-reverse, fade-left) -->
                <div class="row content-block align-items-center flex-md-row-reverse mb-5">
                    <div class="col-md-5 mb-3 mb-md-0" data-aos="fade-left">
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
    # Wait, the structure in services-database.html before <footer might start with <div class="row mb-5 justify-content-center">
    # Let's find it.
    start_idx = html.find('<div class="row mb-5 justify-content-center">')
    if start_idx == -1:
        start_idx = html.find('<div class="row justify-content-center mb-5 mt-4">')
    
    end_idx = html.find('<footer')
    if start_idx != -1 and end_idx != -1:
        html = html[:start_idx] + new_content.strip() + "\n    " + html[end_idx:]
        with open('services-database.html', 'w', encoding='utf-8') as f:
            f.write(html)
            print("Fixed services")

fix_gulf_company()
fix_interest_rates()
fix_services()
