print('Ex 13- Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0]
n[0] = int(input('primeiro numero (base)\n'))
n[1] = int(input('segundo numero (exponencial)\n'))
res = n[0]

for x in range(1,n[1]):
    res = res*n[0]

print(res)