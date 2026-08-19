import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add CSS to hide the overlay on inner pages and ensure the section itself has a clean background
clean_inner_heroes = """
/* Clean up inner pages' hero sections outside the main container box */
.page-hero, .hero-banner, .subscription-hero, .contact-hero {
    background: #ffffff !important; /* Remove any old background images from the section */
}

/* Hide the dark green overlay on inner pages so it only affects the home page */
.page-hero .hero-overlay, 
.hero-banner .hero-overlay, 
.subscription-hero .hero-overlay, 
.contact-hero .hero-overlay {
    display: none !important;
}

/* Ensure the inner containers stand out properly */
.page-hero .container, .hero-banner .container, .subscription-hero .container {
    border-radius: 12px;
    margin-top: 2rem;
    margin-bottom: 2rem;
}
"""

css += clean_inner_heroes

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
