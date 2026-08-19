import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add a script at the end of the body to show an alert if payment=success
payment_script = '''
<!-- Payment Success Notification -->
<div class="modal fade" id="paymentSuccessModal" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header bg-success text-white">
        <h5 class="modal-title"><i class="fa-solid fa-check-circle me-2"></i> Payment Successful!</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-center p-4">
        <p class="mb-0 fs-5">Thank you! Your payment was received successfully.</p>
        <p class="text-muted mt-2">We will be in touch with your requested search shortly.</p>
      </div>
      <div class="modal-footer justify-content-center">
        <button type="button" class="btn btn-success px-4" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('payment') === 'success') {
        const paymentModal = new bootstrap.Modal(document.getElementById('paymentSuccessModal'));
        paymentModal.show();
        // Clean URL
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});
</script>
</body>
'''

if 'paymentSuccessModal' not in content:
    content = content.replace('</body>', payment_script)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
