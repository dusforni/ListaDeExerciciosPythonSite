print('Ex 11 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

sal = float(input('Qual é o salario atual do funcionário?\n'))
print('Salário antes do reajuste era', sal, 'reais')
if(sal>=1500):
    salNovo = sal*1.05
    print('Percentual aplicado foi de 5%')

elif(700 <= sal < 1500):
    salNovo = sal*1.10
    print('Percentual aplicado foi de 10%')
elif(280 <= sal < 700):
    salNovo = sal*1.15
    print('Percentual aplicado foi de 15%')
else:
    salNovo = sal*1.20
    print('Percentual aplicado foi de 20%')

print('Foi aumentado', salNovo - sal, 'reais no seu salário')
print('Então, seu novo salário é de', salNovo)