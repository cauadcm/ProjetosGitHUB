import random
from email.message import EmailMessage
import ssl
import smtplib
from htmlEmail import conteudo_html
from GeraCodigo import codigo


#SENHA DO GMAIL

password = 'irpvgdtuibgdgzpt'


#ATRIBUINDO O CODIGO QUE FOI GERADO NO GERACODIGO

codigo_user = codigo



#FUNÇÃO PARA ENVIAR CÓDIGO
def enviarcodigo(username, email):
    email_sender = 'cauafortests@gmail.com'
    email_password = password
    email_receiver = email
    subject = 'Olá {}! Aqui está seu código de confirmação.'.format(username)
    

    email = EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receiver
    email['subject'] = subject


    #CONTEUDO DO EMAIL EM HTML
    email.add_alternative(conteudo_html, subtype= 'html')

    #CONTEXTO DE SEGURANCA DE COMUNICACAO
    context = ssl.create_default_context()

    #SMTP_SSL COM SMTP DO GMAIL, 465 E O CONTEXTO SSL

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        
        
        #FAZENDO LOGIN E MANDANDO EMAIL NO SERVER SMTP´

        smtp.login(email_sender,email_password)
        smtp.sendmail(email_sender, email_receiver,email.as_string())
