import argparse
import os
from urllib.parse import urlparse
from jinja2 import Environment, FileSystemLoader
from modules.headers import check_security_headers
from modules.ports import scan_ports

def generate_report(target: str, header_results: dict, port_results: list, output_file: str):
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template('report.html')
    
    html_content = template.render(
        target=target,
        headers=header_results,
        ports=port_results
    )
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"[+] Report generated successfully: {output_file}")

def extract_hostname(target: str) -> str:
    """Mengambil hostname/IP murni tanpa skema http:// atau port."""
    if not target.startswith(("http://", "https://")):
        target = f"http://{target}"
    parsed = urlparse(target)
    return parsed.hostname or target

def main():
    parser = argparse.ArgumentParser(description="Automated Vulnerability Scanner & Report Generator")
    parser.add_argument("-t", "--target", required=True, help="Target domain or IP (e.g., example.com)")
    parser.add_argument("-o", "--output", default="report.html", help="Output HTML report filename")
    args = parser.parse_args()

    print(f"[*] Starting scan for target: {args.target}")
    
    # 1. Scan HTTP Security Headers
    print("[*] Checking HTTP Security Headers...")
    header_results = check_security_headers(args.target)
    
    # 2. Scan Open Ports (Menggunakan extract_hostname)
    print("[*] Scanning open ports...")
    clean_host = extract_hostname(args.target)
    port_results = scan_ports(clean_host)
    
    # 3. Generate HTML Report
    generate_report(args.target, header_results, port_results, args.output)

if __name__ == "__main__":
    main()