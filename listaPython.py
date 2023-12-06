#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
produtos=['tv','celular','mouse','teclado','tablete']
vendas=['1000','1500','350','270','900']
texto='brenner'
##########################################################

print(produtos[0])
vendas[3]='300'
print('A venda do produto {} teve o valor de {}'.format(produtos[3],vendas[3]))

# As strings comuns naõ podem ser alteradas os seus indexs, pois elas são imutaveis
# Para modifica-las temos que usar o replace dentro de uma variavel
texto= texto.replace('b','d')
print(texto)
