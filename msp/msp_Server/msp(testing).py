# This Python file uses the following encoding: utf-8

from msp_Response import mspResponse
from msp_Manage import mspManage
from multiprocessing import Process
import threading
from threading import Thread

sHOST = ''
sPORT = 10000

class msp:
    def runResponseServer(self):
        response = mspResponse()
        response.verificationReponse(sHOST, sPORT)

    def runMspServer(self):
        runServer = mspManage()
        runServer.run()

def main():
    m1 = msp()
    m2 = msp()
    
    p1 = Process(target=m1.runMspServer)
    p2 = Process(target=m2.runResponseServer)
    
    p1.start()
    p2.start()

    ##p1.join()
    #p2.join()

    #m1.runResponseServer()

    #Thread(target = m1.runResponseServer()).start()
    #Thread(target = m1.runMspServer()).start()

if __name__ == "__main__":
    #m1 = msp()
    #m1.setAttribute(ID = "id2", password ="pw1")
    #m1.verificationReponse()   # 실패시 none 값 리
    #m1.verificationReponse(sHOST, sPORT)
    #print(m1.memberDict())
    main()
