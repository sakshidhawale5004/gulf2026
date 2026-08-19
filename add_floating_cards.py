import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the HTML for the two floating cards
cards_html = """
                                <!-- Floating Stat Card 1: Data Accuracy -->
                                <div class="hero-3d-element shadow-lg rounded-4 bg-white p-3" style="position: absolute; bottom: 10%; left: -10%; transform: translateZ(80px); z-index: 3; width: 200px; animation: float 5s ease-in-out infinite reverse; border-bottom: 3px solid var(--primary-green);">
                                    <div class="d-flex align-items-center mb-2 gap-2">
                                        <div class="d-flex align-items-center justify-content-center text-white" style="width: 38px; height: 38px; background: var(--primary-green); border-radius: 8px;">
                                            <i class="fa-solid fa-arrow-trend-up fs-5"></i>
                                        </div>
                                        <div class="fw-bold text-dark" style="font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; line-height: 1;">Data Accuracy</div>
                                    </div>
                                    <div class="fw-bold" style="color: var(--primary-green); font-size: 2.2rem; font-family: 'Cormorant Garamond', serif; line-height: 1.1;">100%</div>
                                </div>

                                <!-- Floating Stat Card 2: GCC Coverage -->
                                <div class="hero-3d-element shadow-lg rounded-4 bg-white p-3" style="position: absolute; top: 15%; right: -5%; transform: translateZ(50px); z-index: 3; width: 200px; animation: float 4s ease-in-out infinite; border-bottom: 3px solid var(--primary-orange);">
                                    <div class="d-flex align-items-center mb-2 gap-2">
                                        <div class="d-flex align-items-center justify-content-center text-white" style="width: 38px; height: 38px; background: #e8612c; border-radius: 8px;">
                                            <i class="fa-solid fa-building fs-5"></i>
                                        </div>
                                        <div class="fw-bold text-dark" style="font-family: 'Cormorant Garamond', serif; font-size: 1.1rem; line-height: 1;">GCC Coverage</div>
                                    </div>
                                    <div class="fw-bold" style="color: #e8612c; font-size: 2.2rem; font-family: 'Cormorant Garamond', serif; line-height: 1.1;">100,000+</div>
                                </div>
"""

# The img tag line
img_pattern = r'(<img src="gulftp-hero section\.jpg"[^>]*>)'

# Insert the cards right after the img tag
html = re.sub(img_pattern, r'\g<1>\n' + cards_html, html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
