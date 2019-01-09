# This Python file uses the following encoding: utf-8
import sys, os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
import time, metadata

class blockheader:
    def __init__(self):
        self.version = metadata.metadata["BaseVersion"]
        self.blockNumber = 0
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
            if 'version' in Dict:
                self.version = Dict['version']
            if 'blockNumber' in Dict:
                self.blockNumber = Dict['blockNumber']
            if 'timestamp' in Dict:
                self.timestamp = Dict['timestamp']
            if 'currentBlockHash' in Dict:
                self.currentBlockHash = Dict['currentBlockHash']
            if 'previousBlockHash' in Dict:
                self.previousBlockHash = Dict['previousBlockHash']

        except:
            return False
        else:
            return True
        return False