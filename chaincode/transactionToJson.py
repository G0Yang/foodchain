# This Python file uses the following encoding: utf-8
import json, pathlib, sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
#from ledger.transaction import *
from chaincode.randFileName import *

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class transactionToJson:
    def __init__(self, *args, **kwargs):
        self.data = None
        self.filename = None

        try: self.filename = kwargs['filename']
        except: print("kwargw['filename'] error")

        if self.filename == None:
            return
        else:
            try : self.filename = path + self.filename
            except: print("filename error")

            try : self.data = kwargs['data']
            except: print("data error")

            try : self.saveJson()
            except: print("save error")
            return
        return
    
    def saveJson(self):
        try:
            save = json.dumps(self.data.toDict())
            file = pathlib.Path(self.filename)
            file.write_text(save, encoding='utf-8')
        except:
            return False
        else:
            return True
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
        return False



if __name__ == "__main__":
    tj1 = transactionToJson(filename = "test.json")
    tj1.data = tj1.loadJson()

    t2 = transaction()
    print(type(tj1.data))
    t2.fromDict(Dict = tj1.data)

    print(t2.toDict())

