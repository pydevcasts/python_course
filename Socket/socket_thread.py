import socket
import _thread
import sys


def echo_Server(csocket, addr):
    while True:
        client_data = csocket.recv(2048)
        if client_data:
            csocket.send(client_data)
        else:
            csocket.close()
            return
echoServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
echoServer.bind((('0.0.0.0'), int(sys.argv[1])))
echoServer.listen(3)
while 1:
    cSock, addr = echoServer.accept()
    _thread.start_new_thread(echo_Server, (cSock, addr))