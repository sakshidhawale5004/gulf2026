import re

# 1. Fix index.html cards
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Card 1
old_card1 = re.search(r'<!-- Floating Stat Card 1.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if old_card1:
    new_card1 = """<!-- Floating Stat Card 1: Data Accuracy -->
                                <div class="hero-3d-element shadow-lg rounded-4 bg-white px-3 py-2" style="position: absolute; bottom: 10%; left: -8%; transform: translateZ(80px); z-index: 3; animation: float 5s ease-in-out infinite reverse; border-bottom: 3px solid var(--primary-green);">
                                    <div class="d-flex align-items-center mb-1 gap-2">
                                        <div class="d-flex align-items-center justify-content-center text-white" style="width: 28px; height: 28px; background: var(--primary-green); border-radius: 6px;">
                                            <i class="fa-solid fa-arrow-trend-up" style="font-size: 14px;"></i>
                                        </div>
                                        <div class="fw-bold text-dark" style="font-size: 0.9rem; font-family: 'Manrope', sans-serif;">Data Accuracy</div>
                                    </div>
                                    <div class="fw-bold" style="color: var(--primary-green); font-size: 1.5rem; font-family: 'Plus Jakarta Sans', sans-serif; line-height: 1;">100%</div>
                                </div>"""
    html = html.replace(old_card1.group(0), new_card1)

# Replace Card 2
old_card2 = re.search(r'<!-- Floating Stat Card 2.*?</div>\s*</div>\s*</div>', html, re.DOTALL)
if old_card2:
    new_card2 = """<!-- Floating Stat Card 2: GCC Coverage -->
                                <div class="hero-3d-element shadow-lg rounded-4 bg-white px-3 py-2" style="position: absolute; top: 15%; right: -5%; transform: translateZ(50px); z-index: 3; animation: float 4s ease-in-out infinite; border-bottom: 3px solid var(--primary-orange);">
                                    <div class="d-flex align-items-center mb-1 gap-2">
                                        <div class="d-flex align-items-center justify-content-center text-white" style="width: 28px; height: 28px; background: var(--primary-orange); border-radius: 6px;">
                                            <i class="fa-regular fa-building" style="font-size: 14px;"></i>
                                        </div>
                                        <div class="fw-bold text-dark" style="font-size: 0.9rem; font-family: 'Manrope', sans-serif;">GCC Coverage</div>
                                    </div>
                                    <div class="fw-bold" style="color: var(--primary-orange); font-size: 1.5rem; font-family: 'Plus Jakarta Sans', sans-serif; line-height: 1;">100,000+</div>
                                </div>"""
    html = html.replace(old_card2.group(0), new_card2)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. Fix style.css hero gradient
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace .hero-overlay with the gradient from the prompt
new_overlay = """.hero-overlay {
    position: absolute;
    inset: 0;
    background: linear-gradient(
      90deg,
      rgba(0, 55, 55, 0.85) 0%,
      rgba(0, 55, 55, 0.65) 35%,
      rgba(0, 35, 35, 0.35) 65%,
      rgba(0, 20, 20, 0.15) 100%
    ) !important;
}"""

# Using regex to replace the .hero-overlay block entirely
css = re.sub(r'\.hero-overlay\s*\{[^}]+\}', new_overlay, css, count=1)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Done")
