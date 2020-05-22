print('Ex 15 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Escolha até qual n-ésimo termo você quer a série de Fibonacci'))

x = 1
y = 1
z = 0
print(x)
print(y)
for a in range(1,n+1):
    z = x+y
    print(z)
    y = x
    x = z