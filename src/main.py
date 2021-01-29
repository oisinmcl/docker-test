import http.server
import socketserver
from http import HTTPStatus

print ("App Started")
count = 0

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        global count
        self.send_response(HTTPStatus.OK)
        self.end_headers()
        count = count + 1
        self.wfile.write(bytes('Hello world: ' + str(count), "utf-8"))

httpd = socketserver.TCPServer(('', 43120), Handler)
httpd.serve_forever()