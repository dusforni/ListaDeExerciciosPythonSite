print('Ex 21 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')
veiculo = ['Fusca','Gol  ', 'HB20 ', 'UNO  ','PGOUT ']
consumo = [10,8,6,14,9]
menor = 100000000
menorP = 0
print("COMPARATIVO DE CONSUMO DE COMBUSTÍVEL")

for x in range(0,5):
    print(f'Vaículo: {x+1}')
    print(f'Nome: {veiculo[x]}')
    print(f'Km/Litro: {consumo[x]}')
    print('\n')

print('RELATÓRIO FINAL')
for x in range(0,5):
    print(f'{x+1} - {veiculo[x]} - {consumo[x]} - {round((consumo[x]**-1)*1000,2)} litros - R$ {round(2.25*(consumo[x]**-1)*1000,2)} ')
    if menor > consumo[x]:
        menor = consumo[x]
        menorP = x
print(f' \n O menor consumo é do {veiculo[menorP]}')