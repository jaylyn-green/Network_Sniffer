from flask import Flask, jsonify, request
from monitor.devices import scan_network
from monitor.port_scan import scan_ports
from monitor.sniffer import packet_callback

app = Flask(__name__)

@app.route('/api/devices', methods=['GET'])
def get_devices():
    target_range = "192.168.1.0/24"  # Define network range 
    devices = scan_network(target_range)  #external function
    return jsonify(devices)  

@app.route('/api/device-info', methods = ["GET"])
def device_info():
    device = request.args.get("ip")
    if not device:
        return jsonify({"error": "IP address is required!"}), 400
    
    info = scan_ports(device)   #external function
    return jsonify(info)

def sniffer():
    packet_callback('192.168.1.105')      #change to dynamically set ip
    return

if __name__ == '__main__':
    app.run(debug=True)
