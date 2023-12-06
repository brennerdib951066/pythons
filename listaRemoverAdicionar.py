#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
produtos = ['apple tv','mac','iphone x','ipad','apple warch','mac book','airpods']


##########################################################

# Adicionar o iphone 11
print('produtos {} sem alteração\n'.format(produtos))
produtos.append('iphone 11') # Adicionando
print('produtos {} Adicionado o iphone 11 alteração\n'.format(produtos))

# Remover o iphone x com o remove ou pop

produtos.remove('iphone x')
print('Removendo o produto iphone x {} '.format(produtos))

produtoRemovido = produtos.pop(2) # Pode remover e armazenar em uma variavel
print('O produto removido da lista {}'.format(produtoRemovido))

# Verificando se existe o produto na lista com if

produtoRemovido = "apple tv"
if produtoRemovido not in produtos:
    print('O produto {} não contem na lista'.format(produtoRemovido))
else:
    print('{} É um produto existente'.format(produtoRemovido))

# Verificando com try e except
try:
    produtos.remove('iphone 11')
    print('Foi removido')
except:
    print('Aldo deu errado')
