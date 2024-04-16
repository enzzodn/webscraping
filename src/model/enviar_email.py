import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
import logging
import os

def enviar_email(email_sender, senha_sender):       
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
    body = 

    # ----- EMAIL -----

    msg['From'] = usuario
    msg['To'] = receiver
    msg['Subject'] = subject

    # ----- ENVIO DO EMAIL -----
    logging.info('-- ENVIANDO EMAIL --')
    server.sendmail(msg['From'], receiver.split(','), msg.as_string()) # PARA MAIS DE 1 EMAIL
        
    print(f"-- EMAIL DA EMPRESA - {empresa} - {tipo} - ENVIADO COM SUCESSO PARA: {receiver} --\n")
    server.quit()

def apagar_prints(empresa):
    for i in range(1,5):
        if os.path.exists(f'C:/RPA/arquivos/printscreen_nps_byd_{empresa}_vendas_{i}.png'):
            os.remove(f'C:/RPA/arquivos/printscreen_nps_byd_{empresa}_vendas_{i}.png')
    for i in range(1,6):
        if os.path.exists(f'C:/RPA/arquivos/printscreen_nps_byd_{empresa}_pos_vendas_{i}.png'):
            os.remove(f'C:/RPA/arquivos/printscreen_nps_byd_{empresa}_pos_vendas_{i}.png')