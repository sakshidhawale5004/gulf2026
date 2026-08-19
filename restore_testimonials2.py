import re

with open('index_prev.html', 'r', encoding='utf-16') as f:
    prev_content = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    curr_content = f.read()

# Extract Testimonial Section from prev
pattern_prev = re.compile(r'(<!-- Testimonial Section -->.*?)</section>', re.DOTALL)
match = pattern_prev.search(prev_content)
if not match:
    print("Could not find Testimonial Section in prev")
else:
    testimonial_html = match.group(1) + '</section>'
    
    # Replace Client Case Studies Section in curr
    pattern_curr = re.compile(r'<!-- Client Case Studies Section -->.*?</section>', re.DOTALL)
    curr_content = pattern_curr.sub(testimonial_html, curr_content)
    
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(curr_content)
    print("Restored!")
