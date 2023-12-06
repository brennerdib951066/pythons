#!/usr/bin/env python3

import schedule as rotina
import time

def roda_minha_funcao():
    #with open('python.txt', 'w') as arquivo:
        #arquivo.write('Parabens seu python funcionou com sucesso!')
        #print('Arquivo criado!!!!')


rotina.every(1).minutes.do(roda_minha_funcao)

while True:
    rotina.run_pending()
    print('Opa')
    time.sleep(1)
