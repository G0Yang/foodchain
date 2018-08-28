# This Python file uses the following encoding: utf-8

from msp_Member.msp_M_Auctioneer import msp_Auctioneer
from msp_Member.msp_M_Distributor import msp_Distributor
from msp_Member.msp_M_Producer import msp_Producer
from msp_Member.msp_M_Seller import msp_Seller
from msp_Member.msp_M_Ware_House_Manager import msp_WManager
import pymongo

ipAddress = "202.31.146.50"
port = 27017
conn = pymongo.MongoClient(ipAddress,port) #"mongodb://user1:blockchain@"

db = conn.get_database('msp_member') #db = conn.msp_member
collection = db.get_collection('member') #members = db.member

class createMember:
    def createMember(self):
        
        print("add Member")
        
        _id = ""
        id = input('id : ')
        if(self.validCheck(ID=id)):
            print("ID중복")
            return
        
        password = input('password : ')
        type = input("type( Auctioneer:a/A, Distributor:d/D, Producer:p/P, Seller:s/S:, Ware-House Manager:w/W : ")

        if(type == 'p' or type == 'P'):
            company =input("Company Name: ")
            c_Address =input("Company Adress: ")
            c_Phone =input("Company PhoneNumber: ")
            buisnessNum =input("buisnessNum: ")
            userName =input("Producer Name: ")
            userPhone =input("Producer Phone: ")
            userArea =input("Producer Area: ")
            userAddress =input("Producer Address: ")
            brand =input("Brand: ")
            cm = msp_Producer()
            cm.setAttribute(ID = id, password = password, type = "Producer", company = company, c_Address = c_Address, c_Phone = c_Phone,  buisnessNum = buisnessNum, userName = userName, userPhone = userPhone, userArea = userArea, userAddress = userAddress, brand = brand) 

        elif(type == 'd' or type == 'D'):
            company =input("Company Name: ")
            #p_C_Address =input("Company Adress: ")
            #p_C_Phone =input("Company PhoneNumber: ")
            #buisnessNum =input("buisnessNum: ")
            userName =input("Distributor Name: ")
            userPhone =input("Distributor Phone: ")
            vehicleNum =input("Vehicle Number: ")
            #p_Area =input("Distributor Area: ")
            #p_Address =input("Distributor Address: ")
            cm = msp_Distributor()
            cm.setAttribute(ID = id, password = password, type = "Distributor", company = company, userName = userName, userPhone = userPhone, vehicleNum = vehicleNum) 

        elif(type == 'a' or type == 'A'):
            company =input("Company Name: ")
            #p_C_Address =input("Company Adress: ")
            #p_C_Phone =input("Company PhoneNumber: ")
            #buisnessNum =input("buisnessNum: ")
            userName =input("Auctioneer Name: ")
            userPhone =input("Auctioneer Phone: ")
            #p_Area =input("Auctioneer Area: ")
            #p_Address =input("Auctioneer Address: ")p_Brand =input("Brand: ")
            cm = msp_Auctioneer()
            cm.setAttribute(ID = id, password = password, type = "Auctioneer", company = company, userName = userName, userPhone = userPhone) 

        elif(type == 'w' or type == 'W'):
            company =input("Company Name: ")
            #p_C_Address =input("Company Adress: ")
            #p_C_Phone =input("Company PhoneNumber: ")
            #buisnessNum =input("buisnessNum: ")
            userName =input("WManager Name: ")
            userPhone =input("WManager Phone: ")
            #p_Area =input("Producer Area: ")
            #p_Address =input("Producer Address: ")p_Brand =input("Brand: ")
            cm = msp_WManager()
            cm.setAttribute(ID = id, password = password, type = "WManager", company = company, userName = userName, userPhone = userPhone) 

        elif(type == 's' or type == 'S'):
            company =input("Company Name: ")
            #s_C_Address =input("Company Adress: ")
            #s_C_Phone =input("Company PhoneNumber: ")
            #buisnessNum =input("buisnessNum: ")
            userName =input("Seller Name: ")
            userPhone =input("Seller Phone: ")
            #p_Area =input("Producer Area: ")
            #p_Address =input("Producer Address: ")
            #p_Brand =input("Brand: ")
            cm = msp_Seller()
            cm.setAttribute(ID = id, password = password, type = "Seller", company = company, userName = userName, userPhone = userPhone) 
        
        
        collection.insert_one(cm.memberDict())

    
    def validCheck(self, **kwargs):
        for member in collection.find(kwargs):
            return True
        return False


    def viewMembers(self):
        for members in collection.find():
            print(members)
            
    def findDocument(self, *args, **kwargs):
        for member in collection.find(kwargs):
            return (member[args[0]])
        
    def viewMember(self, element, *args): # 검색할 key/ value
        for member in collection.find({element:args[0]}): #,{'_id':1}
            print(member)
            # print(member['_id']) # _id 출력
        
        #print(collection.find({element:text})['_id'])

    def deleteMember(self,element, key):
        collection.delete_one({element:key})
        print("success")


if __name__ == "__main__":
    r = createMember()
    r.createMember()
