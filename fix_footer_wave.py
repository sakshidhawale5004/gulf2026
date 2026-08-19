import os

with open('style.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Make the footer wave shorter (60px instead of 120px)
content = content.replace(
'''.footer-wave {
    position: absolute;
    top: -119px;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}
.footer-wave svg {
    display: block;
    width: calc(100% + 4px);
    height: 120px;
    margin-left: -2px;
}''',
'''.footer-wave {
    position: absolute;
    top: -59px;
    left: 0;
    width: 100%;
    overflow: hidden;
    line-height: 0;
}
.footer-wave svg {
    display: block;
    width: calc(100% + 4px);
    height: 60px;
    margin-left: -2px;
}'''
)

# Also reduce margin-top on footer
content = content.replace(
'''.footer {
    background-color: var(--primary-green);
    color: #94a3b8;
    padding: 0 0 30px;
    font-size: 0.95rem;
    margin-top: 100px;
    border-top: none;
}''',
'''.footer {
    background-color: var(--primary-green);
    color: #94a3b8;
    padding: 0 0 30px;
    font-size: 0.95rem;
    margin-top: 60px;
    border-top: none;
}'''
)

with open('style.css', 'w', encoding='utf-8') as f:
    f.write(content)
