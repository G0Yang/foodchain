import hashlib, time, binascii
from Crypto.Cipher import AES

class SymmetricKey:
    def __init__(self):
        self.key = ""

    def createKey(self, password):
        self.key = hashlib.sha256(password.encode('utf-8')).digest()
        #print('\n대칭키:', binascii.hexlify(bytearray(self.key)))

        return self.key


def make_pass():
    timekey = int(time.time())
    return str(timekey)

def createkey():
    password = make_pass()
    ck = SymmetricKey()
    sy_key = ck.createKey(password)
    print('#####대칭키가 생성되었습니다.#####')
    print('\n생성된 대칭키:', binascii.hexlify(bytearray(sy_key)))
    #print('\nkey length:',len(sy_key),'byte')
    return sy_key
    
    #return ck.createKey(password)

#if __name__ == "__main__":

    #sy_key = createkey()
    #print('\n대칭키:', binascii.hexlify(bytearray(sy_key)))
    #print('key length:',len(sy_key),'byte')
