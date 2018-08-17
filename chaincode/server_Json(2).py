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
        filename = self.request.recv(1024) # 클라이언트로 부터 파일이름을 전달받음
        filename = filename.decode('utf-8') # 파일이름 이진 바이트 스트림 데이터를 일반 문자열로 변환
 
        filename = path_server + filename

        if not exists(filename): # 파일이 해당 디렉터리에 존재하지 않으면
            return # handle()함수를 빠져 나온다.
 
        print('파일[%s] 전송 시작...' %filename)
        with open(filename, 'rb') as f:
            try:
                data = f.read(1024) # 파일을 1024바이트 읽음
                while data: # 파일이 빈 문자열일때까지 반복
                    data_transferred += self.request.send(data)
                    data = f.read(1024)
            except Exception as e:
                print(e)
 
        print('전송완료[%s], 전송량[%d]' %(filename,data_transferred))
 
 
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
