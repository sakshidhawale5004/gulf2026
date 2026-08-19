import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The hero section ends at:
#                      </div>
#                 </div>
#             </div>
#         </div>
#         <!-- Bottom Curve/Wave -->
# So we need to carefully remove the col-lg-6 that holds the right side.
# Let's find the start of the right column:
right_col_start = html.find('<div class="col-lg-6 d-none d-lg-block position-relative">')
if right_col_start != -1:
    # We need to find where the right column ends. It's right before <!-- Bottom Curve/Wave -->
    # or right before the closing </div> of row.
    # The row closing div is right before the container closing div.
    bottom_curve_idx = html.find('<!-- Bottom Curve/Wave -->')
    # Let's just use regex to remove everything from right_col_start up to the row's closing div.
    # We will just replace it by hand using regex:
    html = re.sub(r'<div class="col-lg-6 d-none d-lg-block position-relative">.*?(?=</div>\s*</div>\s*</div>\s*<!-- Bottom Curve)', '', html, flags=re.DOTALL)

# Add video as background of hero section.
video_bg = '<video src="https://video-previews.elements.envatousercontent.com/h264-video-previews/ba2012e5-151f-4dae-a10e-8d06233e0074/11646827.mp4" autoplay loop muted playsinline class="position-absolute top-0 start-0 w-100 h-100" style="object-fit: cover; z-index: 0;"></video>\n    '
html = html.replace('<div class="hero-overlay"></div>', video_bg + '<div class="hero-overlay" style="z-index: 1;"></div>')

# Ensure the container has z-index 2
html = html.replace('<div class="container hero-content">', '<div class="container hero-content position-relative" style="z-index: 2;">')

# Change col-lg-6 to col-lg-10 mx-auto text-center so it looks great over a background video
html = html.replace('<div class="col-lg-6">', '<div class="col-lg-10 mx-auto text-center">')

# Because the text is centered now, we need to center the buttons
html = html.replace('class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3"', 'class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3 justify-content-center"')

# Change text to white since the video is dark
html = html.replace('class="hero-title motion-fade-up motion-delay-1 text-dark', 'class="hero-title motion-fade-up motion-delay-1 text-white')
html = html.replace('class="hero-subtitle motion-fade-up motion-delay-2 text-muted', 'class="hero-subtitle motion-fade-up motion-delay-2 text-white text-opacity-75')
html = html.replace('bg-white text-dark px-3 py-2 rounded-pill border shadow-sm', 'bg-white bg-opacity-10 text-white px-3 py-2 rounded-pill border border-white border-opacity-25')

# Center the subtitle
html = html.replace('style="max-width: 540px; line-height: 1.7;  font-weight: 200 !important;"', 'style="max-width: 700px; margin: 0 auto; line-height: 1.7;  font-weight: 200 !important;"')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

with open('style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Change the hero overlay to a darker one so the video is readable but the text stands out
dark_overlay = 'linear-gradient(135deg, rgba(15, 23, 42, 0.75) 0%, rgba(2, 6, 23, 0.85) 100%)'
css = re.sub(r'linear-gradient\(135deg,\s*rgba\(255,\s*255,\s*255[^)]+\)\s*0%,\s*rgba\([^)]+\)\s*100%\)', dark_overlay, css)

# Make hero-title and subtitle white again
css = css.replace('.hero-title { color: var(--primary-green) !important; }', '.hero-title { color: #ffffff !important; }')
css = css.replace('.hero-subtitle { color: var(--text-muted) !important; }', '.hero-subtitle { color: rgba(255, 255, 255, 0.85) !important; }')
# remove the hero-section background image if it exists
css = re.sub(r'background:\s*url\([^)]+\)\s*center/cover\s*no-repeat;', '', css)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(css)
