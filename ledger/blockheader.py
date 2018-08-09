import time

class blockheader:
    def __init__(self):
        self.version = 0.1
        self.blockNumber = None
        self.timestamp = time.time()
        self.currentBlockHash = ""
        self.previousBlockHash = ""
        return
    
    def setCurrentHash(self, string):
        try:
            self.currentBlockHash = string
        except:
            return False
        else:
            return True
        return False

    def getCurrentHash(self):
        return self.currentBlockHash


    def setPreviousHash(self, string):
        try:
            self.previousBlockHash = string
        except:
            return False
        else:
            return True
        return False

    def getPreviousHash(self):
        return self.previousBlockHash

    def toDict(self):
        Dict = {
            'version' : self.version,
            'blockNumber' : self.blockNumber,
            'timestamp' : self.timestamp,
            'currentBlockHash' : self.currentBlockHash,
            'previousBlockHash' : self.previousBlockHash
            }
        return Dict

