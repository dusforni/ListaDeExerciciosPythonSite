print('Ex 18 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

Cvoto = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

voto = 30
nvoto = 0
porcentagem = 0
maior = 0
while voto != 0:
    voto = int(input('Número do jogador (0=fim): '))
    if voto<0 or voto>23:
        print('Informe um valor entre 1 e 23 ou 0 para sair!')
    elif voto==0:
        pass
    else:
        nvoto+=1
        Cvoto[voto] += 1
print('\n'*2)
print('RESULTADO DA VOTAÇÃO')
print(f'Foram computador {nvoto} votos')
print('Jodador     Votos    Porcentagem')
for x in range(0,23):
    if Cvoto[x] == 0:
        pass
    else:
        print(f'{x}           {Cvoto[x]}          {Cvoto[x]/nvoto*100}')
    if maior < Cvoto[x]:
        maior = x

print(f'O melhor jogador foi o número {maior}, com {Cvoto[maior]} votos, correspondendo a {Cvoto[maior]/nvoto*100} do total de votos.')