#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
produtos = ['apple tv','mac','iphone x','ipad','apple warch','mac book','airpods']
vendas = ['1000','1500','15000','270','100','1200']

##########################################################

# Saber o tamanho da lista/quantidades de index
tamanho = len(produtos)
print("Tamanho da lista {}".format(tamanho))

# Seber qual é o maior valor
maisVendido = max(vendas)
print('O mais Vendio foi: {}'.format(maisVendido))

# Saber o menor valor
menosVendido = min(vendas)
print('Essse é menos vendido {}'.format(menosVendido))

i = vendas.index(maisVendido)
produtoMaisVendido = produtos[i]
print('O produto mais vendido {}'.format(produtoMaisVendido))
