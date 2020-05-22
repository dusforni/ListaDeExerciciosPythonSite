print('Ex 50 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')
aten = int(input('Até qual série n você deseja?'))
soma = 0
print('S  =  ', end="")
for x in range(1, aten+1):
    soma += 1/x
    print(f'{1}/{x}', end="")
    if x != aten:
        print(' + ', end="")
print(f' = {soma}')