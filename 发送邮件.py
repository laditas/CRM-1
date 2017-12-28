#!/usr/bin/env python
# -*- coding:utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
class Email(object):
    def __init__(self):
        self.email = "m394559@126.com"
        self.user = "武沛齐"
        self.pwd = 'WOshiniba'

    def send(self,subject,body,to,name):

        msg = MIMEText(body, 'plain', 'utf-8')  # 发送内容
        msg['From'] = formataddr([self.user,self.email])  # 发件人
        msg['To'] = formataddr([name, to])  # 收件人
        msg['Subject'] = subject # 主题


        server = smtplib.SMTP("smtp.126.com", 25) # SMTP服务
        server.login(self.email, self.pwd) # 邮箱用户名和密码
        server.sendmail(self.email, [to, ], msg.as_string()) # 发送者和接收者
        server.quit()
