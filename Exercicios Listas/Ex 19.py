print('Ex 19 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

Cvoto = [0,0,0,0,0,0]
sistema = ['Windows' , 'Unix   ' , 'Linux  ' , 'Netware' , 'Mac OS ' , 'Outro  ']
voto = 1
porcentagem = total = maior = maiorI = 0

while voto != 0:
    voto = input("Qual o melhor Sistema Operacional para uso em servidores?")
    while voto.isalpha():
        voto = input("Qual o melhor Sistema Operacional para uso em servidores? - 0 a 6")
    voto = int(voto)
    if 0<voto<=6:
        voto = voto -1
        Cvoto[voto]+=1
        total += 1
        voto = 100000
    else:
        print('Voto inválido')


print('Sistema Operacional     Votos   %')
print('-------------------     -----   ---')
for x in range(0, 6):
    print(f'{sistema[x]}                  {Cvoto[x]}      {Cvoto[x]/total*100}')
    if maior < Cvoto[x]:
        maior = Cvoto[x]
        maiorI = x

print('-------------------     -----   ---')
print(f'TOTAL                    {total}')

print('\n')
print(f'O Sistema Operacional mais votado foi o {sistema[maiorI]} com {maior} votos, correspondendo a {Cvoto[maior]/total*100} dos votos.')