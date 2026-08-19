import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace title
content = content.replace('<title>GulfTP - About Us</title>', '<title>GulfTP - Our Data & Methodology</title>')

# Replace the hero section content
content = re.sub(r'<h1 class="hero-title text-white".*?</h1>', '<h1 class="hero-title text-white" style="font-family: \'Cormorant Garamond\', serif; font-weight: 500;">Our Data & Methodology</h1>', content)
content = re.sub(r'<p class="hero-subtitle text-white-50 mb-0".*?</p>', '<p class="hero-subtitle text-white-50 mb-0" style="font-size: 1.15rem; font-weight: 300;">[TBD by Marketing] Transparent, reliable, and verified transfer pricing data for the GCC region.</p>', content)

new_content = '''    <!-- Data & Methodology Content -->
    <section class="py-5" style="background-color: var(--bg-light);">
        <div class="container">
            <div class="row mb-5">
                <div class="col-12">
                    <div class="p-5 bg-white shadow-sm rounded-4 border-top border-4 border-success">
                        <h2 class="mb-4 text-uppercase">Company Database</h2>
                        <h5 class="text-muted mb-3">[Final content will be provided by the marketing team]</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data sourcing: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data coverage: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Update frequency: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data validation process: [TBD]</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="row mb-5">
                <div class="col-12">
                    <div class="p-5 bg-white shadow-sm rounded-4 border-top border-4 border-warning">
                        <h2 class="mb-4 text-uppercase">Royalty/IP Database</h2>
                        <h5 class="text-muted mb-3">[Final content will be provided by the marketing team]</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data sourcing: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data coverage: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Update frequency: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data validation process: [TBD]</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="row mb-5">
                <div class="col-12">
                    <div class="p-5 bg-white shadow-sm rounded-4 border-top border-4 border-success">
                        <h2 class="mb-4 text-uppercase">Loan/Interest Rate Database</h2>
                        <h5 class="text-muted mb-3">[Final content will be provided by the marketing team]</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data sourcing: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data coverage: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Update frequency: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data validation process: [TBD]</li>
                        </ul>
                    </div>
                </div>
            </div>

            <div class="row mb-5">
                <div class="col-12">
                    <div class="p-5 bg-white shadow-sm rounded-4 border-top border-4 border-warning">
                        <h2 class="mb-4 text-uppercase">Services Database</h2>
                        <h5 class="text-muted mb-3">[Final content will be provided by the marketing team]</h5>
                        <ul class="list-unstyled">
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data sourcing: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data coverage: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Update frequency: [TBD]</li>
                            <li class="mb-2"><i class="fa-solid fa-check text-success me-2"></i> Data validation process: [TBD]</li>
                        </ul>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

content = re.sub(r'<!-- Storytelling Section 1 -->[\s\S]*?<!-- Unique Futuristic Footer -->', new_content + '\n    <!-- Unique Futuristic Footer -->', content)

with open('our-data-methodology.html', 'w', encoding='utf-8') as f:
    f.write(content)
