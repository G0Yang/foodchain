# This Python file uses the following encoding: utf-8

import pymongo
from msp_Member.msp_CreateMember import createMember
import string
ipAddress = "localhost"
port = 27017

class interest:
    def __init__(self):
        conn = pymongo.MongoClient(ipAddress,port)      #"mongodb://user1:blockchain@"
        db = conn.get_database('msp_member')            #db = conn.msp_member

        self.collection = db.get_collection('interest') 
                                  

        self.ipv4 = []
        self.msList = {}
        self.tList = {} #
        
        self.aList = []
        self.dList = []
        self.pList = []
        self.sList = []
        self.wList = []

    def createInterest(self):
        iv = createMember()  #interestValidate
        
        while 1:
            count = 0
            interestCode = input("Code : ")
            if(self.interestValidCheck(InterestCode=interestCode)):
                print("코드중복 - 다시 입력하시오")
                
            else:
                while 1:
                    print("현재 "+str(count)+"명")
                    type = input("type( Auctioneer:a/A, Distributor:d/D, Producer:p/P, Seller:s/S:, Ware-House Manager:w/W (exit:'x'): ")
                    if(type == 'x'):
                        break
                    id = input("id : ")
                    userName = input("Name : ")
                    userPhone = input("Phone : ")
                    
                    if(type=='a' or type == 'A'):
                        if(iv.validCheck(type="Auctioneer", ID=id, userName=userName, userPhone=userPhone)):    # 회원이 있는지 체크
                            print("::확인::\n")
                            userIPv4 = iv.findDocument("userIPv4",ID=id,userName=userName)                      # 회원 ip 저장
                            self.tList[str(count)] =  {"type": "Auctioneer", "userName" : userName, "userPhone":userPhone, "userIPv4":userIPv4} 
                            self.ipv4.append(userIPv4)
                            self.aList.append(userName)
                            self.msList["Auctioneer"] = self.aList
                        else:
                            print("회원이 존재하지 않습니다.\n")
                            continue

                    elif(type=='d' or type == 'D'):
                        if(iv.validCheck(type="Distributor", ID=id, userName=userName, userPhone=userPhone)):
                            print("::확인::\n")
                            userIPv4 = iv.findDocument("userIPv4",ID=id,userName=userName)
                            self.tList[str(count)] =  {"type": "Distributor","userName" : userName, "userPhone":userPhone, "userIPv4":userIPv4}
                            self.ipv4.append(userIPv4)
                            self.dList.append(userName)
                            self.msList["Distributor"] = self.dList

                        else:
                            print("회원이 존재하지 않습니다.\n")
                            continue
                        
                    elif(type=='p' or type == 'P'):
                        if(iv.validCheck(type="Producer", ID=id, userName=userName, userPhone=userPhone)):
                            print("::확인::\n")
                            userIPv4 = iv.findDocument("userIPv4",ID=id,userName=userName)
                            self.tList[str(count)] =  {"type": "Producer","userName" : userName, "userPhone":userPhone, "userIPv4":userIPv4}
                            self.ipv4.append(userIPv4)
                            self.pList.append(userName)
                            self.msList["Producer"] = self.pList

                        else:
                            print("회원이 존재하지 않습니다.\n")
                            continue
                        
                    elif(type=='s' or type == 'S'):
                        if(iv.validCheck(type="Seller", ID=id, userName=userName, userPhone=userPhone)):
                            print("::확인::\n")
                            userIPv4 = iv.findDocument("userIPv4",ID=id,userName=userName)
                            self.tList[str(count)] =  {"type": "Seller","userName" : userName, "userPhone":userPhone, "userIPv4":userIPv4}
                            self.ipv4.append(userIPv4)
                            self.sList.append(userName)
                            self.msList["Seller"] = self.sList

                        else:
                            print("회원이 존재하지 않습니다.\n")
                            continue

                    elif(type=='w' or type == 'W'):
                        if(iv.validCheck(type="WManager", ID=id, userName=userName, userPhone=userPhone)):
                            print("::확인::\n")
                            self.tList[str(count)] =  {"type": "WManager","userName" : userName, "userPhone":userPhone, "userIPv4":userIPv4}
                            self.ipv4.append(userIPv4)
                            self.wList.append(userName)
                            self.msList["WManager"] = self.wList

                        else:
                            print("회원이 존재하지 않습니다.\n")
                            continue

                    
                    count+=1
                    
                    if(count>=3):
                        qus = input("더 입력하시겠습니까?(y/n) :")
                        if(qus == 'y'):
                            continue
                        elif(qus == 'n'):
                            print(self.tList)
                            print(self.msList)
                            print(self.ipv4)
                            self.collection.insert_one({"InterestCode":interestCode, "Members" : self.msList, "NumOfPeople": count, "Memberinfo" : self.tList, "MembersIPv4": self.ipv4 }) #
                            break
                        else:
                            print("error")
                            break
            
    def interestValidCheck(self, **kwargs):                     #이해관계DB 중복체크 
        for member in self.collection.find(kwargs):
            return True
        return False

    
      
    def collectInterestIPv4(self,interestCode):                 #회원 수와 ip주소 반환 

        for interest in self.collection.find({"InterestCode":interestCode}):
            return interest["MembersIPv4"]
        return 'False'





if __name__ == "__main__":
    i = interest()
  
    #i.createInterest()
    print(i.collectInterestIPv4("02"))
    #print(m1.memberDict())
