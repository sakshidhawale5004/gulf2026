import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace my previous overrides block
old_override_start = css.find('/* ==========================================================================')
old_override_start = css.find('MAKE INNER HEROES FULL WIDTH AND REDUCE HEIGHT', old_override_start)

if old_override_start != -1:
    # Back up to the actual comment start
    block_start = css.rfind('/* ==========================================================================', 0, old_override_start)
    if block_start != -1:
        css = css[:block_start]

# Add the newly requested boxed layout
new_overrides = """
/* ==========================================================================
   BOXED INNER HEROES WITH REDUCED HEIGHT AND 20PX BORDER RADIUS
   ========================================================================== */

/* The outer section should be clean */
.page-hero, .hero-banner, .subscription-hero {
    background: #ffffff !important;
    padding: 30px 0 !important; /* Minimal outer padding */
    border-bottom: none !important;
}

/* The inner container gets the background, radius, and shape */
.page-hero .container, .hero-banner .container, .subscription-hero .container {
    background: linear-gradient(135deg, var(--deep-teal) 50%, var(--primary-orange) 50%) !important;
    border-radius: 20px !important;
    padding: 50px 40px !important; /* Reduced inner height, nice side padding */
    margin: 0 auto !important; /* Center it */
    position: relative;
    overflow: hidden !important; /* Crucial for clipping the 3D wireframe corners */
    box-shadow: 0 15px 35px rgba(0,0,0,0.1) !important;
    width: 90% !important; /* Proper width: a bit wider but not touching edges */
    max-width: 1300px !important;
}

/* Ensure contact hero stays exactly as it was (clean white) */
.contact-hero {
    background: #ffffff !important;
}
.contact-hero .container {
    background: transparent !important;
    box-shadow: none !important;
    border-radius: 0 !important;
    padding: 0 !important;
    width: 100% !important;
}

/* Keep the 3D wireframe positioned nicely inside the rounded box */
.hero-3d-wireframe {
    right: 5% !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    width: 250px !important;
    height: 250px !important;
}

/* Title adjustments for shorter height */
.page-hero .container h1, .hero-banner .container .hero-title, .subscription-hero .container h1 {
    margin-bottom: 0.5rem !important;
    font-size: clamp(2rem, 4vw, 3rem) !important;
}
"""

css += new_overrides

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done switching to boxed layout")
