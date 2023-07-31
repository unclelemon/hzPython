python 中有字符串str类型和字节bytes类型
在正常字符串前面加一个b代表这个是一个bytes类型的数据：b'bytesData'
由于 bytes 保存的就是原始的字节（二进制格式）数据，因此 bytes 对象可用于在网络上传输数据，也可用于存储各种二进制格式的文件，比如图片、音乐等文件。
字节串（bytes）由多个字节组成，以字节为单位进行操作。

# 利用字符串的encode()方法编码成bytes，默认使用utf-8字符集
b5 = "学习Python很有趣".encode('utf-8')
print(b5)
#b'\xe5\xad\xa6\xe4\xb9\xa0Python\xe5\xbe\x88\xe6\x9c\x89\xe8\xb6\xa3'
# 调用bytes方法将字符串转成bytes对象
b4 = bytes('我爱Python编程',encoding='utf-8')
print(b4)
#b'\xe6\x88\x91\xe7\x88\xb1Python\xe7\xbc\x96\xe7\xa8\x8b'
# 将bytes 对象解码成字符串，默认使用UTF-8进行解码
st = b5.decode('utf-8')
print(st)#学习Python很有趣

也可以使用base64 对字节串进行转换为字符串str
# base64.encodebytes(s)
对包含任意二进制数据的字节串进行编码，返回包含base64编码的字节串，每76个字节插入一个换行符b'\n'，并且保证以换行符结束。
# base64.decodebytes(s)
对包含一行或多行base64编码数据的字节串s进行解码，返回解码的字节串
# base64.b64encode(s, altchars=None)
对字节串对象s进行编码，返回编码后的字节串，可选参数altchars必须是长度至少为2的字节串对象（额外的字符将被忽略），
用来指定+和/字符的替换字母，允许应用程序生成URL或者文件系统的安全Base64字符串。altchars默认值为None，使用标准的Base64字母。
# base64.b64decode(s, altchars=None, validate=False)
对Base64编码的字节串对象进行解码。

参考博客：https://zhuanlan.zhihu.com/p/260192496
Unicode字符集
utf-8 表示字符编码

# json
json.load()：是从文件中加载内容并转换成json；
json.loads()：是将字符串转换成json。
