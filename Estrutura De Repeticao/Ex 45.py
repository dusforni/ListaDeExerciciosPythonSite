print('Ex 45 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

r = []
aluno = []

nomr = res = prox = respT = 'S'
teste = total = maior = maiorPoint = menor = menorPoint = media = notaTotal = 0

for x in range(0,10):
    respT = input(f'Resposta da questão {x+1}')
    respT = respT.upper()
    while respT != 'A' and respT != 'B' and respT != 'C' and respT!= 'D' and respT != 'E':
        respT = str(input(f'**RESPOSTA INVALIDA \n Resposta questão {x + 1}'))
        respT= res.upper()
    r.insert(x,f'{respT}')
while prox == 'S':
    total = 0
    print('\n'*5)
    nome = str(input('Nome do Aluno?'))
    aluno.insert(teste,f'{nome}')
    for x in range(0,len(r)):

        res = str(input(f'Resposta questão {x+1}'))
        res = res.upper()
        while res != 'A' and res != 'B' and res != 'C' and res != 'D' and res != 'E':
            res = str(input(f'**RESPOSTA INVALIDA \n Resposta questão {x+1}'))
            res = res.upper()
        if res == r[x]:
            total += 1
        if x == len(r):
            teste += 1
        if len(aluno) == 1:
            maior = total
            menor = total
            print('entrou teste')

    if maior < total:
        maior = total
        maiorPoint = teste
        print('entrou maior')
    if menor > total:
        menor = total
        menorPoint = teste
    teste += 1
    notaTotal += total
    prox = str(input('Deseja fazer mais um teste? (s/n)'))
    prox = prox.upper()

print(f'O maior acerto foi: {maior}, do aluno {aluno[maiorPoint]}')
print(f'O menor acerto foi: {menor}, do aluno {aluno[menorPoint]}')
print(f'O total de testes foi: {teste}')
print(f'A média de notas foi: {notaTotal/teste}')