# This Python file uses the following encoding: utf-8

import socketserver, os, pathlib, sys
from os.path import exists

HOST = ''
PORT = 9009
 
 
path_server = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data_transferred = 0
        print('[%s] 연결됨' %self.client_address[0])
        data = self.request.recv(1024) # 클라이언트로 부터 파일이름을 전달받음

        filename = str(data).split('"')[3]

        filename = "tx_" + filename + ".json"

        if filename is not None:
            with open(path_server + filename, 'wb') as f:
                try:
                    f.write(data)
                except Exception as e:
                    print(e)



 
def runServer(Host = HOST, Port  = PORT):
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")
    print(type(Host), type(Port))
    try:
        server = socketserver.TCPServer((Host,Port),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')
 
if __name__ == '__main__':
    HOST = input('HOST : ')
    PORT = int(input('PORT : '))
    runServer(Host = HOST, Port  = PORT)
