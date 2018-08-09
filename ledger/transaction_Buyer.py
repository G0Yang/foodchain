import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from hash256 import Hash256

class transaction:
    def __init__(self, From, To, 배송일자 = "", 받는사람 = "", 전화번호 = "", 주소 = "", 제품명 = "", 수량 = "", 금액 = "", 배송비 = "", 비고 = ""):
        self.T_Header = "TH"
        self.T_Signature = "some Sign"
        self.CreatorIdentity = ""
        self.T_Endorsements = {}
        self.T_timestamp = time.time()
        self.배송일자 = 배송일자
        self.받는사람 = 받는사람
        self.전화번호 = 전화번호
        self.주소 = 주소
        self.제품명 = 제품명
        self.수량 = 수량
        self.금액 = 금액
        self.배송비 = 배송비  
        self.비고 = 비고
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
