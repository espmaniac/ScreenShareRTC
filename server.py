import http.server
import json
import socket

offer = None
answer = None

def get_local_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        ip = s.getsockname()[0]
    except Exception:
        ip = '127.0.0.1'
    finally:
        s.close()
    return ip

class SimpleHandler(http.server.BaseHTTPRequestHandler):
    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()

    def do_POST(self):
        global offer, answer
        content_length = int(self.headers.get('Content-Length', 0))
        body = self.rfile.read(content_length)
        if self.path == '/offer':
            offer = json.loads(body)
            answer = None
            self.send_json({'success': True})
        elif self.path == '/answer':
            answer = json.loads(body)
            self.send_json({'success': True})
        else:
            self.send_error(404)

    def do_GET(self):
        global offer, answer
        if self.path == '/get_offer':
            data = offer if offer is not None else {}
            self.send_json(data)
        elif self.path == '/get_answer':
            data = answer if answer is not None else {}
            self.send_json(data)
        elif self.path == '/myip':
            ip = get_local_ip()
            self.send_response(200)
            self.send_header('Content-Type', 'text/plain')
            self.send_header('Access-Control-Allow-Origin', '*')
            self.end_headers()
            self.wfile.write(ip.encode("utf-8"))
        else:
            self.send_error(404)

    def send_json(self, obj):
        data = json.dumps(obj).encode('utf-8')
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Content-Length', str(len(data)))
        self.end_headers()
        self.wfile.write(data)

if __name__ == '__main__':
    ip = get_local_ip()
    print(f"Signaling server running at http://{ip}:5000")
    server = http.server.HTTPServer(('0.0.0.0', 5000), SimpleHandler)
    server.serve_forever()