import socketserver
import http.server


addr = ("192.168.43.239", 773)
httpServer = socketserver.TCPServer(addr, http.server.SimpleHTTPRequestHandler)
httpServer.serve_forever()