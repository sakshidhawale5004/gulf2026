import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Add the 3D rotating wireframe object
wireframe_css = """
/* ==========================================================================
   3D WIREFRAME OBJECT FOR INNER HEROES
   ========================================================================== */
.page-hero .container, .hero-banner .container, .subscription-hero .container {
    position: relative;
    overflow: hidden;
}

.page-hero .container::after, .hero-banner .container::after, .subscription-hero .container::after {
    content: '';
    position: absolute;
    right: 5%;
    top: -10%;
    width: 400px;
    height: 400px;
    /* A data URI SVG of 3 intersecting rounded squares colored in GulfTP green */
    background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 200 200'%3E%3Crect x='10' y='10' width='180' height='180' rx='60' fill='none' stroke='%230a6b4f' stroke-width='1.5' transform='rotate(15 100 100)'/%3E%3Crect x='10' y='10' width='180' height='180' rx='70' fill='none' stroke='%230a6b4f' stroke-width='1' transform='rotate(40 100 100)'/%3E%3Crect x='10' y='10' width='180' height='180' rx='50' fill='none' stroke='%230a6b4f' stroke-width='2' transform='rotate(75 100 100)'/%3E%3C/svg%3E");
    background-size: contain;
    background-repeat: no-repeat;
    opacity: 0.8;
    animation: wireframeSpin 25s linear infinite;
    pointer-events: none;
    z-index: 0;
}

@keyframes wireframeSpin {
    0% { transform: rotate(0deg) scale(1) translateY(0); }
    33% { transform: rotate(120deg) scale(1.05) translateY(-10px); }
    66% { transform: rotate(240deg) scale(0.95) translateY(10px); }
    100% { transform: rotate(360deg) scale(1) translateY(0); }
}

/* Ensure text stays above the wireframe */
.page-hero .container > *, .hero-banner .container > *, .subscription-hero .container > * {
    position: relative;
    z-index: 2;
}
"""

css += wireframe_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
