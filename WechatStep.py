import requests
import random
import os


password = os.environ['PASSWORD']

if __name__=="__main__":
    url = 'https://apis.jxcxin.cn/api/mi'
    val = 'user=123%40qq.com&password=123&step=1&ver=cxydzsv3.2'
    headers = {'Content-type': 'application/json'}
    step = random.randint(8800,13000)
    data = {
        "user":  "linhaizeng@qq.com",
        "password": "z19951025",
        "step": str(step),
        "ver": "cxydzsv3.2"
    }
    response = requests.post(url=url,params=data,headers=headers)
