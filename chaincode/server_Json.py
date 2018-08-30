# This Python file uses the following encoding: utf-8
import socketserver, os, pathlib, sys, socket
from os.path import exists
from uuid import getnode

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.block import block
from ledger.transaction import transaction

from chaincode.transactionToJson import *
from chaincode.server_Json import *
from chaincode.blockToJson import blockToJson
from chaincode.randFileName import *
from chaincode.leader_rand import *
from chaincode.chainToJson import *



HOST = ''
PORT = 9009

path_server = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"
file_list= os.listdir(path_server)

class MyTcpHandler(socketserver.BaseRequestHandler):
    def handle(self):
        print('[%s] 연결됨' %self.client_address[0])
        data = self.request.recv(1024) 
        okdata = data.decode()
        data = data.decode()
        

        if "ok?" in okdata:
            self.request.send("ok!".encode())
            return 


        print(okdata, type(okdata))
        print(data, type(data))
        
        tmp = str(data).split('B23C000F')
        chainName = tmp[0]
        data = tmp [1]
        
        print()
        print()
        print()
        print()

        print(chainName, type(chainName))
        print(data, type(data))
        data = data.encode()
        print()
        print()
        print()
        print()


        #filename = randFileName()
        #with open(path_server +filename, 'wb') as f:
        #    try:
        #        f.write(data)
        #    except Exception as e:
        #        print(e)
        #
        #de = dc()
        #de.sk_dc(filename)


        if  str(data).split('"')[1] == "TXID":
            filename = str(data).split('"')[3]
            filename = "tx_" + filename + ".json"
            if exists(path_server + filename):
                with open(path_server + leader_rand() +filename, 'wb') as f:
                    try:
                        f.write(data)
                    except Exception as e:
                        print(e)
            else:
                with open(path_server + filename, 'wb') as f:
                    try:
                        f.write(data)                       
                    except Exception as e:
                        print(e)
        else:
            filename = str(data).split('"')[3]
            filename = "block_" + filename + ".json"

            
            print()
            print()
            print()
            print()
            print()

            if filename is not None:
                with open(path_server + filename, 'wb') as f:
                    try:
                        f.write(data)
                    except Exception as e:
                        print(e)
            btj = blockToJson(filename = filename)
            btj.data = btj.loadJson()
            Block = block()
            Block.fromDict(Dict = btj.data)
            filename = str(chainName)
            if not exists(path + filename):
                Chain = chain(CHID = randFileName(), block = Block)
                Chain.append(Block)
                ctj = chainToJson(filename = filename, data = Chain)
                ctj.saveJson()
            else:
                ctj = chainToJson(filename = filename)
                ctj.data = ctj.loadJson()
                Chain = chain()
                Chain.fromDict(Dict = ctj.data)
                Chain.append(Block)
                ctj = chainToJson(filename = filename, data = Chain)
                ctj.saveJson()
            print(Chain.toDict())
            

 
def runServer(Host = HOST, Port  = PORT):
    print('++++++파일 서버를 시작++++++')
    print("+++파일 서버를 끝내려면 'Ctrl + C'를 누르세요.")
    print(type(Host), type(Port))
    print(Host, Port)
    try:
        server = socketserver.TCPServer((Host,Port),MyTcpHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print('++++++파일 서버를 종료합니다.++++++')
 
if __name__ == '__main__':
    HOST = input('HOST : ')
    PORT = int(input('PORT : '))
    runServer(Host = HOST, Port  = PORT)
