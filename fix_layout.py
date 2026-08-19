with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* Restore layout for newsletter hero */
.newsletter-hero {
    min-height: 500px;
    display: flex;
    align-items: center;
    border-top: 15px solid var(--primary-green);
}
""")
print("Done")
