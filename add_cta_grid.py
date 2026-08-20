import re

section_to_add = """    <section class="action-grid-section py-5" style="background-color: #f8f9fa;">
        <div class="container">
            <div class="row justify-content-center">
                <div class="col-lg-10">
                    <div class="row g-4">
                        <div data-aos="fade-up" class="col-md-6">
                            <a href="book-search.html" class="action-box-minimal">
                                <h5>Get a Search</h5>
                                <p>Make a request for a Gulf-Specific Custom Search.</p>
                            </a>
                        </div>
                        <div data-aos="fade-up" class="col-md-6">
                            <a href="update-a-search.html" class="action-box-minimal">
                                <h5>Update a Search</h5>
                                <p>Update your broad Regional (Europe / Asia) search with Gulf Specific Comparables.</p>
                            </a>
                        </div>
                        <div data-aos="fade-up" class="col-md-6">
                            <a href="book-an-appointment.html" class="action-box-minimal">
                                <h5>Book an Appointment</h5>
                                <p>It's time to get your Gulf Transfer Pricing right. Let's Talk.</p>
                            </a>
                        </div>
                        <div data-aos="fade-up" class="col-md-6">
                            <a href="buy-subscription.html" class="action-box-minimal">
                                <h5>Buy Subscription</h5>
                                <p>Access our comprehensive database with multiple searches and expert support for your transfer pricing needs.</p>
                            </a>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

"""

for filename in ['interest-rates-database.html', 'services-database.html']:
    with open(filename, 'r', encoding='utf-8') as f:
        html = f.read()

    # Check if it already exists
    if 'class="action-grid-section"' not in html:
        # Insert before footer
        html = html.replace('<footer class="footer position-relative">', section_to_add + '    <footer class="footer position-relative">')
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Added section to {filename}")
    else:
        print(f"Section already exists in {filename}")
