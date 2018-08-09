import sys
import os
import socket
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from uuid import getnode
from ledger.transaction import *
from chaincode.chainToJson import *

class Stakeholder1:
    def addSign(self, Object, number, Whether):
        Information = Stakeholder()
        Sign = Information.sign
        Object.produce[number] = {'produce':Whether}
        Object.sign[number] = {'sign':Sign}
        return Object
    
    def Verification(self, Object):
        Information = Stakeholder()
        IP = Information.IP
        Mac = Information.Mac
        data = Information.get_database()
        for i in range(0, len(Object.Stakeholders)):
            if Object.Stakeholders.get(str(i)) == {'IP':IP, 'Mac':Mac}:
                node = Information.get_nodedata(Object.creatorID)
                if node:
                    SameCount = 0
                    InconsistencyCount = 0
                    dic = Object.toDict()
                    
                    for k in data.keys():
                        if dic[k] == data[k]:
                            SameCount += 1
                        else :
                            InconsistencyCount += 1
                
                    if (SameCount / (SameCount + InconsistencyCount)) * 100 > 50:
                        self.Object = self.addSign(self.Object, str(i), "agree", Object.creatorID)
                        #print("퍼센트가 " + ((SameCount + InconsistencyCount) / SameCount) * 100 + "이므로 블록생성 찬성")
                    elif (SameCount / (SameCount + InconsistencyCount)) * 100 < 51:
                        self.Object = self.addSign(self.Object, str(i), "Opposition")
                        #print("퍼센트가 " + str((SameCount / (SameCount + InconsistencyCount)) * 100) + "이므로 블록생성 반대")
    
    def __init__(self, Object):
        self.Object = Object
        if type(self.Object) == type(transaction()):
            self.Verification(self.Object)
        else:
            print(2)
            
class Stakeholder:
    def __init__(self):
        self.IP   = '202.31.146.57'
        self.Mac  = '0c:54:a5:49:bf:fa'
        self.name = '김기영'
        self.sign = 'a'


    def get_ipaddress(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        r = s.getsockname()[0]
        s.close()
        return r

    def get_macaddress(self):
        address = getnode()
        h = iter(hex(address)[2:].zfill(12)) 
        return ":".join(i + next(h) for i in h) 

    def get_database(self):
        dic = {
            'creatorID' : "asas",          # 트랜잭션 생성자 서명
            'TXType'    : "생산",          # 트랜잭션 분류
            'T_hash'    : "asd",           # 현재 트랜잭션 해시

            'P_name'    : "딸기",          # 품목 이름
            'P_From'    : "군산시",        # 품목 생산지, 산지
            'P_grade'   : "상급",          # 품목 등급
            'P_wight'   : "2kg",           # 품목 무게, Kg

            'M_name'    : "박신재",        # 생산자 이름
            'M_phone'   : "010-4646-4232", # 생산자 전화
            'M_com'     : "군산대학교",    # 생산자 소속

            'N_state'   : "입고",          # 배송상태
            'N_else'    : "",              # 비고
            }
        return dic

    def get_nodedata(self,num):
        #멤버쉽에 등록된 노드 정보
        node1 = {
            'name' : "김기영",             # 멤버 이름
            'IP'   : "202.31.146.57",      # 멤버 IP
            'MAC'  : "0c:54:a5:49:bf:fa",  # 멤버 MAC
            'sign' : "aa"                  # 멤버 서명
            }
        node2 = {
            'name' : "박신재",             # 멤버 이름
            'IP'   : "202.31.146.48",      # 멤버 IP
            'MAC'  : "90:9f:33:00:da:49",  # 멤버 MAC
            'sign' : "bb"                  # 멤버 서명
            }
        node3 = {
            'name' : "김기도",             # 멤버 이름
            'IP'   : "203.31.147.203",     # 멤버 IP
            'MAC'  : "e0-d5-5e-9a-63-93",  # 멤버 MAC
            'sign' : "cc"                  # 멤버 서명
            }
        node4 = {
            'name' : "정상훈",             # 멤버 이름
            'IP'   : "202.31.146.58",      # 멤버 IP
            'MAC'  : "50-b7-c3-a2-dd-5b",  # 멤버 MAC
            'sign' : "dd"                  # 멤버 서명
            }

        nodes = {
            #'노드 주민번호' : 노드 정보
            'a' : node1,
            'b' : node2,
            'c' : node3,
            'd' : node4
            }

        count = 0
        for k in nodes.keys():
            if num == k:
                return nodes[k]
            elif count ==  len(nodes.keys()):
                return None
            else : 
                count += 1

