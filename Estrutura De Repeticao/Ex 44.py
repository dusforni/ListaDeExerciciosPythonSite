print('Ex 44 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

voto = 1
joao = jose = marina = maria = branco = nulo = votos =0

while voto != 0:
    voto = int(input('Quem você quer votar? \n 1- João \n 2- José \n 3- Marina \n 4- Maria \n 5- Nulo \n 6- Branco \n'))
    while 0>voto or voto>6:
        voto = int(input('**VOTO INVÁLIDO** \n Quem você quer votar? \n 1- João \n 2- José \n 3- Marina \n 4- Maria \n 5- Nulo \n 6- Branco \n '))
    votos += 1
    if voto == 1:
        joao += 1
    if voto == 2:
        jose += 1
    if voto == 3:
        marina += 1
    if voto == 4:
        maria += 1
    if voto == 5:
        nulo += 1
    if voto == 6:
        branco += 1
votos -= 1
print('\n'*5)
print(f'Voto João: {joao}')
print(f'Voto José: {jose}')
print(f'Voto Marina: {marina}')
print(f'Voto Maria: {maria}')
print(f'Voto nulo:{nulo}')
print(f'Voto branco:{branco}')
print(f'%Nulos: {round(nulo/votos*100,2)}')
print(f'%Brancos: {round(branco/votos*100,2)}')