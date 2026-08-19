import re

with open('buy-subscription.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove ng-app
content = content.replace('ng-app="gulfApp"', '')

# Remove angular script
content = re.sub(r'<script src="https://ajax.googleapis.com/ajax/libs/angularjs[^>]+></script>\n?', '', content)

# Update form tag
content = content.replace('<form name="subForm" ng-submit="submitForm()" novalidate>',
                          '<form id="subForm">')

# Convert ng-model to name
content = re.sub(r'ng-model="formData\.([^"]+)"', r'name="\1"', content)

# Remove ng-disabled
content = re.sub(r'ng-disabled="subForm\.\"', 'id="submitBtn"', content)

# Update success and error messages
content = re.sub(r'<div class="alert alert-success mt-3 py-2 text-center mb-0" ng-show="formSuccess" style="font-size: 0.9rem; font-weight: 600;">\s*<i class="fa-solid fa-circle-check me-2"></i> Request received! We\'ll be in touch shortly.\s*</div>',
                 '<div class="alert alert-success mt-3 py-2 text-center mb-0" id="successMessage" style="font-size: 0.9rem; font-weight: 600; display: none;">\n                                <i class="fa-solid fa-circle-check me-2"></i> Request received! We\'ll be in touch shortly.\n                            </div>', content)

content = re.sub(r'<div class="alert alert-danger mt-3 py-2 text-center mb-0" ng-show="formError" style="font-size: 0.9rem; font-weight: 600;">\s*<i class="fa-solid fa-exclamation-circle me-2"></i> Failed to send request\. Please try again\.\s*</div>',
                 '<div class="alert alert-danger mt-3 py-2 text-center mb-0" id="errorMessage" style="font-size: 0.9rem; font-weight: 600; display: none;">\n                                <i class="fa-solid fa-exclamation-circle me-2"></i> Failed to send request. Please try again.\n                            </div>', content)

# Replace angular script with vanilla js
js_script = '''<script>
    document.getElementById('subForm').addEventListener('submit', function(e) {
        e.preventDefault();
        
        const form = this;
        const submitBtn = document.getElementById('submitBtn');
        const successMsg = document.getElementById('successMessage');
        const errorMsg = document.getElementById('errorMessage');
        
        const formData = new FormData(form);
        const data = Object.fromEntries(formData);
        
        submitBtn.disabled = true;
        submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i> Sending...';
        successMsg.style.display = 'none';
        errorMsg.style.display = 'none';
        
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
            submitBtn.innerHTML = 'Get a Quote <i class="fa-solid fa-paper-plane ms-2"></i>';
            
            if (result.success) {
                successMsg.style.display = 'block';
                form.reset();
                setTimeout(() => {
                    successMsg.style.display = 'none';
                }, 5000);
            } else {
                errorMsg.innerHTML = '<i class="fa-solid fa-exclamation-circle me-2"></i> ' + (result.error || "Failed to send request.");
                errorMsg.style.display = 'block';
            }
        })
        .catch(error => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = 'Get a Quote <i class="fa-solid fa-paper-plane ms-2"></i>';
            errorMsg.innerHTML = '<i class="fa-solid fa-exclamation-circle me-2"></i> An error occurred. Please try again.';
            errorMsg.style.display = 'block';
            console.error('Error:', error);
        });
    });
</script>'''

content = re.sub(r'<script>\s*var app = angular\.module[\s\S]*?</script>', js_script, content)

with open('buy-subscription.html', 'w', encoding='utf-8') as f:
    f.write(content)
