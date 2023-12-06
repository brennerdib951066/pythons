#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/video.png'


##########################################################

for i in range(5):
    if i == 0:
        print('É zero')
        #bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
    else:
        arquivoIncremente = arquivo.replace('video','video_{}'.format(i))
        print(i)
        print(arquivoIncremente)


