import os
os.system('cls')
from src.model.trechos import trechos
from src.model.enviar_email import enviar_email

res = 'n'
while res != 's':
    email_receiver = input('DIGITE O EMAIL QUE VAI RECEBER A MENSAGEM, CORRETAMENTE: ')
    res = input('VOCÊ CONFIRMA O EMAIL ACIMA? (s/n): ').lower()
    os.system('cls')

parts = trechos()
enviar_email(email_receiver, parts)