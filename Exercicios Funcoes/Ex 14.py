print('Ex 14 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')
#ESSE ALGORITMO NÃO ASSUME QUE A SOMA TEM QUE DAR 15
#MAIOR SOMA MÍNIMA = A soma mais baixa que dois conjuntos de numeros podem alcançar somando 9
#MENOR SOMA MÁXIMA = A soma mais alta que dois conjuntos de numeros podem alcaçar
num = [1,2,3,4,5,6,7,8,9]
todasLinhas = []
quadrados = []

def criaLinhas(num):
    for i in num:
        for j in num:
            for k in num:
                if i!=j and j!=k and k!=i : #Sabemos que tem que ser todos diferentes
                    if i+j+k>13 and i+j+k<18: #Pode-se afirmar que a MAIOR SOMA minima é 13 ( 9 + 2 + 1 com 6 + 4 + 3 )
                        possivel = [i,j,k]    #Pode-se afirmar que a MENOR SOMA máxima é 18 ( 9 + 5 + 4 com 8 + 7 + 3 )
                        todasLinhas.append(possivel)


def criaColunas(todasLinhas):
    for i in range(0,len(todasLinhas)):
        for j in range(0, len(todasLinhas)):
            for k in range(0,len(todasLinhas)):
                if sum(todasLinhas[i]) == sum(todasLinhas[j]) == sum(todasLinhas[k]): #Verifica Linhas
                        filtro = todasLinhas[i]+todasLinhas[j]+todasLinhas[k]
                        if filtro.count(1)==1 and filtro.count(2)==1 and filtro.count(3)==1 and \
                           filtro.count(4)==1 and filtro.count(5)==1 and filtro.count(6)==1 and \
                           filtro.count(7)==1 and filtro.count(8)==1 and filtro.count(9)==1: #Verifica se tá usando todos os numeros
                            if (filtro[0]+filtro[3]+filtro[6]) == (filtro[1]+filtro[4]+filtro[7]) == (filtro[2]+filtro[5]+filtro[8]) and \
                                (filtro[0] + filtro[4] + filtro[8]) == (filtro[2] + filtro[4] + filtro[6]): #Verifica Colunas e diagonal
                                    print(f'({filtro[0]} , {filtro[1]} , {filtro[2]}) \n({filtro[3]} , {filtro[4]} , {filtro[5]})\n({filtro[6]} , {filtro[7]} , {filtro[8]}) \n')
                                    quadrados.append(filtro)
criaLinhas(num)
criaColunas(todasLinhas)
