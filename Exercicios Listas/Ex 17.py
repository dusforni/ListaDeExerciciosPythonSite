print('Ex 17 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

saltos = []
nome = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']

atleta = 'atleta'
total = 0
while atleta != '':
    print('\n'*2)
    atleta = input('Nome do atleta: ')
    if atleta == '':
        pass
    else:
        for x in range(0,5):
            saltos.insert(x, float(input(f'{nome[x]} salto:  ')))
        for x in range(0,5):
            print(f'{nome[x]} salto: {saltos[x]} m')
        print(' RESULTADO FINAL ')
        print(f' ATLETA: {atleta}')
        print('Resultados:', end=" ")
        for x in range(0,5):
            print(f'{saltos[x]}', end = " - ",)
            total += saltos[x]
        total /= 5
        print(f'\n Média dos saltos: {total}')