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

        # -- 차량 출고 트랜잭션 항목 --
        self.vs_groupname = "" # 단체이름
        self.vs_managername = "" # 담당자이름
        self.vs_managerphone = "" # 담당자전화번호
        self.vs_date = "" # 출고날짜
        self.vs_destinationName = "" # 출하지이름
        self.vs_destinationAddress = "" # 출하지주소
        self.vs_goodsname = "" # 상품이름
        self.vs_quantity = "" # 수량(Box)
        self.vs_weight = "" # 무게(Box당 kg)
        self.vs_temperature = "" # 온도
        self.vs_vn = "" # 출고차량번호
        self.vs_vo = "" # 출고차량운전자
        self.vs_vop = "" # 출고차량운전자전화번호

        
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")
            
            try :   self.vs_groupname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.vs_managername = kwargs['담당자이름']
            except: print("담당자이름 error")
            
            try :   self.vs_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")
            
            try :   self.vs_date = kwargs['출고날짜']
            except: print("출고날짜 error")
            
            try :   self.vs_destinationName = kwargs['출하지이름']
            except: print("출하지이름 error")
            
            try :   self.vs_destinationAddress = kwargs['출하지주소']
            except: print("출하지주소 error")

            try :   self.vs_goodsname = kwargs['상품이름']
            except: print("상품이름 error")
            
            try :   self.vs_quantity = kwargs['수량']
            except: print("수량 error")
            
            try :   self.vs_weight = kwargs['무게']
            except: print("무게 error")
            
            try :   self.vs_temperature = kwargs['온도']
            except: print("온도 error")
            
            try :   self.vs_vn = kwargs['출고차량번호']
            except: print("출고차량번호 error")
            
            try :   self.vs_vo = kwargs['출고차량운전자']
            except: print("출고차량운전자 error")
            
            try :   self.vs_vop = kwargs['출고차량운전자전화번호']
            except: print("출고차량운전자전화번호 error")

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
            
            try :   self.vs_groupname = kwargs['단체이름']
            except: print("단체이름 error")
            
            try :   self.vs_managername = kwargs['담당자이름']
            except: print("담당자이름 error")
            
            try :   self.vs_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")
            
            try :   self.vs_date = kwargs['출고날짜']
            except: print("출고날짜 error")
            
            try :   self.vs_destinationName = kwargs['출하지이름']
            except: print("출하지이름 error")
            
            try :   self.vs_destinationAddress = kwargs['출하지주소']
            except: print("출하지주소 error")

            try :   self.vs_goodsname = kwargs['상품이름']
            except: print("상품이름 error")
            
            try :   self.vs_quantity = kwargs['수량']
            except: print("수량 error")
            
            try :   self.vs_weight = kwargs['무게']
            except: print("무게 error")
            
            try :   self.vs_temperature = kwargs['온도']
            except: print("온도 error")
            
            try :   self.vs_vn = kwargs['출고차량번호']
            except: print("출고차량번호 error")
            
            try :   self.vs_vo = kwargs['출고차량운전자']
            except: print("출고차량운전자 error")
            
            try :   self.vs_vop = kwargs['출고차량운전자전화번호']
            except: print("출고차량운전자전화번호 error")

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

            'vs_groupname' : self.vs_groupname,
            'vs_managername' : self.vs_managername,
            'vs_managerphone' : self.vs_managerphone,
            'vs_date' : self.vs_date,
            'vs_destinationName' : self.vs_destinationName,
            'vs_destinationAddress' : self.vs_destinationAddress,
            'vs_goodsname' : self.vs_goodsname,
            'vs_quantity' : self.vs_quantity,
            'vs_weight' : self.vs_weight,
            'vs_temperature' : self.vs_temperature,
            'vs_vn' : self.vs_vn,
            'vs_vo' : self.vs_vo,
            'vs_vop' : self.vs_vop
            }
        return Dict

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
