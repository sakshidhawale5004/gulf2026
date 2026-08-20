import re

for filename in ['interest-rates-database.html', 'services-database.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Strip Times New Roman
    html = re.sub(r"font-family:\s*'Times New Roman',\s*Times,\s*serif;?", "", html)

    # 2. Add hero banner if missing
    if '<section data-aos="fade-up" class="page-hero">' not in html:
        title = "Interest Rates Database" if "interest" in filename else "Services Database"
        bg_image = "Interest Ratesdatabasebanner.jpg" if "interest" in filename else "Services Database.jpg"
        
        hero_section = f"""    <section data-aos="fade-up" class="page-hero" style="background: linear-gradient(rgba(10, 107, 79, 0.85), rgba(10, 107, 79, 0.85)), url('{bg_image}') center/cover no-repeat; padding: 100px 0;">
        <div class="container">
            <div class="hero-3d-wireframe"><div class="shape"></div><div class="shape"></div><div class="shape"></div></div>
            <h1 class="text-white" style="font-weight: 500 !important; font-size: 3rem;">{title}</h1>
            <div class="breadcrumb-text text-white" style="font-weight: 500;">
                <a href="index.html" class="text-white" style="text-decoration: none;">Home</a> / {title}
            </div>
        </div>
    </section>

"""
        # Insert right after </header>
        html = html.replace('</header>\n', '</header>\n' + hero_section)
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)

print("Updated interest-rates and services pages")
