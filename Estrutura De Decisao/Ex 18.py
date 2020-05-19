import sys

print('Ex 18 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

dia = int(input('Que dia é hoje? dd/mm/aaaa \n'))
mes = int(input('Que mês estamos? Formato dd/mm/aaaa \n'))
ano = int(input('Que ano estamos? dd/mm/aaaa \n'))

if mes > 12 or mes < 1:
    print('Data inválida, mês não existe')
    sys.exit()
if mes%2 != 0 and (1>dia or dia>31):
    print('Data inválida, dia não condiz')
    sys.exit()
if mes%2==0 and (1>dia or dia>30):
    print('Data inválida, dia não condiz')
    sys.exit()
if ano%4==0 and mes == 2 and (1>dia or dia>29):
    print('Data inválida, ano bissexto, dia não condiz')
    sys.exit()
if ano%4!=0 and mes == 2 and (1>dia or dia>28):
    print('Data inválida, ano não bissexto, dia não condiz')
    sys.exit()

print('A data foi:',dia,'/',mes,'/',ano)
