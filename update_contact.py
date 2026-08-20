import re

new_section = """<section data-aos="fade-up" class="contact-hero">
    <div id="particles-js" style="position: absolute; top:0; left:0; width:100%; height:100%; z-index:1;"></div>
    <div class="container position-relative" style="z-index: 2;">
        <div class="row align-items-center">
            
            <!-- Left Side: Contact Info & Text -->
            <div class="col-lg-5 pe-lg-5 mb-5 mb-lg-0 text-start">
                <h1 class="contact-heading text-uppercase text-start" style="color: var(--primary-green-dark); font-weight: 600; line-height: 1.2;">Get in touch for transfer pricing guidance and GCC benchmark searches</h1>
                
                <p class="mb-5 text-muted" style="font-family: 'GT Walsheim', 'Outfit', sans-serif; font-size: 1.1rem; line-height: 1.6;">Let's discuss your transfer pricing requirements and how we can support your GCC benchmarking study. Our experts are ready to assist you.</p>
                
                <div class="email-block mb-4">
                    <div class="email-icon" style="background: rgba(10,107,79,0.1); color: var(--primary-green); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-right: 20px;">
                        <i class="fa-solid fa-envelope"></i>
                    </div>
                    <div class="text-start">
                        <h5 class="mb-1 text-dark" style="font-family: 'GT Walsheim', 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 600;">Email us</h5>
                        <p class="mb-0 text-muted" style="font-family: 'GT Walsheim', 'Outfit', sans-serif;">connect@gulftp.com</p>
                    </div>
                </div>

                <div class="email-block">
                    <div class="email-icon" style="background: rgba(10,107,79,0.1); color: var(--primary-green); width: 60px; height: 60px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-size: 1.5rem; margin-right: 20px;">
                        <i class="fa-brands fa-whatsapp"></i>
                    </div>
                    <div class="text-start">
                        <h5 class="mb-1 text-dark" style="font-family: 'GT Walsheim', 'Outfit', sans-serif; font-size: 1.1rem; font-weight: 600;">WhatsApp us</h5>
                        <p class="mb-0 text-muted" style="font-family: 'GT Walsheim', 'Outfit', sans-serif;">+971 581711600</p>
                    </div>
                </div>
            </div>
            
            <!-- Right Side: The Form -->
            <div class="col-lg-7">
                <div class="p-5 shadow-lg" style="background: rgba(255,255,255,0.85); backdrop-filter: blur(20px); border-radius: 20px; border: 1px solid rgba(0,0,0,0.05);">
                    <form class="contact-form-glass">
                        <div class="row g-4">
                            <div class="col-md-6">
                                <input type="text" class="form-control glass-input py-3" placeholder="First name *" required style="border-radius: 8px; background: white;">
                            </div>
                            <div class="col-md-6">
                                <input type="text" class="form-control glass-input py-3" placeholder="Last name *" required style="border-radius: 8px; background: white;">
                            </div>
                            <div class="col-md-6">
                                <input type="email" class="form-control glass-input py-3" placeholder="Email address *" required style="border-radius: 8px; background: white;">
                            </div>
                            <div class="col-md-6">
                                <input type="tel" class="form-control glass-input py-3" placeholder="Phone number *" required style="border-radius: 8px; background: white;">
                            </div>
                            <div class="col-md-6">
                                <input type="tel" class="form-control glass-input py-3" placeholder="WhatsApp number (optional)" style="border-radius: 8px; background: white;">
                            </div>
                            <div class="col-md-6">
                                <input type="text" class="form-control glass-input py-3" placeholder="Company name *" required style="border-radius: 8px; background: white;">
                            </div>
                            
                            <div class="col-md-6">
                                <select class="form-select glass-select py-3" required style="border-radius: 8px; background: white;">
                                    <option value="" disabled selected>Service needed *</option>
                                    <option value="benchmarking">Benchmarking Study</option>
                                    <option value="policy">Transfer Pricing Policy</option>
                                    <option value="compliance">Compliance & Documentation</option>
                                    <option value="other">Other</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <select class="form-select glass-select py-3" required style="border-radius: 8px; background: white;">
                                    <option value="" disabled selected>GCC Country *</option>
                                    <option value="uae">UAE</option>
                                    <option value="ksa">KSA</option>
                                    <option value="qatar">Qatar</option>
                                    <option value="kuwait">Kuwait</option>
                                    <option value="bahrain">Bahrain</option>
                                    <option value="oman">Oman</option>
                                    <option value="multiple">Multiple</option>
                                </select>
                            </div>
                            
                            <div class="col-12">
                                <textarea class="form-control glass-input py-3" rows="4" placeholder="Describe your transfer pricing needs *" required style="border-radius: 8px; background: white;"></textarea>
                            </div>
                            
                            <div class="col-12 mt-4">
                                <button type="submit" class="send-now-btn w-100 py-3 rounded-3" style="font-size: 1.1rem; display: flex; align-items: center; justify-content: center; gap: 10px;">
                                    <i class="fa-solid fa-paper-plane"></i> Send Request
                                </button>
                            </div>
                        </div>
                    </form>
                </div>
            </div>

        </div>
    </div>
</section>"""

with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the entire section
html = re.sub(r'<section data-aos="fade-up" class="contact-hero">.*?</section>', new_section, html, flags=re.DOTALL)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated contact.html layout")
