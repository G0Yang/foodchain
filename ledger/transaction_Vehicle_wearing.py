# This Python file uses the following encoding: utf-8
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

        # -- 차량 입고 트랜잭션 항목 --
        self.vw_gropsname = "" # 단체이름
        self.vw_managername = "" # 담당자이름
        self.vw_managerphone = "" # 담당자전화번호
        self.vw_date = "" # 입고날짜
        self.vw_origiName = "" # 입고한생산자(단체)이름
        self.vw_originAddress = "" # 입고한생산자(단체)주소
        self.vw_goodsname = "" # 상품이름
        self.vw_quantity = "" # 수량
        self.vw_weight = "" # 무게
        self.vw_temperature = "" # 온도
        self.vw_vn = "" # 입고차량번호
        self.vw_vo = "" # 입고차량운전자
        self.vw_vop = "" # 입고차량운전자전화번호

        
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")
            
            try :   self.vw_gropsname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.vw_managername = kwargs['담당자이름']
            except: print("담당자이름 error")
            
            try :   self.vw_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")
            
            try :   self.vw_date = kwargs['입고날짜']
            except: print("입고날짜 error")
            
            try :   self.vw_origiName = kwargs['입고한생산자(단체)이름']
            except: print("서명 error")
            
            try :   self.vw_originAddress = kwargs['입고한생산자(단체)주소']
            except: print("서명 error")

            try :   self.vw_goodsname = kwargs['상품이름']
            except: print("상품이름 error")
            
            try :   self.vw_quantity = kwargs['수량']
            except: print("서명 error")
            
            try :   self.vw_weight = kwargs['무게']
            except: print("서명 error")
            
            try :   self.vw_temperature = kwargs['온도']
            except: print("서명 error")
            
            try :   self.vw_vn = kwargs['입고차량번호']
            except: print("서명 error")
            
            try :   self.vw_vo = kwargs['입고차량운전자']
            except: print("서명 error")
            
            try :   self.vw_vop = kwargs['입고차량운전자전화번호']
            except: print("서명 error")

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
            
            try :   self.vw_gropsname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.vw_managername = kwargs['담당자이름']
            except: print("담당자이름 error")
            
            try :   self.vw_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")
            
            try :   self.vw_date = kwargs['입고날짜']
            except: print("입고날짜 error")
            
            try :   self.vw_origiName = kwargs['입고한생산자(단체)이름']
            except: print("서명 error")
            
            try :   self.vw_originAddress = kwargs['입고한생산자(단체)주소']
            except: print("서명 error")

            try :   self.vw_goodsname = kwargs['상품이름']
            except: print("상품이름 error")
            
            try :   self.vw_quantity = kwargs['수량']
            except: print("서명 error")
            
            try :   self.vw_weight = kwargs['무게']
            except: print("서명 error")
            
            try :   self.vw_temperature = kwargs['온도']
            except: print("서명 error")
            
            try :   self.vw_vn = kwargs['입고차량번호']
            except: print("서명 error")
            
            try :   self.vw_vo = kwargs['입고차량운전자']
            except: print("서명 error")
            
            try :   self.vw_vop = kwargs['입고차량운전자전화번호']
            except: print("서명 error")

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

            'vw_gropsname' : self.vw_gropsname,
            'vw_managername' : self.vw_managername,
            'vw_managerphone' : self.vw_managerphone,
            'vw_date' : self.vw_date,
            'vw_origiName' : self.vw_origiName,
            'vw_originAddress' : self.vw_originAddress,
            'vw_goodsname' : self.vw_goodsname,
            'vw_quantity' : self.vw_quantity,
            'vw_weight' : self.vw_weight,
            'vw_temperature' : self.vw_temperature,
            'vw_vn' : self.vw_vn,
            'vw_vo' : self.vw_vo,
            'vw_vop' : self.vw_vop
            }
        return Dict

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
