print('Ex 32 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Qual numero você quer fazer o fatorail?\n'))
print('Fatorial:', n)
print(n,'! =', end="")
total = 1

for x in range(0,n-1):
    total = (n - x) * total
    print("", n-x,'.', end="")

print(' 1 = ', end="")
print(total)


