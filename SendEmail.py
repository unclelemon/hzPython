import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad,unpad
import base64
import random
from datetime import datetime

# pip install pycryptodome
# Successfully installed pycryptodome-3.18.0

password = os.environ['passwd']
keys = os.environ['keys']
ivs = os.environ['ivs']

twoColor = [1,3,6]
superLotto = [0,2,5]
dict = ['一','二','三','四','五','六','七']

def getDAES(data):
    cipher = AES.new(keys.encode('utf-8'),AES.MODE_CBC,ivs.encode('utf-8'))
    data = base64.b64decode(bytes(data,encoding='utf8'))
    data = unpad(cipher.decrypt(data),AES.block_size,'pkcs7')
    return data

def email_msg(mail_sender, mail_receivers, subject, text=None, img_pth=None, att_pth=None):
    from_post = "{}<{}>".format(mail_sender.split('@')[0], mail_sender)
    to_post = []
    for post in mail_receivers:
        to_post.append("{}<{}>".format(post.split('@')[0], post))
    to_post = ','.join(to_post)

    mm = MIMEMultipart('related')
    mm["From"] = from_post
    mm["To"] = to_post
    # 邮件主题
    mm["Subject"] = Header(subject, 'utf-8')
    # 正文
    if text:
        message_text = MIMEText(text, "plain", "utf-8")
        mm.attach(message_text)
    # 添加图片
    if img_pth:
        image_data = open(img_pth, 'rb')
        message_image = MIMEImage(image_data.read())
        image_data.close()
        mm.attach(message_image)
    # 添加附件
    if att_pth:
        atta = MIMEText(open(att_pth, 'rb').read(), 'base64', 'utf-8')
        atta["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(att_pth))
        mm.attach(atta)
    return mm

def send_email(mail_host, mail_sender, mail_receivers, port, mail_license, subject, text=None, img_pth=None, att_pth=None):
    stp = smtplib.SMTP()
    stp.connect(mail_host, port)
    stp.set_debuglevel(1)
    stp.login(mail_sender, mail_license)
    msg = email_msg(mail_sender, mail_receivers, subject, text, img_pth, att_pth)
    stp.sendmail(mail_sender, mail_receivers, msg.as_string())
    print("邮件发送成功")
    stp.quit()

def getTwoColorLuckNumbers():
    # 规则是双色球由前区6个红球（在1-33个编号中任意选择6个），后区1个蓝色球（1-16个编号中任意选择1个）组合成一注
    red = random.sample(range(1,34),6)
    red.sort()
    blue = random.sample(range(1,17),1)
    red.append(blue[0])
    return red

def getSuperLottoNumbers():
    # 玩家需要选出5个红球号码和2个蓝球号码来进行投注。红球号码由1-35的数字组成，蓝球号码由1-12的数字组成
    first = random.sample(range(1,36),5)
    first.sort()
    second = random.sample(range(1,13),2)
    second.sort()
    first.append(second[0])
    first.append(second[1])
    return first

    
def sendMessage(text,password,email):
    mail_host = "smtp.qq.com"           # 发件邮箱smtp服务地址。此处用的是qq邮箱
    mail_sender = "linhaizeng@qq.com"         # 发件人邮箱
    mail_receivers = email   # 收件人邮箱
    password = getDAES(password)
    mail_license = str(password, encoding = "utf8")        # 邮箱授权码
    subject = "每日幸运数字"                 # 主题
    text = text                  # 正文
    img_pth = ''                        # 图片路径
    att_pth = ''                        # 附件路径
    send_email(mail_host,
               mail_sender=mail_sender,
               mail_receivers=mail_receivers,
               port=25,
               mail_license=mail_license,
               subject=subject,
               text=text,
               img_pth=img_pth,
               att_pth=att_pth
               )

def judgeDay() -> int:
    weekday = datetime.today().weekday()
    return weekday


def sendMessageByEmail(email):
    weekday = judgeDay()
    luckNumbers = []
    message = ''
    if twoColor.count(weekday) > 0:
        luckNumbers = getTwoColorLuckNumbers()
        message ="双色球\n星期%s,日期：%s \n号码：%s"%(dict[weekday],datetime.today()," ".join(str(x) for x in luckNumbers))
    elif superLotto.count(weekday) > 0:
        luckNumbers = getSuperLottoNumbers()
        message = "大乐透\n星期%s,日期：%s \n号码：%s"%(dict[weekday],datetime.today()," ".join(str(x) for x in luckNumbers))
    else:
        message = '大乐透：1，3,6 双色球 2 4 7 今天周五 无活动'
    sendMessage(message,password,email)



if __name__ == "__main__":
    sendMessageByEmail(["linhaizeng@qq.com"])
    sendMessageByEmail(["gloraint@163.com"])








