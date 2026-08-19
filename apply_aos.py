import re

def add_aos(filename, section_marker, image_col_regex, aos_attr):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Find the section
        marker_idx = html.find(section_marker)
        if marker_idx == -1:
            print(f"Could not find marker '{section_marker}' in {filename}")
            return
            
        # We need to find the <div class="col-lg-..."> that wraps the image.
        # Since it's a row, the image col could be before or after the text col.
        # We search backwards and forwards in a reasonable window (e.g. 2000 chars before, 2000 after)
        start_search = max(0, marker_idx - 2000)
        end_search = min(len(html), marker_idx + 2000)
        window = html[start_search:end_search]
        
        # We look for <div class="col-lg-X"> (with or without other classes like order-1)
        # that contains an <img> tag.
        
        # Actually, let's just do a manual string replace based on what we know about the files.
    except Exception as e:
        print(f"Error: {e}")

# Manual string replacements are safer for complex HTML:
import re

def apply_aos_manual(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    if filepath == 'about.html':
        # 1. GCC Transfer Pricing Comparables You Can Trust (Image is on the RIGHT -> fade-left)
        # Search for: <div class="col-lg-6 order-1 order-lg-2">
        html = re.sub(r'(<div class="col-lg-6 order-1 order-lg-2"[^>]*>)(\s*<img src="Comprehensive Transfer Pricing Solutions.jpeg")', r'<div class="col-lg-6 order-1 order-lg-2" data-aos="fade-left">\2', html)

        # 2. Expert Support for Your Transfer Pricing Needs (Image is on the LEFT -> fade-right)
        # Search for: <div class="col-lg-6 mb-4 mb-lg-0">
        html = re.sub(r'(<div class="col-lg-6 mb-4 mb-lg-0"[^>]*>)(\s*<img src="Expert Support for Your Transfer Pricing Needs.jpg")', r'<div class="col-lg-6 mb-4 mb-lg-0" data-aos="fade-right">\2', html)

        # 3. Comprehensive Transfer Pricing Solutions (Image is on the LEFT -> fade-right)
        # Search for: <div class="col-lg-5"> inside Our Services Section
        html = re.sub(r'(<!-- Image Column -->\s*<div class="col-lg-5")([^>]*>)', r'\1 data-aos="fade-right"\2', html)

    elif filepath == 'index.html':
        # 4. We Provide The Best Transfer Pricing Data in the GCC (Image on LEFT -> fade-right)
        # The wrapper is `<div class="about-image-wrapper">` inside `<div class="col-lg-6">`
        # Let's add it to the wrapper itself
        html = re.sub(r'(<div class="col-lg-6">)(\s*<div class="about-image-wrapper">\s*<img src="about.imagestarting1.jpg")', r'<div class="col-lg-6" data-aos="fade-right">\2', html)

        # 4. Powered by Cutting-Edge Data Analytics (Image on LEFT -> fade-right)
        html = re.sub(r'(<div class="col-lg-6">)(\s*<div class="about-image-wrapper">\s*<img src="We Provide The Best Transfer Pricing Data in the GCC.webp")', r'<div class="col-lg-6" data-aos="fade-right">\2', html)

        # 5. Transfer Pricing Implementation Steps (Image on LEFT -> fade-right)
        html = re.sub(r'(<!-- Image Column -->\s*<div class="col-lg-5")([^>]*>)', r'\1 data-aos="fade-right"\2', html)
        
        # Also let's make sure the 3rd section from index.html (Professional Benchmarking Solutions) gets it if needed, but not requested.

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Applied AOS to {filepath}")

apply_aos_manual('about.html')
apply_aos_manual('index.html')
