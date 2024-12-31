from flask import Flask, jsonify
from monitor.devices import scan_network

app = Flask(__name__)

@app.route('/api/devices', methods=['GET'])

def get_devices():
    target_range = "192.168.1.0/24"  # Define network range 
    devices = scan_network(target_range)  #external function
    return jsonify(devices)  

if __name__ == '__main__':
    app.run(debug=True)
