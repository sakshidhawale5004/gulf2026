import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Revert specific claims
content = content.replace('[TBD] Data Accuracy', '100% Data Accuracy')
content = content.replace('[TBD] GCC Coverage', '100% GCC Coverage')
content = content.replace('Data Accuracy [TBD]', 'Data Accuracy 100%')
content = content.replace('Regional Coverage [TBD]', 'Regional Coverage 100%')

# Revert 100,000+ and 100+ and 100% generally in the hero/stats sections
content = content.replace('[XXX,XXX]+', '100,000+')
content = content.replace('>[TBD]%<', '>100%<')
content = content.replace('>[XXX]+<', '>100+<')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

with open('about.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('[XXX,XXX]', '100,000')

with open('about.html', 'w', encoding='utf-8') as f:
    f.write(content)
