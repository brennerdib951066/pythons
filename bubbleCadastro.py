#!/usr/bin/env python3

import pyautogui as bot
import time
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/cadastroEtiqueta/cadastroDeEtiquetas.png'


##########################################################


for i in range(44):
    time.sleep(1)
    if i == 0:
        bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
        bot.write('Teste Programação')
    elif i > 0 and i < 5:
        arquivoIncremente = arquivo.replace('Etiquetas','Etiquetas_{}'.format(i))
        print(arquivoIncremente)
        bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
        bot.write('Teste Programação')
    elif i >= 4:
        arquivoIncremente = arquivo.replace('Etiquetas','Etiquetas_{}'.format(i))
        print(arquivoIncremente)
        bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
        bot.write('1.52')
    else:

        arquivoIncremente = arquivo.replace('Etiquetas','Etiquetas_{}'.format(i))
        print(arquivoIncremente)
        bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
