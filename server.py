#!/usr/bin/env python3
from http.server import HTTPServer, BaseHTTPRequestHandler;

class requestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('content-type', 'text/html')
        self.end_headers()
        # self.wfile.write('hello hunter'.encode())
        self.wfile.write(self.path[1:].encode())

def main():
    PORT = 3000
    server_address = ("",PORT)
    server = HTTPServer(server_address,requestHandler)
    # print(f"server running on port {PORT}")
    print("server running on port %s" % PORT)
    server.serve_forever()


if __name__ == "__main__":
    main()