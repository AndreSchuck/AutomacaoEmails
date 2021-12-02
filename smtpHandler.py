import smtplib
from email.mime.multipart import MIMEMultipart
from abc import ABC, abstractmethod
from emailFactory import Email
from typing import List


class SMTPServerHandler(ABC):
    """Abstract class that represents an SMTP Server"""
    @abstractmethod
    def __auth__(self):
        return

    @abstractmethod
    def send_email(self):
        return

class SMTPOutlookHandler(SMTPServerHandler):
    def __init__(self, username: str, password: str, email: Email):
        self.username = username
        self.password = password
        self.server = 'smtp.office365.com'
        self.port = 587
        self.email = email

    def __auth__(self):
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.password)
        return smtp

    def send_email(self):
        connection = self.__auth__()
        connection.sendmail(from_addr=self.email.sender, to_addrs=self.email.receivers, msg=self.email.compose_email_as_string())
        connection.quit()


class SMTPGmailHandler(SMTPServerHandler):
    def __init__(self, username: str, password: str, email: Email):
        self.username = username
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        self.email = email

    def __auth__(self):
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.password)
        return smtp

    def send_email(self):
        connection = self.__auth__()
        connection.sendmail(from_addr=self.email.sender, to_addrs=self.email.receivers, msg=self.email.compose_email_as_string())
        connection.quit()
