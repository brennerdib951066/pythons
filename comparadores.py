#!/usr/bin/env python3

#faturamento1 = 2500
#faturamento2 = 2200
#email        = 'brennerbnegmail.com'

#if faturamento1 == faturamento2:
    #print('Os faturamnetos são iguais')
#else:
    #print('Os faturamentos SÃO DIFERENTES')
#email = input('Digite aqui seu email    ')
#if not '@' in email: ###Verificando se nao contem o @ no input
    #print('Email errado')
#else:
    ##print('Email Valido')
    #pass #Caso queira que não mostre nada ou faça nada colocar PASS na codicional

metaFuncionario   = 10000
metaEmpresa       = 250000
vendasFuncionario = 9000
vendasEmpresa     = 2000000

#if vendasFuncionario > metaFuncionario and vendasEmpresa > metaEmpresa:
    #bonus = 0.03 * vendasFuncionario
    #print('Muito Bem ganhou seu bonus, pois cumpristes a sua meta juntamnete com da empresa!\n{}'.format(bonus))
#else:
    #print('Infelizmente esse mes nao cumpriu sua meta!')

nota = 8
metaNota = 9

if nota >= metaNota or (vendasFuncionario > metaFuncionario and vendasEmpresa > metaEmpresa):
    bonus = 0.03 * vendasFuncionario
    print('Pela sua avalição {}, ganhou o bonus'.format(nota))
else:
    print('Não ganhou seu boninho')
