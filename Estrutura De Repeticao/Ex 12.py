print('Ex 12- Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Informe um numero o qual você quer ver a tabuada? - de 1 a 10\n'))
while n<1 or n>10:
    n = int(input('Informe um numero o qual você quer ver a tabuada? - de 0 a 10\n'))

print('Tabuada do', n)

for x in range(1,11):
    res = n*x
    print(n,'x',x,'=', res)