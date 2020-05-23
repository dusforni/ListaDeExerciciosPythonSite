print('Ex 02 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

n = [1.10,1.20,1.30,1.40,1.50,1.60,1.70,1.80,1.90,2.00]

for x in range(0,len(n)):
    point = len(n) - x - 1
    print(n[point], " ", end ="")
#OU
n.reverse()
print('\n'*2)
for x in range(0,len(n)):
    print(n[x], " ", end="")