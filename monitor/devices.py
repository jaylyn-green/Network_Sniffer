from scapy.all import ARP, Ether, srp

def scan_network(ip_range):
    
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")  
    packet = ether / arp

    result = srp(packet, timeout=1, verbose=False)[0]

    devices = []
    count = 0
    for _, received in result:
        count+=1
        devices.append({'num': count, 'ip': received.psrc, 'mac': received.hwsrc})

    return devices
