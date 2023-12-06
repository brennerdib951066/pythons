#!/usr/bin/env python3

import pyautogui as bot
import time
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/hashtag/hashtag.png'


##########################################################

for i in range(3):
    time.sleep(1)
    if i == 0:
        bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
        print(arquivo)
    else:
        ArquivoIncremente = arquivo.replace('tag.png','tag_{}.png'.format(i))
        bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
        print(ArquivoIncremente)
