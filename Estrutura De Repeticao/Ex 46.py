print('Ex 46 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

nomes = ['Primeiro', 'Segundo', 'Terceiro', 'Quarto', 'Quinto']
saltos = [0.0,0.0,0.0,0.0,0.0]
maior = menor = total = salto = 0
nome = 'o'

while nome != '':
    nome = input('Nome do atleta: ')
    if nome != '':
        for x in range(0,5):
            salto = float(input(f'{nomes[x]} salto:'))
            saltos[x] = salto
            if x == 0:
                maior = saltos[x]
                menor = saltos[x]
            if maior < saltos[x]:
                maior = saltos[x]
            if menor > saltos[x]:
                menor = saltos[x]

        print('\n'*5)
        print(f'Atleta: {nome}')
        for x in range(0,5):
            print(f'{nomes[x]} Salto: {saltos[x]} m')
        print(f'\nMelhor salto: {maior} m')
        print(f'Pior salto: {menor} m')

        saltos.remove(menor)
        saltos.remove(maior)
        for x in range(0,len(saltos)):
            total += saltos[x]


        total = total / len(saltos)
        print(f'Média dos demais saltos: {total} m')
        print('\nResultado final:')
        print(f'\n{nome} - {total} m')
        print('\n'*2)
