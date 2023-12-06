#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
import pyautogui as bot
import time

diretorioBase = '/home/brenner/Imagens/imagensBubble/bubble_0.png'
listaEscrever = ['Brenner Santos','Santos','Dev']


##########################################################

i = 0
for i in range(3):

    if i == 0:
        i += 1
        print('É igual')
        bot.click(bot.locateCenterOnScreen(diretorioBase,confidence=0.8),duration=0.25)
        bot.write(listaEscrever[0])
        print(i)
    else:

        print('Não é igual')
        diretorioBases = diretorioBase.replace('0','{}'.format(i))
        bot.click(bot.locateCenterOnScreen(diretorioBases,confidence=0.9),duration=0.25)
        bot.write(listaEscrever[1])
        print(diretorioBases)
        print(i)
        i += 1
        time.sleep(2)
