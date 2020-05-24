print('Ex 13 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def limites(l):
    if l<1:
        l = 1
    if l>20:
        l = 20
    return l



def quadrado(l,c):
    for x in range(1,l+1):
        if c == 1:
            print('|')
        else:
            if x == 0 or x == l:
                print('|','-' * ( c - 2 ),'|')
            else:
                print('|', '+' * (c - 2), '|')


linhas = int(input('Quantidade de linhas?'))
colunas = int(input('Quantidade de colunas?'))
limites(colunas)
limites(linhas)
quadrado(linhas,colunas)