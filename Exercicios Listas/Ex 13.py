print('Ex 13 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')


mes = ['Janeiro','Favereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
temp = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
media = 0
for x in range(0,12):
    temp[x] = float(input(f'Qual foi a temperatura média do mês de {mes[x]}'))
    media += temp[x]
media = media / 12
for x in range(0,12):
    if temp[x]>media:
        print(f'O mês de {mes[x]} fez {temp[x]}')