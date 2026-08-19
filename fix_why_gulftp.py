import re

files = [
    'gulf-company-database.html',
    'interest-rates-database.html',
    'services-database.html',
    'ip-licensing-database.html'
]

link_button = '''<div class="mt-4">
                            <a href="our-data-methodology.html" class="btn-conxora btn-outline px-4 py-2" style="border-color: var(--primary-green); color: var(--primary-green);">
                                <i class="fa-solid fa-book-open me-2"></i> Our Data & Methodology
                            </a>
                        </div>'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Why GulfTP section and add the button after the last <p> tag inside it.
    if file == 'gulf-company-database.html':
        content = content.replace(
            '<p class="section-desc mb-0">With just one powerful login, you\'ll have all the essential tools and data you need to confidently navigate the complexities of Transfer Pricing at your fingertips.</p>',
            '<p class="section-desc mb-0">With just one powerful login, you\'ll have all the essential tools and data you need to confidently navigate the complexities of Transfer Pricing at your fingertips.</p>\n                        ' + link_button
        )
    else:
        content = content.replace(
            'analysis with in-house tools for DEMPE analysis and credit rating estimation.</p>',
            'analysis with in-house tools for DEMPE analysis and credit rating estimation.</p>\n                        ' + link_button
        )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
