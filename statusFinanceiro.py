#!/usr/bin/env python3

import pyautogui as bot
import time
import schedule as rotina
####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/loginBubble/statusFinanceiro/statusFinanceiro.png'


##########################################################

def minhaFuncao():
    time.sleep(3)
    for i in range(7):
        print(i)
        time.sleep(2)
        if i == 0:
            if i == 2:
                print('É 2')
            time.sleep(1)
            bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.5)
        elif i == 3:
            bot.press('down',presses=3)
            bot.press('enter')
            time.sleep(5)
            bot.moveTo(2106,808)
            bot.click()
            bot.press('down',presses=3)
        elif i == 6:
            print('CHEGUEI')
            time.sleep(1)
            with bot.hold('ctrl'):
                bot.press('w')

        else:

            arquivoNovo = arquivo.replace('Financeiro.png','Financeiro_{}.png'.format(i))
            print(arquivoNovo)
            bot.click(bot.locateCenterOnScreen(arquivoNovo,confidence=0.8),duration=0.5)

rotina.every(5).seconds.do(minhaFuncao)

while True:
    rotina.run_pending()
    print('Esperando me chmar')
    time.sleep(2)

#time.sleep(2)
#bot.click()
#bot.keyDown('ctrl')
#bot.press('w')
#bot.keyUp('ctrl')

#bot.hotkey('ctrl','c')
