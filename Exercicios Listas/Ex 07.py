print('Ex 07 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

n = []
soma = 0
mult = 1
for x in range(0,5):
    n.insert(x, int(input(f'Escreva o numero {x+1}')))
print('Os numeros:' , end="")
for x in range(0,5):
    soma += n[x]
    mult *= n[x]
    print(n[x], " ", end="")

print(f'\n Soma: {soma} - Mult: {mult} ')