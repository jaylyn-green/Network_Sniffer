from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  
    packet = ether / arp

    result = srp(packet, timeout=1, verbose=False)[0]

    devices = []
    for _, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return devices
