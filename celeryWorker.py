from celery import Celery
from time import sleep

# from backend.utils.mail import SendMail


import smtplib
from os import path
import os
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr


class SendMail(object):
    smtp_server = os.environ.get("MAIL_SERVER")
    password = os.environ.get("MAIL_PASSWORD")
    from_addr = "2509934810@qq.com"

    def __init__(self, text, sender, receiver, subject, address):
        self.text = text
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.address = address
        self.to_addr = address

        self.msg = MIMEText(self.text, "plain", "utf-8")
        self.msg["From"] = self._format_addr(self.sender + "<" + self.from_addr + ">")
        self.msg["To"] = self._format_addr(self.receiver + "<" + self.to_addr + ">")
        self.msg["Subject"] = Header(self.subject, "utf-8").encode()

    def _format_addr(self, addr):
        name, addr = parseaddr(addr)
        return formataddr((Header(name, "utf-8").encode(), addr))

    def send(self):
        server = smtplib.SMTP_SSL(self.smtp_server, 465)
        server.set_debuglevel(1)
        server.login(self.from_addr, self.password)
        server.sendmail(self.from_addr, [self.to_addr], self.msg.as_string())
        server.close()


celery = Celery(
    "tasks", broker="redis://127.0.0.1:6379/3", backend="redis://127.0.0.1:6379/4"
)


@celery.task
def add(x, y):
    sleep(4)
    return x + y


# @celery.task
def sendMail(text, sender, receiver, subject, address):
    client = SendMail(text, sender, receiver, subject, address)
    client.send()
