import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os
import sys

password = sys.argv[1]

def getDAES(data):
    cipher = AES.new(keys,AES.MODE_CBC,ivs)
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

if __name__ == "__main__":
    mail_host = "smtp.qq.com"           # 发件邮箱smtp服务地址。此处用的是qq邮箱
    mail_sender = "linhaizeng@qq.com"         # 发件人邮箱
    mail_receivers = ["linhaizeng163@163.com"]   # 收件人邮箱
    mail_license = password                   # 邮箱授权码
    subject = "测试定时python发送邮件"                 # 主题
    text = "这里是正文"                   # 正文
    img_pth = ''                        # 图片路径
    att_pth = ''                        # 附件路径
    password = getDAES(password)
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
    
