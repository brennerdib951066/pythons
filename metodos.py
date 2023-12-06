#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
nome  = 'breNner pereira santos'
email = 'brennerbne@gmail.com'
numero = ' 1250.56 '

##########################################################

##############METODOS DE STRINGS##########################
print(nome.capitalize()) #Transformando a primeira letra em Maiuscula
print(nome.casefold())   #Transforma todas as letras em minusculas
print(nome.count(' '))   #Verifica a qunatidade de caraceteres dentro dos parentenses
print(email.endswith('@gmail.com')) #Verifica se existe um conjunto de caraceteres Resposta TRUE ou FALSE
print(email.find('@'))   #verifica a posicao da string dentro dos parentenses tras como resposta o indice
print(numero.replace('.',',')) # Substituindo o .(ponto) por ,(virgula)
print(numero.strip())          # Corta os espacos iniciais e finais das strings
print(nome.title())            #Coloca as primeiras letras de cada palavra em maiusculas

##########################################################
