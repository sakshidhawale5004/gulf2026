import glob
import re

# 1. Update style.css to hide the asterisk
with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Replace the display block of the asterisk to hide it, or just add display: none !important
hide_asterisk = """
/* REMOVED Floating Asterisk Badge as requested */
.page-hero .container::after, .hero-banner .container::after, .contact-hero .container::after {
    display: none !important;
}

/* Also hide the static squiggly lines since we'll use particles */
.page-hero .container::before, .hero-banner .container::before, .contact-hero .container::before {
    display: none !important;
}
"""

css += hide_asterisk

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)

# 2. Inject particles.js script to all HTML files except index.html
particle_script = """
<!-- 3D Constellation Particles Script -->
<script src="https://cdn.jsdelivr.net/npm/particles.js@2.0.0/particles.min.js"></script>
<script>
document.addEventListener("DOMContentLoaded", function() {
    var heroContainers = document.querySelectorAll('.page-hero .container, .hero-banner .container, .contact-hero .container');
    heroContainers.forEach(function(container, index) {
        if (container.querySelector('.particles-hero')) return; // Already added
        var particleDiv = document.createElement('div');
        var id = 'particles-hero-' + index;
        particleDiv.id = id;
        particleDiv.className = 'particles-hero';
        particleDiv.style.position = 'absolute';
        particleDiv.style.top = '0';
        particleDiv.style.left = '0';
        particleDiv.style.width = '100%';
        particleDiv.style.height = '100%';
        particleDiv.style.zIndex = '1';
        particleDiv.style.pointerEvents = 'none';
        container.insertBefore(particleDiv, container.firstChild);
        
        particlesJS(id, {
          "particles": {
            "number": {"value": 50, "density": {"enable": true, "value_area": 800}},
            "color": {"value": "#F59A16"},
            "shape": {"type": "circle"},
            "opacity": {"value": 0.8, "random": true},
            "size": {"value": 4, "random": true},
            "line_linked": {"enable": true, "distance": 150, "color": "#F59A16", "opacity": 0.5, "width": 1.5},
            "move": {"enable": true, "speed": 3, "direction": "none", "random": true, "straight": false, "out_mode": "out", "bounce": false}
          },
          "interactivity": {
            "detect_on": "canvas",
            "events": {"onhover": {"enable": false}, "onclick": {"enable": false}, "resize": true}
          },
          "retina_detect": true
        });
    });
});
</script>
"""

html_files = glob.glob('*.html')
for html_file in html_files:
    if html_file == 'index.html':
        continue
    
    with open(html_file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Check if we already injected it
    if "<!-- 3D Constellation Particles Script -->" not in html:
        # Inject right before </body>
        if "</body>" in html:
            html = html.replace("</body>", particle_script + "\n</body>")
        else:
            html += particle_script
            
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(html)

print("Done updating CSS and HTML files.")
