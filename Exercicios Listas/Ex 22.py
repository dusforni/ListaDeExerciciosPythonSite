print('Ex 22 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

mouse = []
defeito = ['Necessita de esfera                ', 'Necessita de limpeza               ', 'Necessita troca do cabo ou conector', 'Quebrado ou inultilizado           ']
defeitos = [0,0,0,0]
id = 'o'
indicador = 0
round = 0
while id != '':
    id = input('Mouser ID: ')
    if id != '':
        indicador = input('Defeito do mouse: 1 a 4 ')

        while indicador.isalpha():
            indicador = input('Defeito do mouse: 1 a 4 - Errou')
        indicador = int(indicador)
        if 1 <= indicador<=4:
            indicador = indicador - 1
            mouse.insert(round, id)
            defeitos[indicador] += 1
            round += 1
        else:
            print('invalido')

print(f'Quantidade de mouse: {round}')
print(f'Situação                             Quantidade -  Percentual')
for x in range(0,4):
    if round != 0:
        print(f'{x+1} - {defeito[x]} - {defeitos[x]} -       {defeitos[x]/round*100}%')
    else:
        print('Teste não rodou')