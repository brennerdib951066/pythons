#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
nome = input('Qual é seu nome?   ')
email = input('Seu Email?   ')

##########################################################

print(email.find('@'))
if nome and email:
    posicaoA = email.find('@')
    servidor = email[posicaoA:]
    if posicaoA != -1 and '.' in servidor:
        print('Email valido')
    else:
        print('Email fora do normal')
else:
    print('Email inválido')
