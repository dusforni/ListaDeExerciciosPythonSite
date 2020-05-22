print('Ex 47 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

notas = [0,0,0,0,0,0,0.0]
nota = maior  = maiorPoint = menor = menorPoint = media = total = nNota = 0
nome = input('Nome do atleta?')
for x in range(0, 7):
    notas[x] = float(input(f'Nota do jurado {x+1}\n'))

    if x == 0:
        maior = notas[x]
        menor = notas[x]
    if maior < notas[x]:
        maior = notas[x]
        maiorPoint = x
    if menor > notas[x]:
        menor = notas[x]
        menorPoint = x

print('\n'*5)
print(f'Atleta: {nome}')

for x in range(0, len(notas)):
    print(f'Nota: {notas[x]}')

print('\n'*2)
print(' ** Resultado final **')
print(f'Atleta: {nome}')
print(f'Melhor nota: {maior}')
print(f'Menor nota: {menor}')
notas.remove(maior)
notas.remove(menor)
for x in range(0, len(notas)):
    total += notas[x]
print(f'Média: {total/5}')
