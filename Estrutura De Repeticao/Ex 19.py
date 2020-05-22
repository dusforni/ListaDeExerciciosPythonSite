print('Ex 19 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0,0,0,0,0,0,0]
y = 1;
z = 0

for x in range(0, len(n)):
    print('Insira o', y, end="")
    n[x] = float(input(' numero\n'))
    while 0>n[x] or 1000<n[x]:
        n[x] = float(input('Só pode numeros entre 0 a 1000, escreva novamente \n'))
    y = y+1



maior = n[0]
menor = n[0]
mudou = 1
soma = 0
while mudou == 1:
    mudou = 0
    for x in range(0, len(n)):
        if maior < n[x]:
            maior = n[x]
            mudou = 1
        if menor > n[x]:
            menor = n[x]
            mudou = 1

for x in range(0, len(n)):
    soma = soma + n[x]

print('Maior:', maior)
print('Menor:', menor)
print('Soma:', soma)