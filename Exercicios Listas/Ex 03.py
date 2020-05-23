print('Ex 03 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

n = [10,9,8,5]

maior  = n[0]
menor = n[0]
media = 0
for x in range(0, len(n)):
    media += n[x]
    if maior < n[x]:
        maior = n[x]
    elif menor > n[x]:
        menor = n[x]
media = media/len(n)
print(f'Maior: {maior} \nMenor: {menor} \nMédia: {media}')