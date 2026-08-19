import re

filepath = 'ip-licensing-database.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

new_bottom = """
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

start_broken = html.find('<div class="row justify-content-center mb-5 mt-4">')
end_broken = html.find('<footer')

if start_broken != -1 and end_broken != -1:
    html = html[:start_broken] + new_bottom + "\n    " + html[end_broken:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed!")
else:
    print(f"Indices: start={start_broken}, end={end_broken}")
