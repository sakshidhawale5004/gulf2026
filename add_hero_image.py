import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('<section class="hero-section position-relative overflow-hidden">')
end_idx = html.find('<!-- Stat Bar beneath fold -->')

hero_html = html[start_idx:end_idx]

# Un-center text
hero_html = hero_html.replace('<div class="col-lg-10 mx-auto text-center">', '<div class="col-lg-6">')
hero_html = hero_html.replace('style="max-width: 700px; margin: 0 auto; line-height: 1.7;  font-weight: 200 !important;"', 'style="max-width: 540px; line-height: 1.7; font-weight: 200 !important;"')
hero_html = hero_html.replace('class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3 justify-content-center"', 'class="hero-buttons motion-fade-up motion-delay-3 d-flex flex-wrap gap-3"')

# Now add the right column after the left column closing div.
# We will use regex to find where the <div class="col-lg-6"> ends.
# It ends right before </div>\n            </div>\n        </div>
new_right_col = """
                <div class="col-lg-6 d-none d-lg-block position-relative">
                    <div class="motion-fade-up motion-delay-2" style="z-index: 2; position: relative;">
                        <div class="continuous-float">
                            <div class="position-relative hero-3d-wrapper" data-tilt data-tilt-max="12" data-tilt-speed="400" data-tilt-perspective="1000" data-tilt-glare="true" data-tilt-max-glare="0.5">
                                <img src="gulftp-hero section.jpg" alt="GulfTP Platform" class="img-fluid rounded-4 shadow-lg hero-3d-element" style="border: 1px solid rgba(255,255,255,0.15); border-radius: 20px;">
                            </div>
                        </div>
                    </div>
                </div>
"""

# We just inject it before the last </div>\n            </div>\n        </div> of the hero content.
# Wait, let's locate the row: <div class="row align-items-center g-5">
# In hero_html:
# <div class="col-lg-6">
# ...
# </div>
# [WE NEED TO INJECT HERE]
# </div> <!-- row -->

# Use a safer replacement logic.
parts = hero_html.split('<div class="row align-items-center g-5">')
if len(parts) > 1:
    before_row = parts[0]
    row_content = parts[1]
    
    # We find the closing div of the left column. Since there is only one column right now (the left one), 
    # and it ends where the row ends. The row content ends with </div>\n        </div>\n    </section>
    
    # Actually, let's just do a rfind for the </div> that closes the col-lg-6.
    row_close_idx = row_content.rfind('</div>', 0, row_content.rfind('</div>', 0, row_content.rfind('</div>'))) 
    # It's better to just regex match the whole left column.
    pass

# Simpler way: we know what's at the end of the left column:
# </a>\n                    </div>\n                </div>
# We can replace this specific string to inject the right column.

inject_point = '</a>\n                    </div>\n                </div>'
if inject_point in hero_html:
    hero_html = hero_html.replace(inject_point, inject_point + '\n' + new_right_col)

html = html[:start_idx] + hero_html + html[end_idx:]

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

