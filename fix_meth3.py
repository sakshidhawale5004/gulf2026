import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_content = '''    <!-- Data & Methodology Content -->
    <section class="py-5" style="background-color: var(--bg-light); position: relative;">
        <!-- Decorative Background -->
        <div style="position: absolute; top: 0; right: 0; width: 400px; height: 400px; background: radial-gradient(circle, rgba(245,145,32,0.1) 0%, rgba(255,255,255,0) 70%); z-index: 0; pointer-events: none;"></div>
        <div style="position: absolute; bottom: 0; left: 0; width: 500px; height: 500px; background: radial-gradient(circle, rgba(8,102,75,0.08) 0%, rgba(255,255,255,0) 70%); z-index: 0; pointer-events: none;"></div>

        <div class="container position-relative z-index-1">
            <div class="text-center mb-5">
                <span class="badge bg-success bg-opacity-10 text-success px-3 py-2 rounded-pill mb-3" style="font-weight: 600; letter-spacing: 1px;">OUR PROCESS</span>
                <h2 class="display-5 fw-bold" style="color: var(--primary-green-dark); font-family: 'Cormorant Garamond', serif;">Data Integrity & Methodology</h2>
                <p class="lead text-muted mx-auto mt-3" style="max-width: 700px; font-size: 1.1rem;">We employ rigorous validation, verification, and benchmarking processes to ensure that all transfer pricing data is highly accurate and regulation-compliant across the GCC.</p>
            </div>

            <div class="row g-4">
                <!-- Company Database -->
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="100">
                    <div class="card h-100 border-0 shadow-lg p-5" style="border-radius: 20px; border-top: 5px solid var(--primary-green) !important; background: white; transition: transform 0.3s ease;">
                        <div class="d-flex align-items-center mb-4">
                            <div class="bg-success bg-opacity-10 text-success rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 60px; height: 60px; font-size: 1.5rem;">
                                <i class="fa-solid fa-building"></i>
                            </div>
                            <h3 class="mb-0 text-uppercase" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.6rem; color: var(--primary-green-dark);">Company Database</h3>
                        </div>
                        <p class="text-muted mb-4 pb-2 border-bottom">[Marketing team to provide final overview of the Company Database methodology and scope here.]</p>
                        
                        <div class="d-flex flex-column gap-3">
                            <div class="d-flex">
                                <i class="fa-solid fa-satellite-dish text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Data Sourcing</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain where the company data is sourced from]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-globe text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Coverage</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the regional/global coverage and volume]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-clock-rotate-left text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain how frequently the data is updated]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-shield-check text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Validation Process</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the QA and compliance validation process]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Royalty/IP Database -->
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="200">
                    <div class="card h-100 border-0 shadow-lg p-5" style="border-radius: 20px; border-top: 5px solid var(--primary-orange) !important; background: white; transition: transform 0.3s ease;">
                        <div class="d-flex align-items-center mb-4">
                            <div class="bg-warning bg-opacity-10 text-warning rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 60px; height: 60px; font-size: 1.5rem;">
                                <i class="fa-solid fa-fingerprint"></i>
                            </div>
                            <h3 class="mb-0 text-uppercase" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.6rem; color: var(--primary-green-dark);">Royalty/IP Database</h3>
                        </div>
                        <p class="text-muted mb-4 pb-2 border-bottom">[Marketing team to provide final overview of the Royalty and IP Database methodology here.]</p>
                        
                        <div class="d-flex flex-column gap-3">
                            <div class="d-flex">
                                <i class="fa-solid fa-satellite-dish text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Data Sourcing</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain where the IP data is sourced from]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-globe text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Coverage</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the regional/global coverage and volume]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-clock-rotate-left text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain how frequently the data is updated]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-shield-check text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Validation Process</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the QA and compliance validation process]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Loan/Interest Rate Database -->
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="300">
                    <div class="card h-100 border-0 shadow-lg p-5" style="border-radius: 20px; border-top: 5px solid var(--primary-green) !important; background: white; transition: transform 0.3s ease;">
                        <div class="d-flex align-items-center mb-4">
                            <div class="bg-success bg-opacity-10 text-success rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 60px; height: 60px; font-size: 1.5rem;">
                                <i class="fa-solid fa-chart-line"></i>
                            </div>
                            <h3 class="mb-0 text-uppercase" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.6rem; color: var(--primary-green-dark);">Interest Rate Database</h3>
                        </div>
                        <p class="text-muted mb-4 pb-2 border-bottom">[Marketing team to provide final overview of the Loan and Interest Rate Database methodology here.]</p>
                        
                        <div class="d-flex flex-column gap-3">
                            <div class="d-flex">
                                <i class="fa-solid fa-satellite-dish text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Data Sourcing</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain where the interest rate data is sourced from]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-globe text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Coverage</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the regional/global coverage and volume]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-clock-rotate-left text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain how frequently the data is updated]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-shield-check text-orange mt-1 me-3" style="color: var(--primary-orange);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Validation Process</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the QA and compliance validation process]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Services Database -->
                <div class="col-lg-6" data-aos="fade-up" data-aos-delay="400">
                    <div class="card h-100 border-0 shadow-lg p-5" style="border-radius: 20px; border-top: 5px solid var(--primary-orange) !important; background: white; transition: transform 0.3s ease;">
                        <div class="d-flex align-items-center mb-4">
                            <div class="bg-warning bg-opacity-10 text-warning rounded-circle d-flex align-items-center justify-content-center me-3" style="width: 60px; height: 60px; font-size: 1.5rem;">
                                <i class="fa-solid fa-handshake"></i>
                            </div>
                            <h3 class="mb-0 text-uppercase" style="font-family: 'Cormorant Garamond', serif; font-weight: 600; font-size: 1.6rem; color: var(--primary-green-dark);">Services Database</h3>
                        </div>
                        <p class="text-muted mb-4 pb-2 border-bottom">[Marketing team to provide final overview of the Services Database methodology here.]</p>
                        
                        <div class="d-flex flex-column gap-3">
                            <div class="d-flex">
                                <i class="fa-solid fa-satellite-dish text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Data Sourcing</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain where the services data is sourced from]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-globe text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Coverage</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the regional/global coverage and volume]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-clock-rotate-left text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Update Cadence</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain how frequently the data is updated]</p>
                                </div>
                            </div>
                            <div class="d-flex">
                                <i class="fa-solid fa-shield-check text-success mt-1 me-3" style="color: var(--primary-green);"></i>
                                <div>
                                    <h6 class="mb-1 fw-bold text-dark">Validation Process</h6>
                                    <p class="text-muted small mb-0">[TBD: Explain the QA and compliance validation process]</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>
'''

content = re.sub(r'    <!-- Data & Methodology Content -->[\s\S]*?</section>', new_content, content)

with open('our-data-methodology.html', 'w', encoding='utf-8') as f:
    f.write(content)
