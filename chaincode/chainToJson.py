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
            ch = chain(filename = kwargs['filename'].split('.')[0])
            ch.fromDict(Data)
            self.data = ch

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
    for _ in range(0,10):
        print(randFileName())
    '''
    ctj = chainToJson(filename = randFileName())
    ctj.data = ctj.loadJson()

    ch = chain()
    ch.fromDict(Dict = ctj.data)

    print(ch.toDict())
    '''