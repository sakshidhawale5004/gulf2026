import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# The hero section has <section class="hero-section ...
start_idx = html.find('<section class="hero-section')
end_idx = html.find('<!-- Stat Bar beneath fold -->')

hero_html = html[start_idx:end_idx]

# 1. Replace the col-lg-6 block in hero_html
hero_html = re.sub(r'<div class="col-lg-6">', '<div class="col-lg-10 mx-auto text-center">', hero_html, count=1)

# 2. Remove the right column in hero_html completely
hero_html = re.sub(r'<div class="col-lg-6 d-none d-lg-block position-relative">.*?(?=</div>\s*</div>\s*</div>\s*<!-- Bottom Curve)', '', hero_html, flags=re.DOTALL)

# 3. Add video background
video_bg = '<video src="https://video-previews.elements.envatousercontent.com/h264-video-previews/ba2012e5-151f-4dae-a10e-8d06233e0074/11646827.mp4" autoplay loop muted playsinline class="position-absolute top-0 start-0 w-100 h-100" style="object-fit: cover; z-index: 0;"></video>\n    '
hero_html = hero_html.replace('<div class="hero-overlay"></div>', video_bg + '<div class="hero-overlay" style="z-index: 1;"></div>')

hero_html = hero_html.replace('<div class="container hero-content">', '<div class="container hero-content position-relative" style="z-index: 2;">')
hero_html = hero_html.replace('class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3"', 'class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3 justify-content-center"')
hero_html = hero_html.replace('class="hero-title motion-fade-up motion-delay-1 text-dark"', 'class="hero-title motion-fade-up motion-delay-1 text-white"')
hero_html = hero_html.replace('class="hero-title motion-fade-up motion-delay-1 text-dark mb-4"', 'class="hero-title motion-fade-up motion-delay-1 text-white mb-4"')
hero_html = hero_html.replace('class="hero-subtitle motion-fade-up motion-delay-2 text-muted', 'class="hero-subtitle motion-fade-up motion-delay-2 text-white text-opacity-75')
hero_html = hero_html.replace('bg-white text-dark px-3 py-2 rounded-pill border shadow-sm', 'bg-white bg-opacity-10 text-white px-3 py-2 rounded-pill border border-white border-opacity-25')
hero_html = hero_html.replace('style="max-width: 540px; line-height: 1.7;  font-weight: 200 !important;"', 'style="max-width: 700px; margin: 0 auto; line-height: 1.7;  font-weight: 200 !important;"')

html = html[:start_idx] + hero_html + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
