import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from os.path import basename

class EmailError(Exception):
    pass
class EmailSendError(EmailError):
    pass
class EmailLoginError(EmailError):
    pass
class EmailSMTPError(EmailError):
    pass
class EmailAttachmentError(EmailError):
    pass
class EmailUnknownError(EmailError):
    pass
class EmailCreationError(EmailError):
    pass

def send_email(subject:str, body:str, username:str, passwd:str, to:str, cc:str="", bcc:str="", files:list[str]=None, server:str='smtp.outlook.com') -> None:
    """Sends an email via smtp authentication """

    port = '587'

    try:
        msg = MIMEMultipart('alternative')
        msg['Subject'] = subject
        msg['From'] = username
        msg['To'] = to
        msg['CC'] = cc
        msg['BCC'] = bcc
        msg.attach(MIMEText(body, 'html'))
    except Exception as e:
        raise EmailCreationError(f"Failed to create email from function arguments: {e}")

    try:
        for f in files or []:
            with open(f, "rb") as file:
                part = MIMEApplication(file.read(), Name=basename(f))
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
    except Exception as e:
        raise EmailAttachmentError(f"Failed to get attachment(s): {e}")

    with smtplib.SMTP(server, port) as smtp:
        try:
            smtp.starttls()
            smtp.ehlo()
        except Exception as e:
            raise EmailSMTPError(f"Python SMTP failed to start {e}")           

        try: 
            smtp.login(username, passwd)
        except Exception as e: 
            raise EmailLoginError(f"Email login failure: {e}")
        
        try: 
            smtp.sendmail(username, to, msg.as_string())
        except Exception as e:
            raise EmailSendError(f"Failed to send email: {e}")
        
        try:
            smtp.quit()
        except Exception as e:
            raise EmailSMTPError(f"Failed to quit Python SMTP session: {e}")