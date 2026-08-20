import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the column div
html = html.replace('<div class="col-lg-7 col-xl-7 position-relative h-100 d-none d-lg-block pb-4">', 
                    '<div class="col-lg-7 col-xl-7 position-relative h-100 d-none d-lg-block p-0">')

# Replace the image container div
# Old: <div class="w-100 position-relative shadow-lg mt-4 me-4" style="height: calc(100% - 2rem); min-height: 85vh; background: url('herosectionimagefinal.jpg') center/cover no-repeat; border-top-left-radius: 120px; border-bottom-left-radius: 120px; border-top-right-radius: 20px; border-bottom-right-radius: 20px; overflow: hidden;">
# New: <div class="w-100 h-100 position-relative shadow-lg" style="min-height: 85vh; background: url('herosectionimagefinal.jpg') center/cover no-repeat; border-top-left-radius: 80px; border-bottom-left-radius: 80px; overflow: hidden;">
old_img_div = """<div class="w-100 position-relative shadow-lg mt-4 me-4" style="height: calc(100% - 2rem); min-height: 85vh; background: url('herosectionimagefinal.jpg') center/cover no-repeat; border-top-left-radius: 120px; border-bottom-left-radius: 120px; border-top-right-radius: 20px; border-bottom-right-radius: 20px; overflow: hidden;">"""
new_img_div = """<div class="w-100 h-100 position-relative shadow-lg" style="min-height: 85vh; background: url('herosectionimagefinal.jpg') center/cover no-repeat; border-top-left-radius: 100px; border-bottom-left-radius: 100px; overflow: hidden;">"""
html = html.replace(old_img_div, new_img_div)

# Improve the floating pill design to match the screenshot
# Old: <div class="position-absolute bottom-0 start-50 translate-middle-x mb-5 bg-white rounded-pill shadow-lg d-flex align-items-center justify-content-around py-3 px-4" style="width: 85%; max-width: 800px; z-index: 10;">
# New (softer, glassier, rounded-4 instead of fully pill if it looks better, but wait, screenshot is fully pill shaped):
old_pill = """<div class="position-absolute bottom-0 start-50 translate-middle-x mb-5 bg-white rounded-pill shadow-lg d-flex align-items-center justify-content-around py-3 px-4" style="width: 85%; max-width: 800px; z-index: 10;">"""
new_pill = """<div class="position-absolute bottom-0 start-50 translate-middle-x mb-5 rounded-pill shadow-lg d-flex align-items-center justify-content-around py-3 px-5" style="width: 85%; max-width: 800px; z-index: 10; background: rgba(255, 255, 255, 0.95); backdrop-filter: blur(15px); border: 1px solid rgba(255,255,255,0.4);">"""
html = html.replace(old_pill, new_pill)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed right side hero")
