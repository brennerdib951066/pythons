#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################



##########################################################

nome = input('Nome:   ')
sobreNome = input('Sobrenome:   ')

if nome and sobreNome:
    print('ola! {} {}'.format(nome.title(),sobreNome.title())) # cada letra no inicia das palavras serão maiusculas
else:
    print('Preencha o(s) campo(s)')

