print('Ex 01 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def traingulo(n):
    for  x in range(1, n+1):
        for y in range(0, x):
            print(x, end=" ")
        print('\n', end="")


num = int(input('Até qual numero?'))
traingulo(num)