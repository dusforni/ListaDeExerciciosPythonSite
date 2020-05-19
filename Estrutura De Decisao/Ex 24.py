print('Ex 24 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

x = float(input('Escreva o primeiro numero\n'))
y = float(input('Escreva o segundo numero\n'))
op = input('O que você quer fazer com esse numero? /, *, + ou -')

if(op=='/'):
    res = x/y
    print(res)
    if(res%2==0):
        print('par')
    else:
        print('impar')
    if (res > 0):
        print('positivo')
    elif (res == 0):
        print('zero')
    else:
        print('negativo')
    if(res//1 == res):
        print('Inteiro')
    else:
        print('Decimal')

if(op=='*'):
    res = x*y
    print(res)
    if(res%2==0):
        print('par')
    else:
        print('impar')
    if (res > 0):
        print('positivo')
    elif (res == 0):
        print('zero')
    else:
        print('negativo')
    if(res//1 == res):
        print('Inteiro')
    else:
        print('Decimal')

if(op=='+'):
    res = x+y
    print(res)
    if(res%2==0):
        print('par')
    else:
        print('impar')
    if (res > 0):
        print('positivo')
    elif (res == 0):
        print('zero')
    else:
        print('negativo')
    if(res//1 == res):
        print('Inteiro')
    else:
        print('Decimal')

if(op=='-'):
    res = x-y
    print(res)
    if(res%2==0):
        print('par')
    else:
        print('impar')
    if (res > 0):
        print('positivo')
    elif (res == 0):
        print('zero')
    else:
        print('negativo')
    if(res//1 == res):
        print('Inteiro')
    else:
        print('Decimal')

