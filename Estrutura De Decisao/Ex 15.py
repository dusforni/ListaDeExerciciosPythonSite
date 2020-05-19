print('Ex 15 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

print('Escreva os lados de um triangulo')
verdade = 0
lado1 = float(input('Lado 1\n'))
lado2 = float(input('Lado 2\n'))
lado3 = float(input('Lado 3\n'))

#Verifica se é triangulo
if(lado1< lado2+lado3):
    verdade = verdade + 1
if(lado2< lado1+lado3):
    verdade = verdade + 1
if (lado3 < lado2 + lado1):
   verdade = verdade + 1

if (verdade==3):
    print('É um triângulo')

    if (lado1==lado2==lado3):
        print('É um triangulo equilátero')
    elif (lado1 == lado2 and lado2 != lado3) or (lado2==lado3 and lado2 != lado1) or (lado1==lado3 and lado1 != lado2):
        print('É um triangulo Isósceles')
    else:
        print('É um triangulo escaleno')

if (verdade<3):
    print('Não é um triangulo')

