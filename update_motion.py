import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

particles_html = """
                 <!-- High Quality Motion Element: Data Network -->
                 <div id="hero-motion-element" class="position-relative shadow-lg rounded-4 overflow-hidden bg-white" style="height: 450px; width: 100%; border: 1px solid rgba(0,0,0,0.05); transform: perspective(1000px) rotateY(-5deg); transition: transform 0.5s ease;">
                     <!-- Mac-style Window Header -->
                     <div class="position-absolute top-0 start-0 w-100 p-3 border-bottom bg-light d-flex align-items-center gap-2 z-3">
                         <div class="rounded-circle" style="width: 12px; height: 12px; background: #ff5f56;"></div>
                         <div class="rounded-circle" style="width: 12px; height: 12px; background: #ffbd2e;"></div>
                         <div class="rounded-circle" style="width: 12px; height: 12px; background: #27c93f;"></div>
                         <div class="ms-3 fw-bold text-muted" style="font-size: 0.85rem;"><i class="fa-solid fa-network-wired me-2"></i>Live GCC Data Network</div>
                     </div>
                     
                     <!-- Particles Container -->
                     <div id="tsparticles-hero" style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; z-index: 1;"></div>
                     
                     <!-- Overlay Data Card -->
                     <div class="position-absolute bottom-0 end-0 m-4 p-3 bg-white rounded-3 shadow-sm z-3 border" style="width: 220px; animation: float 4s ease-in-out infinite;">
                         <div class="d-flex align-items-center gap-2 mb-2">
                             <div class="spinner-grow spinner-grow-sm text-success" role="status"></div>
                             <span class="fw-bold" style="color: var(--primary-green); font-size: 0.9rem;">System Active</span>
                         </div>
                         <div class="text-muted" style="font-size: 0.8rem; line-height: 1.4;">Processing 100k+ Comparable Records in real-time.</div>
                     </div>
                 </div>
"""

# Find the start of the <div class="motion-fade-up motion-delay-2" style="z-index: 2; position: relative;">
# and replace everything inside it.
start_idx = html.find('<div class="motion-fade-up motion-delay-2" style="z-index: 2; position: relative;">')
if start_idx != -1:
    end_idx = html.find('</div>\n                </div>\n            </div>\n        </div>', start_idx)
    if end_idx != -1:
        html = html[:start_idx] + f'<div class="motion-fade-up motion-delay-2" style="z-index: 2; position: relative;">\n{particles_html}\n' + html[end_idx:]

scripts = """
    <!-- tsParticles scripts for high quality motion data network -->
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-engine@2/tsparticles.engine.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-basic@2/tsparticles.basic.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-particles-links@2/tsparticles.interaction.particles.links.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-external-grab@2/tsparticles.interaction.external.grab.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-external-push@2/tsparticles.interaction.external.push.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-move-base@2/tsparticles.move.base.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-shape-circle@2/tsparticles.shape.circle.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-color@2/tsparticles.updater.color.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-opacity@2/tsparticles.updater.opacity.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-size@2/tsparticles.updater.size.min.js"></script>
    
    <script>
      document.addEventListener("DOMContentLoaded", function() {
        async function loadParticles(tsParticles) {
            await tsParticles.load("tsparticles-hero", {
                fpsLimit: 60,
                particles: {
                    number: { value: 60, density: { enable: true, value_area: 800 } },
                    color: { value: ["#08664b", "#f59120"] },
                    shape: { type: "circle" },
                    opacity: { value: 0.6, random: false },
                    size: { value: 4, random: true },
                    links: { enable: true, distance: 150, color: "#08664b", opacity: 0.3, width: 1.5 },
                    move: { enable: true, speed: 1.5, direction: "none", random: false, straight: false, outModes: "bounce" }
                },
                interactivity: {
                    events: { onHover: { enable: true, mode: "grab" }, onClick: { enable: true, mode: "push" } },
                    modes: { grab: { distance: 140, links: { opacity: 0.8 } }, push: { quantity: 4 } }
                },
                detectRetina: true,
                background: { color: "#ffffff" }
            });
        }
        if (window.tsParticles) {
            loadParticles(window.tsParticles);
        }
      });
    </script>
</body>
"""

if "tsparticles-hero" not in html:
    html = html.replace('</body>', scripts)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
