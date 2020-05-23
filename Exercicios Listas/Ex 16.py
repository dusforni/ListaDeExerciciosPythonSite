print('Ex 16 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

faixa = [0,0,0,0,0,0,0,0,0]

vendas = sal = indFaixa = 0
while vendas != -1:
    vendas = float(input('Quantos reais o vendedor vendeu? -1 para sair \n'))
    while vendas<-1:
        vendas = float(input('Quantos reais o vendedor vendeu? - positivo \n'))
    if vendas == -1:
        pass
    else:
        sal = 200+0.09*vendas
        indFaixa = int((sal//100)-2)

        if indFaixa > 8:
            indFaixa = 8

        faixa[indFaixa] = faixa[indFaixa] + 1
        continuar = vendas
for x in range(0, len(faixa)):
    if x != (len(faixa)-1):
        print(f'{(x+2)*100} - {(x+3)*100-1} faixa salarial: {faixa[x]}')
    else:
        print(f'{(x+2)*100} em diante            : {faixa[x]}')


