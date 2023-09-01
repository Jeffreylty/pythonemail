# -*- coding: UTF-8 -*-
import smtplib
import email.mime.multipart
import email.mime.text
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def send_email(smtpHost,port, sendAddr, password, recipientAddrs, subject='', content='', file_path=''):
    msg = email.mime.multipart.MIMEMultipart()
    msg['from'] = sendAddr
    msg['to'] = recipientAddrs
    msg['subject'] = subject
    content = content
    txt = email.mime.text.MIMEText(content, 'plain', 'utf-8')
    msg.attach(txt)
    print("准备添加附件...")
    part = MIMEApplication(open(file_path,'rb').read())
    part.add_header('Content-Disposition', 'attachment', filename="chromedriver")
    msg.attach(part)
    smtp = smtplib.SMTP_SSL(smtpHost, port)
    smtp.login(sendAddr, password)
    smtp.sendmail(sendAddr, recipientAddrs.split(";"), str(msg))
    print("发送成功！")
    smtp.quit()

if __name__ == "__main__":
    try:
 
        smtpHost = 'smtp.qq.com'
        port = 465 
        sendAddr ='2684199641@qq.com'
        password = input("请输入邮箱授权码：")
        file_path =  input("请输入文件地址: ")
        recipientAddrs = 'liutianyi20@huawei.com'
        subject='python test'
        content='Hello world'
        send_email(smtpHost, port, sendAddr, password, recipientAddrs, subject, content, file_path)
    except Exception as err:
        print(err)
