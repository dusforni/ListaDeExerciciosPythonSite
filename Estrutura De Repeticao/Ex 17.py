print('Ex 17 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Qual numero você deseja fazer um fatorial? \n'))
n1= n
n2 = 0
if n == 0:
    n2 = 1
for x in range(1,n):
    n2 = n1*(n-x)
    n1 = n2

print(n2)


