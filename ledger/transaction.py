# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import metadata
from DIgitalEnvelope.lib.libhash import libhash
from chaincode.randFileName import *

class transaction:
    def __init__(self, *args, **kwargs):

        self.flag = {}

        # 제안서 부분
        self.TXID = randFileName().split('.')[0]
        self.timestamp = time.time()
        self.verstion = metadata.metadata["BaseVersion"]
        self.creatorID = {} # 트랜잭션 생성자 서명
        self.TXType = "" # 트랜잭션 분류
        self.timeout = 0
        self.T_hash = "" # 현재 트랜잭션 해시
        self.txCount = 0

        # 검증 부분
        self.endorsers = {}
        self.sign = {}
        self.produce = {}

        # 추가될 해당 트랜잭션의 항목들
        # 품목
        self.P_name = "" # 이름
        self.P_From = "" # 생산지, 산지
        self.P_grade = "" # 등급
        self.P_wight = "" # 무게, Kg

        # 생산자
        self.M_name = "" # 이름
        self.M_phone = "" # 전화
        self.M_com = "" # 소속

        # 기타
        self.N_state = "" # 배송상태
        self.N_else = "" # 비고
        
        try:
            if '타입' in kwargs:
                self.N_state = kwargs['타입'] 

            if '생산자' in kwargs:
                self.M_name = kwargs['생산자'] 

            if '전화번호' in kwargs:
                self.M_phone = kwargs['전화번호'] 

            if '검증' in kwargs:
                self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 

            if '이름' in kwargs:
                self.P_name = kwargs['이름'] 

            if '산지' in kwargs:
                self.P_From = kwargs['산지'] 
                
            if '등급' in kwargs:
                self.P_grade = kwargs['등급'] 

            if '무게' in kwargs:
                self.P_wight = kwargs['무게'] 

            if '사인' in kwargs:
                self.sign[str(len(self.sign))] = kwargs['사인'] 

            if '서명' in kwargs:
                self.creatorID = kwargs['서명'] 

            self.T_hash = libhash(str(self.toDict())).getsha256()

        except Exception as e:
            print(e)
        return 

    def getHash(self):
        return self.T_hash

    def setAttribute(self, *args, **kwargs):
        try:
            if '타입' in kwargs:
                self.N_state = kwargs['타입'] 

            if '생산자' in kwargs:
                self.M_name = kwargs['생산자'] 

            if '전화번호' in kwargs:
                self.M_phone = kwargs['전화번호'] 

            if '검증' in kwargs:
                self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 

            if '이름' in kwargs:
                self.P_name = kwargs['이름'] 

            if '산지' in kwargs:
                self.P_From = kwargs['산지'] 
                
            if '등급' in kwargs:
                self.P_grade = kwargs['등급'] 

            if '무게' in kwargs:
                self.P_wight = kwargs['무게'] 

            if '사인' in kwargs:
                self.sign[str(len(self.sign))] = kwargs['사인'] 

            if '서명' in kwargs:
                self.creatorID = kwargs['서명'] 
            
            self.T_hash = libhash(str(self.toDict())).getsha256()

        except Exception as e:
            print(e)
        else:
            return False
            return True



        return False

    def toDict(self):
        Dict = {
            'TXID' : self.TXID,
            'timestamp' : self.timestamp,
            'verstion' : self.verstion,
            'creatorID' : self.creatorID,
            'TXType' : self.TXType,
            'timeout' : self.timeout,
            'T_hash' : self.T_hash,
            "txCount" : self.txCount,

            'endorsers' : self.endorsers,
            'sign'      : self.sign,
            'produce'   : self.produce,

            'P_name' : self.P_name,
            'P_From' : self.P_From,
            'P_grade' : self.P_grade,
            'P_wight' : self.P_wight,

            'M_name' : self.M_name,
            'M_phone' : self.M_phone,
            'M_com' : self.M_com,

            'N_state' : self.N_state,
            'N_else' : self.N_else
            }
        return Dict

    def fromDict(self, Dict):
        if type(Dict) is not type(dict()):
            print("false")
            return False
        try:
            
            if 'TXID' in Dict:
                self.TXID = Dict['TXID'] 

            if 'timestamp' in Dict:
                self.timestamp = Dict['timestamp'] 

            if 'verstion' in Dict:
                self.verstion = Dict['verstion'] 

            if 'creatorID' in Dict:
                self.creatorID = Dict['creatorID'] 

            if 'TXType' in Dict:
                self.TXType = Dict['TXType'] 

            if 'timeout' in Dict:
                self.timeout = Dict['timeout'] 
                
            if 'T_hash' in Dict:
                self.T_hash = Dict['T_hash'] 

            if 'txCount' in Dict:
                self.txCount = Dict['txCount'] 



            if 'endorsers' in Dict:
                self.endorsers = Dict['endorsers'] 
                
            if 'sign' in Dict:
                self.sign = Dict['sign'] 

            if 'produce' in Dict:
                self.produce = Dict['produce'] 

                

            if 'P_name' in Dict:
                self.P_name = Dict['P_name'] 

            if 'P_From' in Dict:
                self.P_From = Dict['P_From'] 
                
            if 'P_grade' in Dict:
                self.P_grade = Dict['P_grade'] 

            if 'P_wight' in Dict:
                self.P_wight = Dict['P_wight'] 

                

            if 'M_name' in Dict:
                self.M_name = Dict['M_name'] 
                
            if 'M_phone' in Dict:
                self.M_phone = Dict['M_phone'] 

            if 'M_com' in Dict:
                self.M_com = Dict['M_com'] 

                
                
            if 'N_state' in Dict:
                self.N_state = Dict['N_state'] 

            if 'N_else' in Dict:
                self.N_else = Dict['N_else'] 
        except Exception as e:
            print(e)
        else:
            return True
        return False

    def toJson(self):
        try:
            save = json.dumps(self.toDict())
            file = pathlib.Path(self.TXID)
            file.write_text(save, encoding='utf-8')
        except:
            return False
        else:
            return True
        return

    def fromJson(self):
        Data = None
        try:
            file = pathlib.Path(self.TXID)
            file_text = file.read_text(encoding='utf-8')
            Data = json.loads(file_text)
        except:
            return False
        else:
            return Data
        return False


if __name__ == "__main__":
    t1 = transaction(이름='딸기', 검증={'IP':'202.31.146.57'}, 타입="입고") # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
