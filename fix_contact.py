import re

with open('contact.html', 'r', encoding='utf-8') as f:
    content = f.read()

js_script = '''<script>
    document.getElementById('contactForm').addEventListener('submit', function(e) {
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
            submitBtn.innerHTML = '<i class="fas fa-paper-plane me-2"></i> Send Request';
            
            if (result.success) {
                successMsg.style.display = 'block';
                form.reset();
                setTimeout(() => {
                    successMsg.style.display = 'none';
                }, 5000);
            } else {
                errorMsg.innerHTML = '<i class="fa-solid fa-exclamation-circle me-2"></i> ' + (result.error || "Failed to send your message.");
                errorMsg.style.display = 'block';
            }
        })
        .catch(error => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = '<i class="fas fa-paper-plane me-2"></i> Send Request';
            errorMsg.innerHTML = '<i class="fa-solid fa-exclamation-circle me-2"></i> An error occurred. Please try again.';
            errorMsg.style.display = 'block';
            console.error('Error:', error);
        });
    });
</script>'''

content = re.sub(r'<script>\s*var app = angular\.module[\s\S]*?</script>', js_script, content)

with open('contact.html', 'w', encoding='utf-8') as f:
    f.write(content)
