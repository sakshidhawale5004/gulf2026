import re

with open('book-search.html', 'r', encoding='utf-8') as f:
    content = f.read()

cancel_script = '''
<!-- Payment Cancel Notification -->
<div class="modal fade" id="paymentCancelModal" tabindex="-1" aria-hidden="true">
  <div class="modal-dialog modal-dialog-centered">
    <div class="modal-content">
      <div class="modal-header bg-danger text-white">
        <h5 class="modal-title"><i class="fa-solid fa-times-circle me-2"></i> Payment Cancelled</h5>
        <button type="button" class="btn-close btn-close-white" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body text-center p-4">
        <p class="mb-0 fs-5">Your payment was cancelled and no charges were made.</p>
        <p class="text-muted mt-2">You can try submitting the form again when you're ready.</p>
      </div>
      <div class="modal-footer justify-content-center">
        <button type="button" class="btn btn-secondary px-4" data-bs-dismiss="modal">Close</button>
      </div>
    </div>
  </div>
</div>

<script>
document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.get('payment') === 'cancel') {
        const cancelModal = new bootstrap.Modal(document.getElementById('paymentCancelModal'));
        cancelModal.show();
        window.history.replaceState({}, document.title, window.location.pathname);
    }
});
</script>
</body>
'''

if 'paymentCancelModal' not in content:
    content = content.replace('</body>', cancel_script)

with open('book-search.html', 'w', encoding='utf-8') as f:
    f.write(content)
