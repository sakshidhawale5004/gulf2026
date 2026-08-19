import re

files = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'services-database.html',
    'ip-licensing-database.html'
]

banner_link = '''</section>

    <!-- Methodology Link Banner -->
    <section class="py-3" style="background-color: var(--primary-green-dark);">
        <div class="container text-center">
            <a href="our-data-methodology.html" class="text-white text-decoration-none" style="font-size: 1.1rem; font-weight: 500;">
                <i class="fa-solid fa-book-open me-2 text-warning"></i> Learn about our Data & Methodology <i class="fa-solid fa-arrow-right ms-2 text-warning"></i>
            </a>
        </div>
    </section>

    <main class="container section-padding">'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = content.replace('</section>\n\n    <main class="container section-padding">', banner_link)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
