import os
os.system('cls')
from src.model.trechos import trechos
from src.model.enviar_email import enviar_email

# trechos()
res = 'n'
while res != 's':
    email_sender = input('DIGITE SEU EMAIL CORRETAMENTE: ')
    senha_sender = input('DIGITE SUA SENHA CORRETAMENTE: ')
    res = input('VOCÊ CONFIRMA OS DADOS ACIMA? (s/n): ').lower()
    os.system('cls')

enviar_email(email_sender, senha_sender)