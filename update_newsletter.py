import re

# 1. Revert particle color in contact.html
with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()
html = html.replace('"color": {"value": "#ffffff"}', '"color": {"value": "#F59A16"}')
html = html.replace('"color": "#ffffff"', '"color": "#F59A16"')
with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Update Newsletter layout in index.html to be a 3D box
with open('index.html', 'r', encoding='utf-8') as f:
    index_html = f.read()

# Replace the newsletter section with a 3D boxed version
old_newsletter = re.search(r'<!-- Newsletter Section -->.*?</section>', index_html, re.DOTALL)
if old_newsletter:
    new_newsletter = """<!-- Newsletter Section -->
    <section class="py-5" style="background-color: var(--bg-light);">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="newsletter-card position-relative overflow-hidden" style="background: linear-gradient(135deg, var(--deep-teal) 0%, #002b25 100%); border-radius: 24px; padding: 60px; box-shadow: 0 20px 40px rgba(0,0,0,0.15); transition: transform 0.5s ease, box-shadow 0.5s ease; border: 1px solid rgba(255,255,255,0.1);">
                        <!-- Moving 3D subtle gradient orb -->
                        <div style="position: absolute; top: -50%; left: -50%; width: 200%; height: 200%; background: radial-gradient(circle at 50% 50%, rgba(245, 154, 22, 0.15) 0%, transparent 50%); animation: slowDrift 15s ease-in-out infinite; pointer-events: none;"></div>
                        
                        <div class="position-relative" style="z-index: 2;">
                            <div class="text-white text-center mx-auto" style="max-width: 600px;">
                                <h2 class="mb-3 text-white">Newsletter</h2>
                                <p class="mb-4 text-white-50">Get the latest market updates.<br>Subscribe to our Newsletter today!</p>
                                <form class="newsletter-form mx-auto" style="max-width: 500px;">
                                    <div class="d-flex flex-column flex-sm-row gap-2">
                                        <input type="email" class="form-control px-4 py-3 border-0" placeholder="Enter your email" style="border-radius: 50px; box-shadow: inset 0 2px 4px rgba(0,0,0,0.05);" required>
                                        <button type="submit" class="btn btn-orange px-5 py-3" style="border-radius: 50px; white-space: nowrap; box-shadow: 0 10px 20px rgba(245, 154, 22, 0.3);">Subscribe</button>
                                    </div>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>"""
    
    index_html = index_html.replace(old_newsletter.group(0), new_newsletter)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(index_html)

# Add CSS for the newsletter card hover effect
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
.newsletter-card:hover {
    transform: translateY(-15px) perspective(1000px) rotateX(2deg);
    box-shadow: 0 40px 60px rgba(0,0,0,0.2) !important;
}
""")
print("Done")
