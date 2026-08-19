import re

with open('about.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. We Provide Gulf Data paragraph
html = html.replace(
    '<p style="font-size: 1rem; opacity: 0.8; margin-top: 16px; line-height: 1.7;">Comprehensive transfer pricing data covering the Middle East & North Africa region.</p>',
    '<p style="color: rgba(255,255,255,0.9); font-size: 1rem; margin-top: 16px; line-height: 1.7;">Comprehensive transfer pricing data covering the Middle East & North Africa region.</p>'
)

# 2. Why Choose GulfTP paragraph
html = html.replace(
    '<p style="font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px;">GulfTP is the premier transfer pricing database specifically designed for the Gulf region. We provide comprehensive, high-quality data and tools to empower your transfer pricing analysis.</p>',
    '<p style="color: rgba(255,255,255,0.9); font-size: 1.1rem; line-height: 1.8; margin-bottom: 30px;">GulfTP is the premier transfer pricing database specifically designed for the Gulf region. We provide comprehensive, high-quality data and tools to empower your transfer pricing analysis.</p>'
)

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("Added white color to dark section paragraphs")
