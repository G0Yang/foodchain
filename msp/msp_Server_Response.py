# This Python file uses the following encoding: utf-8

import pymongo
from socket import *
import sys

ipAddress = "localhost"
port = 27017

sHOST = ''
sPORT = 10000

class mspResponse:
    def verificationValue(self, type, *args):
            
        conn = pymongo.MongoClient(ipAddress,port)      #"mongodb://user1:blockchain@"
        db = conn.get_database('msp_member')            #db = conn.msp_member
        collection = db.get_collection('member')        #members = db.member

          
            
        if(type=="p" or type=="P"): # Producer
            try:
                for member in collection.find({"type":"Producer","p_Name":args[0],"p_Phone":args[1]}):
                    return 'True'
            except:
                return 'False'

        elif(type=="d" or type=="D"): # Distributor
            for member in collection.find({"ID":id,"type":"Distributor"}):
                return (member["d_Company"],member["d_Name"],member["d_Phone"])
            
        elif(type=="a" or type=="A"): # Auctioneer
            for member in collection.find({"ID":id,"type":"Auctioneer"}):
                return (member["a_Company"],member["a_Name"],member["a_Phone"])

        elif(type=="w" or type=="W"): # Ware-House Manager
            for member in collection.find({"ID":id,"type":"wManager"}):
                return (member["w_Company"],member["w_Name"],member["w_Phone"])

        elif(type=="s" or type=="S"): # Seller
            for member in collection.find({"type":"Seller","s_Name":args[0],"s_Phone":args[1]}):
                return 'True'
            return 'False'
        
        else:
            return 'False'

    def verificationReponse(self, HOST, PORT):
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        while True:
            try:
                serverSocket = socket(AF_INET, SOCK_STREAM)
                serverSocket.bind(ADDR)
                serverSocket.listen(100)
                conn, addr_info = serverSocket.accept()
                data = conn.recv(BUFSIZE)
                msg = data.decode()
                type = msg.split('/')[0]
                name = msg.split('/')[1]              # 슬라이싱 하는 이유 = 데이터를 두개 이상씩 보내기 힘듬
                phone = msg.split('/')[2]
                data = self.verificationValue(type, name, phone)
                #msg = data[0]+'/'+data[1]+'/'+data[2]
                conn.sendall(data.encode())
                print(addr_info )
                print(" connect : " + msg + " => ("+data +")"+" send" )
                
        
            except Exception as e :
                print('socket error')
                sys.exit()

            conn.close()
        

if __name__ == "__main__":
    m1 = mspResponse()
    #m1.setAttribute(ID = "id2", password ="pw1")
    #m1.verificationReponse()   # 실패시 none 값 리
    m1.verificationReponse(sHOST, sPORT)
    #print(m1.memberDict())
