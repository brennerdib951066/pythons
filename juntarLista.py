#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
produtos = ['apple tv','mac','iphone 11','Ipad','apple whatch','mac book','airpods']
novosProdutos = ['iphone 12','ioculos']

vendas = [1000,1500,15000,20000,270,900,100,1200]
vendasIphone = [15000]
vendasIphone11 = [20000]
##########################################################

# Adicionando uma lista na outra lista

print(produtos) # lista Original
# 1 Metodo
produtos.extend(novosProdutos)
print('Metodo extend {}'.format(produtos))

#2 Metodo
todosOsProdutos = produtos + novosProdutos
print('Metodo com uma nova variavel {}'.format(todosOsProdutos))

# Somando os indices da variavel vendas
totalIphone = vendas[2] + vendas[3]
print('O indice 2 + 3 será de: {}'.format(totalIphone))

# Somando uma lista com apenas 1 indice das variaveis vendasIphone e vendasIphone11

totalIphoneLista = vendasIphone[0] + vendasIphone11[0]
print('Somando apenas por 1 indice as variaveis vendasIphone + vendasIphone11, total= {}'.format(totalIphoneLista))

# Ordenar uma lista
# metodo 1
produtos.sort() # Assim irá Ordenar de maiuscula para minuscula
print('ORDEM de UPP para lower {}'.format(produtos))

# Metodo 2

vendas.sort(reverse=True) # Assim irá Ordenar do maior para menor
print('vendas produtos {}'.format(vendas))
