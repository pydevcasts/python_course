import socketserver
import http.server


class ReqHandler(http.server.SimpleHTTPRequestHandler):
    def do_Get(self):
        if self.path == 'Date/':
            self.wfile.write(b"Persmission Dinied!")
            b = bytes(self.headers)
            self.wfile.write(b)
        else:
            http.server.SimpleHTTPRequestHandler.do_GET(self)
add =("", 773)
httpServer = socketserver.TCPServer(add, ReqHandler)
httpServer.serve_forever()