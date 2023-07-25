# -*- encoding: utf-8 -*-
# CreateTime: 2022/2/20 20:00
# Author: @HzLin

from Crypto import Random
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

"""
pip install pycryptodome
AES加密方式有五种：ECB, CBC, CTR, CFB, OFB
CBC加密需要一个十六位的key(密钥)和一个十六位iv(偏移量)  常用
ECB加密不需要iv
cryptor不能写在主函数中同时给加密函数与解密函数使用，所以加密和解密都要重新创建对象
密码转换为16进制
"""


class MyAES:
    def __init__(self, key, mode=AES.MODE_CBC, iv=Random.new().read(AES.block_size)):
        """
        key 秘钥必须是16（AES-128）,24, 32
        iv 长度等于AES块大小的不可重复的秘钥向量
        本类内实现了 ECB, CBC 两种加密模式，默认为 AES.MODE_CBC 加密模式
        """
        self.key, self.mode, self.iv = key.encode(), mode, iv

    def __add_to_16(self, text):
        """ 如果string不足16位则用空格补齐16位 """
        if len(text.encode()) % 16:
            add = 16 - (len(text.encode()) % 16)
        else:
            add = 0
        text += ("\0" * add)
        return text.encode()

    def encode_aes(self, text):
        """ 使用 AES 加密字符串 """
        # 初始化 AES 对象, cryptor不能写在主函数中同时给加密函数与解密函数使用，所以加密和解密都要重新创建对象
        if self.mode == AES.MODE_ECB:
            cryptos = AES.new(key=self.key, mode=self.mode)
        elif self.mode == AES.MODE_CBC:
            cryptos = AES.new(key=self.key, mode=self.mode, iv=self.iv)
        cipher_text = cryptos.encrypt(self.__add_to_16(text))
        # 由于AES加密后的字符串不一定是ascii字符集，所以转为16进制字符串
        return b2a_hex(cipher_text)

    def decode_aes(self, text):
        """ aes 解密 并去掉补足的空格"""
        # 初始化 AES 对象, cryptor不能写在主函数中同时给加密函数与解密函数使用，所以加密和解密都要重新创建对象
        if self.mode == AES.MODE_ECB:
            cryptos = AES.new(key=self.key, mode=self.mode)
        elif self.mode == AES.MODE_CBC:
            cryptos = AES.new(key=self.key, mode=self.mode, iv=self.iv)
        plain_text = cryptos.decrypt(a2b_hex(text))
        return bytes.decode(plain_text).rstrip("\0")


if __name__ == '__main__':
    a = MyAES(key="this is a 16 key", mode=AES.MODE_CBC)
    # a = MyAES(key="this is a 16 key", mode=AES.MODE_ECB)
    result = a.encode_aes("nishiwode")
    print(result)
    r = a.decode_aes(result)
    print(r)

