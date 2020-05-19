print('Ex 06 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

num1 = float(input('Escreva o numero 1 \n'))
num2 = float(input('Escreva o numero 2 \n'))
num3 = float(input('Escreva o numero 3 \n'))

if (num1>num2 and num1>num3):
    print('O numero', num1, 'é o maior')
if (num2>num1 and num2>num3):
    print('O numero', num2, 'é o maior')
if (num3>num1 and num3>num2):
    print('O numero', num3, 'é o maior')