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

        # -- 재고관리 트랜잭션 항목 --
        self.IM_groupname = "" # 단체이름

        self.IM_managername = "" # 담당자이름
        self.IM_managerphone = "" # 담당자전화번호

        self.IM_wn = "" # 창고번호
        self.IM_zn = "" # 구역번호
        self.IM_date = "" # 재고확인날짜
        self.IM_time = "" # 재고확인시간

        self.IM_goodsname = "" # 상품이름
        self.IM_quantity = "" # 수량(Box)
        self.IM_weight = "" # 무게(Box당kg)


        
        try:            
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")

            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.IM_groupname = kwargs['단체이름']
            except: print("단체이름 error")

            try :   self.IM_managername = kwargs['담당자이름']
            except: print("담당자이름 error")

            try :   self.IM_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")

            try :   self.IM_wn = kwargs['창고번호']
            except: print("창고번호 error")

            try :   self.IM_zn = kwargs['구역번호']
            except: print("창고번호 error")

            try :   self.IM_date = kwargs['재고확인날짜']
            except: print("재고확인날짜 error")

            try :   self.IM_time = kwargs['재고확인시간']
            except: print("재고확인시간 error")

            try :   self.IM_goodsname = kwargs['상품이름']
            except: print("상품이름 error")

            try :   self.IM_quantity = kwargs['수량']
            except: print("수량 error")

            try :   self.IM_weight = kwargs['무게']
            except: print("무게 error")

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

            try :   self.IM_groupname = kwargs['단체이름']
            except: print("단체이름 error")

            try :   self.IM_managername = kwargs['담당자이름']
            except: print("담당자이름 error")

            try :   self.IM_managerphone = kwargs['담당자전화번호']
            except: print("담당자전화번호 error")

            try :   self.IM_wn = kwargs['창고번호']
            except: print("창고번호 error")

            try :   self.IM_zn = kwargs['구역번호']
            except: print("창고번호 error")

            try :   self.IM_date = kwargs['재고확인날짜']
            except: print("재고확인날짜 error")

            try :   self.IM_time = kwargs['재고확인시간']
            except: print("재고확인시간 error")

            try :   self.IM_goodsname = kwargs['상품이름']
            except: print("상품이름 error")

            try :   self.IM_quantity = kwargs['수량']
            except: print("수량 error")

            try :   self.IM_weight = kwargs['무게']
            except: print("무게 error")

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

            'IM_groupname' : self.IM_groupname,
            'IM_managername' : self.IM_managername,
            'IM_managerphone' : self.IM_managerphone,
            'IM_wn' : self.IM_wn,
            'IM_zn' : self.IM_zn,
            'IM_date' : self.IM_date,
            'IM_time' : self.IM_time,
            'IM_goodsname' : self.IM_goodsname,
            'IM_quantity' : self.IM_quantity,
            'IM_weight' : self.IM_weight
            }
        return Dict

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(담당자전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
