import requests

RECOMMENDED_HEADERS = [
    "Strict-Transport-Security",
    "X-Frame-Options",
    "X-Content-Type-Options",
    "Content-Security-Policy",
    "Referrer-Policy"
]

def check_security_headers(target_url: str) -> dict:
    results = {"missing": [], "present": {}}
    try:
        if not target_url.startswith(("http://", "https://")):
            target_url = f"https://{target_url}"
            
        response = requests.get(target_url, timeout=5, allow_redirects=True)
        headers = response.headers

        for header in RECOMMENDED_HEADERS:
            if header in headers:
                results["present"][header] = headers[header]
            else:
                results["missing"].append(header)
    except requests.RequestException as e:
        results["error"] = str(e)
        
    return results