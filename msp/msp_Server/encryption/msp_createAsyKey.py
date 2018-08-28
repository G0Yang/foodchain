# This Python file uses the following encoding: utf-8

from Crypto.PublicKey import RSA
import os


class createAsymmetricKey:
    def __init__(self):
        self.private_key = ""
        self.public_key = ""

    def createPrivateKey(self,keyname):
        self.private_key = RSA.generate(2048)
        private_pem = self.private_key.exportKey(format='PEM', passphrase='password')
        if os.path.isfile('encryption/privateKey/'+keyname+'_private.pem'):
            print("이미 파일이 존재한다. 다시입력 하시오")
            return
        else:
            with open('privateKey/'+keyname+'_private.pem', 'wb') as f:
                f.write(private_pem)
                print("PrivateKey create success")
        
        return self.private_key
        
    
    def createPublicKey(self, PrivateKeyFile, keyname):
        self.public_key = self.private_key.publickey()
        public_pem = self.public_key.exportKey()
        if os.path.isfile('encryption/publicKey/'+keyname+'_public.pem'):
            #print("이미 파일이 존재한다. 다시입력 하시오")
            return
        else:
            with open('publicKey/'+keyname+'_public.pem', 'wb') as f:
                f.write(public_pem)
                print("PublicKey create success")
                
        return self.public_key

    def createKey(self, keyname):
        return self.createPrivateKey(keyname), self.createPublicKey(self.private_key,keyname)


    def run(self, keyname):
        self.createKey(keyname)

if __name__ == "__main__":
    
    r = createAsymmetricKey()
    r.run('sims3')
