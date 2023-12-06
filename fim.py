#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
texto = 'brenner@gmail.com.'
custo = 5000
faturamento = 27000
lucro = faturamento -custo
imposto = 0.15758
preco = 100
valorImposto = round(preco*imposto,1)
#valorImposto = preco*imposto
##########################################################

#if texto.endswith('.'):
    #print('Termina')
    #print(texto)
    #texto = texto.replace('com.','com')
    #print(texto)
#else:
    #print('Não termina')

#print('MEU {:>50}'.format(texto))

lucroTexto = 'R${:_.2f}'.format(lucro)
print(lucroTexto.replace('.',',').replace('_','.'))
print('Seu imposto arredondado é: {}'.format(valorImposto))
