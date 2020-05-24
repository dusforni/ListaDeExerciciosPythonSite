print('Ex 10 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')
import random
dado1 = [1,2,3,4,5,6]
dado2 = [1,2,3,4,5,6]

def Craps(ponto):

    random.shuffle(dado1)
    random.shuffle(dado2)
    resultado = dado1[0]+dado2[0]

    print(f'Você tirou {dado1[0]} e {dado2[0]} totalizando {resultado}')

    if (resultado == 7 or resultado == 11) and ponto == 0:
        print('Você ganhou!')
        ponto = -1
    elif (resultado == 2 or resultado == 3 or resultado == 12) and ponto == 0:
        print('Craps, você perdeu!')
        ponto = -1
    elif resultado == ponto:
        print('Você ganhou!')
        ponto = -1
    elif ponto>=0 and resultado == 7:
        print('Você perdeu!')
        ponto = -1
    elif ponto == 0:
        ponto = resultado



    return ponto


ponto = 0

while ponto != -1:
    ponto = Craps(ponto)
