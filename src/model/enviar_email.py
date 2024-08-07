import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import os

senha = open('senha.txt', 'r')
linha = senha.readlines()
senha.close()


def enviar_email(email_receiver, parts):       
    # ----- VARIAVEIS -----
    host = 'smtp.gmail.com'
    port = '587'
    email_sender = 'enzzodev@gmail.com'
    senha_sender = linha[0]

    # ----- CONEXÃO -----
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(email_sender, senha_sender)

    msg = MIMEMultipart()
    subject = 'BOT - PROJETO WEB SCRAPING'
    body = f"""
    <h2>{parts[0]}</h2>
    <img src = "cid:logo_python" alt = "Logo Python">
    <p>{parts[1]}</p>
    <p>{parts[2]}</p>
    <p>{parts[3]}</p>
    <p>{parts[4]}</p>
    
    Caso queira saber mais sobre esta linguagem de programação <a href="https://pt.wikipedia.org/wiki/Python">CLIQUE AQUI</a>!
    """

    # ----- EMAIL -----

    msg['From'] = email_sender
    msg['To'] = email_receiver
    msg['Subject'] = subject

    image = open('logo_python.png', 'rb')
    msg_image = MIMEImage(image.read())
    image.close()

    msg_image.add_header('Content-ID', '<logo_python>')
    msg.attach(msg_image)

    msg.attach(MIMEText(body, 'html'))

    # ----- ENVIO DO EMAIL -----
    server.sendmail(msg['From'], msg['To'], msg.as_string())
        
    print(f"-- EMAIL ENVIADO COM SUCESSO PARA: {email_receiver} --\n")
    server.quit()

    os.remove('logo_python.png')