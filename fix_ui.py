import re
import glob

# 1. Fix style.css for premium-left-panel text colors and subscription-hero
with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Fix text colors in form left panels */
.premium-left-panel h1, 
.premium-left-panel h2, 
.premium-left-panel h3, 
.premium-left-panel h4, 
.premium-left-panel h5, 
.premium-left-panel h6,
.premium-left-panel .title,
.premium-left-panel .demo-heading {
    color: #ffffff !important;
}
.premium-left-panel p,
.premium-left-panel small,
.premium-left-panel .text-white-50 {
    color: rgba(255, 255, 255, 0.8) !important;
}

/* Subscription hero should match other internal heroes */
.subscription-hero {
    background: transparent !important;
    padding: 60px 20px !important;
    text-align: left !important;
}
.subscription-hero .container {
    background-color: #ffffff; 
    border-radius: 24px;
    padding: 70px 80px;
    position: relative;
    overflow: hidden;
    box-shadow: 0 15px 35px rgba(0,0,0,0.04);
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 250px;
    border: 1px solid rgba(0,0,0,0.03);
}
.subscription-hero h1 {
    color: var(--primary-green-dark) !important;
    font-size: 52px !important;
    margin-bottom: 15px !important;
    position: relative;
    z-index: 3;
}
.subscription-hero .breadcrumb-text {
    color: var(--text-muted) !important;
    position: relative;
    z-index: 3;
    font-weight: 600;
}
""")

# 2. Fix contact.html inline styles and text colors
with open('contact.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove inline background rules for contact-hero
html = re.sub(r'\.contact-hero\s*\{[^}]+\}', '.contact-hero {\n        position: relative;\n        padding: 100px 0;\n        display: flex;\n        align-items: center;\n    }', html)
html = re.sub(r'\.contact-hero::before\s*\{[^}]+\}', '', html)

# Change text-white to text-dark for contact text so it's visible on white container
html = html.replace('text-white text-uppercase', 'text-dark text-uppercase')
# Only replace text-white inside the container to avoid breaking navbar
container_idx = html.find('<div class="container">')
if container_idx != -1:
    pre = html[:container_idx]
    post = html[container_idx:]
    post = post.replace('text-white', 'text-dark')
    html = pre + post

# Ensure h1 uses primary green
html = re.sub(r'<h1 class="contact-heading[^"]*"', r'<h1 class="contact-heading text-uppercase text-start" style="color: var(--primary-green-dark);"', html)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Done")
