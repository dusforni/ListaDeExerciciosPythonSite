print('Ex 12 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

i = [11,12,13,14,15,11,12,13,14,15,11,12,13,14,15,11,12,13,14,15,11,12,13,14,15,11,12,13,14,15]
a = [1.1,1.2,1.4,1.2,1.1,1.5,1.1,1.3,1.0,1.8,1.1,1.2,1.4,1.2,1.1,1.5,1.1,1.3,1.0,1.8,1.1,1.2,1.4,1.2,1.1,1.5,1.1,1.3,1.0,1.8]
media = anao = 0
for x in range(0,30):
    media += a[x]
media/30
for x in range(0,30):
    if i[x]>13 and a[x]<media:
        anao += 1

print(f'Numero de anoes: {anao}')