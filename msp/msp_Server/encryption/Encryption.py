# This Python file uses the following encoding: utf-8

from Crypto.PublicKey import RSA
from Crypto import Random
from Crypto.Cipher import PKCS1_OAEP
import ast

# 생성한 공개키와 비밀키를 읽어온다.
public_key_file = open('public.pem', 'r')
private_key_file = open('private.pem', 'r')

public_key = RSA.importKey(public_key_file.read())
private_key = RSA.importKey(private_key_file.read(), passphrase='password')

plain_text = 'data'
print('원래 문자열:', plain_text)

# 암호화 실행
encryptor = PKCS1_OAEP.new(public_key)
encrypted = encryptor.encrypt(plain_text.encode('utf-8'))
#encrypted = public_key.encrypt(plain_text.encode('utf-8'), random_func)
print('암호화된 문자열:', encrypted)

# 복호화 실행
decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(ast.literal_eval(str(encrypted)))
print('복호화된 문자열:', decrypted.decode('utf-8'))

public_key_file.close()
private_key_file.close()
