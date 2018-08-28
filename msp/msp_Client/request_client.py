# This Python file uses the following encoding: utf-8

from socket import *
import select
import sys



class client:
    def login(self):

        HOST = '202.31.146.50'
        PORT = 10000
        BUFSIZE = 1024
        ADDR = (HOST,PORT)
        Socket = socket(AF_INET, SOCK_STREAM)


        try:
            userID = input("ID : ")
            userPassword = input("Password :")
            
            Socket.connect(ADDR)
            request = userID+"\\--\\"+userPassword
            Socket.sendall(request.encode())
            data = Socket.recv(1024)
            msg = data.decode()
            return msg

        except Exception as e :
            print('%s:%s'%ADDR)
            print("접속이 실패하였습니다")
            return False
        else:
            return True

        
                             
class mspRequest: # 로그인
    def verificationRequest(self, *args):
        HOST = '202.31.146.50'
        PORT = 10000
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        Socket = socket(AF_INET, SOCK_STREAM)

        try:
            Socket.connect(ADDR)
            if(len(args) == 2):
                request = args[0]+"\\--\\"+args[1]
                
            elif(len(args) == 3):
                request = args[0]+"\\--\\"+args[1]+"\\--\\"+args[2]
                
            Socket.sendall(request.encode())
            data = Socket.recv(1024)
            msg = data.decode()
            Socket.close()
            return msg

        except Exception as e :
            print('%s:%s'%ADDR)
            return False

class ipv4Request: # 이해관계자 리스트 반환
    def ipv4Request(self, *args):
        HOST = '202.31.146.50'
        PORT = 10000
        BUFSIZE = 1024
        ADDR = (HOST,PORT)

        Socket = socket(AF_INET, SOCK_STREAM)
        ipList=[]
        try:
            Socket.connect(ADDR)
            Socket.sendall(args[0].encode())
            data = Socket.recv(1024)
            msg = data.decode()
            if(msg.count('\\--\\')==0):
                return msg
            else:
                for i in range(int(msg.split('\\--\\')[0])):
                    ipList.append(msg.split('\\--\\')[i+1]) 
                #print(ipList)
                Socket.close()
                return int(msg.split('\\--\\')[0]), ipList

        except Exception as e :
            print('%s:%s'%ADDR)
            return False





        
if __name__ == "__main__":
    ms = mspRequest()
    #print(ms.verificationRequest('a','박신종','010-6682-8590')) # ('type', 'id') 있으면 값을 튜플형태로 리턴
                                         # 없으면 False값 리턴
    print("")
    ip = ipv4Request()
    num, ip = ip.ipv4Request("01")
    print(ip)
    
    """
    print(ms.verificationRequest('a1','a1'))
    print(ms.verificationRequest('a2','a2'))
    print(ms.verificationRequest('a3','a3'))
    print(ms.verificationRequest('a4','a4'))
    print(ms.verificationRequest('a5','a5'))
    """
