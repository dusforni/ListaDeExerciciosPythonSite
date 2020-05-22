print('Ex 28 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

cd = int(input('Quantos CDs você tem?\n'))
pCD = {}
soma = 0
media = 0
for x in range(0,cd):
    print('Qual é o valor do CD', x+1, end="")
    pCD[x] = float(input(':\n'))
    soma = soma + pCD[x]

media  = soma / cd
print("Você gastou um total de",soma,'reias na sua coleção')
print('Você gastou em média:', media,'por CD')

