print('Ex 33 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

temperatura = {}
tempPoint = 0
temperatura[tempPoint] = 0
inserir = 's'

soma = 0
media = 0

while inserir == 's':
    print('Medida', tempPoint+1, end=' ')
    temperatura[tempPoint] = float(input('Temperatura: \n'))
    if(tempPoint == 0):
        maior = temperatura[tempPoint]
        menor = temperatura[tempPoint]
    soma = temperatura[tempPoint] + soma
    if (maior<temperatura[tempPoint]):
        maior = temperatura[tempPoint]
    elif (menor>temperatura[tempPoint]):
        menor = temperatura[tempPoint]
    tempPoint = tempPoint + 1
    inserir = input('Inserir mais um? (s/n)')

tamanho = len(temperatura)
media = soma/tamanho
print('Média:', media)
print('Maior:', maior)
print('Menor:', menor)





