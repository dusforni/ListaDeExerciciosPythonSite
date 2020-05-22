print('Ex 14 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0,0,0,0,0,0]
par = 0
impar = 0
for x in range(0,10):
    print('Numero', x+1)
    n[x] = int(input('Escreva o numero inteiro'))
    if (n[x]%2==0):
        par = par+1
    else:
        impar = impar+1

print('Pares', par)
print('Impares', impar)