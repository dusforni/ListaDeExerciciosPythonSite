print('Ex 10 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

turno = input('Qual turno você estuda? (M, V ou N) \n')

if(turno == 'M' or turno == 'm'):
    print('Bom dia!')
elif(turno== 'V' or turno =='v'):
    print('Boa tarde!')
elif(turno =='N' or turno =='n'):
    print('Boa noite!')
else:
    print('Valor inválido')