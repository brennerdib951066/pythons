#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Operações com String.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1T8Wj4GgryCVh_1ujmjNCLlJFQDkmdq7C

# Operações com String

str -> transforma número em string<br>
in -> verifica se um texto está contido dentro do outro<br>
operador + -> concatenar string<br>
format e {} -> substitui valores<br>
%s -> substitui textos<br>
%d -> substitui números decimais<br>

Vamos deixar uma cartilha para download
"""

faturamento = 1000
custo = 500
lucro = faturamento - custo

"""Uso do str() e do concatenar com +"""

print ('STR O faturamento da loja foi de: ' + str(faturamento))

"""Uso do Format"""

print('O faturamento foi de: {}\nO custo foi de: {}\nO lucro foi de: {}'.format(faturamento,custo,lucro))
#######################UMA VARIACAO DE FORMAT(variaveis)###########

print('INDICES O faturamento foi de: {0}\nO custo foi de: {1}\nO lucro foi de: {2}'.format(faturamento,custo,lucro))

#Pegando pelo indice dentro da lista do format(variavel)
###################################################################

"""Uso do %s e %d"""

#print ('O faturamento foi de: ')

"""Uso do in (mais exercícios práticos nas próximas aulas)"""

#print('@' in 'lira@gmail.com')
#print('@' in 'lira.gmail.com')