print('Ex 05 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

n = []
p = []
i = []
ppar = pimpar = 0
for x in range(0,20):
    n.insert(x, int(input(f'Escreva um numero: {x+1}')))
    if n[x]%2 == 0:
        p.insert(ppar,n[x])
        ppar += 1
    else:
        i.insert(x, n[x])
        pimpar += 1


for x in range(0,20):
    print(n[x], " ", end="")
print('FIM NUMEROS\n')
for x in range(0,len(p)):
    print(p[x], " ", end="")
print('FIM PAR\n')
for x in range(0,len(i)):
    print(i[x], " ", end="")
print('FIM IMPAR')
