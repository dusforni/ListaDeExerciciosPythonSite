print('Ex 04 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')


n = ['a','b','c','d','e','f','g','h','i','j']
index = {}
tamindex = 0
consoante = 0
for x in range(0, len(n)):
    if n[x] == 'a' or n[x] == 'e' or n[x] == 'i' or n[x] == 'o' or n[x] == 'u':
        pass
    else:
        consoante += 1
        index[tamindex] = x
        tamindex += 1

print(f'Foram {consoante} consoantes')
tamindex = len(index)
print('São elas: ', end="")
for x in range(0, tamindex):
    print(n[index[x]], "" , end="")