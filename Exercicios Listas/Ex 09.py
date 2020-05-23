print('Ex 09 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

A = []
total = 0
for x in range(0,10):
    A.insert(x, int(input(f'{x+1}º numero inteiro: ')))
    print(A[x])
for x in range(0,10):
    total += A[x]**2

print(f'Soma do quadrado: {total}')