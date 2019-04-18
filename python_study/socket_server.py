#-*- coding: utf-8 -*-
import socket
import datetime

HOST='0.0.0.0'
PORT=3456
#AF_INET说明使用IPV4地址，SOCK_STREAM指TCP
s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen(1)

while True:
    conn,addr=s.accept()
    print('Client %s connected!' % str(addr))
    dt = datetime.datetime.now()
    str = "current time is " + str(dt)
    str =str.encode()
    conn.send(str)
    print( "sent:", str)
    conn.close()