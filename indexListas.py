#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
produtos=['tv','celular','tablet','mouse','teclado','geladeira','forno']
estoques=['100','150','100','120','70','90','80']

# Verificando se existe o produto nos dados recebidos
produto = input('Insira o produto')
i = produtos.index('geladeira')
if produto in produtos:
    iUsuario = produtos.index('geladeira')
    print('O produto {} Existe'.format(produto))
else:
    print('O produto {}, não existe'.format(produto))
##########################################################


#qtdsEmEstoque = estoques[i]
#print('O produto {} está no estoque {}'.format(produtos[i],qtdsEmEstoque))
