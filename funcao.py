#!/usr/bin/env python3

####################VARIAVEIS DO PROGRAMA##################
arquivo = '/home/brenner/Imagens/imagensBubble/loginBubble/acessoBubble.png'
email = 'setor.administrativo.dib@teste.com'
senha = '652516'


##########################################################

#a = 10
#b = 20
def acesso(email,senha):
    login = senha
    return login
print(acesso)


login = input('Setor de Acesso:  ')
if login == 'comercial':
    email = 'setor.comercial.dib@teste.com'
    resultado = acesso(email,senha)
    print(acesso)
elif login == 'financeiro':
    email = 'setor.financeiro.dib@teste.com'
elif login == 'posvendas':
    email = 'setor.posvendas.dib@teste.com'
else:
    print('Email inválido!')
    try:
        print('Certo')
    except:
        print('Nada')


#for i in range(3):
    #time.sleep(1)
    #if i == 0:
        #bot.click(bot.locateCenterOnScreen(arquivo,confidence=0.8),duration=0.25)
        #bot.write(email)
    #else:
        #arquivoIncremente = arquivo.replace('acessoBubble','acessoBubble_{}'.format(i))
        #print(arquivoIncremente)
        #bot.click(bot.locateCenterOnScreen(arquivoIncremente,confidence=0.8),duration=0.25)
        #bot.write(senha)
