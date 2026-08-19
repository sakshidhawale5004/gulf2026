import os
import glob
import re

html_files = glob.glob('*.html')

js_snippet = '''
<!-- Newsletter Script -->
<script>
document.addEventListener("DOMContentLoaded", function() {
    const newsletterForms = document.querySelectorAll('.newsletter-form');
    newsletterForms.forEach(form => {
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            
            const submitBtn = form.querySelector('button[type="submit"]');
            const emailInput = form.querySelector('input[type="email"]');
            const originalBtnHTML = submitBtn.innerHTML;
            
            // Create or get message container
            let msgContainer = form.nextElementSibling;
            if (!msgContainer || !msgContainer.classList.contains('newsletter-msg')) {
                msgContainer = document.createElement('div');
                msgContainer.classList.add('newsletter-msg', 'mt-2', 'small');
                form.parentNode.insertBefore(msgContainer, form.nextSibling);
            }
            
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i>';
            msgContainer.style.display = 'none';
            
            const data = {
                form_type: 'Newsletter',
                email: emailInput.value
            };
            
            fetch('submit-form-simple.php', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            })
            .then(response => response.json())
            .then(result => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHTML;
                
                msgContainer.style.display = 'block';
                if (result.success) {
                    msgContainer.innerHTML = '<span class="text-success"><i class="fa-solid fa-check-circle me-1"></i> Subscribed successfully!</span>';
                    form.reset();
                    setTimeout(() => { msgContainer.style.display = 'none'; }, 5000);
                } else {
                    msgContainer.innerHTML = '<span class="text-danger"><i class="fa-solid fa-exclamation-circle me-1"></i> ' + (result.error || "Subscription failed.") + '</span>';
                }
            })
            .catch(error => {
                submitBtn.disabled = false;
                submitBtn.innerHTML = originalBtnHTML;
                msgContainer.style.display = 'block';
                msgContainer.innerHTML = '<span class="text-danger"><i class="fa-solid fa-exclamation-circle me-1"></i> An error occurred.</span>';
                console.error('Error:', error);
            });
        });
    });
});
</script>
</body>
'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if 'subscribeNewsletter()' in content or 'newsletter-form' in content:
        # Replace form tag
        content = re.sub(r'<form\s+ng-submit="subscribeNewsletter\(\)"\s*>', '<form class="newsletter-form">', content)
        content = re.sub(r'<form\s+ng-submit="subscribeNewsletter\(\)"\s+class="([^"]+)">', r'<form class="newsletter-form \1">', content)
        
        # Replace ng-model
        content = content.replace('ng-model="userEmail"', 'name="email"')
        
        # Add JS snippet if not present
        if 'Newsletter Script' not in content:
            content = content.replace('</body>', js_snippet)
            
        # Clean up old angular definitions from index.html if present
        if 'subscribeNewsletter = function()' in content:
            content = re.sub(r'\\.subscribeNewsletter\s*=\s*function\(\)\s*\{[\s\S]*?\}\s*;\s*\}\s*;\s*', '', content)
            
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
