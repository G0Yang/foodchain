#RSAprivate:개인키로복호화
#SymmetricKey_Dec:대칭키로복호화
import struct, hashlib
import binascii, os, ast
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

path = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) + "\data_server\\"

class RSAprivate:
    def __init__(self):
        self.data = ""
        self.private_key = ""
        self.decrypted = ""

    def load_private_key(self, keyname, password):     # 개인키 불러오기(암호 필요)
        try:
            private_key_file = open(path+keyname+'_private.pem', 'r')
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

class SymmetricKey_Dec:
    def __init__(self):
        pass

    def decrypt_file(self, key, in_filename, out_filename, chunksize=24 * 1024):
        with open(path+in_filename, 'rb') as infile:
            origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
            iv = infile.read(16)
            decryptor = AES.new(key, AES.MODE_CBC, iv)

            with open(path+out_filename + '.json', 'wb') as outfile:
                while True:
                    chunk = infile.read(chunksize)
                    if len(chunk) == 0:
                        break
                    outfile.write(decryptor.decrypt(chunk))

                outfile.truncate(origsize)
class dc:
    def sk_dc(self, ip):
        #sk_ec파일열기
        f1 = open(path + ip, 'rb')
        sk_ecdata = f1.read()
    
        #sk_ec rootca공개키로 복호화
        print('\n#####대칭키 복호화를 시작합니다.#####')
        keyname = ip
        password = 'password'#일단고정된값

        sk_dc = RSAprivate()
        sk_dc.decrpyt(sk_ecdata, keyname, password)
        dc_key = sk_dc.decrypted
        return dc_key

    def bl_dc(self, key, filename):
        #csr파일 공개키로 복호화
        print('\n#####블록 복호화를 시작합니다.#####')
        in_filename = filename
        bl_dc = SymmetricKey_Dec()
        bl_dc.decrypt_file(key, in_filename, out_filename = in_filename)
    """
    outfile = open('test.json','rb')
    csr_dedata = outfile.read()
    print('\n복호화된 파일:', csr_dedata, type(csr_dedata))
    """
