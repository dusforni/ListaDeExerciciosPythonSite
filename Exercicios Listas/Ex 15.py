print('Ex 15 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

x = []
indice = 0
fim = 0
tam = media = soma = amedia = bsete = conf = 0
while fim != -1:
    fim = float(input(f'numero {indice+1}'))
    if fim == -1:
        pass
    else:
        x.insert(indice,fim)
        indice = indice+1
tam = len(x)
print('a. ')
print(f'Total de numeros inseridos: {tam}')

print('b. ')
for y in range(0,tam):
    print(x[y], " ", end="")
print('\n'*2)
x.reverse()
print('c. ')
for y in range(0,tam):
    print(x[y])
    soma += x[y]
print('\n'*2)
print('d. ')
print(f'Soma: {soma}')
media = soma / tam
print('\n'*2)
print('e. ')
print(f'Media: {media}')

print('\n'*2)
print('f. ')
print(f'Acima da media: ', end="")
for y in range(0, tam):
    if x[y]>media:
        amedia += 1
        print(x[y], end=" ")
print(f'totalizando {amedia} numeros')

print('\n'*2)
print('f. ')
print(f'Abaixo de sete: ', end="")
for y in range(0, tam):
    if x[y]<7:
        bsete += 1
        print(x[y], end=" ")
print(f'totalizando {amedia} numeros')

print('\n'*2)
print('*'*3,' TERMINOU ','*'*3)

