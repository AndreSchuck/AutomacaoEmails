import smtplib
from email.mime.multipart import MIMEMultipart
from abc import ABC, abstractmethod


class SMTPServerHandler(ABC):
    @abstractmethod
    def __auth__(self):
        return

    @abstractmethod
    def send_email(self, send_from: str, send_to: list, message: MIMEMultipart):
        return


class SMTPOutlookHandler(SMTPServerHandler):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.server = 'smtp.office365.com'
        self.port = 587

    def __auth__(self):
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.password)
        return smtp

    def send_email(self, send_from: str, send_to: list, message: MIMEMultipart):
        connection = self.__auth__()
        connection.sendmail(from_addr=send_from, to_addrs=send_to, msg=message)
        connection.quit()


class SMTPGmailHandler(SMTPServerHandler):
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.server = 'smtp.gmail.com'
        self.port = 587

    def __auth__(self):
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.password)
        return smtp

    def send_email(self, send_from: str, send_to: list, message: MIMEMultipart):
        connection = self.__auth__()
        connection.sendmail(from_addr=send_from, to_addrs=send_to, msg=message)
        connection.quit()
