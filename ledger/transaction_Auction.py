# This Python file uses the following encoding: utf-8

# 감독기관 \ 서류명 에 의해 작성 됨.
# 법률 근거 0000 에 의해서 최소 정보 [  ] 가 산출 됨.


import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256.hash256 import *

class transaction_Auction:
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

        # -- 경매 트랜잭션 항목 --
        self.A_goodsname = "" # 상품 이름
        self.A_grade = "" # 상품 등급
        self.A_groupname = "" # 단체 이름
        self.A_CRNumber = "" # 사업자등록번호
        self.A_managername = "" # 담당자 이름
        self.A_managerphone = "" # 담장자 전화
        self.A_date = "" # 경매날짜
        self.A_price = "" # 낙찰금액

        
        try:
            try :   self.endorsers[str(len(self.endorsers))] = kwargs['검증'] 
            except: print("검증 error")
            
            try :   self.sign[str(len(self.sign))] = kwargs['사인'] 
            except: print("사인 error")
            
            try :   self.creatorID = kwargs['서명']
            except: print("서명 error")

            try :   self.A_goodsname = kwargs['상품이름'] 
            except: print("이름 error")

            try :   self.A_grade = kwargs['상품등급'] 
            except: print("등급 error")

            try :   self.A_groupname = kwargs['단체이름'] 
            except: print("단체 이름 error")
            
            try :   self.A_CRNumber = kwargs['사업자등록번호'] 
            except: print("사업자등록번호 error")

            try :   self.A_managername = kwargs['담당자이름'] 
            except: print("담당자 이름 error")

            try :   self.A_managerphone = kwargs['담장자전화'] 
            except: print("담장자 전화 error")

            try :   self.A_date = kwargs['경매날짜'] 
            except: print("경매날짜 error")

            try :   self.A_price = kwargs['낙찰금액'] 
            except: print("낙찰금액 error")

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

            try :   self.A_goodsname = kwargs['상품이름'] 
            except: print("이름 error")

            try :   self.A_grade = kwargs['상품등급'] 
            except: print("등급 error")

            try :   self.A_groupname = kwargs['단체이름'] 
            except: print("단체 이름 error")
            
            try :   self.A_CRNumber = kwargs['사업자등록번호'] 
            except: print("사업자등록번호 error")

            try :   self.A_managername = kwargs['담당자이름'] 
            except: print("담당자 이름 error")

            try :   self.A_managerphone = kwargs['담장자전화'] 
            except: print("담장자 전화 error")

            try :   self.A_date = kwargs['경매날짜'] 
            except: print("경매날짜 error")

            try :   self.A_price = kwargs['낙찰금액'] 
            except: print("낙찰금액 error")

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

            'P_name' : self.P_name,
            'P_grade' : self.P_grade,

            'A_groupname' : self.A_groupname,
            'A_CRNumber' : self.A_CRNumber,
            'A_managername' : self.A_managername,
            'A_managerphone' : self.A_managerphone,
            'A_date' : self.A_date,
            'A_price' : self.A_price
            }
        return Dict

if __name__ == "__main__":
    t1 = transaction(상품이름='딸기', 검증={'IP':'202.31.146.57'}) # 초기 생성
    t1.setAttribute(전화번호 = "010-1234-5678") # 변경부분, 추가부분 입력

    print(t1.toDict())
