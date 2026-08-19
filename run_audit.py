import glob
from bs4 import BeautifulSoup
import json

html_files = glob.glob('*.html')
audit = []

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
        
    title_tag = soup.find('title')
    title = title_tag.text.strip() if title_tag else None
    
    meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
    meta_desc = meta_desc_tag['content'].strip() if meta_desc_tag and meta_desc_tag.has_attr('content') else None
    
    audit.append({
        'file': file,
        'title': title,
        'meta_description': meta_desc
    })

with open('seo_audit.json', 'w', encoding='utf-8') as f:
    json.dump(audit, f, indent=4)
