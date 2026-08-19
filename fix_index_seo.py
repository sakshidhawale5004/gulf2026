import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

new_head = '''    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>GulfTP - Premier GCC Transfer Pricing Database</title>
    <meta name="description" content="GulfTP is the premier transfer pricing benchmarking database built entirely for the GCC region. Elevate your financial strategies with high-precision data.">
    
    <!-- Open Graph / Facebook -->
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://www.gulftp.com/">
    <meta property="og:title" content="GulfTP - Premier GCC Transfer Pricing Database">
    <meta property="og:description" content="GulfTP is the premier transfer pricing benchmarking database built entirely for the GCC region. Elevate your financial strategies with high-precision data.">
    <meta property="og:site_name" content="GulfTP">
    
    <!-- Structured Data -->
    <script type="application/ld+json">
    {
      "@context": "https://schema.org",
      "@type": "WebSite",
      "name": "GulfTP",
      "url": "https://www.gulftp.com/"
    }
    </script>'''

content = re.sub(r'<meta charset="UTF-8">\s*<meta name="viewport" content="width=device-width, initial-scale=1\.0">\s*<title>GulfTP - Transfer Pricing Data</title>', new_head, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
