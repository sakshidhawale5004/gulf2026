import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the Navbar to be solid white on the home page
html = re.sub(
    r'<nav class="navbar navbar-expand-lg fixed-top navbar-dark py-3" id="mainNav">',
    r'<nav class="navbar navbar-expand-lg fixed-top navbar-light py-3 bg-white shadow-sm" id="mainNav">',
    html
)

# 2. Replace the Hero Section completely
# The hero section starts at <!-- Video Hero Section --> and ends before <!-- About Company Section -->
start_hero = html.find('<!-- Video Hero Section -->')
end_hero = html.find('<!-- About Company Section (Conxora Style) -->')

if start_hero == -1:
    start_hero = html.find('<section class="hero position-relative')

if end_hero == -1:
    end_hero = html.find('<!-- About Company Section')

if start_hero != -1 and end_hero != -1:
    new_hero = """<!-- Split Hero Section -->
    <section class="hero position-relative d-flex align-items-center overflow-hidden bg-white" style="min-height: 100vh; padding-top: 80px;">
        <div class="container-fluid p-0 h-100">
            <div class="row g-0 h-100 align-items-stretch">
                
                <!-- Left Text Column -->
                <div class="col-lg-5 col-xl-5 px-4 px-md-5 py-5 d-flex flex-column justify-content-center position-relative z-index-2">
                    <div class="ps-xl-5 mt-4">
                        
                        <div class="d-inline-flex align-items-center mb-4 px-3 py-2 rounded-pill bg-white shadow-sm" style="border: 1px solid rgba(0,0,0,0.05);">
                            <span class="d-inline-block rounded-circle me-2" style="width:8px; height:8px; background-color: var(--primary-orange);"></span>
                            <span class="text-muted fw-medium" style="font-size: 0.8rem; letter-spacing: 1px;">GCC REGIONAL DATA</span>
                        </div>
                        
                        <h1 class="hero-title text-dark mb-4" style="font-size: clamp(2.5rem, 4vw, 4.5rem); font-weight: 600 !important; line-height: 1.1; letter-spacing: -1px;">
                            Unlock Over <br>
                            <span style="color: var(--primary-orange);">100,000+</span><br>
                            Comparable<br>
                            Companies
                        </h1>
                        
                        <p class="hero-subtitle text-muted mb-5" style="max-width: 480px; font-size: 1.1rem; line-height: 1.7;">
                            GulfTP is the premier transfer pricing benchmarking database built entirely for the GCC region. Elevate your financial strategies with high-precision data.
                        </p>
                        
                        <div class="d-flex flex-wrap gap-3 mb-5">
                            <a href="buy-subscription.html" class="btn fw-medium px-4 py-3 rounded-2 shadow-sm d-flex align-items-center gap-2" style="background: var(--primary-orange); color: white; border: none;">
                                <i class="fa-solid fa-magnifying-glass"></i> REQUEST BENCHMARK
                            </a>
                            <a href="book-a-demo.html" class="btn fw-medium px-4 py-3 rounded-2 d-flex align-items-center gap-2" style="background: transparent; border: 2px solid #e2e8f0; color: var(--deep-teal);">
                                BOOK DEMO <i class="fa-regular fa-calendar"></i>
                            </a>
                        </div>
                        
                        <div class="d-flex align-items-center gap-3 mt-4 scroll-explore" style="opacity: 0.7;">
                            <span class="text-muted fw-medium" style="font-size: 0.75rem; letter-spacing: 1px;">SCROLL TO EXPLORE</span>
                            <div class="rounded-circle d-flex align-items-center justify-content-center" style="width:30px; height:30px; border: 1px solid #e2e8f0;">
                                <i class="fa-solid fa-arrow-down text-muted" style="font-size: 0.75rem;"></i>
                            </div>
                        </div>
                        
                    </div>
                </div>
                
                <!-- Right Image Column -->
                <div class="col-lg-7 col-xl-7 position-relative h-100 d-none d-lg-block">
                    <!-- The massive border-radius container -->
                    <div class="w-100 position-relative shadow-lg" style="height: 95vh; margin-top: 2.5vh; background: url('herosectionimagefinal.jpg') center/cover no-repeat; border-top-left-radius: 100px; border-bottom-left-radius: 100px; overflow: hidden;">
                        
                        <!-- Overlay for better contrast if image is too bright -->
                        <div class="position-absolute top-0 start-0 w-100 h-100" style="background: linear-gradient(to right, rgba(10,34,28,0.7), rgba(10,34,28,0.2));"></div>

                        <!-- Floating Info Bar -->
                        <div class="position-absolute bottom-0 start-50 translate-middle-x mb-5 bg-white rounded-pill shadow-lg d-flex align-items-center justify-content-around py-3 px-4" style="width: 85%; max-width: 800px; z-index: 10;">
                            
                            <div class="d-flex align-items-center gap-3">
                                <div class="fs-3" style="color: var(--primary-green);"><i class="fa-solid fa-chart-simple"></i></div>
                                <div>
                                    <div class="fw-bold text-dark fs-5" style="line-height: 1;">100K+</div>
                                    <div class="text-muted" style="font-size: 0.8rem; line-height: 1.2;">Comparable<br>Companies</div>
                                </div>
                            </div>
                            
                            <div style="width:1px; height:40px; background:#e2e8f0;"></div>
                            
                            <div class="d-flex align-items-center gap-3">
                                <div class="fs-3" style="color: var(--primary-green);"><i class="fa-solid fa-earth-americas"></i></div>
                                <div>
                                    <div class="fw-bold text-dark fs-5" style="line-height: 1;">GCC</div>
                                    <div class="text-muted" style="font-size: 0.8rem; line-height: 1.2;">Regional<br>Coverage</div>
                                </div>
                            </div>
                            
                            <div style="width:1px; height:40px; background:#e2e8f0;"></div>
                            
                            <div class="d-flex align-items-center gap-3">
                                <div class="fs-3" style="color: var(--primary-green);"><i class="fa-solid fa-clock-rotate-left"></i></div>
                                <div>
                                    <div class="fw-bold text-dark fs-5" style="line-height: 1;">24/7</div>
                                    <div class="text-muted" style="font-size: 0.8rem; line-height: 1.2;">Data<br>Access</div>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
                
            </div>
        </div>
    </section>

    """
    html = html[:start_hero] + new_hero + html[end_hero:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated Hero Section")
