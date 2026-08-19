import os
import re
import glob

# 1. Update style.css
css_file = 'style.css'
with open(css_file, 'r', encoding='utf-8') as f:
    css = f.read()

# Update root variables
root_replacement = """:root {
    --primary-green: #006B57;
    --primary-green-dark: #004C42;
    --deep-teal: #003C3A;
    --primary-orange: #F59A16;
    --primary-orange-light: #F7A950;
    --accent-red: #ED1B2F;
    
    --text-dark: #12312D;
    --text-muted: #64736F;
    --bg-light: #F7F9F8;
    --bg-white: #FFFFFF;
    
    --glass-bg: rgba(255, 255, 255, 0.85);
    --glass-border: rgba(255, 255, 255, 0.2);
    --shadow-sm: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    --shadow-md: 0 10px 15px -3px rgba(0, 0, 0, 0.05), 0 4px 6px -2px rgba(0, 0, 0, 0.025);
    --shadow-lg: 0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
    --shadow-glow-green: 0 10px 25px -5px rgba(0, 107, 87, 0.4);
    --shadow-glow-orange: 0 10px 25px -5px rgba(245, 154, 22, 0.4);
}"""

css = re.sub(r':root\s*\{[^}]+\}', root_replacement, css, count=1)

# Update font import
css = re.sub(r"@import url\([^)]+\);", "@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap');", css)

# Replace 'Inter' and 'Cormorant Garamond'
css = css.replace("'Inter', sans-serif", "'Manrope', sans-serif")
css = css.replace("'Cormorant Garamond', serif", "'Plus Jakarta Sans', sans-serif")

