import sys
import os
import socket
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from uuid import getnode
from ledger.transaction_Strawberry import *
from chaincode.chainToJson import *
import stakeholder_1 
import stakeholder_2 
import operator

class endorser1:
    def addSign(self, Object, number, Whether, sign):
        Information = Endorser()
        Sign = Information.sign
        Object.produce[number] = {'produce':Whether}
        Object.sign[number] = {'sign':Sign}
        return Object
    
    def Verification(self, Object):
        Information = Endorser()
        IP = Information.IP
        Mac = Information.Mac
        data = Information.get_database()
        for i in range(0, len(Object.endorsers)):
            if Object.endorsers.get(str(i)) == {'IP':IP, 'Mac':Mac}:
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
                        print("퍼센트가 " + str((SameCount / (SameCount + InconsistencyCount)) * 100) + "이므로 블록생성 찬성")
                        return self.Object
                    elif (SameCount / (SameCount + InconsistencyCount)) * 100 < 51:
                        self.Object = self.addSign(self.Object, str(i), "Opposition", Object.creatorID)
                        print("퍼센트가 " + str((SameCount / (SameCount + InconsistencyCount)) * 100) + "이므로 블록생성 반대")
                        return self.Object
    



    def __init__(self, Object):
        self.Object = Object
        if type(self.Object) == type(transaction()):
            self.Verification(self.Object)
        else:
            print(2)
            
class Endorser:
    def __init__(self):
        self.IP   = '202.31.146.57'
        self.Mac  = '90:9f:33:00:da:49'
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
            'creatorID'      : "asas",          # 트랜잭션 생성자 서명
            'TXType'         : "생산",          # 트랜잭션 분류
            'T_hash'         : "asd",           # 현재 트랜잭션 해시

            'To_name1'       : "박신재", # 생산자(단체)이름
            'To_phone'       : "010-4646-4232", # 생산자(단체)전화번호
            'To_address1'    : "블루빌", # 생산자(단체)주소
            'To_name2'       : "군산대", # 브랜드
            'To_name3'       : "딸기", # 상품이름(재배품목명)
            'To_kind'        : "매향", # 재배품종명
            'To_address2'    : "디지털정보관", # 재배지주소
            'To_culture'     : "하우스", # 재배작형
            'To_harvesting'  : "2018-06-01", # 수확날짜
            'To_shipment'    : "2018-06-05", # 출하날짜
            'To_weight'      : "10", # 무게
            'To_rating'      : "상", # 등급
            'To_htn'         : "123-12-12312", # 이력추적관리번호
            'To_pesticide'   : "", # 농약제품명
            'To_pusage'      : "", # 농약용도
            'To_pshape'      : "" # 농약형태
            }
        return dic

    def get_nodedata(self,num):
        #멤버쉽에 등록된 노드 정보
        node1 = {
            'name' : "김기영",             # 멤버 이름
            'IP'   : "202.31.146.57",      # 멤버 IP
            'MAC'  : "90:9f:33:00:da:49",  # 멤버 MAC
            }
        node2 = {
            'name' : "박신재",             # 멤버 이름
            'IP'   : "202.31.146.48",      # 멤버 IP
            'MAC'  : "0c:54:a5:49:bf:fa",  # 멤버 MAC
            }
        node3 = {
            'name' : "김기도",             # 멤버 이름
            'IP'   : "203.31.147.203",     # 멤버 IP
            'MAC'  : "e0-d5-5e-9a-63-93",  # 멤버 MAC
            }
        node4 = {
            'name' : "정상훈",             # 멤버 이름
            'IP'   : "202.31.146.58",      # 멤버 IP
            'MAC'  : "50-b7-c3-a2-dd-5b",  # 멤버 MAC
            }

        nodes = {
            #'노드 인증서' : 노드 정보
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
 
class leader:
    def __init__(self, Object):
        self.Object = Object
        AgreeCount = 0
        OppositionCount = 0
        if type(self.Object) == type(transaction()):
            Information = Endorser()
            for i in range(0, len(Object.endorsers)):
                if self.Object.produce.get(str(i)) == {"produce":"agree"}:
                    AgreeCount += 1
                elif self.Object.produce.get(str(i)) == {"produce":"Opposition"}:
                    OppositionCount += 1

            if (AgreeCount / (AgreeCount + OppositionCount)) * 100 > 50:
                print("퍼센트가 " + str((AgreeCount / (AgreeCount + OppositionCount)) * 100) + "이므로 블록생성 가능")
            elif (AgreeCount / (AgreeCount + OppositionCount)) * 100 < 51:
                print("퍼센트가 " + str((AgreeCount / (AgreeCount + OppositionCount)) * 100) + "이므로 블록생성 불가능")

        else:
            print(2)

