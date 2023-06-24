import random
from email.message import EmailMessage
import ssl
import smtplib


#SENHA DO GMAIL

password = 'ezdhdsicxtglwclq'


#O CÓDIGO DE 5 DIGITOS QUE SERÁ GERADO

codigo = str(random.randint(10000, 99999))


#FUNÇÃO PARA ENVIAR CÓDIGO
def enviarcodigo(username, email):
    email_sender = 'cauacostacrf@gmail.com'
    email_password = password
    email_receiver = email
    subject = 'Olá {}! Aqui está seu código de confirmação.'.format(username)
    body = 'Copie seu código: {}'.format(codigo)


    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['subject'] = subject
    email.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_receiver,email.as_string())
