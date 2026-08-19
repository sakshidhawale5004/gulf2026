import re

with open('kuwait-transfer-pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update Hero Image
content = re.sub(
    r"url\('https://images.unsplash.com/photo-1544551763-46a013bb70d5\?auto=format&fit=crop&q=80&w=1920'\)", 
    "url('https://images.unsplash.com/photo-1577717903315-1691ae25ab3f?auto=format&fit=crop&q=80&w=1920')", # Kuwait towers/cityscape placeholder
    content
)

# New Main Section Layout
new_main = '''    <main class="container section-padding" style="padding-top: 80px; padding-bottom: 80px;">
        <div class="row gx-5">
            <!-- Left Column: Content & Tabs -->
            <div class="col-lg-8" data-aos="fade-up">
                <div class="mb-5">
                    <span class="badge bg-success bg-opacity-10 text-success px-3 py-2 rounded-pill mb-3" style="font-weight: 600; letter-spacing: 1px;">KUWAIT TP OVERVIEW</span>
                    <h2 class="display-6 fw-bold mb-4" style="color: var(--primary-green-dark); font-family: 'Cormorant Garamond', serif;">Transfer Pricing Landscape in Kuwait</h2>
                    <p class="lead text-muted" style="font-size: 1.15rem; line-height: 1.8;">
                        The current related party rules are included in Income Tax Law No. 28/2009 effective 1 January 2010. Broadly similar related party rules were also included in the old Income Tax Law, the Law of Income Tax on Companies of 1981.
                    </p>
                    <p class="text-muted" style="font-size: 1.05rem; line-height: 1.8;">
                        While the current tax law includes related party provisions, there are no formalized tax rules on transfer pricing documentation. However, the Kuwait Tax Authority expects that appropriate TP documentation will be made available under a tax audit or investigation.
                    </p>
                </div>

                <!-- Custom Interactive Tabs for Documentation -->
                <div class="mt-5">
                    <h3 class="mb-4 fw-bold" style="font-family: 'Cormorant Garamond', serif; color: var(--primary-green);">Documentation Requirements</h3>
                    
                    <ul class="nav nav-pills mb-4" id="pills-tab" role="tablist">
                        <li class="nav-item" role="presentation">
                            <button class="nav-link active rounded-pill px-4" id="pills-local-tab" data-bs-toggle="pill" data-bs-target="#pills-local" type="button" role="tab" style="font-weight: 500;">Local File</button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link rounded-pill px-4 mx-2" id="pills-master-tab" data-bs-toggle="pill" data-bs-target="#pills-master" type="button" role="tab" style="font-weight: 500;">Master File</button>
                        </li>
                        <li class="nav-item" role="presentation">
                            <button class="nav-link rounded-pill px-4" id="pills-cbcr-tab" data-bs-toggle="pill" data-bs-target="#pills-cbcr" type="button" role="tab" style="font-weight: 500;">CbCR</button>
                        </li>
                    </ul>
                    
                    <div class="tab-content bg-white p-5 rounded-4 shadow-sm border border-light" id="pills-tabContent">
                        <div class="tab-pane fade show active" id="pills-local" role="tabpanel">
                            <div class="d-flex align-items-center mb-3">
                                <i class="fa-solid fa-file-invoice text-orange fs-3 me-3" style="color: var(--primary-orange);"></i>
                                <h4 class="mb-0 fw-bold text-dark">Local File</h4>
                            </div>
                            <p class="text-muted mb-0" style="line-height: 1.7;">While a formal Local File requirement is not explicitly defined in the law, maintaining documentation that substantiates the arm's length nature of local intercompany transactions is highly recommended to defend against tax audits.</p>
                        </div>
                        <div class="tab-pane fade" id="pills-master" role="tabpanel">
                            <div class="d-flex align-items-center mb-3">
                                <i class="fa-solid fa-file-contract text-success fs-3 me-3" style="color: var(--primary-green);"></i>
                                <h4 class="mb-0 fw-bold text-dark">Master File</h4>
                            </div>
                            <p class="text-muted mb-0" style="line-height: 1.7;">Multinational enterprises operating in Kuwait are encouraged to have Master File documentation available, providing the Kuwait Tax Authority with a high-level overview of their global business operations and transfer pricing policies.</p>
                        </div>
                        <div class="tab-pane fade" id="pills-cbcr" role="tabpanel">
                            <div class="d-flex align-items-center mb-3">
                                <i class="fa-solid fa-globe text-primary fs-3 me-3"></i>
                                <h4 class="mb-0 fw-bold text-dark">Country-by-Country Reports</h4>
                            </div>
                            <p class="text-muted mb-0" style="line-height: 1.7;">Kuwait has joined the OECD Inclusive Framework on BEPS and is taking steps to implement minimum standards, including Country-by-Country Reporting (CbCR) for applicable multinational enterprise groups.</p>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Column: Sticky Sidebar -->
            <div class="col-lg-4 mt-5 mt-lg-0" data-aos="fade-left" data-aos-delay="200">
                <div class="sticky-top" style="top: 120px;">
                    
                    <!-- Quick Facts Card -->
                    <div class="card border-0 shadow-lg mb-4" style="border-radius: 16px; background: linear-gradient(145deg, var(--primary-green-dark), var(--primary-green)); color: white;">
                        <div class="card-body p-4">
                            <h4 class="fw-bold mb-4 border-bottom border-light pb-3 border-opacity-25"><i class="fa-solid fa-bolt text-warning me-2"></i> Kuwait Quick Facts</h4>
                            
                            <ul class="list-unstyled mb-0">
                                <li class="d-flex mb-3">
                                    <i class="fa-solid fa-check-circle text-warning mt-1 me-3"></i>
                                    <span><strong>OECD Principles:</strong> Generally followed in practice despite no formalized local TP rules.</span>
                                </li>
                                <li class="d-flex mb-3">
                                    <i class="fa-solid fa-check-circle text-warning mt-1 me-3"></i>
                                    <span><strong>Audits:</strong> Authorities actively expect substantiation during tax audits.</span>
                                </li>
                                <li class="d-flex mb-3">
                                    <i class="fa-solid fa-check-circle text-warning mt-1 me-3"></i>
                                    <span><strong>BEPS:</strong> Member of the OECD Inclusive Framework.</span>
                                </li>
                                <li class="d-flex">
                                    <i class="fa-solid fa-database text-warning mt-1 me-3"></i>
                                    <span><strong>Databases:</strong> External benchmarking databases are crucial for defensibility.</span>
                                </li>
                            </ul>
                        </div>
                    </div>

                    <!-- CTA Card -->
                    <div class="card border-0 shadow-sm" style="border-radius: 16px; background: var(--bg-light);">
                        <div class="card-body p-4 text-center">
                            <div class="bg-white rounded-circle d-inline-flex align-items-center justify-content-center shadow-sm mb-3" style="width: 70px; height: 70px;">
                                <i class="fa-solid fa-magnifying-glass-chart fs-3 text-orange" style="color: var(--primary-orange);"></i>
                            </div>
                            <h4 class="fw-bold mb-2 text-dark">Need Kuwait Data?</h4>
                            <p class="text-muted small mb-4">Run a highly targeted benchmark search specifically filtered for Kuwaiti comparables.</p>
                            <a href="book-search.html" class="btn btn-orange w-100 rounded-pill fw-bold py-2 shadow-sm text-white" style="background-color: var(--primary-orange); border: none;">Book a Search <i class="fa-solid fa-arrow-right ms-2"></i></a>
                        </div>
                    </div>

                </div>
            </div>
        </div>
    </main>'''

content = re.sub(r'<main class="container section-padding">[\s\S]*?</main>', new_main, content)

# Remove the angular code from the bottom since we are not using accordion
content = re.sub(r'<script>\s*var app = angular\.module[\s\S]*?</script>', '', content)

with open('kuwait-transfer-pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
