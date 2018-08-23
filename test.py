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

global ip 

import socketserver, os, pathlib, sys, socket
from os.path import exists

from ledger.block import block
from ledger import transaction
from chaincode.transactionToJson import *
from chaincode.server_Json import *
from chaincode.blockToJson import blockToJson
from chaincode.randFileName import *
from chaincode.leader_rand import *

from uuid import getnode
from ledger.transaction import *
from chaincode.chainToJson import *

ip = ['202.31.146.57','202.31.147.203','202.31.146.48','202.31.146.58']

# 1. run server
def socket_server():
    try :
        HOST = "202.31.146.57"
        PORT =  9009
        runServer(Host = HOST, Port  = PORT)
    except:
        print()
    return False

# 2. make tx

def makeTransaction():
    print("make transaction")
    생산자 = input('생산자 이름 : ')
    전화번호 = input('전화번호 : ')

    타입 = input('배송 상태 : ')

    이름 = input('이름 : ')
    산지 = input('산지 : ')
    등급 = input('등급 : ')
    무게 = input('무게 : ')

    try : tx = transaction(생산자 = 생산자, 전화번호 = 전화번호, 이름 = 이름, 산지 = 산지, 등급 = 등급, 무게 = 무게, 타입 = 타입)
    except : print("error!")
    else : print("done!!")

    print(tx.toDict())
    return tx


# 3. take_atfter_tx
def take_after_tx(filename):
    ttj = transactionToJson(filename = filename)
    ttj.data = ttj.loadJson()
    Transaction = transaction()
    Transaction.fromDict(Dict = ttj.data)
    print(Transaction.toDict())
    return Transaction
    
# 4. agree

class endorser:
    def addSign(self, Object, number, Whether, sign):
        Information = Endorser()
        Sign = Information.sign
        Object.produce = Whether
        Object.sign = Sign
        return Object
    
    def Verification(self, Object):
        Information = Endorser()
        IP = Information.IP
        data = Information.get_database()
        for i in range(0, len(Object.endorsers)):
            if Object.endorsers.get(str(i)) == {'IP':IP}:
                
                SameCount = 0
                InconsistencyCount = 0
                dic = Object.toDict()
                print(data)
                print(dic)
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
        self.name = '김기도'
        self.sign = 'GD'


    def get_ipaddress(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("gmail.com",80))
        r = s.getsockname()[0]
        s.close()
        return r
    
    def get_database(self):
        dic = {
            "P_name": "딸기",  
            "P_From": "군산",
            "P_grade": "특",
            "P_wight": "10",
            "M_name": "김기도",
            "M_phone": "01092668459",
            "N_state": "보통",
            }
        return dic


# 6. leader Synthesis
class leader:
    def __init__(self,Txname):
        path_dir = os.path.dirname(__file__) + "\data_server\\"
        global result
        file_list = os.listdir(path_dir)
        file_list.sort()
        count=0
        discount=0
        for i in file_list:
            if i.find(Txname) is not -1:
                ttj = transactionToJson(filename = i)
                ttj.data = ttj.loadJson()
                Transaction = transaction()
                Transaction.fromDict(Dict = ttj.data)
                print(Transaction.toDict())
                if Transaction.produce == 'agree':
                    count=count+1
                else:
                    discount= discount+1
        result = count/(count+discount)*100
         
        if result>50:
             print("블록 찬성여부가 " + str(result) + "%이므로 블록을 생성합니다.")
             
        else:
             print("블록 찬성여부가 " + str(result) + "%이므로 블록을 생성하지 않습니다.")
        
        
# 7. make_block
def make_block(tx):
    Block = block(tx)
    print(Block.toDict())
    btj = blockToJson(filename = "block_" + Block.blockID+".json", data = Block)
    btj.saveJson()

# 9. block dispersion
def block_dispersion(Host,Port,filename):
    print(type(Host), Host)
    path = os.path.dirname(__file__) + "\data_server\\"
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
                
# 10. chain append
def chain_append():
    path = os.path.dirname(__file__) + "\data_server\\"
    filename = str(input('체인에 연결시킬 블록 : '))
    btj = blockToJson(filename = filename)
    btj.data = btj.loadJson()
    Block = block()
    Block.fromDict(Dict = btj.data)
    chid = input('CHID : ')
    filename = "ch_" + chid + ".json"
    if not exists(path + filename):
        Chain = chain(CHID = chid, block = Block)
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

if __name__ == "__main__":
    filename = ""
    result = 0
    tx=None

    while True:
        
        print("---------------- socket - blockchain test ----------------")
        print("1. run server")
        print("2. make tx")
        print("3. make block")
        print("4. Block dispersion")
        print("0. 종료")
    
        num = int(input('select : '))
        if num == 1:
            print("1. run server")
            socket_server()
        elif num==0:
            break
    
        elif num == 2:
            print("2. make tx")
            tx = makeTransaction()
        
        elif num == 3:
            print("3. make block")
            make_block(tx)
            
        elif num == 4:
            print("4. Block dispersion")
            filename = input('filename : ')
            for i in ip:
                block_dispersion(Host = i,Port= 9009,filename=filename)
