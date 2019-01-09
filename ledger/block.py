# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.transaction import transaction, libhash

from ledger.blockheader import *
from chaincode.randFileName import *

class block:
    def __init__(self, *args, **kwargs):
        self.transactionCount = 0
        self.blocksize = 0
        self.blockID=""
        self.BH = blockheader()
        self.BB = []
        if "blockID" in kwargs:
            self.blockID = kwargs['blockID']
            self.fromJson()
        try: 
            tx = None
            if args:
                tx = args[0]

            if str(type(tx)) == "<class 'ledger.transaction.transaction'>":
                self.BB.append(tx)
                self.BH.setCurrentHash(libhash(str(tx.toDict())).getsha256())
                self.transactionCount = self.transactionCount + 1
                self.BB[0].txCount = self.transactionCount
                sizeof = str(self.toDict())
                self.blocksize = len(sizeof)
                self.blockID = randFileName()[0:-5]
            
        except:
            print("block_init Error")
        return
        
    def append(self, Object):
        try: 
            if str(type(Object)) == "<class 'ledger.transaction.transaction'>":
                self.BB.append(Object)
                self.transactionCount = self.transactionCount + 1
                self.BB[-1].txCount = self.transactionCount
                self.blocksize = len(str(self.toDict()))
                self.BH.setCurrentHash(libhash(str(Object.toDict())).getsha256())
            else:
                return False
        except Exception as e:
            print(e)
            return False

        return True

    def setCurrentBlockHash():
        string = ""
        try:
            for i in self.BB:
                string = string + i.getHash()
            self.BH.currentBlockHash = libhash(str(i.toDict())).getsha256()
        except:
            return False
        else:
            return True
        return False

    def setPreviousHash(self, string):
        if self.BH.setPreviousHash(string): return True
        else: return False
        return False

    def toDict(self):
        Dict = {
            'blockID' : self.blockID,
            'transactionCount' : self.transactionCount,
            'blocksize' : self.blocksize,
            'blockheader' : self.BH.toDict()
            }
        txList = []
        for i in self.BB:
            txList.append(i.toDict())
        Dict["blockbody"] = txList
        return Dict

    def fromDict(self, Dict):
        try:
            if 'blockID' in Dict:
                self.blockID = Dict['blockID']
            if 'transactionCount' in Dict:
                self.transactionCount = Dict['transactionCount']
            if 'blocksize' in Dict:
                self.blocksize = Dict['blocksize']

            try : 
                bh =  blockheader()
                bh.fromDict(Dict = Dict['blockheader'])
                self.BH = bh
            except: print("blockheader error") 

            try:
                for i in Dict['blockbody']:
                    if i['TXType'] == "Producer":
                        tx = transaction_Producer()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

                    elif i['TXType'] == "Auctioneer":
                        tx = transaction_Auction()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

                    elif i['TXType'] == "WManager":
                        tx = transaction_Inventory_Management()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

                    elif i['TXType'] == "Distributor_1":
                        tx = transaction_Vehicle_wearing()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

                    elif i['TXType'] == "Distributor_2":
                        tx = transaction_Vehicle_shipment()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

                    elif i['TXType'] == "Seller":
                        tx = transaction_Seller()
                        tx.fromDict(Dict = i)
                        self.BB.append(tx)

            except: print("blockbody error")

        except:
            return False
        else:
            return True
        return False
    
    def toJson(self):
        try:
            save = json.dumps(self.toDict())
            file = pathlib.Path(self.blockID)
            file.write_text(save, encoding='utf-8')
        except:
            return False
        else:
            return True
        return False

    def fromJson(self):
        Data = None
        try:
            file = pathlib.Path(self.blockID)
            file_text = file.read_text(encoding='utf-8')
            Data = json.loads(file_text)
        except:
            return False
        else:
            return True
        return False

        
if __name__ == "__main__":
    t1 = transaction(이름 = "딸기", 타입 = "보냄")
    
    print()
    print("---------------------------------------------------")
    b1 = block(t1)
    print(b1.toDict())
    print("---------------------------------------------------")
    print()
    print()
    print()

    t2 = transaction(이름 = "딸기", 타입 = "받음")
    
    print("---------------------------------------------------")
    b1.append(t2)
    print()
    print(b1.toDict())
    print("---------------------------------------------------")
