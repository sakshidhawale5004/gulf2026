import re
import glob

# 1. Fix HTML files for particles color and add data-aos dynamically if possible
html_files = glob.glob('*.html')
for html_file in html_files:
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Change particle color from orange to white so it's visible on the half-half background
    html = html.replace('"color": {"value": "#F59A16"}', '"color": {"value": "#ffffff"}')
    html = html.replace('"color": "#F59A16"', '"color": "#ffffff"')
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(html)

# 2. Append CSS for Half/Half background and generic motion effects
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* ==========================================================================
   USER REQUEST: HALF DARK GREEN / HALF ORANGE INTERNAL HEROES
   ========================================================================== */
.page-hero .container, .hero-banner .container, .contact-hero .container, .subscription-hero .container {
    background: linear-gradient(135deg, var(--deep-teal) 50%, var(--primary-orange) 50%) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2) !important;
}

/* Force all text inside these half/half containers to be white */
.page-hero .container h1, .hero-banner .container .hero-title, .contact-hero .container .contact-heading, .subscription-hero .container h1,
.page-hero .container .breadcrumb-text, .hero-banner .container .breadcrumb-text, .contact-hero .container .breadcrumb-text, .subscription-hero .container .breadcrumb-text,
.page-hero .container p, .hero-banner .container p, .contact-hero .container p, .subscription-hero .container p,
.page-hero .container a, .hero-banner .container a, .contact-hero .container a, .subscription-hero .container a {
    color: #ffffff !important;
    text-shadow: 0 2px 5px rgba(0,0,0,0.3) !important;
}

/* ==========================================================================
   USER REQUEST: ANIMATION & MOTION EFFECTS FOR ALL SECTIONS
   ========================================================================== */

/* Universal hover floating effect for all cards and block elements */
.card, 
.bg-white.p-4.rounded-4, 
.premium-left-panel, 
.service-block, 
.contact-form-glass,
.pricing-card {
    transition: transform 0.5s cubic-bezier(0.175, 0.885, 0.32, 1.275), box-shadow 0.5s ease !important;
}

.card:hover, 
.bg-white.p-4.rounded-4:hover, 
.premium-left-panel:hover, 
.service-block:hover, 
.contact-form-glass:hover,
.pricing-card:hover {
    transform: translateY(-12px) !important;
    box-shadow: 0 30px 60px rgba(0,0,0,0.12) !important;
}

/* Add a subtle pulse animation to primary buttons */
@keyframes softPulse {
    0% { box-shadow: 0 0 0 0 rgba(245, 154, 22, 0.4); }
    70% { box-shadow: 0 0 0 15px rgba(245, 154, 22, 0); }
    100% { box-shadow: 0 0 0 0 rgba(245, 154, 22, 0); }
}

.btn-orange:hover, .btn-primary:hover {
    animation: softPulse 1.5s infinite;
}

/* Add a slow drifting animation to the background SVG overlays if any */
@keyframes slowDrift {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.comparables-data-section, .newsletter-hero {
    background-size: 200% 200% !important;
    animation: slowDrift 20s ease infinite !important;
}
""")
print("Done")
