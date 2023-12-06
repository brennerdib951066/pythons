#!/usr/bin/env python3

import webbrowser as web
import pyautogui as bot
import time
####################VARIAVEIS DO PROGRAMA##################
urls = ['https://www.youtube.com/watch?v=5KuieNMJWYw&list=RDGMEMc6JZQrQ__ROET3gGdz-TrwVM5KuieNMJWYw&start_radio=1','https://www.youtube.com/watch?v=dwluwXqN8nk']

auto = ['/home/brenner/Imagens/canal.png','/home/brenner/Imagens/voltar.png','/home/brenner/Imagens/menu.png']

##########################################################

while True:
    for clicks in auto:
        bot.click(bot.locateCenterOnScreen(clicks,confidence=0.8),duration=0.25)
        time.sleep(1.5)
