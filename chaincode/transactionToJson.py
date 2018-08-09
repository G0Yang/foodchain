import json, pathlib, sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from ledger.transaction import *
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
            try : self.filename = path + "tx_" + self.filename
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

    



if __name__ == "__main__":
    t1 = transaction(이름 = "kim")
    tj1 = transactionToJson(filename = randFileName(), data = t1)
    print(tj1.data.toDict())

