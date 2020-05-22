print('Ex 24 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0,0,0,0,0,0]

div = 0
soma = 0
for x in range(0, len(n)):
    print("Nota", x+1, end="")
    n[x] = int(input(': \n'))
for x in range(0, len(n)):
    soma = soma + n[x]
    div = div +1
total = soma/div
print('Média é', total)