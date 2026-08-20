import re

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's redesign the footer CSS completely.

new_footer_css = """
/* ==========================================================================
   NEW REDESIGNED FOOTER (Dark Teal & Orange Reference Design)
   ========================================================================== */
.footer {
    background-color: var(--deep-teal); /* Dark green/teal base */
    color: #e2e8f0;
    padding: 0 0 30px;
    font-size: 0.95rem;
    margin-top: 60px;
    border-top: none;
    position: relative;
    overflow: hidden; /* For the giant watermark */
}

/* Giant background watermark imitating the reference "A" */
.footer::before {
    content: '*';
    position: absolute;
    top: 50%;
    left: 10%;
    transform: translateY(-50%) rotate(15deg);
    font-size: 800px;
    font-family: 'GT Walsheim', 'Outfit', sans-serif;
    color: var(--primary-green); /* A lighter green overlay on the dark teal */
    opacity: 0.05;
    z-index: 0;
    line-height: 0;
    pointer-events: none;
}
.footer::after {
    content: '*';
    position: absolute;
    bottom: -20%;
    right: 5%;
    transform: rotate(-15deg);
    font-size: 500px;
    font-family: 'GT Walsheim', 'Outfit', sans-serif;
    color: var(--primary-orange);
    opacity: 0.03;
    z-index: 0;
    line-height: 0;
    pointer-events: none;
}

.footer-wave {
    position: absolute;
    top: -59px;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
    z-index: 2;
}
.footer-wave svg {
    display: block;
    width: calc(100% + 4px);
    height: 60px;
    margin-left: -2px;
}
.footer-wave path {
    fill: var(--deep-teal) !important;
}

.footer-heading {
    color: var(--primary-orange) !important; /* Orange combination as requested */
    margin-bottom: 25px;
    font-weight: 500 !important; /* Synchronized font weight */
    font-size: 1.15rem;
    letter-spacing: 0.5px;
    position: relative;
    z-index: 2;
}

.footer-link {
    color: #f8fafc !important; /* Bright white text like the reference */
    text-decoration: none;
    transition: all 0.3s ease;
    display: block;
    margin-bottom: 14px;
    font-size: 0.95rem;
    position: relative;
    z-index: 2;
}
.footer-link:hover {
    color: var(--primary-orange) !important;
    transform: translateX(6px);
}

.footer-contact {
    color: #f8fafc;
    position: relative;
    z-index: 2;
}
.footer-contact a {
    color: #f8fafc;
    text-decoration: none;
    transition: 0.3s;
}
.footer-contact a:hover {
    color: var(--primary-orange);
}

.footer-bottom-bar {
    margin-top: 50px;
    padding-top: 25px;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    font-size: 0.85rem;
    color: #cbd5e1;
    position: relative;
    z-index: 2;
}
.footer-legal-links a {
    color: var(--primary-orange);
    text-decoration: none;
    transition: 0.3s ease;
}
.footer-legal-links a:hover {
    color: white;
}

.social-icons-modern {
    display: flex;
    gap: 12px;
    position: relative;
    z-index: 2;
}
.social-icons-modern a {
    display: flex;
    align-items: center;
    justify-content: center;
    width: 40px;
    height: 40px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.08);
    color: white;
    text-decoration: none;
    transition: all 0.3s ease;
}
.social-icons-modern a:hover {
    background: var(--primary-orange);
    color: white;
    transform: translateY(-3px);
}

/* Redesign the newsletter input */
.footer-input {
    background: rgba(255, 255, 255, 0.05) !important;
    border: 1px solid rgba(255,255,255,0.1) !important;
    color: white !important;
    border-radius: 8px;
    padding: 12px 45px 12px 15px;
}
.footer-input::placeholder {
    color: rgba(255,255,255,0.4) !important;
}
.footer-submit-btn {
    position: absolute;
    right: 5px;
    top: 50%;
    transform: translateY(-50%);
    background: var(--primary-orange) !important;
    color: white !important;
    border: none;
    border-radius: 6px;
    width: 35px;
    height: 35px;
    display: flex;
    align-items: center;
    justify-content: center;
}
.footer-submit-btn:hover {
    background: white !important;
    color: var(--primary-orange) !important;
}
"""

# Now we need to replace the old .footer CSS rules.
# This might be tricky because there are many fragmented footer rules.
# A safer approach is to strip all old .footer rules and append the new ones.
# Let's find and remove blocks starting with .footer
css = re.sub(r'\.footer\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-wave\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-wave svg\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-heading\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-link\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-link:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-contact\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-bottom-bar\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-legal-links a\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-legal-links a:hover\s*\{[^}]*\}', '', css)
css = re.sub(r'\.social-icons-modern\s*\{[^}]*\}', '', css)
css = re.sub(r'\.social-icons-modern a\s*\{[^}]*\}', '', css)
css = re.sub(r'\.social-icons-modern a:hover\s*\{[^}]*\}', '', css)

# There might also be footer-newsletter, footer-input etc.
css = re.sub(r'\.footer-newsletter\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-input\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-input::placeholder\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-submit-btn\s*\{[^}]*\}', '', css)
css = re.sub(r'\.footer-submit-btn:hover\s*\{[^}]*\}', '', css)

css += new_footer_css

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Redesigned footer in style.css")
