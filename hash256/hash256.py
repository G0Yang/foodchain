import hashlib

class hash256:
    def __init__(self, *args, **kwargs):
        self.hexSHA256 = ""
        try:
            hashSHA = hashlib.sha256()
            hashSHA.update(args[0].encode('utf-8'))
            hexSHA256 = hashSHA.hexdigest()
            self.hexSHA256 = hexSHA256.upper()
        except:
            print("args[0] is not string")
        return
    
    def getHash(self):
        return self.hexSHA256

    def help(self):
        helpDoc =   "h1 = Hash256(\"sds\")\n" + \
                    "print(h1.getHash())\n" + \
                    ">>> 22A3C85609D4D626BC01CD87DF71D01F6BB9A62EFCE214D37B0D4FAF4F3EBB74"
        return helpDoc
