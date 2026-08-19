import os

dir_path = r"c:\Users\Sakshi\Downloads\new\gulftp-20-6-2026"

def replace_in_file(filename, replacements):
    path = os.path.join(dir_path, filename)
    if not os.path.exists(path):
        print(f"File not found: {filename}")
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
        # Save as UTF-8
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filename}")
    else:
        print(f"No changes made to {filename}")

# 1. Contact
replace_in_file("contact.html", [
    ('<h1 class="contact-heading">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>',
     '<h1 class="contact-heading" style="font-weight: 400; text-transform: capitalize;">Get in touch for transfer pricing<br>guidance and GCC benchmark searches</h1>')
])

# 2. Ready to Get Started
rtgs_old = '<h2 style="font-size: 2.5rem; font-weight: 800; margin-bottom: 15px;">Ready to Get Started?</h2>'
rtgs_new = '<h2 class="text-white" style="font-size: 2.5rem; font-weight: 400; margin-bottom: 15px;">Ready to Get Started?</h2>'

for f in ["interest-rates-database.html", "gulf-company-database.html", "ip-licensing-database.html", "services-database.html"]:
    replace_in_file(f, [(rtgs_old, rtgs_new)])

# 3. Book Search
replace_in_file("book-search.html", [
    ('<h6 class="mb-1">Submit Your Request</h6>', '<h6 class="mb-1 text-white">Submit Your Request</h6>'),
    ('<h6 class="mb-1">Secure Your Report</h6>', '<h6 class="mb-1 text-white">Secure Your Report</h6>'),
    ('<h6 class="mb-1">Receive Your Benchmarking Report</h6>', '<h6 class="mb-1 text-white">Receive Your Benchmarking Report</h6>')
])

# 4. Update a search
replace_in_file("update-a-search.html", [
    ('<h1 class="display-5 mb-4 text-white">Update A Search</h1>', '<h1 class="display-5 mb-4 text-white" style="text-transform: capitalize;">Update A Search</h1>'),
    ('<h6 class="mb-1">Provide Previous Details</h6>', '<h6 class="mb-1 text-white">Provide Previous Details</h6>'),
    ('<h6 class="mb-1">Secure Your Report</h6>', '<h6 class="mb-1 text-white">Secure Your Report</h6>'),
    ('<h6 class="mb-1">Receive Your Data</h6>', '<h6 class="mb-1 text-white">Receive Your Data</h6>')
])

# 5. Book a demo
replace_in_file("book-a-demo.html", [
    ('<h1 class="display-5 mb-4 text-white fw-normal">Book A Demo</h1>', '<h1 class="display-5 mb-4 text-white fw-normal" style="text-transform: capitalize;">Book A Demo</h1>')
])

# 6. Book an appointment
replace_in_file("book-an-appointment.html", [
    ('<h1 class="display-5 mb-4 text-white">Book An Appointment</h1>', '<h1 class="display-5 mb-4 text-white" style="text-transform: capitalize;">Book An Appointment</h1>')
])

print("Done")
