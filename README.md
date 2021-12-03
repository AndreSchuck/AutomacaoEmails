# AutomacaoEmails
This project seeks to create a simple script to send email using python

## Getting Started

### Dependencies
- et-xmlfile==1.1.0
- numpy==1.21.3
- openpyxl==3.0.9
- pandas==1.1.5
- python-dateutil==2.8.2
- pytz==2021.3
- six==1.16.0
- xlrd==2.0.1

See requirements.txt file in this repository,

### Installing


- Git clone this repository 
```
git clone https://github.com/AndreSchuck/AutomacaoEmails.git
```

- Install requirements.txt
```
pip install -r path/to/requirements.txt
```

### Code Modules
- emailObject.py

    This module contains the class that represents an Email object. The Email class abstracts the composition of an email using the MIME protocol, where the main parts that make up an email (Sender, Recivers, Subject, Message, Attachments) are passed as parameters when the class is instantiated.


- smtpHandler.py

    This module abstracts the sending of emails from different providers (Gmail and Outlook are currently supported). If the provider you want to send the email to is Outlook, then use the SMTPOutlookHandler class, if the provider is Gmail use the SMTPGmailHandler class.

### Executing program


```python
# Import  emailObject, smtpHandler and pathlib libs into your project
from emailObject import EmailObject
import smtpHandler
from pathlib import Path

# Instantiate EmailObject class
subject = "Email subject"
message = "Email message"
attatchments_file_path = Path("/file_path.txt")

email = EmailObject(sender='test@teste.com',
                    receivers=['test@teste.com'],
                    subject=subject,
                    message=message,
                    attachments_path_list=[attatchments_file_path])
                    
# Pass the Email instance in a smtpHandler 
outlookEmail = smtpHandler.SMTPOutlookHandler(username='outlook email account', password='outlook account password', email=email)
gmailEmail = smtpHandler.SMTPGmailHandler(username='gmail email account', password='gmail account password', email=email)

# Call send_email method
outlookEmail.send_email()
gmailEmail.send_email()
```


