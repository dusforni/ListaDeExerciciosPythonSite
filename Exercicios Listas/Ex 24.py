print('Ex 24 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')
import random

dado = [1,2,3,4,5,6]
res = []

for x in range(0,100):
    random.shuffle(dado)

    res.insert(x, dado[1])

print(f' Um - {res.count(1)} \n Dois - {res.count(2)} \n Três - {res.count(3)} '
      f'\n Quatro - {res.count(4)} \n Cinco - {res.count(5)} \n Seis - {res.count(6)} \n')