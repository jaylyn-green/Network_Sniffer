from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        print(f"Packet: {packet['IP'].src} -> {packet['IP'].dst}, Protocol: {packet['IP'].proto}")

# Capture packets on the specified network interface
print("Starting packet capture...")
sniff(filter="ip", prn=packet_callback, count=10)  #could change to check for certain protocols


