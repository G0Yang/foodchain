# This Python file uses the following encoding: utf-8

from socket import *
import select
import sys
HOST = '202.31.146.50'
PORT = 10000
BUFSIZE = 1024
ADDR = (HOST,PORT)

Socket = socket(AF_INET, SOCK_STREAM)

try:
    Socket.connect(ADDR)
    type = 'p a6'
    #line = (type.encode(),id.encode())
    #print(line)
    Socket.send(type.encode())
    data = socket.recv[1024]
    msg=data.decode()
    print(msg)
    print(msg.split('/'))

except Exception as e :
    print('%s:%s'%ADDR)
    sys.exit()

print('connect is success')
