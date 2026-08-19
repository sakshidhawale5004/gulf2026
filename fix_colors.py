with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Fix text color in internal hero white containers */
.page-hero .container, .hero-banner .container, .contact-hero .container, .subscription-hero .container {
    color: var(--text-color, #333) !important;
}

/* Ensure paragraph text specifically is dark */
.contact-hero .container p, .page-hero .container p, .hero-banner .container p, .subscription-hero .container p {
    color: var(--text-muted, #555) !important;
}
""")
print("Done")
