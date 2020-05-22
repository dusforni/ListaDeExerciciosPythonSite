print('Ex 26 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

eleitores = int(input('Numero de eleitores \n'))

votos = {}
c1 = 0
c2 = 0
c3 = 0
for x in range(0, eleitores):

    votos[x] = int(input('Vote! 1,2 ou 3\n'))
    while  1>votos[x] and votos[x]>3:
        votos[x] = int(input('Votos inválido! 1,2 ou 3\n'))
    if(votos[x]==1):
        c1 = c1 + 1
    elif(votos[x]==2):
        c2 = c2 +1
    else:
        c3 = c3 + 1

print('Candidato 1:', c1 , 'votos')
print('Candidato 2:', c2 , 'votos')
print('Candidato 3:', c3 , 'votos')