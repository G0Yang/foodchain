# This Python file uses the following encoding: utf-8

import sys, os, json, pathlib
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger import transaction
from chaincode import transactionToJson



class msp:
    def __init__(self):
        self.perm = {'E':'endorser', 'P':'peer', 'C':'commiter', 'O':'orderer', 'L':'leader', "M" : "maker", "D" : "Distributor", "S" : "seller"}

    def getJson(self):
        self.data = {}

        return self.data

    def addMember(self, Object):
        self.data

    def getpermmission(self, PW, ID):
        if ID == "1" and PW == "1":
            return self.perm['M']
        elif ID == "2" and PW == "2":
            return self.perm['L']
        elif ID == "3" and PW == "3":
            return self.perm['C']
        elif ID == "4" and PW == "4":
            return self.perm['O']
        elif ID == "5" and PW == "5":
            return self.perm['P']
        elif ID == "6" and PW == "6":
            return self.perm['E']
        elif ID == "7" and PW == "7":
            return self.perm['D']
        elif ID == "8" and PW == "8":
            return self.perm['S']
        return "F"


class member:
    def __init__(self, IP, name):
        self.data={
          "IP" : IP,
          "name" : name
        }
        return self.data


    
if __name__ == "__main__1":
    t1 = transaction.transaction("A", "B")
    print(t1)
    t1.appendEndorserIdentitiy(endorser.Endorser("202.31.146.1", "Kim"))
    print(t1.T_Endorsements)
    t1.appendEndorserIdentitiy(endorser.Endorser("202.31.146.2", "Park"))
    print(t1.T_Endorsements)
    t1.appendEndorserIdentitiy(endorser.Endorser("202.31.146.3", "Lee"))
    print(t1.T_Endorsements)


    



#b1 = transaction.transaction("A", "B")
#BJ = blockToJson(b1)
#BH = transactionToJson.transactionToJson(b1).getData()

#j1 = json.dumps(BH)

#print(json.dumps(BH))
#print()
#print()
#print()
#print()

#file = pathlib.Path('example.json')
#file.write_text(dict_to_json(BH, data_to_json), encoding='utf-8')

#file = pathlib.Path('example.json')
#file_text = file.read_text(encoding='utf-8')
#json_data = json.loads(file_text)

#print(json_data, type(json_data))
#print(file_text, type(file_text))
