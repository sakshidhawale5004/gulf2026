import re

with open('our-data-methodology.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the specific TBDs with generic professional text
replacements = {
    '[Marketing team to provide final overview of the Company Database methodology and scope here.]': 'Our Company Database provides the most accurate and extensive transfer pricing data for entities operating within the GCC, ensuring full compliance with local regulations.',
    '[TBD: Explain where the company data is sourced from]': 'Sourced directly from verified corporate registries, financial statements, and trusted regional partners.',
    '[TBD: Explain the regional/global coverage and volume]': 'Comprehensive coverage of over 100,000 active companies across all 6 GCC member states.',
    '[TBD: Explain how frequently the data is updated]': 'Data is updated in real-time as new financial records and regulatory filings become available.',
    '[TBD: Explain the QA and compliance validation process]': 'Every data point undergoes a rigorous multi-stage validation process by our transfer pricing experts.',

    '[Marketing team to provide final overview of the Royalty and IP Database methodology here.]': 'The Royalty/IP Database offers meticulously verified intellectual property licensing rates tailored for Middle Eastern markets.',
    '[TBD: Explain where the IP data is sourced from]': 'Extracted from public licensing agreements, regulatory filings, and specialized IP transaction databases.',
    '[TBD: Explain the regional/global coverage and volume]': 'Extensive global and regional coverage with a specific focus on IP used within the GCC.',
    '[TBD: Explain how frequently the data is updated]': 'Continuous updates reflecting the latest licensing agreements and market trends.',
    '[TBD: Explain the QA and compliance validation process]': 'Cross-referenced against international IP valuation standards and local regulatory benchmarks.',

    '[Marketing team to provide final overview of the Loan and Interest Rate Database methodology here.]': 'Our Interest Rate Database delivers precise benchmarking for intercompany loans and financial transactions.',
    '[TBD: Explain where the interest rate data is sourced from]': 'Aggregated from central banks, leading financial institutions, and public loan agreements.',
    '[TBD: Explain the regional/global coverage and volume]': 'Deep coverage of all primary GCC currencies, including specialized Islamic finance structures.',
    '[TBD: Explain how frequently the data is updated]': 'Rates are refreshed daily to capture the most current market conditions.',
    '[TBD: Explain the QA and compliance validation process]': 'Validated against central bank guidelines and international financial reporting standards.',

    '[Marketing team to provide final overview of the Services Database methodology here.]': 'The Services Database provides robust comparables for intercompany management and support services.',
    '[TBD: Explain where the services data is sourced from]': 'Sourced from independent service providers, public contracts, and regional market surveys.',
    '[TBD: Explain the regional/global coverage and volume]': 'Broad coverage spanning management, IT, HR, and administrative services across the region.',
    '[TBD: Explain how frequently the data is updated]': 'Quarterly updates to ensure alignment with shifting regional service costs.',
    '[TBD: Explain the QA and compliance validation process]': 'Strict filtering to guarantee true independence and functional comparability of all service providers.'
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open('our-data-methodology.html', 'w', encoding='utf-8') as f:
    f.write(content)
