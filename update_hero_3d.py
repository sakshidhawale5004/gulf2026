import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Define the new 3D elements HTML
new_3d_html = """
                 <!-- Abstract 3D UI Elements replacing the image -->
                 <div class="abstract-3d-scene" style="position: relative; height: 400px; width: 100%; perspective: 1000px;">
                     
                     <!-- Main Central Dashboard Card -->
                     <div class="hero-3d-element shadow-lg rounded-4 bg-white p-4" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%) rotateY(-15deg) rotateX(5deg); width: 85%; height: 280px; z-index: 2; border: 1px solid rgba(0,0,0,0.05); transition: transform 0.5s ease;">
                         <div class="d-flex justify-content-between align-items-center mb-4 border-bottom pb-3">
                             <div class="fw-bold" style="color: var(--primary-green); font-size: 1.1rem;"><i class="fa-solid fa-chart-line me-2"></i> Benchmarking Analysis</div>
                             <div class="badge bg-light text-dark border">Live Data</div>
                         </div>
                         <!-- Mock Bars -->
                         <div class="d-flex align-items-end gap-3 h-50 mt-4 px-2">
                             <div class="w-100 rounded-top" style="background: var(--primary-green); height: 40%; opacity: 0.8;"></div>
                             <div class="w-100 rounded-top" style="background: var(--primary-orange); height: 75%; opacity: 0.9;"></div>
                             <div class="w-100 rounded-top" style="background: var(--primary-green); height: 55%; opacity: 0.85;"></div>
                             <div class="w-100 rounded-top" style="background: var(--primary-green); height: 90%; opacity: 0.95;"></div>
                             <div class="w-100 rounded-top" style="background: var(--primary-orange); height: 65%; opacity: 0.8;"></div>
                         </div>
                     </div>

                     <!-- Floating Stat Card 1 -->
                     <div class="hero-3d-element shadow-lg rounded-4 bg-white p-3 d-flex align-items-center gap-3" style="position: absolute; top: 10%; right: -5%; transform: translateZ(50px); z-index: 3; border: 1px solid rgba(0,0,0,0.05); width: 220px; animation: float 4s ease-in-out infinite;">
                         <div class="rounded-circle d-flex align-items-center justify-content-center text-white shadow-sm" style="width: 45px; height: 45px; background: var(--primary-orange);">
                             <i class="fa-solid fa-database"></i>
                         </div>
                         <div>
                             <div class="fw-bold fs-5" style="color: var(--primary-green); line-height: 1;">100,000+</div>
                             <div class="text-muted" style="font-size: 0.8rem;">Comparable Records</div>
                         </div>
                     </div>

                     <!-- Floating Stat Card 2 -->
                     <div class="hero-3d-element shadow-lg rounded-4 bg-white p-3 d-flex align-items-center gap-3" style="position: absolute; bottom: 5%; left: -5%; transform: translateZ(80px); z-index: 3; border: 1px solid rgba(0,0,0,0.05); width: 230px; animation: float 5s ease-in-out infinite reverse;">
                         <div class="rounded-circle d-flex align-items-center justify-content-center text-white shadow-sm" style="width: 45px; height: 45px; background: var(--primary-green);">
                             <i class="fa-solid fa-check-double"></i>
                         </div>
                         <div>
                             <div class="fw-bold fs-5" style="color: var(--primary-orange); line-height: 1;">Real-Time</div>
                             <div class="text-muted" style="font-size: 0.8rem;">GCC Compliance Data</div>
                         </div>
                     </div>

                 </div>
"""

# Replace the img tag with the new 3D HTML
# The original img tag is inside the <div class="position-relative hero-3d-wrapper" ...>
html = re.sub(r'<img[^>]+src="Benchmarking_Gulf_Companies_database_GulfTP_-e1755427819209\.webp"[^>]*>', new_3d_html, html)

# We also need to add keyframes for 'float' if it doesn't exist
css_addition = """
@keyframes float {
  0% { transform: translateY(0px) translateZ(50px); }
  50% { transform: translateY(-15px) translateZ(50px); }
  100% { transform: translateY(0px) translateZ(50px); }
}
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

if '@keyframes float' not in css:
    css += css_addition

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
