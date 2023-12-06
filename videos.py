#!/usr/bin/env python3

import pyautogui as bot
import time
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/abaVideos/video.png'


##########################################################

#bot.click(bot.locateCenterOnScreen(arquivo[0],confidence=0.8),duration=0.25)
#time.sleep(1)
#bot.click(bot.locateCenterOnScreen(arquivo[1],confidence=0.8),duration=0.25)
#time.sleep(1)
#bot.click(bot.locateCenterOnScreen(arquivo[2],confidence=0.8),duration=0.25)
#time.sleep(1)
#bot.click(bot.locateCenterOnScreen(arquivo[1],confidence=0.8),duration=0.25)
#time.sleep(1)
#bot.click(bot.locateCenterOnScreen(arquivo[4],confidence=0.8),duration=0.25)
#time.sleep(3)
#bot.click(bot.locateCenterOnScreen(arquivo[5],confidence=0.8),duration=0.25)
#time.sleep(1)
#bot.click(bot.locateCenterOnScreen(arquivo[6],confidence=0.8),duration=0.25)

def abaDeVideos():
    for i in range(9):
        time.sleep(1)
        if i == 0:
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
        else:
            arquivoIncremente = arquivo.replace('video','video_{}'.format(i))
            bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)


        #print(arquivoIncremente)
#abaDeVideos()
