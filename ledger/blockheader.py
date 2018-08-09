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

    def fromDict(self, Dict):
        try:
            try: self.version = Dict['version']
            except: print()
            try: self.blockNumber = Dict['blockNumber']
            except: print()
            try: self.timestamp = Dict['timestamp']
            except: print()
            try: self.currentBlockHash = Dict['currentBlockHash']
            except: print()
            try: self.previousBlockHash = Dict['previousBlockHash']
            except: print()
        except:
            return False
        else:
            return True
        return False