#SymmetricKey_Enc:대칭키로암호화
#RSApublic:개인키로암호화
import struct, hashlib
import binascii, os, ast
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
from . import createSymKey

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class SymmetricKey_Enc:
    def __init__(self):
        pass

    def encrypt_file(self, key, in_filename, out_filename=None, chunksize=64*1024):
        if not out_filename:
            out_filename = in_filename[:-5]
        iv = Random.new().read(AES.block_size)
        encryptor = AES.new(key, AES.MODE_CBC, iv)
        filesize = os.path.getsize(path+in_filename)
        
        with open(path+in_filename, 'rb') as infile:
            with open(path+out_filename, 'wb') as outfile:
                outfile.write(struct.pack('<Q', filesize))
                outfile.write(iv)
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    elif len(chunk) % 16 != 0:
                        chunk += b' ' * (16 - len(chunk) % 16)
                    outfile.write(encryptor.encrypt(chunk))

        
class RSApublic:
    def __init__(self):
        self.data = ""
        self.public_key = ""
        self.encrypted = ""

    def load_public_key(self,keyname):
        try:
            public_key_file = open(path+keyname+'_public.pem', 'r')
            self.public_key = RSA.importKey(public_key_file.read())
        except:
            print(' 공개키가 존재하지 않는다' )


    def encrypt(self, data, keyname):
        try:
            self.load_public_key(keyname)
            encryptor = PKCS1_OAEP.new(self.public_key)
            self.encrypted = encryptor.encrypt(data)
            with open(path+keyname+'_skec.txt','wb') as outfile:
                outfile.write(self.encrypted)
        except:
            print('암호화에 실패하였습니다.')

class en:
    def create_key(self):
        key = createSymKey.createkey()
        return key

    def tr_ec(self, key, in_filename):
        #print('\n#####블록 암호화를 시작합니다.#####')
        #파일명만
        out_filename = in_filename[:-5]
        print('파일이름:',in_filename,'\n', out_filename,'\n',binascii.hexlify(bytearray(key)))
        tr_ec = SymmetricKey_Enc()
        tr_ec.encrypt_file(key, in_filename, out_filename)

    def sk_ec(self, key, keyname):
        #print('\n#####대칭키 암호화를 시작합니다.#####')
        #print('\n'+keyname+'대칭키',binascii.hexlify(bytearray(key)))
        #keyname =''
        password = 'password'#일단고정된값
        sk_ec = RSApublic()
        sk_result = sk_ec.encrypt(key, keyname)
