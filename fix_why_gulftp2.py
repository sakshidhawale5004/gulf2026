import re

files = [
    'interest-rates-database.html',
    'services-database.html',
    'ip-licensing-database.html'
]

link_button = '''
                          <div class="mt-4" data-aos="fade-up">
                              <a href="our-data-methodology.html" class="btn-conxora btn-outline px-4 py-2" style="border-color: var(--primary-green); color: var(--primary-green);">
                                  <i class="fa-solid fa-book-open me-2"></i> Our Data & Methodology
                              </a>
                          </div>
'''

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the end of the credit rating estimation paragraph
    content = re.sub(r'(credit rating estimation\.\s*</p>)', r'\1' + link_button, content)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
