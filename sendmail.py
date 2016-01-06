import smtplib
import getopt
import sys
import os
import time

from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import email.encoders as encoders

from httplib2 import socks
import socket

def send_mail(mail_from,mail_to,subject,text):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = mail_from
    msg['To'] = mail_to
    html = text
    part2 = MIMEText(html,'html')
    msg.attach(part2)

    #s = smtplib.SMTP('135.251.50.68')
    aliyun_user = "liqinglu2005@aliyun.com"
    aliyun_passwd = "monarchs2013"
    #socket.socket = socks.socksocket
    #socks.setdefaultproxy(socks.PROXY_TYPE_HTTP,"135.251.33.16",80,username="ad4\\qinglul",password="Haiku*2015")
    try:
        s = smtplib.SMTP_SSL('smtp.aliyun.com',465) # 115.124.18.136
        #s = smtplib.SMTP('smtp.aliyun.com',25) # 115.124.18.136
        #s.helo()
        #s.ehlo()
        #s.starttls()
        #s.ehlo()
        s.login(aliyun_user,aliyun_passwd)
        s.sendmail(mail_from,mail_to,msg.as_string())
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False

def main():
    #print send_mail("liqinglu2005@aliyun.com","qinglu.li@alcatel-sbell.com.cn","test","I test")
    print send_mail("liqinglu2005@aliyun.com","liqinglu2005@aliyun.com","test","I test")

if __name__ == "__main__":
    main()
