# Automated Vulnerability Scanner & Report Generator

A lightweight Python-based security auditing tool designed to inspect target domains/IPs for missing HTTP security headers and open network ports, automatically generating structured HTML security reports.

## Features
- **HTTP Security Headers Inspection:** Identifies missing security headers such as HSTS, CSP, X-Frame-Options, and more.
- **Port Scanning & Banner Grabbing:** Scans common ports using raw socket connections to retrieve service banners.
- **Automated HTML Reporting:** Uses Jinja2 templating to construct clean, actionable audit reports.

## Prerequisites
- Python 3.x
- Dependencies listed in `requirements.txt`

## Installation
```bash
git clone [https://github.com/](https://github.com/)<username>/vuln-scanner.git
cd vuln-scanner
pip install -r requirements.txt