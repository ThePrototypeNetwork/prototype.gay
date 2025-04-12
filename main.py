import http.server
import socketserver
import subprocess

PORT = 2020

class MyHandler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
                if 'curl' in self.headers.get('User-Agent', ''):
                        result = subprocess.run(['/root/.cargo/bin/viu' ,'-w', '70', '-h', '30', '-t', 'faggot.png'], capture_output=True, text=True)
                        output = result.stdout
                        self.send_response(200)
                        self.send_header('Content-type', 'text/plain')
                        self.end_headers()
                        self.wfile.write(output.encode())
                else:
                        self.send_response(200)
                        self.send_header('Content-type', 'image/png')
                        self.end_headers()
                        with open('faggot.png', 'rb') as f:
                                self.wfile.write(f.read())

with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
