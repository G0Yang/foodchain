import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.transaction import transaction
from ledger.blockheader import *
from hash256.hash256 import *

class block:
    def __init__(self, *args, **kwargs):
        self.transactionCount = 0
        self.blocksize = 0
        self.BH = blockheader()
        self.BB = []
        try: 
            tx = args[0]
            if str(type(tx)) == "<class 'ledger.transaction.transaction'>":
                self.BB.append(tx)
                self.BH.setCurrentHash(hash256(str(tx.toDict())).getHash())
                self.transactionCount = self.transactionCount + 1
                self.BB[0].txCount = self.transactionCount
                sizeof = str(self.toDict())
                self.blocksize = len(sizeof)
        except:
            print("init Error")
        return
        
    def append(self, Object):
        try: 
            if str(type(Object)) == "<class 'ledger.transaction.transaction'>":
                self.BB.append(Object)  

                self.transactionCount = self.transactionCount + 1
                self.BB[-1].txCount = self.transactionCount

                self.blocksize = len(str(self.toDict()))
                self.BH.setCurrentHash(hash256(str(self.toDict())).getHash())
            else:
                return False
        except:
            print("append Error")
            return False

        return True

    def setCurrentBlockHash():
        string = ""
        try:
            for i in self.BB:
                string = string + i.getHash()
            self.BH.currentBlockHash = hash256(string).getHash()
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
            try : self.transactionCount = Dict['transactionCount']
            except: print("transactionCount error")

            try : self.blocksize = Dict['blocksize']
            except: print("blocksize error")

            try : 
                bh =  blockheader()
                bh.fromDict(Dict = Dict['blockheader'])
                self.BH = bh
            except: print("blockheader error")

            try:
                for i in Dict['blockbody']:
                    tx = transaction()
                    tx.fromDict(Dict = i)
                    self.BB.append(tx)
            except: print("blockbody error")

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

