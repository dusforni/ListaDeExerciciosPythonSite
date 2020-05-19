print('Ex 14 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

Nota1 = float(input('Escreva a nota 1 \n'))
Nota2 = float(input('Escreva a nota 2 \n'))
while 0>Nota1>10 :
    Nota1 = float(input('Nota 1 inválida, escreva novamente'))
while 0>Nota2>10:
    Nota2 = float(input('Nota 2 inválida, escreva novamente'))
media = (Nota1 + Nota2) / 2

if(media>=9):
    print('Conceito A')
    print('Nota foi:', media)
    print('Aprovado')
if (7.5<=media<9):
    print('Conceito B')
    print('Nota foi:', media)
    print('Aprovado')
if (6<=media<7.5):
    print('Conceito C')
    print('Nota foi:', media)
    print('Aprovado')
if (4<=media<6):
    print('Conceito D')
    print('Nota foi:', media)
    print('Reprovado')
if (media<4):
    print('Conceito E')
    print('Nota foi:', media)
    print('Reprovado')