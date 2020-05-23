print('Ex 08 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

i = []
a = []

for x in range(0,5):
    i.insert(x,int(input(f'Informe a idade da {x+1} pessoa')))
    a.insert(x, float(input(f'Informe a altura da {x+1} pessoa')))

i.reverse()
a.reverse()


for x in range(0,5):

    print(f'Idade: {i[x]} , Altura: {a[x]}')