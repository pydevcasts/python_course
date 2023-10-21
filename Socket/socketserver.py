import socketserver

class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print("New Client Connected", self.client_address)
        data = "predefined value"
        while len(data):
            data = self.request.recv(2048)
            print("New message has been recieved from:", self.client_address)
            print(data)
            self.request.send(b""" We reveived your message: "%s" """ %data)

addrs = ("192.168.43.239", 773)
server = socketserver.TCPServer(addrs, ClientHandler)
server.serve_forever()
