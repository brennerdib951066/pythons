#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
nota = 10
venda = 5002
meta = 2500

##########################################################

#if nota >= 7:
    #print('Aprovado sua nota: {}'.format(nota))
#else:
    #if nota >= 5:
        #print('Recuperação sua nota: {}'.format(nota))
    #else:
        #print('Repetira o ano letivo sua vergonha: {}'.format(nota))

if venda < meta:
    print('Sua venda é de: {}, não ganhou bonus'.format(venda))
elif venda >= meta*2:
    bonus = 0.75 * venda
    print('cumpriu a meta! Aqui está seu bonus: {}'.format(bonus))
else:
    bonus = 2 * venda
    print('Você ganhou {} de bonus'.format(bonus))
