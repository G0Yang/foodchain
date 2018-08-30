# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256.hash256 import *

class transaction_Producer:
    def __init__(self, *args, **kwargs):

        self.flag = {}

        #-- 고정 트랜잭션 항목 --
        # 제안서 부분
        self.TXID = ""
        self.timestamp = time.time()
        self.verstion = 0.2
        self.creatorID = {} # 트랜잭션 생성자 서명
        self.TXType = "Producer" # 트랜잭션 분류
        self.timeout = 0
        self.T_hash = "" # 현재 트랜잭션 해시

        # 검증 부분
        self.endorsers = {}
        self.sign = {}
        self.produce = {}

        # -- 생산 트랜잭션 항목 --
        self.P_name = "" # 생산자(단체)이름
        self.P_phone = "" # 생산자(단체)전화번호
        self.P_address = "" # 생산자(단체)주소
        self.P_brand = "" # 브랜드
        self.P_goodsname = "" # 상품이름(재배품목명)
        self.P_kind = "" # 재배품종명
        self.P_CAddress = "" # Culture Address
        self.P_culture = "" # 재배작형
        self.P_harvesting = "" # 수확날짜
        self.P_shipment = "" # 출하날짜
        self.P_weight = "" # 무게
        self.P_rating = "" # 등급
        self.P_sc = "" # 당도
        self.P_htn = "" # 이력추적관리번호
        self.P_CRNumber = "" # 사업자등록번호
        self.P_pesticide = "" # 농약제품명
        self.P_pusage = "" # 농약용도
        self.P_pshape = "" # 농약형태

        
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")

            try :   self.produce[str(len(self.produce))] = kwargs['동의'] 
            except: print("동의 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.P_name = kwargs['생산자이름'] 
            except: print("생산자이름 error")

            try :   self.P_phone = kwargs['생산자전화번호'] 
            except: print("생산자전화번호 error")

            try :   self.P_address = kwargs['생산자주소'] 
            except: print("생산자주소 error")

            try :   self.P_brand = kwargs['브랜드'] 
            except: print("브랜드 error")
            
            try :   self.P_goodsname = kwargs['상품이름'] 
            except: print("상품이름 error")

            try :   self.P_kind = kwargs['재배품종'] 
            except: print("재배품종 error")

            try :   self.P_CAddress = kwargs['재배지주소'] 
            except: print("재배지주소 error")

            try :   self.P_culture = kwargs['재배작형'] 
            except: print("재배작형 error")
            
            try :   self.P_harvesting = kwargs['수확날짜'] 
            except: print("수확날짜 error")
            
            try :   self.P_shipment = kwargs['출하날짜'] 
            except: print("출하날짜 error")
            
            try :   self.P_weight = kwargs['무게'] 
            except: print("무게 error")
            
            try :   self.P_rating = kwargs['등급'] 
            except: print("등급 error")
            
            try :   self.P_sc = kwargs['당도'] 
            except: print("당도 error")
            
            try :   self.P_htn = kwargs['이력추적관리번호'] 
            except: print("이력추적관리번호 error")
            
            try :   self.P_CRNumber = kwargs['사업자등록번호'] 
            except: print("사업자등록번호 error")

            try :   self.P_pesticide = kwargs['농약제품명'] 
            except: print("농약제품명 error")
            
            try :   self.P_pusage = kwargs['농약용도'] 
            except: print("농약용도 error")
            
            try :   self.P_pshape = kwargs['농약형태'] 
            except: print("농약형태 error")

            self.T_hash = hash256(str(self.toDict())).getHash()

        except:
            print("error")
        return 

    def setAttribute(self, *args, **kwargs):
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")

            try :   self.produce[str(len(self.produce))] = kwargs['동의'] 
            except: print("동의 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.P_name = kwargs['생산자이름'] 
            except: print("생산자이름 error")

            try :   self.P_phone = kwargs['생산자전화번호'] 
            except: print("생산자전화번호 error")

            try :   self.P_address = kwargs['생산자주소'] 
            except: print("생산자주소 error")

            try :   self.P_brand = kwargs['브랜드'] 
            except: print("브랜드 error")
            
            try :   self.P_goodsname = kwargs['상품이름'] 
            except: print("상품이름 error")

            try :   self.P_kind = kwargs['재배품종'] 
            except: print("재배품종 error")

            try :   self.P_CAddress = kwargs['재배지주소'] 
            except: print("재배지주소 error")

            try :   self.P_culture = kwargs['재배작형'] 
            except: print("재배작형 error")
            
            try :   self.P_harvesting = kwargs['수확날짜'] 
            except: print("수확날짜 error")
            
            try :   self.P_shipment = kwargs['출하날짜'] 
            except: print("출하날짜 error")
            
            try :   self.P_weight = kwargs['무게'] 
            except: print("무게 error")
            
            try :   self.P_rating = kwargs['등급'] 
            except: print("등급 error")
            
            try :   self.P_sc = kwargs['당도'] 
            except: print("당도 error")
            
            try :   self.P_htn = kwargs['이력추적관리번호'] 
            except: print("이력추적관리번호 error")
            
            try :   self.P_CRNumber = kwargs['사업자등록번호'] 
            except: print("사업자등록번호 error")

            try :   self.P_pesticide = kwargs['농약제품명'] 
            except: print("농약제품명 error")
            
            try :   self.P_pusage = kwargs['농약용도'] 
            except: print("농약용도 error")
            
            try :   self.P_pshape = kwargs['농약형태'] 
            except: print("농약형태 error")

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

            'endorsers' : self.endorsers,
            'sign'      : self.sign,
            'produce'   : self.produce,

            'P_name' : self.P_name,
            'P_phone' : self.P_phone,
            'P_address' : self.P_address,
            'P_brand' : self.P_brand,
            'P_goodsname' : self.P_goodsname,
            'P_kind' : self.P_kind,
            'P_CAddress' : self.P_CAddress,
            'P_culture' : self.P_culture,
            'P_harvesting' : self.P_harvesting,
            'P_shipment' : self.P_shipment,
            'P_weight' : self.P_weight,
            'P_rating' : self.P_rating,
            'P_sc' : self.P_sc,
            'P_htn' : self.P_htn,
            'P_CRNumber' : self.P_CRNumber,
            'P_pesticide' : self.P_pesticide,
            'P_pusage' : self.P_pusage,
            'P_pshape' : self.P_pshape
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

            try :   self.P_name = Dict['P_name']
            except: print()

            try :   self.P_phone = Dict['P_phone']
            except: print()

            try :   self.P_address = Dict['P_address']
            except: print()

            try :   self.P_brand = Dict['P_brand']
            except: print()
            
            try :   self.P_goodsname = Dict['P_goodsname']
            except: print()

            try :   self.P_kind = Dict['P_kind']
            except: print()

            try :   self.P_CAddress = Dict['P_CAddress']
            except: print()

            try :   self.P_culture = Dict['P_culture']
            except: print()
            
            try :   self.P_harvesting = Dict['P_harvesting']
            except: print()
            
            try :   self.P_shipment = Dict['P_shipment']
            except: print()
            
            try :   self.P_weight = Dict['P_weight']
            except: print()
            
            try :   self.P_rating = Dict['P_rating']
            except: print()
            
            try :   self.P_sc = Dict['P_sc']
            except: print()
            
            try :   self.P_htn = Dict['P_htn']
            except: print()
            
            try :   self.P_CRNumber = Dict['P_CRNumber']
            except: print()

            try :   self.P_pesticide = Dict['P_pesticide']
            except: print()
            
            try :   self.P_pusage = Dict['P_pusage']
            except: print()
            
            try :   self.P_pshape = Dict['P_pshape']
            except: print()

        except:
            return False
        else:
            return True
        return False

#if __name__ == "__main__":
#    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
#    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

#    print(t1.toDict())

