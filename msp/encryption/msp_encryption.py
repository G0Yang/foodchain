# This Python file uses the following encoding: utf-8

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

class RSApublic:
    def __init__(self):
        self.data = ""
        self.public_key = ""
        self.encrypted = ""

    def load_public_key(self,keyname):
        try:
            public_key_file = open(keyname+'_public.pem', 'r')
            self.public_key = RSA.importKey(public_key_file.read())
        except:
            print(" 공개키가 존재하지 않는다" )


    def encrypt(self, data, keyname):        
        try:
            self.load_public_key(keyname)
            encryptor = PKCS1_OAEP.new(self.public_key)
            self.encrypted = encryptor.encrypt(data.encode('utf-8'))
        except:
            print("암호화에 실패하였습니다.")



class RSAprivate:
    def __init__(self):
        self.data = ""
        self.private_key = ""
        self.decrypted = ""

    def load_private_key(self, keyname, password):     # 개인키 불러오기(암호 필요)
        try:
            private_key_file = open(keyname+'_private.pem', 'r')
            self.private_key = RSA.importKey(private_key_file.read(), passphrase=password)
        except:
            print(" 개인키가 존재하지 않는다" )


    def decrpyt(self, encrypted, keyname, password):   # 복호화 - 개인키 사

        try:
            self.load_private_key(keyname, password)
            decryptor = PKCS1_OAEP.new(self.private_key)
            self.decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))

        except:
            print("복호화에 실패하였습니다.")

        #print(self.decrypted)
        #print("복호화에 실패하였습니다.")
            

            
       
    
if __name__ == "__main__":
    string = "hello world!asdjalskdjsakdlkasjdklsajlkdjaslkdjaslkdjalsjdlsajldkasjlkdjsakldjalskdjlksajdlksajdlksajlkdasjlkdjaslkdjaslk"
    keyname = "ShinJae"
    password = 'password'

    print(string)
    
    ec = RSApublic()                #ec.load_public_key()
    ec.encrypt(string, keyname)
    print('암호화된 문자열:', ec.encrypted)


    dc = RSAprivate()
    dc.decrpyt(ec.encrypted, keyname, password)
    print('복호화된 문자열:', dc.decrypted.decode('utf-8'))



    #print(decrypted.decode('utf-8'))
