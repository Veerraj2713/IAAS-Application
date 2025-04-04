from flask import Flask, jsonify
import socket
import os
import platform

app = Flask(__name__)

@app.route('/')
def server_info():
    return jsonify({
        'hostname': socket.gethostname(),
        'ip_address': socket.gethostbyname(socket.gethostname()),
        'os': platform.system(),
        'os_version': platform.release(),
        'cpu_count': os.cpu_count(),
        'memory': os.sysconf('SC_PAGE_SIZE') * os.sysconf('SC_PHYS_PAGES')  # Total memory in bytes
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)