print('Ex 06 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

medias = []
nomes = []
media = 0
for x in range(0,20):
    nomes.insert(x, input(f'Nome do aluno {x+1}'))
    for y in range(0,4):
        media += float(input(f'Nota da prova {y+1}:'))

    medias.insert(x, media/4)
    media = 0
    print('\n'*2)

for x in range(0,20):
    if medias[x] >= 7:
        print(f'{nomes[x]} - {medias[x]}')
