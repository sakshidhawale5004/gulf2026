import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the envato video URL with the local herosectionvideo.mp4
old_url = "https://video-previews.elements.envatousercontent.com/h264-video-previews/ba2012e5-151f-4dae-a10e-8d06233e0074/11646827.mp4"
new_url = "herosectionvideo.mp4"

html = html.replace(old_url, new_url)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
