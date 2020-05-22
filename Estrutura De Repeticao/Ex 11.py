print('Ex 11- Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')


n = [0, 0]
n[0] = int(input('Escolha o primeiro numero inteiro \n'))
n[1] = int(input('Escolha o segundo numero inteiro \n'))

caminho = 1
soma = 0
if (n[0]>n[1]):
    dist = n[0]-n[1]
    while caminho < dist:
        n[1]=n[1]+1
        caminho=caminho + 1
        print(n[1])
        soma = soma+n[1]
else:
    dist = n[1]-n[0]
    while caminho < dist:
        n[0]=n[0]+1
        caminho=caminho + 1
        print(n[0])
        soma= soma+n[0]

print('A soma é:',soma)
