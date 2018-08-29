from Crypto.PublicKey import RSA
import os

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class createAsymmetricKey:
    def __init__(self):
        self.private_key = ""
        self.public_key = ""

    def createPrivateKey(self,keyname):
        self.private_key = RSA.generate(2048)
        private_pem = self.private_key.exportKey(format='PEM', passphrase='password')
        with open(path+keyname+'_private.pem', 'wb') as f:
            f.write(private_pem)
        return self.private_key
        
    
    def createPublicKey(self, PrivateKeyFile, keyname):
        self.public_key = self.private_key.publickey()
        public_pem = self.public_key.exportKey()
        with open(path+keyname+'_public.pem', 'wb') as f:
           f.write(public_pem)
        
        return self.public_key
        

def createKey(keyname):
    ck = createAsymmetricKey()
    print("create success")
    return ck.createPrivateKey(keyname), ck.createPublicKey(ck.private_key,keyname)

if __name__ == "__main__":
    
    keyname = "202.31.146.57"
    pr_key, pb_key = createKey(keyname)
    print(pr_key)
    print(pb_key)
