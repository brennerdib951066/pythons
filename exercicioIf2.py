#!/usr/bin/env python3
metaVendas          = 1000
bonus               = 0
vendas_funcionario1 = 1000
vendas_funcionario2 = 770
vendas_funcionario3 = 2700

if vendas_funcionario1 >= metaVendas:
    if vendas_funcionario1 >= 20000:
        bonus = 0.15 * vendas_funcionario1
        print('Ganhou 15% {} o 1Funcionario'.format(bonus))
    else:
        bonus = 0.10 * vendas_funcionario1
        print('Ganhou 10% {} o 1Funcionario'.format(bonus))
else:
    bonus = 0
    print('FUncionario 1 ganhou {}'.format(bonus))
if vendas_funcionario2 >= metaVendas:
    if vendas_funcionario2 >= 20000:
        bonus = 0.15
        print('Ganhou 15% {} o 2Funcionario'.format(bonus))
else:
    bonus = 0
    print('Nao ganhou nada o funcionario 2 {}'.format(bonus))
if vendas_funcionario3 >= metaVendas:
    if vendas_funcionario3 >= 2000:
        bonus = 0.15 * vendas_funcionario3
        print('Ganhou 15% {} o 3Funcionario'.format(bonus))
else:
    bonus = 0
    print('Não ganhou nada o funcionario 3 {}'.format(bonus))
#Resposta:
#O funcionário 1 ganhou 100 de bônus
#O funcionário 2 ganhou 0 de bônus
#O funcionário 3 ganhou 270 de bônus

#### 2. Cálculo de bônus com uma nova regra

#- Agora, crie um novo código que calcule e dê um print no bônus dos funcionários novamente. Porém há uma nova regra nesse 2º caso:

#A meta é 1000 vendas<br>
#Agora, os funcionários que venderem muito acima da meta ganham mais bônus do que os outros. Então o bônus é definido da seguinte forma:<br>

#- Se vendas funcionário for maior ou igual a 2000, então o bônus é de 15% sobre o valor de vendas
#- Se vendas funcionário for menor do que 2000 e maior ou igual a 1000, então o bônus é de 10% sobre o valor de vendas
#- Se vendas funcionário for menos do que 1000 então o bônus do funcionário é de 0.

#Use as mesmas variáveis de vendas_funcionários
#"""

##crie seu código aqui
##obs: há 2 formas de fazer, com if dentro de if ou então com if e elif. Escolha a que você preferir

#"""Resposta:
#O funcionário 1 ganhou 100 de bônus
#O funcionário 2 ganhou 0 de bônus
#O funcionário 3 ganhou 405 de bônus
#"""
