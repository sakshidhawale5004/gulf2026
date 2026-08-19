import codecs

def update_about(content):
    # Change all font-weight: 800 to font-weight: 500 for consistency with the home page
    content = content.replace('font-weight: 800;', 'font-weight: 500;')
    # There is also one instance of font-weight: 600 in the navbar that we should probably leave alone, but let's check
    return content

try:
    with codecs.open('about.html', 'r', encoding='utf-8-sig') as f:
        content = f.read()
    new_content = update_about(content)
    if new_content != content:
        with codecs.open('about.html', 'w', encoding='utf-8-sig') as f:
            f.write(new_content)
        print("Updated about.html headings weight to 500")
    else:
        print("No changes made.")
except Exception as e:
    print(f"Error: {e}")
