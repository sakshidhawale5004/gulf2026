import glob

html_files = glob.glob('*.html')

old_nav = '''                        <li class="nav-item">
                            <a class="nav-link" href="about.html">About Us</a>
                        </li>'''
new_nav = '''                        <li class="nav-item">
                            <a class="nav-link" href="our-data-methodology.html">Data & Methodology</a>
                        </li>
                        <li class="nav-item">
                            <a class="nav-link" href="about.html">About Us</a>
                        </li>'''

old_footer = '''                    <a href="buy-subscription.html" class="footer-link">Buy Subscription</a>
                    <a href="about.html" class="footer-link">About Us</a>'''
new_footer = '''                    <a href="buy-subscription.html" class="footer-link">Buy Subscription</a>
                    <a href="our-data-methodology.html" class="footer-link">Data & Methodology</a>
                    <a href="about.html" class="footer-link">About Us</a>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    content = content.replace(old_nav, new_nav)
    content = content.replace(old_footer, new_footer)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
