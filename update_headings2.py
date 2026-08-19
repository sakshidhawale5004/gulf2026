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

# 1. Contact
replace_in_file("contact.html", [
    ('<h1 class="contact-heading" style="font-weight: 400; text-transform: capitalize;">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>',
     '<h1 class="contact-heading" style="font-weight: 300; text-transform: uppercase; text-align: left;">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>')
])

# 2. Book Search
replace_in_file("book-search.html", [
    ('<h1 class="display-5 mb-4 text-white">Request a GCC Benchmark Search</h1>', 
     '<h1 class="display-5 mb-4 text-white" style="text-transform: uppercase;">Request a GCC Benchmark Search</h1>')
])

# 3. Update a search
replace_in_file("update-a-search.html", [
    ('<h1 class="display-5 mb-4 text-white" style="text-transform: capitalize;">Update A Search</h1>', 
     '<h1 class="display-5 mb-4 text-white" style="text-transform: uppercase;">Update A Search</h1>')
])

# 4. Book a demo
replace_in_file("book-a-demo.html", [
    ('<h1 class="display-5 mb-4 text-white fw-normal" style="text-transform: capitalize;">Book A Demo</h1>', 
     '<h1 class="display-5 mb-4 text-white fw-normal" style="text-transform: uppercase;">Book A Demo</h1>')
])

# 5. Book an appointment
replace_in_file("book-an-appointment.html", [
    ('<h1 class="display-5 mb-4 text-white" style="text-transform: capitalize;">Book An Appointment</h1>', 
     '<h1 class="display-5 mb-4 text-white" style="text-transform: uppercase;">Book An Appointment</h1>')
])

print("Done")
