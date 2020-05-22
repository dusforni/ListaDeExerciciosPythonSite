print('Ex 42 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')
m25 = m50 = m50 = m75 = m100 = 0
n = 0
while n>= 0:
    n = float(input('Digite um numero? 0-100, negativo para parar'))
    while 100<n:
        n = float(input('Digite um numero? 0-100, negativo para parar'))
    if n>=0:
        if n<=25:
            m25 += 1
        elif n<=50:
            m50 += 1
        elif n<=75:
            m75 += 1
        else:
            m100 += 1
print(f'Menor 25: {m25} ')
print(f'Entre 26 - 50: {m50} ')
print(f'Entre 51 - 75: {m25} ')
print(f'Entre 76 - 100: {m25} ')