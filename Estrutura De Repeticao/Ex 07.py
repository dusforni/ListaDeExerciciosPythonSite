print('Ex 07 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0]
n[0] = float(input('Informe numero 1 \n'))
n[1] = float(input('Informe numero 2 \n'))
n[2] = float(input('Informe numero 3 \n'))
n[3] = float(input('Informe numero 4 \n'))
n[4] = float(input('Informe numero 5 \n'))

maior = n[0]
maioratual = n[2]
mudou = 1
while mudou == 1:
    mudou = 0
    for x in n:
        if(maior < x):
            maior = x
            mudou = 1

print(maior)

