import re
with open('book-search.html', 'r', encoding='utf-8') as f:
    content = f.read()

old_options = '''                            <option>Saudi Arabia</option>
                            <option>Qatar</option>
                            <option>Bahrain</option>
                            <option>Oman</option>
                            <option>Egypt</option>
                            <option>Multiple Countries</option>'''

new_options = '''                            <option>Saudi Arabia</option>
                            <option>Kuwait</option>
                            <option>Qatar</option>
                            <option>Bahrain</option>
                            <option>Oman</option>
                            <option disabled>--- Wider Middle East ---</option>
                            <option>Egypt</option>
                            <option>Multiple Countries</option>'''

content = content.replace(old_options, new_options)

with open('book-search.html', 'w', encoding='utf-8') as f:
    f.write(content)
