import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Remove the background and border-radius from the container
css = re.sub(
    r'\.page-hero \.container, \.hero-banner \.container, \.contact-hero \.container, \.subscription-hero \.container\s*\{[^}]*background:[^}]*\}',
    '', css
)
css = re.sub(
    r'\.page-hero \.container, \.hero-banner \.container, \.subscription-hero \.container\s*\{[^}]*border-radius:[^}]*\}',
    '', css
)
css = re.sub(
    r'\.page-hero \.container, \.hero-banner \.container, \.subscription-hero \.container\s*\{[^}]*overflow:\s*hidden;[^}]*\}',
    '', css
)

# Wait, there are multiple definitions. Let's just override them with a new block at the end.
# It's safer to just append overriding CSS.

overrides = """
/* ==========================================================================
   MAKE INNER HEROES FULL WIDTH AND REDUCE HEIGHT
   ========================================================================== */

/* Remove the boxed layout from the containers */
.page-hero .container, .hero-banner .container, .subscription-hero .container {
    background: transparent !important;
    border-radius: 0 !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
    box-shadow: none !important;
    overflow: visible !important;
}

/* Apply the split background directly to the full-width section */
.page-hero, .hero-banner, .subscription-hero {
    background: linear-gradient(135deg, var(--deep-teal) 50%, var(--primary-orange) 50%) !important;
    padding: 60px 0 !important; /* Reduced height */
    position: relative;
    overflow: hidden !important; /* For the 3D wireframe */
    border-bottom: 1px solid rgba(255,255,255,0.1);
}

/* Keep contact hero white as requested previously */
.contact-hero {
    background: #ffffff !important;
}
.contact-hero .container {
    background: transparent !important;
    box-shadow: none !important;
    margin-top: 0 !important;
    margin-bottom: 0 !important;
}

/* Move the 3D wireframe to the section level so it isn't clipped weirdly */
.hero-3d-wireframe {
    /* Position it near the right edge of the screen */
    right: 5% !important;
    top: 50% !important;
    transform: translateY(-50%) !important;
    width: 250px !important;
    height: 250px !important;
}

/* Adjust title sizes slightly if needed for the shorter height */
.page-hero .container h1, .hero-banner .container .hero-title, .subscription-hero .container h1 {
    margin-bottom: 0.5rem !important;
    font-size: clamp(2.2rem, 5vw, 3.2rem) !important;
}
"""

with open('style.css', 'a', encoding='utf-8') as f:
    f.write(overrides)

print("Done writing overrides")
