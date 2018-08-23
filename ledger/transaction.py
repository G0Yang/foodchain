# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

import metadata
from hash256.hash256 import *

class transaction:
    def __init__(self, *args, **kwargs):

        self.flag = {}

        # 제안서 부분
        self.TXID = ""
        self.timestamp = time.time()
        self.verstion = metadata.BaseVersion
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
            # self.endorsers[str(len(self.endorsers))] = kwargs['검증']
            # self.N_state = kwargs['타입']
            try :   self.N_state = kwargs['타입'] 
            except: print("타입 error")
            
            try :   self.M_name = kwargs['생산자'] 
            except: print("생산자 error")

            try :   self.M_phone = kwargs['전화번호'] 
            except: print("전화번호 error")

            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.P_name = kwargs['이름'] 
            except: print("이름 error")

            try :   self.P_From = kwargs['산지'] 
            except: print("산지 error")

            try :   self.P_grade = kwargs['등급'] 
            except: print("등급 error")

            try :   self.P_wight = kwargs['무게'] 
            except: print("무게 error")

            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            self.T_hash = hash256(str(self.toDict())).getHash()

        except:
            print("error")
        return 

    def getHash(self):
        return self.T_hash

    def setAttribute(self, *args, **kwargs):
        try:
            # self.endorsers[str(len(self.endorsers))] = kwargs['검증']
            # self.N_state = kwargs['타입']
            try :   self.N_state = kwargs['타입'] 
            except: self.flag['타입'] = False
            
            try :   self.M_name = kwargs['생산자'] 
            except: self.flag['생산자'] = False

            try :   self.M_phone = kwargs['전화번호'] 
            except: self.flag['전화번호'] = False

            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: self.flag['검증'] = False
            
            try :   self.P_name = kwargs['이름'] 
            except: self.flag['이름'] = False

            try :   self.P_From = kwargs['산지'] 
            except: self.flag['산지'] = False

            try :   self.P_grade = kwargs['등급'] 
            except: self.flag['등급'] = False

            try :   self.P_wight = kwargs['무게'] 
            except: self.flag['무게'] = False

            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: self.flag['사인'] = False
            
            try :   self.creatorID = kwargs['서명']
            except: self.flag['서명'] = False
            
            self.T_hash = hash256(str(self.toDict())).getHash()

        except:
            print("error")
        else:
            if False in self.flag:
                for i in self.flag:
                    print(i, "is error")
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
            try : self.TXID = Dict['TXID']
            except: print()
            try : self.timestamp = Dict['timestamp']
            except: print()
            try : self.verstion = Dict['verstion']
            except: print()
            try : self.creatorID = Dict['creatorID']
            except: print()
            try : self.TXType = Dict['TXType']
            except: print()
            try : self.timeout = Dict['timeout']
            except: print()
            try : self.T_hash = Dict['T_hash']
            except: print()
            try : self.txCount = Dict['txCount']
            except: print()

            try : self.endorsers = Dict['endorsers']
            except: print()
            try : self.sign = Dict['sign']
            except: print()
            try : self.produce = Dict['produce']
            except: print()

            try : self.P_name = Dict['P_name']
            except: print()
            try : self.P_From = Dict['P_From']
            except: print()
            try : self.P_grade = Dict['P_grade']
            except: print()
            try : self.P_wight = Dict['P_wight']
            except: print()

            try : self.M_name = Dict['M_name']
            except: print()
            try : self.M_phone = Dict['M_phone']
            except: print()
            try : self.M_com = Dict['M_com']
            except: print()

            try : self.N_state = Dict['N_state']
            except: print()
            try : self.N_else = Dict['N_else']
            except: print()
        except:
            return False
        else:
            return True
        return False

if __name__ == "__main__":
    t1 = transaction(이름='딸기', 검증={'IP':'202.31.146.57'}, 타입="입고") # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