# Remove any old .btn-outline-white or scroll-indicator so we don't duplicate
# Let's just append new styles
new_styles = """
/* REDESIGN STYLES */
body {
    font-family: 'Manrope', sans-serif;
    color: var(--text-dark);
}

h1, h2, h3, h4, h5, h6, .hero-title, .section-title {
    font-family: 'Plus Jakarta Sans', sans-serif;
}

/* Navbar */
.navbar-custom {
    background-color: rgba(255, 255, 255, 0.95);
    backdrop-filter: blur(10px);
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}

.navbar-nav .nav-link {
    font-family: 'Manrope', sans-serif;
    font-weight: 500;
    color: var(--primary-green-dark) !important;
    position: relative;
}

.navbar-nav .nav-link:hover, .navbar-nav .nav-link.active {
    color: var(--primary-green) !important;
}

.navbar-nav .nav-link::after {
    content: '';
    position: absolute;
    bottom: -2px;
    left: 50%;
    transform: translateX(-50%);
    width: 0;
    height: 2px;
    background-color: var(--primary-orange);
    transition: width 0.3s ease;
}

.navbar-nav .nav-link:hover::after, .navbar-nav .nav-link.active::after {
    width: 20px;
}

/* Hero Section */
.hero-section {
    min-height: 80vh;
}
@media (max-width: 991px) {
    .hero-section {
        min-height: 75vh;
    }
}
@media (max-width: 767px) {
    .hero-section {
        min-height: 650px;
    }
}

.hero-overlay {
    background: linear-gradient(
      90deg,
      rgba(0, 76, 66, 0.90) 0%,
      rgba(0, 76, 66, 0.72) 35%,
      rgba(0, 76, 66, 0.35) 65%,
      rgba(0, 76, 66, 0.08) 100%
    ) !important;
    box-shadow: inset 0 0 100px rgba(0, 60, 58, 0.5); /* Vignette */
}

/* Hero Content */
.hero-title {
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 700 !important;
    font-size: 60px !important;
    line-height: 1.1;
    max-width: 650px;
}
@media (max-width: 767px) {
    .hero-title {
        font-size: 40px !important;
    }
}
.hero-title span.highlight {
    color: var(--primary-orange);
}

.hero-badge {
    background: rgba(255, 255, 255, 0.15) !important;
    border: 1px solid rgba(255, 255, 255, 0.3) !important;
    font-family: 'Manrope', sans-serif;
    font-size: 13px !important;
    letter-spacing: 0.5px !important;
    padding: 6px 16px !important;
    border-radius: 50px;
}
.hero-badge .fa-chart-pie {
    color: var(--primary-orange) !important;
}

.hero-subtitle {
    font-size: 18px !important;
    line-height: 1.6;
    max-width: 580px !important;
    opacity: 0.85;
}

/* Primary CTA */
.btn-conxora.btn-orange, .btn-primary {
    background-color: var(--primary-orange) !important;
    color: #fff !important;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    font-size: 15px;
    padding: 15px 24px;
    border-radius: 8px;
    border: none;
    box-shadow: var(--shadow-md);
    transition: all 0.3s ease;
    display: inline-flex;
    align-items: center;
}
.btn-conxora.btn-orange:hover, .btn-primary:hover {
    transform: translateY(-3px) !important;
    filter: brightness(1.1);
    box-shadow: var(--shadow-lg);
}
.btn-conxora.btn-orange i {
    transition: transform 0.3s ease;
}
.btn-conxora.btn-orange:hover i {
    transform: translateX(4px);
}

/* Secondary CTA / Outline */
.btn-outline-white {
    border: 1px solid rgba(255,255,255,0.75) !important;
    color: #ffffff !important;
    background: transparent !important;
    font-family: 'Manrope', sans-serif;
    font-weight: 700;
    border-radius: 8px;
    padding: 15px 24px;
    transition: all 0.3s ease;
}
.btn-outline-white:hover {
    background: #ffffff !important;
    color: var(--primary-green) !important;
}

/* Hero Floating Card */
.hero-3d-element {
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.2) !important;
    box-shadow: var(--shadow-lg);
    animation: floatingCard 6s ease-in-out infinite;
    transform: translateY(0);
}
@keyframes floatingCard {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-8px);
  }
}

/* Subtle Hero Background Motion */
.hero-section video {
    animation: slowZoom 20s alternate infinite ease-in-out;
}
@keyframes slowZoom {
    0% { transform: scale(1); }
    100% { transform: scale(1.04); }
}

/* Scroll Indicator */
.scroll-indicator {
    position: absolute;
    bottom: 30px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    flex-direction: column;
    align-items: center;
    color: rgba(255,255,255,0.7);
    font-size: 12px;
    letter-spacing: 2px;
    z-index: 10;
}
.scroll-line {
    width: 1px;
    height: 40px;
    background: rgba(255,255,255,0.2);
    margin-top: 10px;
    position: relative;
    overflow: hidden;
}
.scroll-line::after {
    content: '';
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 50%;
    background: #fff;
    animation: scrollLine 2s infinite;
}
@keyframes scrollLine {
    0% { transform: translateY(-100%); }
    100% { transform: translateY(200%); }
}

/* Cards */
.feature-card, .service-card, .card {
    background: #ffffff;
    border: 1px solid #E6ECE9 !important;
    border-radius: 16px !important;
    box-shadow: var(--shadow-sm);
    padding: 30px;
    transition: all 0.3s ease;
}
.feature-card:hover, .service-card:hover, .card:hover {
    transform: translateY(-6px);
    border-color: var(--primary-green) !important;
    box-shadow: var(--shadow-md);
}
.feature-card:hover i, .service-card:hover i {
    color: var(--primary-orange) !important;
}

/* Icons */
.icon-container i {
    color: var(--primary-green);
    transition: color 0.3s ease;
}
.feature-card:hover .icon-container i {
    color: var(--primary-orange);
}

/* Backgrounds */
.bg-light {
    background-color: var(--bg-light) !important;
}
.bg-green-dark {
    background-color: var(--deep-teal) !important;
    color: #fff;
}

/* Button System Additions */
.btn-green {
    background-color: var(--primary-green) !important;
    color: #fff !important;
    font-weight: 700;
    border-radius: 8px;
    transition: all 0.25s ease;
}
.btn-green:hover {
    background-color: var(--primary-green-dark) !important;
    transform: translateY(-2px);
    box-shadow: var(--shadow-md);
}
.btn-outline-green {
    background: transparent;
    border: 1px solid var(--primary-green) !important;
    color: var(--primary-green) !important;
    font-weight: 700;
    border-radius: 8px;
    transition: all 0.25s ease;
}
.btn-outline-green:hover {
    background: var(--primary-green) !important;
    color: #fff !important;
}

/* Micro-animations */
.motion-fade-up {
    animation: fadeUp 0.7s forwards;
    opacity: 0;
}
@keyframes fadeUp {
    from { opacity: 0; transform: translateY(25px); }
    to { opacity: 1; transform: translateY(0); }
}

@media (prefers-reduced-motion: reduce) {
    *, ::before, ::after {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
        scroll-behavior: auto !important;
    }
}
"""

with open(css_file, 'w', encoding='utf-8') as f:
    f.write(css + "\n" + new_styles)

print("Updated style.css")

# 2. Update HTML files
html_files = glob.glob("*.html")
for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        html = f.read()

    # Highlight 100,000+ in hero title
    html = re.sub(r'(Unlock Over\s*)(100,000\+)', r'\1<span class="highlight">\2</span>', html, flags=re.IGNORECASE)

    # Add scroll indicator in hero section
    if 'hero-section' in html and 'scroll-indicator' not in html:
        # insert before the closing section tag or after hero-content
        html = html.replace('</section>', '    <div class="scroll-indicator">SCROLL TO EXPLORE<div class="scroll-line"></div></div>\n    </section>', 1)
        
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated HTML files")
