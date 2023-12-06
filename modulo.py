#!/usr/bin/env python3

import pyautogui as bot
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/abaVideos/video.png'
variavel = 'ola'
variavel2 = 'ola 2'
##########################################################

def bla():
    bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
    bot.write(email)
