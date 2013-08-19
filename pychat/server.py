#!/usr/bin/env python

# tcp chat server
import socket
import select
import argparse

def broadcast_data (sock, msg):
    for socket in CONNECTIONS:
        if socket != server_socket and socket != sock :
            try :
                socket.send(msg)
            except :
                socket.close()
                CONNECTIONS.remove(socket)
 
if __name__ == "__main__":

    CONNECTIONS = []
    BUFLEN = 1024

    parser = argparse.ArgumentParser(description='tcp chat server; supply port')
    parser.add_argument('port', type=int, help='port for chat server')
    args = parser.parse_args()
    port=args.port

     
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind(("0.0.0.0", port))
    server_socket.listen(2)
 
    CONNECTIONS.append(server_socket)
 
    print "Chat server started on port " + str(port)
 
    while True:
        # get readable sockets, throw away rest
        rSocks, _, _ = select.select(CONNECTIONS,[],[])
 
        for sock in rSocks:
            # new connection
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                CONNECTIONS.append(sockfd)
                print "Client (%s, %s) connected" % addr
                 
                broadcast_data(sockfd, "[%s:%s] entered chat\n" % addr)
             
            # message from client
            else:
                try:
                    data = sock.recv(BUFLEN)
                    if data:
                        broadcast_data(sock, "\r" + '<' + str(sock.getpeername()) + '> ' + data)                
                
                # client is offline
                except:
                    broadcast_data(sock, "Client (%s, %s) is offline\n" % addr)
                    print "Client (%s, %s) is offline" % addr
                    sock.close()
                    CONNECTIONS.remove(sock)
                    continue
     
    server_socket.close()