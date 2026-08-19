import re

css_file = 'style.css'

new_styles = """
/* INTERNAL PAGE HERO REDESIGN */
.page-hero, .hero-banner, .contact-hero {
    background: transparent !important;
    padding: 60px 20px !important;
    text-align: left !important;
}

.page-hero .container, .hero-banner .container, .contact-hero .container {
    background-color: #ffffff; 
    /* Orange and Green spots */
    background-image: 
        radial-gradient(circle at 10% 80%, rgba(0, 107, 87, 0.08) 0%, transparent 60%),
        radial-gradient(circle at 85% 20%, rgba(245, 154, 22, 0.08) 0%, transparent 50%);
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

/* Abstract Squiggly Lines for light background */
.page-hero .container::before, .hero-banner .container::before, .contact-hero .container::before {
    content: '';
    position: absolute;
    right: -100px;
    top: -100px;
    width: 600px;
    height: 600px;
    background-image: url("data:image/svg+xml,%3Csvg viewBox='0 0 600 600' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M500,300 C500,450 350,550 200,500 C50,450 50,200 200,100 C350,0 500,150 500,300 Z' fill='none' stroke='rgba(0,107,87,0.1)' stroke-width='1.5'/%3E%3Cpath d='M550,300 C550,500 400,600 150,500 C-50,400 0,150 200,50 C400,-50 550,100 550,300 Z' fill='none' stroke='rgba(245,154,22,0.1)' stroke-width='1.5'/%3E%3Cpath d='M450,300 C450,400 300,500 150,450 C20,400 60,180 180,120 C300,60 450,200 450,300 Z' fill='none' stroke='rgba(0,107,87,0.15)' stroke-width='1'/%3E%3C/svg%3E");
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
    color: #ffffff; /* White text for contrast against orange */
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

/* Text Colors */
.page-hero h1, .hero-banner .hero-title, .contact-hero .contact-title {
    color: var(--primary-green-dark) !important;
    font-size: 52px !important;
    margin-bottom: 15px !important;
    position: relative;
    z-index: 3;
}

.page-hero .breadcrumb-text, .hero-banner .breadcrumb-text, .contact-hero .breadcrumb-text,
.page-hero .breadcrumb-text a, .hero-banner .breadcrumb-text a, .contact-hero .breadcrumb-text a {
    color: var(--text-muted) !important;
    position: relative;
    z-index: 3;
    font-weight: 600;
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

print("Updated style.css with white background")
