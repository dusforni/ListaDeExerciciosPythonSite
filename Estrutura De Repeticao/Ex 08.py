print('Ex 08 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0]
n[0] = float(input('Informe numero 1 \n'))
n[1] = float(input('Informe numero 2 \n'))
n[2] = float(input('Informe numero 3 \n'))
n[3] = float(input('Informe numero 4 \n'))
n[4] = float(input('Informe numero 5 \n'))
soma = 0
div = 0
for x in n:
    soma = soma + x
    div = div + 1

media = soma / div

print('Some é:', soma)
print('Média é:', media)