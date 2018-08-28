# This Python file uses the following encoding: utf-8

class msp_Producer:
    def __init__(self, *args, **kwargs):


        self._id = ""             # 식별넘버 (Serial Number)
        self.ID = ""              # 회원 ID
        self.password = ""        # 회원 password
        self.type = "Producer"            # 관리구분 생산/유통/판매 => p/P
        self.company = ""       # 소속기관
        self.c_Address = ""     # 소속기관 주소
        self.c_Phone = ""       # 소속기관 번호
        self.buisnessNum = ""     # 사업자등록번호
        #self.CorporationNum      # 법인등록번호
        self.userName = ""
        self.userPhone = ""
        
        self.userArea = ""          # 지역, (우편번호)
        #self.p_Address = ""    # 주소
        self.userBrand = ""
        self.userIPv4 = ""
        #self.faxNum = ""        # 팩스번호
        #self.item = ""          # 대표품목
        #self.prCert = 0          # private key
        #self.pbCert = 0          # publick key

        

        #

    def setAttribute(self, *args, **kwargs):
        try:
            self.ID = kwargs['ID']
            self.password = kwargs['password']
            #self.type = kwargs['type']
            self.company = kwargs['company']
            self.c_Address = kwargs['c_Address']
            self.c_Phone = kwargs['c_Phone']
            self.buisnessNum = kwargs['buisnessNum']
            self.userName = kwargs['userName']
            self.userPhone = kwargs['userPhone']
            self.userArea = kwargs['userArea']
            self.userAddress = kwargs['userAddress']
            self.brand = kwargs['brand']
            #self.company = kwargs['company']
            #
            #
            #
            print("success")
        except:
            print("error")

        return False

    def memberDict(self):
        Dict = {
            #'_id' : self._id,
            'ID' : self.ID,
            'password' : self.password,
            'type' : self.type,
            'company' : self.company,
            'c_Address' : self.c_Address,
            'c_Phone' : self.c_Phone,
            'buisnessNum' : self.buisnessNum,
            'userName' : self.userName,
            'userPhone' : self.userPhone,
            'userArea' : self.userArea,
            'userAddress' : self.userAddress,
            'brand' : self.brand,
            'userIPv4' : self.userIPv4
            }
        return Dict
