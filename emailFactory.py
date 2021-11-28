from pathlib import Path
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
from email import encoders

class Email:
    def __init__(self, sender: str, receivers: list, subject: str, message: str, attachments_path_list: list = None):
        self.email = MIMEMultipart()
        self.sender = sender
        self.receivers = receivers
        self.subject = subject
        self.message = message
        self.attachments_paths_list = attachments_path_list
        return

    def set_sender(self):
        self.email['From'] = self.sender

    def set_receivers(self):
        self.email['To'] = COMMASPACE.join(self.receivers)
        return

    def set_date(self):
        self.email['Date'] = formatdate(localtime=True)

    def set_message_subject(self):
        self.email['Subject'] = self.subject

    def set_message_body(self):
        self.email.attach(MIMEText(self.message))

    def set_message_attachments(self):
        for file_path in self.attachments_paths_list:
            with open(file_path, 'rb') as binary_pdf:
                file_name = Path(file_path).name
                payload = MIMEBase('application', 'octate-stream', Name=file_name)
                payload.set_payload(((binary_pdf).read()))
                encoders.encode_base64(payload)
                payload.add_header('Content-Decomposition', 'attachment', filename=file_name)
                self.email.attach(payload)

    def compose_message_as_string(self):
        self.set_sender()
        self.set_receivers()
        self.set_date()
        self.set_message_subject()
        self.set_message_body()
        if self.set_message_attachments() is not None:
            self.set_message_attachments()
        return self.email.as_string()
