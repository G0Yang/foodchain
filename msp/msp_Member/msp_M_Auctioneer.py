# This Python file uses the following encoding: utf-8

#경매자


class msp_Auctioneer:  
    def __init__(self, *args, **kwargs):


        self._id = ""             # 식별넘버 (Serial Number)
        self.ID = ""              # 회원 ID
        self.password = ""        # 회원 password
        self.type = "Auctioneer"            # 관리구분 생산/유통/판매 => p/P
        self.company = ""       # 소속기관
        #self.p_C_DetailArea       # 소속기관 주소
        #self.buisnessNum         # 사업자등록번호
        #self.CorporationNum      # 법인등록번호
        self.userName = ""
        self.userPhone = ""
        
        #self.p_Area = ""          # 지역, (우편번호)
        #self.p_DetailArea = ""    # 주소
        #self.p_Brand
        
        #self.faxNum = ""        # 팩스번호
        #self.item = ""          # 대표품목
        #self.prCert = 0          # private key
        #self.pbCert = 0          # publick key

        

        #

    def setAttribute(self, *args, **kwargs):
        try:
            self.ID = kwargs['ID']
            self.password = kwargs['password']
            self.company = kwargs['company']
            #self.p_C_DetailArea = kwargs['p_C_DetailArea']
            #self.buisnessNum = kwargs['buisnessNum']
            self.userName = kwargs['userName']
            self.userPhone = kwargs['userPhone']
            #self.p_Area = kwargs['p_Area']
            #self.p_DetailArea = kwargs['p_DetailArea']
            #self.p_Brand = kwargs['p_Brand']
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
            #'p_C_DetailArea' : self.p_C_DetailArea,
            #'buisnessNum' : self.buisnessNum
            'userName' : self.userName,
            'userPhone' : self.userPhone
            #'p_Area' : self.p_Area
            #'p_DetailArea' : self.p_DetailArea
            #'p_Brand' : self.p_Brand
            }
        return Dict
