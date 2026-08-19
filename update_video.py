import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the tsparticles container with the video tag
video_tag = '<video src="https://video-previews.elements.envatousercontent.com/h264-video-previews/ba2012e5-151f-4dae-a10e-8d06233e0074/11646827.mp4" autoplay loop muted playsinline style="width: 100%; height: 100%; position: absolute; top: 0; left: 0; z-index: 1; object-fit: cover;"></video>'
html = re.sub(r'<div id="tsparticles-hero"[^>]*></div>', video_tag, html)

# Remove the tsParticles scripts
scripts_to_remove = [
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-engine@2/tsparticles.engine.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-basic@2/tsparticles.basic.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-particles-links@2/tsparticles.interaction.particles.links.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-external-grab@2/tsparticles.interaction.external.grab.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-interaction-external-push@2/tsparticles.interaction.external.push.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-move-base@2/tsparticles.move.base.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-shape-circle@2/tsparticles.shape.circle.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-color@2/tsparticles.updater.color.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-opacity@2/tsparticles.updater.opacity.min.js"></script>',
    '<script src="https://cdn.jsdelivr.net/npm/tsparticles-updater-size@2/tsparticles.updater.size.min.js"></script>',
    '<!-- tsParticles scripts for high quality motion data network -->'
]

for s in scripts_to_remove:
    html = html.replace(s, '')

# Also remove the inline script for tsParticles
html = re.sub(r'<script>\s*document\.addEventListener\("DOMContentLoaded", function\(\) {\s*async function loadParticles.*?if \(window\.tsParticles\).*?\}\s*\);\s*</script>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
