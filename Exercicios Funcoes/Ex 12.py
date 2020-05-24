print('Ex 12 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

import random
def embaralha(palavra):
    ralvaap = list(palavra)
    random.shuffle(ralvaap)
    tam = len(ralvaap)
    fPalavra = ''
    for x in range(0, tam):
        fPalavra += ralvaap[x]
    fPalavra = fPalavra.upper()
    return fPalavra

palavra = input('Escreve ai!')

ralvaap = embaralha(palavra)
print(ralvaap)