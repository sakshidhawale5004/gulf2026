import re

with open('kuwait-transfer-pricing.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix the Quick Facts heading color
content = content.replace(
    '<h4 class="fw-bold mb-4 border-bottom border-light pb-3 border-opacity-25">',
    '<h4 class="fw-bold text-white mb-4 border-bottom border-light pb-3 border-opacity-25">'
)

# Add more info section
more_info = '''
                <!-- Additional Info Section -->
                <div class="mt-5 pt-4 border-top">
                    <h3 class="mb-4 fw-bold" style="font-family: 'Cormorant Garamond', serif; color: var(--primary-green);">Key Transfer Pricing Rules & Audits</h3>
                    
                    <div class="row g-4">
                        <div class="col-md-6">
                            <div class="p-4 rounded-4 bg-white shadow-sm h-100 border-start border-4 border-success">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-link text-success me-2"></i> Related Party Definition</h5>
                                <p class="text-muted small mb-0">While no strict statutory definition exists solely for TP purposes, the Kuwait Tax Authority (KTA) broadly looks at control, shared ownership, and significant influence when determining if entities are related under Income Tax Law No. 28/2009.</p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-4 rounded-4 bg-white shadow-sm h-100 border-start border-4 border-warning">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-scale-balanced text-warning me-2"></i> Tax Audits & Penalties</h5>
                                <p class="text-muted small mb-0">The KTA has increasingly scrutinized intercompany transactions during tax audits. If a transaction is found not to be at arm's length, the KTA may adjust taxable income, resulting in additional tax liabilities and potential delay fines.</p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-4 rounded-4 bg-white shadow-sm h-100 border-start border-4 border-info">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-handshake-angle text-info me-2"></i> Advanced Pricing Agreements</h5>
                                <p class="text-muted small mb-0">Currently, there is no formal Advance Pricing Agreement (APA) program in Kuwait. Taxpayers must rely on strong documentation and benchmarking to defend their pricing retrospectively during audits.</p>
                            </div>
                        </div>
                        <div class="col-md-6">
                            <div class="p-4 rounded-4 bg-white shadow-sm h-100 border-start border-4 border-primary">
                                <h5 class="fw-bold mb-3"><i class="fa-solid fa-building-columns text-primary me-2"></i> Accepted Methods</h5>
                                <p class="text-muted small mb-0">In practice, the KTA accepts the standard OECD transfer pricing methods (CUP, Resale Price, Cost Plus, TNMM, and Profit Split), with a strong preference for the CUP method when internal comparables are available.</p>
                            </div>
                        </div>
                    </div>
                </div>
'''

content = content.replace(
    '                        </div>\n                    </div>\n                </div>\n            </div>\n\n            <!-- Right Column: Sticky Sidebar -->',
    '                        </div>\n                    </div>\n                </div>\n' + more_info + '\n            </div>\n\n            <!-- Right Column: Sticky Sidebar -->'
)

with open('kuwait-transfer-pricing.html', 'w', encoding='utf-8') as f:
    f.write(content)
