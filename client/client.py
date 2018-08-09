import time, sys, os, json, pathlib, socket, threading
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256.hash256 import *
from ledger.transaction import *
from ledger.block import *
from chaincode.transactionToJson import *
from chaincode.blockToJson import *
from msp.msp import *

class client:
    def __init__(self, *args, **kwargs):
        self.perm = ""
        try : self.perm = self.logging(kwargs['ID'], kwargs['PW'])
        except : print("set permmision denind")
        self.sign = self.perm
        return 

    def logging(self, ID, PW):
        m1 = msp()
        perm = m1.getpermmission(ID, PW)
        return perm

    def generateTX(self, tx):
        self.tx = [tx]
        if type(tx) != type(transaction):
            return False
        else:
            # Socket 기반 TX 보내기
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect(('202.31.146.57', 4000))
                line = tx.toString()
                s.sendall(line.encode())

            # Json으로 저장
            #t1 = transactionToJson.transactionToJson(tx)
            #BH = tj.getData()  
            #j1 = json.dumps(BH)
            #file = pathlib.Path('example.json')
            #file.write_text(transactionToJson.dict_to_json(BH, transactionToJson.data_to_json), encoding='utf-8')
            # -----------------------------------------------------------------------
            return True
        return False


    def getTX(self):
        while True:
            state = self.run_server()
                # 0:T_Header, 1:T_Signature, 2:CreatorIdentity, 3:T_timestamp, 4:T_Hash, 5 :From
                # 6:To, 7:품목, 8:등급, 9:품종, 10:산지, 11:무게, 12:이름, 13:전화번호
                # 14~ : T_Endorsements
            tx = transaction.transaction(state[5], state[6], state[12], state[13], state[7], \
                                         state[9], state[8], state[10], state[11])
            print((state[5], state[6], state[12], state[13], state[7], state[9], state[8], state[10], state[11]))
            b1 = block.block(tx)
            btj = blockToJson.blockToJson(b1)
            btj.saveBlockToJson(b1)

    def run_server(self, port = 4000):
        host = '202.31.146.57'
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((host, port))
            s.listen(1)
            conn, addr = s.accept()
            msg = conn.recv(1024)
            msg1 = f'{msg.decode()}'    
            msg1 = msg1.split(' ')
            #conn.sendall(msg)
            conn.close()
        return msg1

if __name__ == "__main__":
    c1 = client("1","1") # login
    c2 = client("2","2") # login
    print("login 1, 2")


    t = threading.Thread(target=c1.getTX)
    t.start()
    print("Thread Start", t)

    time.sleep(2)

    flag = c2.generateTX(transaction("A", "B", "Kim", "010-1234-5678", "딸기", "딸기", "A등급", "군산", "15Kg")) # make TX
    flag = c2.generateTX(transaction("A", "B", "Kim", "010-1234-5678", "딸기", "딸기", "A등급", "군산", "15Kg")) # make TX
    flag = c2.generateTX(transaction("A", "B", "Kim", "010-1234-5678", "딸기", "딸기", "A등급", "군산", "15Kg")) # make TX
    print(flag)

    time.sleep(2)

    print("exit")

        
    #t1 = transaction.transaction("d", "s")
    #c1 = client()
    #c1.generateTX(t1)

    #file = pathlib.Path('example.json')
    #file_text = file.read_text(encoding='utf-8')
    #json_data = json.loads(file_text)

    #print(file_text, type(file_text))
