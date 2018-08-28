# This Python file uses the following encoding: utf-8

from msp_interest import interest
import msp_interest
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
                for member in collection.find({"type":"Producer","userName":args[0],"userPhone":args[1]}):
                    return 'True'
            except:
                return 'False'

        elif(type=="d" or type=="D"): # Distributor
            try:
                for member in collection.find({"type":"Distributor","userName":args[0],"userPhone":args[1]}):
                    return 'True'
            except:
                return 'False'
            
        elif(type=="a" or type=="A"): # Auctioneer
            try:
                for member in collection.find({"type":"Auctioneer","userName":args[0],"userPhone":args[1]}):
                    return 'True'
            except:
                return 'False'

        elif(type=="w" or type=="W"): # Ware-House Manager
            try:
                for member in collection.find({"type":"WManager","userName":args[0],"userPhone":args[1]}):
                    return 'True'
            except:
                return 'False'

        elif(type=="s" or type=="S"): # Seller
            for member in collection.find({"type":"Seller","userName":args[0],"userPhone":args[1]}):
                #print(member["_id"])
                return 'True'
            return 'False'
        
        else:
            return 'False'

    def login(self, *args):
        
        conn = pymongo.MongoClient(ipAddress,port)      #"mongodb://user1:blockchain@"
        db = conn.get_database('msp_member')            
        collection = db.get_collection('member')
        
        for member in collection.find({"ID":args[0],"password":args[1]}):  # [0]:id, [1]:password, [2]: ip
            collection.update_one({"ID": args[0] }, {"$set": {'userIPv4' : args[2]}})
            return 'True'
        return 'False'
        
    #def ipv4Response(self, *args):
        
    def verificationReponse(self, HOST, PORT):
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        while True:
            try:
                serverSocket = socket(AF_INET, SOCK_STREAM)
                serverSocket.bind(ADDR)
                serverSocket.listen(100)
                conn, addr_info = serverSocket.accept()
                data = conn.recv(1024)
                msg = data.decode()
                ipList = []
                if(msg.count('\\--\\') == 0):
                    ipInfo = interest()
                    ipList = ipInfo.collectInterestIPv4(msg)
                    if(ipList == 'False'):
                        data = ipList
                        conn.sendall(data.encode())
                        print("ipResponse - False"+" ("+addr_info[0]+")")
                    else:
                        message = str(len(ipList))
                        for i in range(len(ipList)):
                            message += "\\--\\" +ipList[i]
                    
                        print("ipResponse - Success"+" ("+addr_info[0]+")")
                        conn.sendall(message.encode())
                    
                    #print(" login connect - id:" + id +", password:" + password + " ( "+addr_info[0] +" )" )

                    
                elif(msg.count('\\--\\') == 1):
                    id = msg.split('\\--\\')[0]
                    password = msg.split('\\--\\')[1]
                    data = self.login(id,password, addr_info[0])        #login
                    conn.sendall(data.encode())
                    print(" login connect - id:" + id +", password:" + password + " ( "+addr_info[0] +" )" )
                    
                elif(msg.count('\\--\\') == 2):
                    type = msg.split('\\--\\')[0]
                    name = msg.split('\\--\\')[1]              
                    phone = msg.split('\\--\\')[2]
                    data = self.verificationValue(type, name, phone)
                    conn.sendall(data.encode())
                    print(" validate connect - " + type +" / " + name +" / " + phone +" / "+ " => '"+data +"'"+" send" + " ("+addr_info[0]+" )" )
                        #collection.update_one({"userName":name}, {"$set": {'userIPv4' : addr_info[0]}})

                conn.close()

            except:
                print('socket error')
                sys.exit()
            
        

if __name__ == "__main__":
    m1 = mspResponse()
    #m1.setAttribute(ID = "id2", password ="pw1")
    #m1.verificationReponse()   # 실패시 none 값 리
    m1.verificationReponse(sHOST, sPORT)
    #print(m1.memberDict())
