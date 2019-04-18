#-*- coding: utf-8 -*-
import socket
import datetime

HOST='127.0.0.1'
PORT=3456

s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
print("connect %s:%d OK"% (HOST, PORT))
date=s.recv(1024)
print("Received: ", date)
s.close()