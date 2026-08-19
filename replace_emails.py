import os
import glob

files = glob.glob('*.html') + glob.glob('*.md')
for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    changed = False
    
    # In header/top-bar
    if '<li><i class="fa-solid fa-envelope"></i> connect@gulftp.com</li>' in content:
        content = content.replace('<li><i class="fa-solid fa-envelope"></i> connect@gulftp.com</li>', 
                                  '<li><i class="fa-solid fa-envelope"></i> connect@gulftp.com (admin@gulftp.com as parent)</li>')
        changed = True

    # In footer
    if '<a href="mailto:connect@gulftp.com">connect@gulftp.com</a>' in content:
        content = content.replace('<a href="mailto:connect@gulftp.com">connect@gulftp.com</a>', 
                                  '<a href="mailto:connect@gulftp.com">connect@gulftp.com (admin@gulftp.com as parent)</a>')
        changed = True
        
    # In contact page or other places
    if 'class="mb-0 text-white" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com</p>' in content:
        content = content.replace('class="mb-0 text-white" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com</p>',
                                  'class="mb-0 text-white" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com (admin@gulftp.com as parent)</p>')
        changed = True
        
    if 'class="mb-0 text-white-50" style="font-family: \'Inter\', sans-serif;">Email us at: <strong class="text-white">connect@gulftp.com</strong></p>' in content:
        content = content.replace('class="mb-0 text-white-50" style="font-family: \'Inter\', sans-serif;">Email us at: <strong class="text-white">connect@gulftp.com</strong></p>',
                                  'class="mb-0 text-white-50" style="font-family: \'Inter\', sans-serif;">Email us at: <strong class="text-white">connect@gulftp.com (admin@gulftp.com as parent)</strong></p>')
        changed = True

    if '<p class="mb-0 text-muted">Email us at: <strong>connect@gulftp.com</strong></p>' in content:
        content = content.replace('<p class="mb-0 text-muted">Email us at: <strong>connect@gulftp.com</strong></p>',
                                  '<p class="mb-0 text-muted">Email us at: <strong>connect@gulftp.com (admin@gulftp.com as parent)</strong></p>')
        changed = True

    if 'class="mb-0 text-white-50 small ms-4" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com</p>' in content:
        content = content.replace('class="mb-0 text-white-50 small ms-4" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com</p>',
                                  'class="mb-0 text-white-50 small ms-4" style="font-family: \'Inter\', sans-serif;">connect@gulftp.com (admin@gulftp.com as parent)</p>')
        changed = True

    if changed:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
