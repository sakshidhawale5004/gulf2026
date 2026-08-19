import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_section = '''    <!-- Client Case Studies Section -->
    <section data-aos="fade-up" class="case-studies-section py-5 bg-white">
        <div class="container py-5">
            <div class="text-center mb-5">
                <span class="sub-title" style="color: var(--primary-orange); font-weight: 600; text-transform: uppercase; letter-spacing: 1px;"><i class="fa-solid fa-book-open-reader me-2"></i> Client Success</span>
                <h2 class="section-title mt-2" style="color: var(--primary-green);">Client Case Studies</h2>
                <p class="text-muted mx-auto mt-3" style="max-width: 600px;">See how leading enterprises across the GCC leverage GulfTP to streamline compliance, mitigate risks, and optimize their transfer pricing strategies.</p>
            </div>
            
            <div class="row g-4">
                <!-- Case Study 1 -->
                <div data-aos="fade-up" class="col-lg-4 col-md-6">
                    <div class="card h-100 border-0 shadow-sm case-study-card" style="border-radius: 15px; background: var(--bg-light); border-top: 4px solid var(--primary-green) !important;">
                        <div class="card-body p-4 p-xl-5 d-flex flex-column">
                            <span class="badge mb-3 align-self-start" style="background: rgba(10, 107, 79, 0.1); color: var(--primary-green); padding: 8px 12px; font-weight: 600;">[Industry - e.g. Retail]</span>
                            <h5 class="fw-bold mb-4" style="color: var(--primary-green);">[Marketing: Insert Case Study 1 Title]</h5>
                            
                            <div class="mb-3">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Challenge</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of the client's transfer pricing challenge here.]</p>
                            </div>
                            
                            <div class="mb-4">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Solution</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of how GulfTP's database solved the problem here.]</p>
                            </div>
                            
                            <div class="mt-auto pt-3 border-top">
                                <h6 class="fw-bold mb-1" style="color: #08664b;">Key Impact</h6>
                                <p class="text-dark fst-italic mb-0" style="font-size: 0.9rem;">"[Marketing: Insert a 1-sentence powerful quote or metric about the result here.]"</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Case Study 2 -->
                <div data-aos="fade-up" data-aos-delay="100" class="col-lg-4 col-md-6">
                    <div class="card h-100 border-0 shadow-sm case-study-card" style="border-radius: 15px; background: var(--bg-light); border-top: 4px solid var(--primary-green) !important;">
                        <div class="card-body p-4 p-xl-5 d-flex flex-column">
                            <span class="badge mb-3 align-self-start" style="background: rgba(10, 107, 79, 0.1); color: var(--primary-green); padding: 8px 12px; font-weight: 600;">[Industry - e.g. Manufacturing]</span>
                            <h5 class="fw-bold mb-4" style="color: var(--primary-green);">[Marketing: Insert Case Study 2 Title]</h5>
                            
                            <div class="mb-3">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Challenge</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of the client's transfer pricing challenge here.]</p>
                            </div>
                            
                            <div class="mb-4">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Solution</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of how GulfTP's database solved the problem here.]</p>
                            </div>
                            
                            <div class="mt-auto pt-3 border-top">
                                <h6 class="fw-bold mb-1" style="color: #08664b;">Key Impact</h6>
                                <p class="text-dark fst-italic mb-0" style="font-size: 0.9rem;">"[Marketing: Insert a 1-sentence powerful quote or metric about the result here.]"</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Case Study 3 -->
                <div data-aos="fade-up" data-aos-delay="200" class="col-lg-4 col-md-6">
                    <div class="card h-100 border-0 shadow-sm case-study-card" style="border-radius: 15px; background: var(--bg-light); border-top: 4px solid var(--primary-green) !important;">
                        <div class="card-body p-4 p-xl-5 d-flex flex-column">
                            <span class="badge mb-3 align-self-start" style="background: rgba(10, 107, 79, 0.1); color: var(--primary-green); padding: 8px 12px; font-weight: 600;">[Industry - e.g. Technology]</span>
                            <h5 class="fw-bold mb-4" style="color: var(--primary-green);">[Marketing: Insert Case Study 3 Title]</h5>
                            
                            <div class="mb-3">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Challenge</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of the client's transfer pricing challenge here.]</p>
                            </div>
                            
                            <div class="mb-4">
                                <h6 class="fw-bold" style="color: var(--primary-orange); font-size: 0.9rem; text-transform: uppercase;">The Solution</h6>
                                <p class="text-muted" style="font-size: 0.95rem; line-height: 1.6;">[Marketing: Insert a 2-3 sentence description of how GulfTP's database solved the problem here.]</p>
                            </div>
                            
                            <div class="mt-auto pt-3 border-top">
                                <h6 class="fw-bold mb-1" style="color: #08664b;">Key Impact</h6>
                                <p class="text-dark fst-italic mb-0" style="font-size: 0.9rem;">"[Marketing: Insert a 1-sentence powerful quote or metric about the result here.]"</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>'''

# Regex to match the entire Testimonial Section
import re
pattern = re.compile(r'<!-- Testimonial Section -->.*?<!-- Contact Info Section -->', re.DOTALL)
content = pattern.sub(new_section + '\n\n    <!-- Contact Info Section -->', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
