# This Python file uses the following encoding: utf-8

import time, sys, os, random
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from ledger.transaction import *
from ledger.block import block
from hash256.hash256 import *
from chaincode.randFileName import *

class chain:
    def __init__(self, *args, **kwargs):
        self.CHID = randFileName().split('.')[0]
        self.chains = []
        self.C_Hash = None
        print(len(self.chains))

        self.FlagID = None
        self.FlagREV = None

        try : self.CHID = kwargs['CHID']
        except : print("CHID error")
        try : self.chains = kwargs['chains']
        except : print("chains error")
        try : self.C_Hash = kwargs['C_Hash']
        except : print("C_Hash error")
        
        try : 
            b1 = args[0]
            if str(type(b1)) == "<class 'ledger.block.block'>":
                b1.BH.blockNumber = 1
                self.chains.append(b1)
        except : print("block append error")

        if self.C_Hash is None:
            self.set_Hash()
        print("end")
        return
        
    def getCHID(self):
        return self.CHID

    def append(self, Object):
        try :
            if str(type(Object)) == "<class 'ledger.block.block'>":
                self.chains.append(Object)
                self.set_Hash()
                if len(self.chains) > 1:
                    self.chains[-1].BH.previousBlockHash = self.chains[-2].BH.currentBlockHash
                    self.chains[-1].BH.blockNumber = self.chains[-2].BH.blockNumber + 1
        except:
            return False
        else:
            return True
        return False

    def set_Hash(self):
        try:

            self.C_Hash = hash256(str(self.toDict())).getHash()
        except:
            return False
        else:
            return True
        return False

    def toDict(self):
        Dict = {
            'CHID' : self.CHID,
            'C_Hash' : self.C_Hash
            }
        chList = []
        for i in self.chains:
            chList.append(i.toDict())
        Dict["chains"] = chList
        return Dict

    def fromDict(self, Dict):
        try:
            try : self.CHID = Dict['CHID']
            except: print()

            try : self.C_Hash = Dict['C_Hash']
            except: print()

            try:
                for i in Dict['chains']:
                    Block = block()
                    Block.fromDict(Dict = i)
                    self.chains.append(Block)
            except: print()

        except:
            return False
        else:
            return True
        return False
        
if __name__ == "__main__":
    t1 = transaction(이름 = "딸기", 타입 = "보냄")
    b1 = block(t1)
    c1 = chain(b1)
    
    print()
    print()
    print(t1.toDict())
    print()
    print(b1.toDict())
    print()
    print(c1.toDict())

    
    t2 = transaction(이름 = "딸기", 타입 = "받음")
    b2 = block(t2)
    c1.append(b2)
    
    print()
    print()
    print(t2.toDict())
    print()
    print(b2.toDict())
    print()
    print(c1.toDict())

    
    t3 = transaction(이름 = "딸기", 타입 = "다시 보냄")
    t4 = transaction(이름 = "딸기", 타입 = "다시 받음")
    b3 = block(t3)
    b3.append(t4)
    c1.append(b3)
    
    print()
    print()
    print(t3.toDict())
    print(t4.toDict())
    print()
    print(b3.toDict())
    print()
    print(c1.toDict())
