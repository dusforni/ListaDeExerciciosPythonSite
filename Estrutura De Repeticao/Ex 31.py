print('Ex 31 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

precos = {}
posProd : int #Define a posição do produto
fim = 1

posProd = 0
soma = 0
print('Para finalizar digite 0')
while fim != 0:
    print('Produto ', posProd+1, end="")
    precos[posProd] = float(input(': \n'))
    fim = precos[posProd]
    soma = precos[posProd] + soma
    posProd = posProd + 1

print('Total:', soma)
din = float(input('Valor que o cliente forneceu?'))
while din<soma:
    din = float(input('Insuficiente - Valor que o cliente forneceu?'))
print('')
print('')

print('Lojas Tabajara')

for x in range(0, len(precos)):
    print('Produto', x+1,': R$', precos[x])

print('Total:', soma)
print('Dinheiro:', din)
troco = din - soma

print('Troco:', troco)
