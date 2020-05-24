print('Ex 06 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def periodo(h):
    if h>=12:
        perio = 'P'
    else:
        perio = 'A'
    return perio

def saida(h, perio):
    if h>=12:
        h -= 12
    if perio == 'P':
        perio = 'P.M.'
    else:
        perio = 'A.M.'

    print(f'{h}:{mi} {perio}')

ho = 0
while ho != -1:
    ho = int(input('Horas? -1 para parar'))
    if ho == -1:
        pass
    else:
        mi = int(input('Minutos?'))

        perio = periodo(ho)
        saida(ho, perio)