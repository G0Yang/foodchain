# This Python file uses the following encoding: utf-8

# 기영 202.31.146.57
# 기도 202.31.147.203
# 신재 202.31.146.48
# 상훈 202.31.146.58
# PORT 9009

# 가정
# 1. 기존 장부는 있다. (Chain은 이미 있다.)
# 2. 기존 장부에 트랜잭션을 발생시켜 블록화를 하고 채인에 추가함
# 3. 채인에 추가할 때 FlagDB까지 갱신을 시켜야 한다.
# 4. 트랜잭션은 이미 만들어진 data_server\tx_52qp2i55919387.json 을 기본으로 한다.
# 5. 기존 장부는 data_server\ch_8srkziel366214.json 을 기본으로 한다.
# 6. 마지막 10. chain append는 모든 노드가 최대한 비슷한 시간에 동시에 수행되어야 한다.
# 7. 결론적으로 tx_52qp2i55919387.json 의 내용이 합의를 통해서 ch_8srkziel366214.json 에 추가되어야 한다.

import socketserver, os, pathlib, sys, socket
from os.path import exists

from ledger.block import block
from ledger import transaction
from chaincode.transactionToJson import *
from chaincode.server_Json import *
from chaincode.blockToJson import blockToJson
from chaincode.randFileName import *



# 1. run server
def socket_server():
    try :
        HOST = "202.31.147.203"
        PORT =  9009
        runServer(Host = HOST, Port  = PORT)
    except:
        print()
    return False

# 2. send tx

def send_tx(Host, Port, filename):
    path = os.path.dirname(__file__) + "\data_client\\"
    filename = path + filename

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((Host,Port))

        if not exists(filename): # 파일이 해당 디렉터리에 존재하지 않으면
            print("not exists(filename)")
            return # handle()함수를 빠져 나온다.

        with open(filename, 'rb') as f:
            try:
                data = f.read()
                sock.sendall(data)
                print(data)
            except Exception as e:
                print(e)

# 3. take_atfter_tx
def take_after_tx():
    filename= str(input('받은 파일 이름: '))
    ttj = transactionToJson(filename = filename)
    ttj.data = ttj.loadJson()
    Transaction = transaction()
    Transaction.fromDict(Dict = ttj.data)
    print(Transaction.toDict())
    
    print(Transaction.P_From)

# 4. agree
class endorser:
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
        self.IP   = self.get_ipaddress()
        self.Mac  = self.get_macaddress()
        self.name = 'Park Sin Jae'
        self.sign = 'b'


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
    def __init__(self, t):
        temp = []

        for i in range(0, len(t)):
            temp.append(t[i])

        for i in range(0, len(t)):
            for j in range(0, len(t)):
                if temp[i].sign[str(j)]:
                    temp[0].sign[str(j)] = temp[i].sign[str(j)]
                if temp[i].produce[str(j)]:
                    temp[0].produce[str(j)] = temp[i].produce[str(j)]

        self.Object = temp[0]
        AgreeCount = 0
        OppositionCount = 0
        if type(self.Object) == type(transaction()):
            Information = Endorser()
            for i in range(0, len(temp[0].endorsers)):
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
# 7. make_block
def make_block():
    filename = str(input('블록화시킬 트랜잭션 : '))
    ttj = transactionToJson(filename = filename)
    ttj.data = ttj.loadJson()
    Transaction = transaction()
    Transaction.fromDict(Dict = ttj.data)
    Block = block(Transaction)
    print(Block.toDict())
    btj = blockToJson(filename = "block_" + Block.blockID+".json", data = Block)

# 9. block dispersion
def block_dispersion():
    Host = input('HOST : ')
    Port = int(input('PORT : '))
    filename = input('filename : ')
    path = os.path.dirname(__file__) + "\data_client\\"
    filename = path + filename

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((Host,Port))

        if not exists(filename): # 파일이 해당 디렉터리에 존재하지 않으면
            print("not exists(filename)")
            return # handle()함수를 빠져 나온다.

        with open(filename, 'rb') as f:
            try:
                data = f.read()
                sock.sendall(data)
                print(data)
            except Exception as e:
                print(e)

if __name__ == "__main__":
    while True:
        
        print("---------------- socket - blockchain test ----------------")
        print("1. run server")
        print("2. send tx")
        print("3. take after tx")
        print("4. agree")
        print("5. send leader")
        print("6. leader Synthesis")
        print("7. make block")
        print("8. renewal FlagDB")
        print("9. Block dispersion")
        print("10. chain append")
        print("0. 종료")
    
        num = int(input('select : '))
        if num == 1:
            print("1. run server")
            socket_server()
        elif num==0:
            break
    
        elif num == 2:
            print("2. send tx")
            send_tx("202.31.146.58", 9009, "tx_9z3crvy7897529.json")
    
        elif num == 3:
            print("3. take after tx")
            take_after_tx()
    
        elif num == 4:
            print("4. agree")
            
    
        elif num == 5:
            print("5. send leader")
    
        elif num == 6:
            print("6. leader Synthesis")
    
        elif num == 7:
            print("7. make block")
            make_block()
    
        elif num == 8:
            print("8. renewal FlagDB")
    
        elif num == 9:
            print("9. Block dispersion")
            block_dispersion()
    
        elif num == 10:
            print("10. chain append")        
