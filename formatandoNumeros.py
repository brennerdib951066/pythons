#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
email       = 'brennebne@gmail.com'
custo       = 500
faturamento = 270
lucro       = faturamento - custo

custo2      = 5000
faturamento2= 2700
lucro2      = faturamento2 - custo2

imposto     = 0.14568
preco       = 100
valorImposto= round(preco * imposto,2)
##########################################################

print('Meu email não é{:>50} lallala'.format(email)) #Alinhando o texto depois das chaves para direita

print('Meu email não é{:^50} lallala'.format(email)) #Alinhando o texto depois das chaves para o centro

print('Meu custo é {:+}\nMeu Faturamento é {:+}\nMeu lucro é de {:+}'.format(custo,faturamento,lucro)) # Na aritimética o resultado aparecerá positivo ou negativo

print('Meu custo é {:+,}\nMeu Faturamento é {:+,}\nMeu lucro é de {:+,}'.format(custo2,faturamento2,lucro2)) # Na aritimética o resultado aparecerá separado com virgula

print('Meu custo é {:.2f}\nMeu Faturamento é {:.2f}\nMeu lucro é de {:.2f}'.format(custo2,faturamento2,lucro2)) # Definindo a quantidade de casas decimais com o .(ponto)2f

print('Meu custo é {:.2%}\nMeu Faturamento é {:.2%}\nMeu lucro é de {:.2%}'.format(custo2,faturamento2,lucro2)) # Definindo a quantidade de casas decimais e a porcentagem com o .(ponto)2%

print('Meu custo é R$ {:,.2f}\nMeu Faturamento é R$ {:,.2f}\nMeu lucro é de R$ {:,.2f}'.format(custo2,faturamento2,lucro2))
lucroTexto = 'R$ {:_.2f}'.format(lucro)
print(lucroTexto.replace('.',',').replace('_','.'))

# Definindo a quantidade de casas decimais e formatando para moeda brasileira .(ponto)2f

print('O imposto é no valor de {}'.format(valorImposto)) # Definindo a quantidade de casas decimais e a porcentagem com o .(ponto)2%
