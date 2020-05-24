print('Ex 08 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def digitos(x):
    x = str(x)
    x = len(x)
    return x


num = int(input('Digite um numero!'))

y = digitos(num)
print(f'{y} digitos')