# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256.hash256 import *

class transaction_Seller:
    def __init__(self, *args, **kwargs):
        #-- 고정 트랜잭션 항목 --
        # 제안서 부분
        self.TXID = ""
        self.timestamp = time.time()
        self.verstion = 0.2
        self.creatorID = {} # 트랜잭션 생성자 서명
        self.TXType = "Seller" # 트랜잭션 분류
        self.timeout = 0
        self.T_hash = "" # 현재 트랜잭션 해시

        # 검증 부분
        self.endorsers = {}
        self.sign = {}
        self.produce = {}

        # -- 판매 트랜잭션 항목 --
        self.S_groupname = "" # 단체이름
        self.S_CRNumber = "" # 사업자등록번호
        self.S_managername = "" # 담당자이름
        self.S_managerphone = "" # 담당자전화번호

        self.S_goodsname = "" # 상품이름
        self.S_htnumber = "" # 이력추적 관리번호
        self.S_weight = "" # 상품무게

        self.S_date = "" # 판매날짜
        self.S_price = "" # 판매가격

        self.S_buyername = "" # 구매자이름
        self.S_buyerphone = "" # 구매자전화번호


        
        try:            
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")

            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.S_groupname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.S_CRNumber = kwargs['사업자등록번호']
            except: print("사업자등록번호 error")

            try :   self.S_managername = kwargs['담당자이름']
            except: print("담당자이름 error")

            try :   self.S_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")

            try :   self.S_goodsname = kwargs['상품이름']
            except: print("상품이름 error")

            try :   self.S_htnumber = kwargs['이력추적관리번호']
            except: print("이력추적 관리번호 error")

            try :   self.S_weight = kwargs['상품무게']
            except: print("상품 무게 error")

            try :   self.S_date = kwargs['판매날짜']
            except: print("판매날짜 error")

            try :   self.S_price = kwargs['판매가격']
            except: print("판매가격 error")

            try :   self.S_buyername = kwargs['구매자이름']
            except: print("구매자이름 error")

            try :   self.S_buyerphone = kwargs['구매자전화번호']
            except: print("구매자전화번호 error")

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

            try :   self.S_groupname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.S_CRNumber = kwargs['사업자등록번호']
            except: print("사업자등록번호 error")

            try :   self.S_managername = kwargs['담당자이름']
            except: print("담당자이름 error")

            try :   self.S_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")

            try :   self.S_goodsname = kwargs['상품이름']
            except: print("상품이름 error")

            try :   self.S_htnumber = kwargs['이력추적관리번호']
            except: print("이력추적 관리번호 error")

            try :   self.S_weight = kwargs['상품무게']
            except: print("상품 무게 error")

            try :   self.S_date = kwargs['판매날짜']
            except: print("판매날짜 error")

            try :   self.S_price = kwargs['판매가격']
            except: print("판매가격 error")

            try :   self.S_buyername = kwargs['구매자이름']
            except: print("구매자이름 error")

            try :   self.S_buyerphone = kwargs['구매자전화번호']
            except: print("구매자전화번호 error")

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

            'S_groupname' : self.S_groupname,
            'S_CRNumber' : self.S_CRNumber,
            'S_managername' : self.S_managername,
            'S_managerphone' : self.S_managerphone,
            'S_goodsname' : self.S_goodsname,
            'S_htnumber' : self.S_htnumber,
            'S_weight' : self.S_weight,
            'S_date' : self.S_date,
            'S_price' : self.S_price,
            'S_buyername' : self.S_buyername,
            'S_buyerphone' : self.S_buyerphone

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

            try :   self.S_groupname = Dict['S_groupname']
            except: print()

            try :   self.S_CRNumber = Dict['S_CRNumber']
            except: print()

            try :   self.S_managername = Dict['S_managername']
            except: print()

            try :   self.S_managerphone = Dict['S_managerphone']
            except: print()
            
            try :   self.S_goodsname = Dict['S_goodsname']
            except: print()

            try :   self.S_htnumber = Dict['S_htnumber']
            except: print()

            try :   self.S_weight = Dict['S_weight']
            except: print()

            try :   self.S_date = Dict['S_date']
            except: print()
            
            try :   self.S_price = Dict['S_price']
            except: print()
            
            try :   self.S_buyername = Dict['S_buyername']
            except: print()
            
            try :   self.S_buyerphone = Dict['S_buyerphone']
            except: print()
            
        except:
            return False
        else:
            return True
        return False

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(담당자전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
