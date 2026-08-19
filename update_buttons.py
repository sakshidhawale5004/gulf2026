import glob

html_files = glob.glob("*.html")
for f_name in html_files:
    with open(f_name, 'r', encoding='utf-8') as f:
        html = f.read()

    # Update BOOK SEARCH in navbar
    html = html.replace('class="btn-conxora text-center">BOOK SEARCH</a>', 'class="btn-outline-green btn px-3 py-2 text-center" style="font-size: 14px;">BOOK SEARCH</a>')
    html = html.replace('class="btn-conxora">BOOK SEARCH</a>', 'class="btn-outline-green btn px-3 py-2" style="font-size: 14px;">BOOK SEARCH</a>')
    
    # Update BOOK DEMO in navbar
    html = html.replace('class="btn-conxora text-center">BOOK DEMO</a>', 'class="btn-orange btn px-3 py-2 text-center" style="font-size: 14px; color: white;">BOOK DEMO</a>')
    html = html.replace('class="btn-conxora">BOOK DEMO</a>', 'class="btn-orange btn px-3 py-2" style="font-size: 14px; color: white;">BOOK DEMO</a>')
    
    # Update primary button in hero if it needs a specific class just in case
    # btn-conxora btn-orange -> btn-orange
    html = html.replace('btn-conxora btn-orange', 'btn-orange btn')
    
    with open(f_name, 'w', encoding='utf-8') as f:
        f.write(html)
