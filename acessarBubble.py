#!/usr/bin/env python3

import pyautogui as bot
import time
from videos import *
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/loginBubble/acessoBubble.png'
email = 'setor.administrativo.dib@teste.com'
senha = '652516'
##########################################################

login = input('Setor de Acesso:  ')
if login == 'comercial':
    email = 'setor.comercial.dib@teste.com'
    for i in range(3):
        time.sleep(1)
        if i == 0:
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
            bot.write(email)
        elif i == 1:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
            bot.write(senha)
        elif i == 2:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
            #bot.write(senha)
elif login == 'financeiro':
    email = 'setor.financeiro.dib@teste.com'
    for i in range(3):
        time.sleep(1)
        if i == 0:
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
            bot.write(email)
        elif i == 1:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
            bot.write(senha)
        elif i == 2:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
elif login == 'posvendas':
    email = 'setor.posvendas.dib@teste.com'
    for i in range(3):
        time.sleep(1)
        if i == 0:
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
            bot.write(email)
        elif i == 1:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
            bot.write(senha)
        elif i == 2:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
else:
    #print('Email inválido!')
    for i in range(3):
        time.sleep(1)
        if i == 0:
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
            bot.write(email)
        elif i == 1:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
            bot.write(senha)
        elif i == 2:
            arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
            print(arquivoIncremente)
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)

time.sleep(8)
abaDeVideos()
