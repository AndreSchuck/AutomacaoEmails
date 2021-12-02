from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders
from typing import List, Optional

class Email:
    """Class that represents a basic Email structure, with sender, recivers, subject, message and attachments"""

    def __init__(self, sender: str, receivers: List[str], subject: str,
                 message: str, attachments_path_list: Optional[List[Path]] = None):

        self.email = MIMEMultipart()
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.message = message
        self.attachments_paths_list = attachments_path_list
        return

    def set_sender(self):
        """Functions that set email sender"""

        self.email['From'] = self.sender

    def set_receivers(self):
        """Functions that set email receivers"""

        self.email['To'] = COMMASPACE.join(self.receivers)
        return

    def set_date(self):
        """Functions that set email date"""

        self.email['Date'] = formatdate(localtime=True)
        return

    def set_message_subject(self):
        """Functions that set email subject"""

        self.email['Subject'] = self.subject
        return

    def set_message_body(self):
        """Functions that set email message body"""

        self.email.attach(MIMEText(self.message))
        return

    def set_message_attachments(self):
        """Functions that set email attachments"""

        for file_path in self.attachments_paths_list:
            with open(file_path, 'rb') as binary_pdf:
                file_name = file_path.name
                payload = MIMEBase('application', 'octate-stream', Name=file_name)
                payload.set_payload((binary_pdf.read()))
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment', filename=file_name)
                self.email.attach(payload)
        return

    def compose_email_as_mimemultipart(self) -> MIMEMultipart:
        """Functions that bounds email parts together by calling Email class methods and retrieve an email"""
        self.set_sender()
        self.set_receivers()
        self.set_date()
        self.set_message_subject()
        self.set_message_body()
        if self.set_message_attachments() is not None:
            self.set_message_attachments()
        return self.email

    def compose_email_as_string(self) -> str:
        return self.compose_email_as_mimemultipart().as_string()
#c