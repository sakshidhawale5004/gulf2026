import os

filepath = r"c:\Users\Sakshi\Downloads\new\gulftp-20-6-2026\about.html"

try:
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
except UnicodeDecodeError:
    with open(filepath, "r", encoding="windows-1252") as f:
        content = f.read()

old_str = '<h2 style="font-size: 2.8rem; margin-bottom: 0; line-height: 1.2;">We Provide<br><span style="color: #f39223;">Gulf Data</span></h2>'
new_str = '<h2 style="font-size: 2.8rem; margin-bottom: 0; line-height: 1.2; color: white;">We Provide<br><span style="color: #f39223;">Gulf Data</span></h2>'

content = content.replace(old_str, new_str)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)
print("Updated about.html")
