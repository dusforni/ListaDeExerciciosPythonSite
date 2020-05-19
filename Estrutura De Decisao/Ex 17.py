print('Ex 17 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

ano = int(input('Informe um ano \n'))

ResAno = ano%4
if(ResAno==0):
    print('Ano bissexto')
else:
    print('Não é bissexto')