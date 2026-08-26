import socket

COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    80: "HTTP",
    443: "HTTPS",
    3306: "MySQL",
    8000: "HTTP-ALT"  # Tambahkan port 8000 untuk pengujian lokal
}

def scan_ports(target_host: str) -> list:
    open_ports = []
    
    for port, service in COMMON_PORTS.items():
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1.0)  # Timeout koneksi
        result = sock.connect_ex((target_host, port))
        
        if result == 0:
            banner = "No banner"
            try:
                sock.settimeout(1.0)  # Timeout khusus saat membaca data
                sock.send(b"HEAD / HTTP/1.0\r\n\r\n")
                banner = sock.recv(512).decode('utf-8', errors='ignore').strip().split('\n')[0]
            except Exception:
                pass
                
            open_ports.append({
                "port": port,
                "service": service,
                "banner": banner if banner else "No banner retrieved"
            })
        sock.close()
        
    return open_ports