import os

dir_path = r"c:\Users\Sakshi\Downloads\new\gulftp-20-6-2026"

def replace_in_file(filename, replacements):
    path = os.path.join(dir_path, filename)
    if not os.path.exists(path):
        return
    
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(path, "r", encoding="windows-1252") as f:
            content = f.read()

    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
    
    if content != original_content:
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")

# Reduce heading sizes on pages using display-5
for f in ["book-a-demo.html", "book-an-appointment.html", "book-search.html", "update-a-search.html"]:
    replace_in_file(f, [
        ('class="display-5', 'class="display-6')
    ])

# Reduce heading size in contact.html css
replace_in_file("contact.html", [
    ('font-size: 2.4rem;', 'font-size: 2.0rem;')
])

# Make subheadings white on book-an-appointment.html
replace_in_file("book-an-appointment.html", [
    ('<h6 class="mb-0">Flexible Timing</h6>', '<h6 class="mb-0 text-white">Flexible Timing</h6>'),
    ('<h6 class="mb-0">Expert Consultation</h6>', '<h6 class="mb-0 text-white">Expert Consultation</h6>'),
    ('<h6 class="mb-0">Confidential</h6>', '<h6 class="mb-0 text-white">Confidential</h6>'),
    ('<h6 class="mb-0">WhatsApp Support</h6>', '<h6 class="mb-0 text-white">WhatsApp Support</h6>')
])

print("Done")
