print('Ex 03 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

Sexo = input('Qual é o seu sexo? F/M \n')

if(Sexo == 'F' or Sexo == 'f'):
    print('Feminino')
elif(Sexo == 'M' or Sexo == 'm'):
    print('Masculino')
else:
    print('Sexo inválido')