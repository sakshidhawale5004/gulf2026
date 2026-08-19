import re

# 1. about.html
with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Story section 1: image on right -> fade-left
# We add it to story-image-box in the first section.
# Let's replace the first instance of <div class="story-image-box">
html = html.replace('<div class="story-image-box">', '<div class="story-image-box" data-aos="fade-left">', 1)

# Story section 2: image on left -> fade-right
# The second instance of <div class="story-image-box">
html = html.replace('<div class="story-image-box">', '<div class="story-image-box" data-aos="fade-right">', 1)

# Our Services Section: "Comprehensive Transfer Pricing Solutions"
# The wrapper is <div class="solution-image-wrapper">. Image on left -> fade-right.
html = html.replace('<div class="solution-image-wrapper">', '<div class="solution-image-wrapper" data-aos="fade-right">')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)

# 2. index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Note: In my previous script, I applied fade-right to the col-lg-6 wrappers in index.html.
# Let's make sure it's applied correctly to the image wrapper or column.
# The user already saw them (maybe or maybe not). Let's explicitly add them to the wrapper just to be safe.

# In "We Provide The Best Transfer Pricing Data in the GCC"
# The wrapper is <div class="about-image-wrapper">
html = html.replace('<div class="about-image-wrapper">', '<div class="about-image-wrapper" data-aos="fade-right">', 1)

# In "Powered by Cutting-Edge Data Analytics"
html = html.replace('<div class="about-image-wrapper">', '<div class="about-image-wrapper" data-aos="fade-right">', 1)

# In "Transfer Pricing Implementation Steps"
# The wrapper is <div class="tp-image-wrapper">
html = html.replace('<div class="tp-image-wrapper">', '<div class="tp-image-wrapper" data-aos="fade-right">')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("AOS attributes applied")
