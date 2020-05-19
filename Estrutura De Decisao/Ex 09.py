print('Ex 09 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

num1 = float(input('Escreva o numero 1 \n'))
num2 = float(input('Escreva o numero 2 \n'))
num3 = float(input('Escreva o numero 3 \n'))

if (num1>num2 and num1>num3):
    maior = num1
    if(num2>num3):
        medio = num2
        menor = num3
    if(num3>num2):
        medio = num3
        menor = num2
if (num2>num1 and num2>num3):
    maior = num2
    if(num1>num3):
        medio = num1
        menor = num3
    if(num3>num1):
        medio = num3
        menor = num1
if (num3>num1 and num3>num2):
    maior = num3
    if(num1>num2):
        medio = num1
        menor = num2
    if(num2>num1):
        medio = num3
        menor = num1

print('O maior é', maior)
print('O médio é', medio)
print('O menor é', menor)