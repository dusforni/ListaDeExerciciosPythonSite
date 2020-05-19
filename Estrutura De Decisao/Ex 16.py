print('Ex 16 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

import sys #Para fazer sistema out

print('Sabendo que uma equação de segundo grau é dada por: ax^2+bx+c, então \n')

a = float(input('Informe a \n'))
if(a == 0):
    print('Equação não é de segundo grau')
    sys.exit()
b = float(input('Informe b \n'))

c = float(input('Informe c \n'))

delta = b**2-4*a*c

if(delta<0):
    print('Não existe raizes reais')
    sys.exit()
elif(delta==0):
    print('Apenas uma raiz')
    raiz = -b/(2*a)
    print(raiz)
else:
    print('Duas raizes reais')
    raiz1 = (-b + delta) / (2 * a)
    raiz2 = (-b - delta) / (2 * a)
    print('Raiz 1', raiz1, 'Raiz 2', raiz2)