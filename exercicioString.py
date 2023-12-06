#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
cpf = input('Digite seu cpf(Insira apenas numeros)')


##########################################################


# Tratar espacos no inicio e no final
cpf = cpf.strip()
# Tratar os .Pontos
cpf = cpf.replace('.','')
# Tratrar os tracos
cpf = cpf.replace('-','')
print(len(cpf))
if len(cpf) == 11 and cpf.isnumeric():
    print('Dados inseridos corretamente {}'.format(cpf))
else:
    print('Dados completamente errados')
