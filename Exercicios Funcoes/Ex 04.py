print('Ex 04 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def positivo(x):
    if x> 0:
        return 'P'
    else:
        return 'N'

x = int(input('numero?'))

retorna = positivo(x)
print(retorna)
