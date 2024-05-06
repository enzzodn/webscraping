import os
os.system('cls')
from src.model.trechos import trechos
from src.model.enviar_email import enviar_email

res = 'n'
while res != 's':
    email_sender = input('DIGITE SEU EMAIL, CORRETAMENTE: ')
    senha_sender = input('DIGITE SUA SENHA, CORRETAMENTE: ')
    email_receiver = input('DIGITE O EMAIL QUE VAI RECEBER A MENSAGEM, CORRETAMENTE: ')
    res = input('VOCÊ CONFIRMA OS DADOS ACIMA? (s/n): ').lower()
    os.system('cls')

parts, logo = trechos()
enviar_email(email_sender, senha_sender, email_receiver, parts, logo)