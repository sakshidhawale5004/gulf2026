import re

for filename in ['interest-rates-database.html', 'services-database.html', 'ip-licensing-database.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the specific row that has col-md-7 and col-md-5 (the text/image split)
    # and ensure it has align-items-center
    html = re.sub(r'(<div class="row)(">\s*<div class="col-md-7">)', r'\1 align-items-center\2', html)
    
    # Let's also make sure the images have shadow and better styling
    html = re.sub(r'(class="img-fluid rounded)(")', r'\1 shadow-sm"\2 style="min-height: 250px; object-fit: cover;"', html)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated alignments")
