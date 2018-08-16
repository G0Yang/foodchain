import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256.hash256 import *

class transaction:
    def __init__(self, *args, **kwargs):
        #-- 고정 트랜잭션 항목 --
        # 제안서 부분
        self.TXID = ""
        self.timestamp = time.time()
        self.verstion = 0.2
        self.creatorID = {} # 트랜잭션 생성자 서명
        self.TXType = "" # 트랜잭션 분류
        self.timeout = 0
        self.T_hash = "" # 현재 트랜잭션 해시

        # 검증 부분
        self.endorsers = {}
        self.sign = {}
        self.produce = {}

        # -- 토마토 트랜잭션 항목 --
        self.O_name = "" # 생산자(단체)이름
        self.O_phone = "" # 생산자(단체)전화번호
        self.O_address = "" # 생산자(단체)주소
        self.O_brand = "" # 브랜드
        self.O_goodsname = "" # 상품이름(재배품목명)
        self.O_kind = "" # 재배품종명
        self.O_CAddress = "" # Culture Address
        self.O_culture = "" # 재배작형
        self.O_harvesting = "" # 수확날짜
        self.O_shipment = "" # 출하날짜
        self.O_weight = "" # 무게
        self.O_rating = "" # 등급
        self.O_htn = "" # 이력추적관리번호
        self.O_pesticide = "" # 농약제품명
        self.O_pusage = "" # 농약용도
        self.O_pshape = "" # 농약형태

        
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.O_name = kwargs['생산자이름'] 
            except: print("생산자(단체)이름 error")

            try :   self.O_phone = kwargs['생산자전화번호'] 
            except: print("생산자(단체)전화번호 error")

            try :   self.O_address1 = kwargs['생산자주소'] 
            except: print("생산자(단체)주소 error")

            try :   self.O_brand = kwargs['브랜드'] 
            except: print("브랜드 error")
            
            try :   self.O_goodsname = kwargs['상품이름'] 
            except: print("상품이름 error")

            try :   self.O_kind = kwargs['재배품종'] 
            except: print("재배품종 error")

            try :   self.O_CAddress = kwargs['재배지주소'] 
            except: print("재배지주소 error")

            try :   self.O_culture = kwargs['재배작형'] 
            except: print("재배작형 error")
            
            try :   self.O_harvesting = kwargs['수확날짜'] 
            except: print("수확날짜 error")
            
            try :   self.O_shipment = kwargs['출하날짜'] 
            except: print("출하날짜 error")
            
            try :   self.O_weight = kwargs['무게'] 
            except: print("무게 error")
            
            try :   self.O_rating = kwargs['등급'] 
            except: print("등급 error")
            
            try :   self.O_htn = kwargs['이력추적관리번호'] 
            except: print("이력추적관리번호 error")

            try :   self.O_pesticide = kwargs['농약제품명'] 
            except: print("농약제품명 error")
            
            try :   self.O_pusage = kwargs['농약용도'] 
            except: print("농약용도 error")
            
            try :   self.O_pshape = kwargs['농약형태'] 
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
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.O_name = kwargs['생산자이름'] 
            except: print("생산자(단체)이름 error")

            try :   self.O_phone = kwargs['생산자전화번호'] 
            except: print("생산자(단체)전화번호 error")

            try :   self.O_address1 = kwargs['생산자주소'] 
            except: print("생산자(단체)주소 error")

            try :   self.O_brand = kwargs['브랜드'] 
            except: print("브랜드 error")
            
            try :   self.O_goodsname = kwargs['상품이름'] 
            except: print("상품이름 error")

            try :   self.O_kind = kwargs['재배품종'] 
            except: print("재배품종 error")

            try :   self.O_CAddress = kwargs['재배지주소'] 
            except: print("재배지주소 error")

            try :   self.O_culture = kwargs['재배작형'] 
            except: print("재배작형 error")
            
            try :   self.O_harvesting = kwargs['수확날짜'] 
            except: print("수확날짜 error")
            
            try :   self.O_shipment = kwargs['출하날짜'] 
            except: print("출하날짜 error")
            
            try :   self.O_weight = kwargs['무게'] 
            except: print("무게 error")
            
            try :   self.O_rating = kwargs['등급'] 
            except: print("등급 error")
            
            try :   self.O_htn = kwargs['이력추적관리번호'] 
            except: print("이력추적관리번호 error")

            try :   self.O_pesticide = kwargs['농약제품명'] 
            except: print("농약제품명 error")
            
            try :   self.O_pusage = kwargs['농약용도'] 
            except: print("농약용도 error")
            
            try :   self.O_pshape = kwargs['농약형태'] 
            except: print("농약형태 error")

            self.T_hash = hash256(str(self.toDict())).getHash()

        except:
            print("error")
        else:
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

            'To_name1' : self.To_name1,
            'To_phone' : self.To_phone,
            'To_address1' : self.To_address1,
            'To_name2' : self.To_name2,
            'To_name3' : self.To_name3,
            'To_kind' : self.To_kind,
            'To_address2' : self.To_address2,
            'To_culture' : self.To_culture,
            'To_harvesting' : self.To_harvesting,
            'To_shipment' : self.To_shipment,
            'To_weight' : self.To_weight,
            'To_rating' : self.To_rating,
            'To_htn' : self.To_htn,
            'To_pesticide' : self.To_pesticide,
            'To_pusage' : self.To_pusage,
            'To_pshape' : self.To_pshape
            }
        return Dict

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())