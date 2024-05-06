import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import logging
import os

def enviar_email(email_sender, senha_sender, email_receiver, parts, logo):       
    # ----- VARIAVEIS -----
    host = 'smtp.gmail.com'
    port = '587'

    # ----- CONEXÃO -----
    server = smtplib.SMTP(host, port)
    server.ehlo()
    server.starttls()
    server.login(email_sender, senha_sender)

    msg = MIMEMultipart()
    subject = 'BOT - PROJETO WEB SCRAPING'
    body = f"""
    <h2>{parts[0]}</h2> <img src = "cid:python_logo" alt = "Logo Python">
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

    image = open('C:/logo_python.png', 'rb')
    msg_image = MIMEImage(image.read())
    image.close()

    msg_image.attach('Content-ID', '<Logo Python>')
    msg.attach(msg_image)

    msg.attach(MIMEText(body, 'html'))

    # ----- ENVIO DO EMAIL -----
    logging.info('-- ENVIANDO EMAIL --')
    server.sendmail(msg['From'], msg['To'], msg.as_string())
        
    print(f"-- EMAIL ENVIADO COM SUCESSO PARA: {email_receiver} --\n")
    server.quit()

    os.remove('C:/logo_python.png')