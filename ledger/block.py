# This Python file uses the following encoding: utf-8
import time, sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

#from ledger.transaction import transaction
from ledger.transaction_Producer import transaction_Producer
from ledger.transaction_Vehicle_wearing import transaction_Vehicle_wearing
from ledger.transaction_Vehicle_shipment import transaction_Vehicle_shipment
from ledger.transaction_Inventory_Management import transaction_Inventory_Management
from ledger.transaction_Auction import transaction_Auction
from ledger.transaction_Seller import transaction_Seller

from ledger.blockheader import *
from hash256.hash256 import *
from chaincode.randFileName import *

class block:
    def __init__(self, *args, **kwargs):
        self.transactionCount = 0
        self.blocksize = 0
        self.blockID=""
        self.BH = blockheader()
        self.BB = []
        try: 
            tx = args[0]
            list_tx = ["<class 'ledger.transaction.transaction'>",
                       "<class 'ledger.transaction_Producer.transaction_Producer'>",
                       "<class 'ledger.transaction_Vehicle_wearing.transaction_Vehicle_wearing'>",
                       "<class 'ledger.transaction_Vehicle_shipment.transaction_Vehicle_shipment'>",
                       "<class 'ledger.transaction_Inventory_Management.transaction_Inventory_Management'>",
                       "<class 'ledger.transaction_Auction.transaction_Auction'>",
                       "<class 'ledger.transaction_Seller.transaction_Seller'>"]

            for i in list_tx:
                if str(type(tx)) == i:
                    self.BB.append(tx)
                    self.BH.setCurrentHash(hash256(str(tx.toDict())).getHash())
                    self.transactionCount = self.transactionCount + 1
                    self.BB[0].txCount = self.transactionCount
                    sizeof = str(self.toDict())
                    self.blocksize = len(sizeof)
                    self.blockID=randFileName()[0:-5]
            
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
            try: self.blockID = Dict['blockID']
            except: print("blockID error")
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
