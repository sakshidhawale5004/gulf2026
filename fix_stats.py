import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace specific claims
content = content.replace('100% Data Accuracy', '[TBD] Data Accuracy')
content = content.replace('100% GCC Coverage', '[TBD] GCC Coverage')
content = content.replace('Data Accuracy 100%', 'Data Accuracy [TBD]')
content = content.replace('Regional Coverage 100%', 'Regional Coverage [TBD]')

# Replace 100,000+ and 100+ and 100% generally in the hero/stats sections
content = content.replace('100,000+', '[XXX,XXX]+')
content = content.replace('>100%<', '>[TBD]%<')
content = content.replace('>100+<', '>[XXX]+<')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
