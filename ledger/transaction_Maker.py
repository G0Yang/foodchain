import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256 import Hash256

class transaction:
    def __init__(self, From, To, 출고일 = "", 추적번호 = "",품목명 = "", 규격 = "", 출고수량 = "", 출고단가 = "", 출고금액 = "",재고수량 ="",재고단가="",재고금액=""):
        self.T_Header = "TH"
        self.T_Signature = "some Sign"
        self.CreatorIdentity = ""
        self.T_Endorsements = {}
        self.T_timestamp = time.time()
        self.출고일 = 출고일
        self.추적번호 = 추적번호
        self.품목명 = 품목명
        self.규격 = 규격
        self.출고수량 = 출고수량
        self.출고단가 = 출고단가
        self.출고금액 = 출고금액
        self.재고수량 = 재고수량
        self.재고단가 = 재고단가
        self.재고금액 = 재고금액
        self.String = From + "에서 " + To + "로 이동."
        self.T_Hash = Hash256.Hash256(self.String).getHash()

    def setCreatorIdentity(self, Object):
        self.CreatorIdentity = Object

    def appendEndorserIdentitiy(self, Object):
        self.T_Endorsements[Object.IP] = Object.name


class Endorser:
    def __init__(self, IP, name):
        self.IP = IP
        self.name = name
