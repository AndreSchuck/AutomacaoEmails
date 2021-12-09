import smtplib
from abc import ABC, abstractmethod
from .emailObject import EmailObject

class SMTPServerHandler(ABC):
    """Abstract class that represents an SMTP Server"""
    @abstractmethod
    def auth(self):
        """ Abstract private method to deal with authentication of email providers """
        return

    @abstractmethod
    def send_email(self):
        """Abstract method to send an email using some email server, as gmail or outlook."""
        return

class SMTPOutlookHandler(SMTPServerHandler):
    """Class that abstracts the process of sending emails using Outlook email servers
        Attributes:
        :parameter username: Outlook valid email
        :type username: str

        :parameter password: Outlook's email password
        :type password: str

        :parameter email: EmailObject instance
        :type email: EmailObject
     """

    def __init__(self, username: str, password: str, email: EmailObject):
        """Inits SMTPOutlookHandler with Outlook existing account, represend by username and password parameters and
        an EmailObject instance. """
        self.username = username
        self.__password = password
        self.server = 'smtp.office365.com'
        self.port = 587
        self.email = email

    def auth(self) -> smtplib.SMTP:
        """This private method provides tls connection with Outlook email server"""
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.__password)
        return smtp

    def send_email(self) -> None:
        """This method sends emails using Outlook email servers"""
        connection = self.auth()
        connection.sendmail(from_addr=self.email.sender, to_addrs=self.email.receivers, msg=self.email.compose_email_as_string())
        connection.quit()


class SMTPGmailHandler(SMTPServerHandler):
    """Class that abstracts the process of sending emails using Gmail email servers

        Attributes:
        :parameter username: Outlook valid email
        :type username: str

        :parameter password: Outlook's email password
        :type password: str

        :parameter email: EmailObject instance
        :type email: EmailObject
     """
    def __init__(self, username: str, password: str, email: EmailObject):
        """Inits SMTPGmailHandler with Gmail existing account, represented by username and password parameters and
        an EmailObject instance. """
        self.username = username
        self.__password = password
        self.server = 'smtp.gmail.com'
        self.port = 587
        self.email = email

    def auth(self) -> smtplib.SMTP:
        """This private method provides tls connection with Gmail email server"""
        smtp = smtplib.SMTP(self.server, self.port)
        smtp.starttls()
        smtp.login(self.username, self.__password)
        return smtp

    def send_email(self) -> None:
        """This method sends emails using Gmail email servers"""
        connection = self.auth()
        connection.sendmail(from_addr=self.email.sender, to_addrs=self.email.receivers, msg=self.email.compose_email_as_string())
        connection.quit()
