#!/usr/bin/env python

import socket
import select
import string
import sys
import argparse

def prompt():
    sys.stdout.write('<You> ')
    sys.stdout.flush()

if __name__=="__main__":
    
    parser = argparse.ArgumentParser(description='tcp chat client; supply host and port')
    parser.add_argument('host', help='chat server hostname')
    parser.add_argument('port', type=int, help='port at which to connect to server')

    args = parser.parse_args()

    host=args.host
    port=args.port

    BUFLEN=1024
    
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)
     
    # connect to remote host
    try:
        sock.connect((host, port))
    except:
        print 'Unable to connect'
        sys.exit()
     
    print 'Welcome to chat room'
    prompt()
     
    while True:
        socket_list = [sys.stdin, sock]
         
        # Get readable sockets, throw away extras
        rSocks, _, _ = select.select(socket_list , [], [])
         
        for s in rSocks:
            #incoming message from server
            if s == sock:
                data = sock.recv(BUFLEN)
                if not data:
                    print '\nDisconnected from chat room'
                    exit()
                else:
                    sys.stdout.write(data)
                    prompt()
             
            #user entered a message
            else:
                msg = sys.stdin.readline()
                sock.send(msg)
                prompt()