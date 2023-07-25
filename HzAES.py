import base64
import sys

from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad

keys = b'zheshiyige16weiz'
ivs = b'zysyg16wdeivsyhg'
def getDAES(data):
    cipher = AES.new(keys,AES.MODE_CBC,ivs)
    print(f'明文：{data}')
    # 可打印的ASCII字符 转换为 二进制字符串
    data = base64.encodebytes(bytes(data,encoding='utf8'))
    data = unpad(cipher.decrypt(data),AES.block_size,'pkcs7')
    print(f"解密后的密码：{str(data,encoding='utf-8')}")

def getAES(data):
    cipher = AES.new(keys,AES.MODE_CBC,ivs)
    data = cipher.encrypt(pad(bytes(data,encoding='utf-8'),AES.block_size,'pkcs7'))
    # 将生成的二进制字符串密码转换为可打印的ASCII字符
    data = base64.b64encode(data)
    print(f"加密后的密码{str(data)}")

if __name__=='__main__':
    print("0:解密 ; 1:加密")
    data = sys.argv[2]
    if sys.argv[1] == '0':
        getDAES(data)
    else:
        getAES(data)
