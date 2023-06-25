import random
from email.message import EmailMessage
import ssl
import smtplib
from htmlEmail import conteudo_html
from GeraCodigo import codigo
#SENHA DO GMAIL

password = 'ezdhdsicxtglwclq'


#O CÓDIGO DE 5 DIGITOS QUE SERÁ GERADO

codigo_user = codigo

#FUNÇÃO PARA ENVIAR CÓDIGO
def enviarcodigo(username, email):
    email_sender = 'cauacostacrf@gmail.com'
    email_password = password
    email_receiver = email
    subject = 'Olá {}! Aqui está seu código de confirmação.'.format(username)
    


    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['subject'] = subject



    email.add_alternative(conteudo_html, subtype= 'html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_receiver,email.as_string())
