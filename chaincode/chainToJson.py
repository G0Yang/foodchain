import json, pathlib, sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ledger.chain import *
from chaincode.randFileName import *

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class chainToJson:
    def __init__(self, *args, **kwargs):
        self.data = None
        self.filename = None
        try:
            try : self.data = kwargs['data']
            except: print("data error")
            try : self.filename = path + "ch_" + kwargs['filename']
            except: print("filename error")
        except:
            return

        if self.filename is None and self.data is not None:
            print("filename is None and data is not None")
            self.filename = path + "ch_" + randFileName()
            self.saveJson()

        elif self.filename is not None and self.data is None:
            print("filename is not None and data is None")
            Data = self.loadJson()
            print(type(Data))

        elif self.filename is not None and self.data is not None:
            print("filename is not None and data is not None")
            Data = self.loadJson()
            if Data:
                print()
            else:
                self.saveJson()

        return
    
    def loadJson(self):
        Data = None
        try:
            file = pathlib.Path(self.filename)
            file_text = file.read_text(encoding='utf-8')
            Data = json.loads(file_text)
        except:
            return False
        else:
            return Data
        return Data

    def saveJson(self):
        try:
            save = json.dumps(self.data.toDict())
            file = pathlib.Path(self.filename)
            file.write_text(save, encoding='utf-8')
        except:
            return False
        else:
            return True
        return False

    def append(self, *args, **kwargs):
        try:
            Data = self.loadJson()

            Chain = chain(CHID = Data['CHID'], chains = Data['chains'], C_Hash = Data['C_Hash'])
            print("Chain", Chain)
            #print(Chain.toDict())
        except:
            print()
        return False


if __name__ == "__main__":
    t1 = transaction(이름 = "딸기", 타입 = "보냄")
    b1 = block(t1)
    c1 = chain(b1)
    
    
    t2 = transaction(이름 = "딸기", 타입 = "받음")
    b2 = block(t2)
    c1.append(b2)
    
    
    t3 = transaction(이름 = "딸기", 타입 = "다시 보냄")
    t4 = transaction(이름 = "딸기", 타입 = "다시 받음")
    b3 = block(t3)
    b3.append(t4)
    c1.append(b3)


    ctj = chainToJson(filename = c1.getCHID() + ".json", data = c1)

    print("----------------------------------------")
    ctj.append()