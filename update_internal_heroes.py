import re
import glob

css_file = 'style.css'

new_styles = """
/* INTERNAL PAGE HERO REDESIGN */
.page-hero, .hero-banner, .contact-hero {
    background: transparent !important;
    padding: 40px 20px !important;
    text-align: left !important;
}

.page-hero .container, .hero-banner .container, .contact-hero .container {
    background-color: var(--deep-teal); /* Dark premium background replacing purple */
    border-radius: 24px;
    padding: 70px 80px;
    position: relative;
    overflow: hidden;
    box-shadow: var(--shadow-lg);
    display: flex;
    flex-direction: column;
    justify-content: center;
    min-height: 250px;
}

/* Abstract Squiggly Lines mimicking the reference */
.page-hero .container::before, .hero-banner .container::before, .contact-hero .container::before {
    content: '';
    position: absolute;
    right: -100px;
    top: -100px;
    width: 600px;
    height: 600px;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M500,300 C500,450 350,550 200,500 C50,450 50,200 200,100 C350,0 500,150 500,300 Z' fill='none' stroke='rgba(255,255,255,0.1)' stroke-width='1.5'/%3E%3Cpath d='M550,300 C550,500 400,600 150,500 C-50,400 0,150 200,50 C400,-50 550,100 550,300 Z' fill='none' stroke='rgba(255,255,255,0.06)' stroke-width='1.5'/%3E%3Cpath d='M450,300 C450,400 300,500 150,450 C20,400 60,180 180,120 C300,60 450,200 450,300 Z' fill='none' stroke='rgba(255,255,255,0.15)' stroke-width='1'/%3E%3C/svg%3E");
    background-repeat: no-repeat;
    background-size: contain;
    z-index: 1;
    pointer-events: none;
}

/* Floating Asterisk Badge (3D element) */
.page-hero .container::after, .hero-banner .container::after, .contact-hero .container::after {
    content: '✱';
    position: absolute;
    right: 50px;
    bottom: 50px;
    width: 60px;
    height: 60px;
    background-color: var(--primary-orange);
    color: #12312D; /* Dark text for contrast */
    font-size: 38px;
    line-height: 65px;
    text-align: center;
    border-radius: 50%;
    z-index: 2;
    animation: floatingCard 5s ease-in-out infinite;
    box-shadow: 0 10px 25px rgba(245, 154, 22, 0.4); /* Orange glow */
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: sans-serif;
}

/* Ensure text is above background elements */
.page-hero h1, .hero-banner .hero-title, .contact-hero .contact-title,
.page-hero .breadcrumb-text, .hero-banner .breadcrumb-text, .contact-hero .breadcrumb-text,
.page-hero p, .hero-banner p, .contact-hero p {
    position: relative;
    z-index: 3;
}

.page-hero h1, .hero-banner .hero-title, .contact-hero .contact-title {
    font-size: 52px !important;
    margin-bottom: 15px !important;
}

.page-hero .breadcrumb-text, .hero-banner .breadcrumb-text, .contact-hero .breadcrumb-text {
    font-size: 16px;
    opacity: 0.85;
}

@media (max-width: 768px) {
    .page-hero .container, .hero-banner .container, .contact-hero .container {
        padding: 50px 30px;
        border-radius: 16px;
    }
    .page-hero h1, .hero-banner .hero-title, .contact-hero .contact-title {
        font-size: 36px !important;
    }
    .page-hero .container::after, .hero-banner .container::after, .contact-hero .container::after {
        right: 20px;
        bottom: 20px;
        width: 45px;
        height: 45px;
        font-size: 28px;
        line-height: 50px;
    }
}
"""

with open(css_file, 'a', encoding='utf-8') as f:
    f.write(new_styles)

print("Updated style.css")
