import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Locate the value added section
start_idx = html.find('<!-- Value Added Services Section -->')
if start_idx != -1:
    end_idx = html.find('</section>', start_idx)
    section_html = html[start_idx:end_idx]
    
    # We want to remove Card 5 to Card 8.
    # The structure has comments like <!-- Card 5 -->
    
    # Let's find <!-- Card 5 -->
    card_5_idx = section_html.find('<!-- Card 5 -->')
    
    # We need to find the end of Card 8. Or just everything up to the Get In Touch button container.
    get_in_touch_idx = section_html.find('<div class="text-center mt-5">', card_5_idx)
    
    if card_5_idx != -1 and get_in_touch_idx != -1:
        # Remove everything between <!-- Card 5 --> and <div class="text-center mt-5">
        new_section_html = section_html[:card_5_idx] + '            </div>\n\n            ' + section_html[get_in_touch_idx:]
        
        # We need to ensure the closing </div> for the row is still there. 
        # Wait, the closing </div> for the row is just before <div class="text-center mt-5">.
        # So I will just use regex or split to carefully remove Cards 5 through 8.
        pass

# Let's use a simpler string replace since we know the exact HTML structure I wrote earlier.
# The HTML for cards 5-8 looks like this:
html_to_remove = """
                <!-- Card 5 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-magnifying-glass"></i></div>
                        <h4>Custom Searches</h4>
                        <p>Can't find what you need? Request bespoke benchmarking searches tailored to your exact industry and transaction type.</p>
                        <a href="book-search.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 6 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-screwdriver-wrench"></i></div>
                        <h4>DEMPE Analysis Tools</h4>
                        <p>Leverage our built-in tools to allocate returns for Development, Enhancement, Maintenance, Protection, and Exploitation of intangibles.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 7 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-file-invoice"></i></div>
                        <h4>Local & Master File</h4>
                        <p>Export robust data and analysis ready to be integrated seamlessly into your transfer pricing documentation and compliance reports.</p>
                        <a href="#" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>
                <!-- Card 8 -->
                <div class="col-lg-3 col-md-6">
                    <div class="value-card">
                        <div class="value-icon-circle"><i class="fa-solid fa-headset"></i></div>
                        <h4>Expert Analyst Support</h4>
                        <p>Connect directly with our transfer pricing specialists to help navigate complex transactions and defend your positions.</p>
                        <a href="contact.html" class="value-link">Learn More <i class="fa-solid fa-arrow-right"></i></a>
                    </div>
                </div>"""

# Remove exact string if it matches
html_clean = html.replace(html_to_remove, '')

if html_clean == html:
    print("Exact match failed, trying regex")
    # Let's find <!-- Card 5 --> to <!-- Card 8 --> div close
    pattern = r'<!-- Card 5 -->.*?<!-- Card 8 -->.*?</div>\s*</div>'
    html_clean = re.sub(pattern, '', html, flags=re.DOTALL)
    
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_clean)

print("Done removing boxes")
