import nmap

def scan_ports(ip):
    nm = nmap.PortScanner()
    nm.scan(ip, '1-1024')  # Scan ports (1-1024)
    return nm[ip]


