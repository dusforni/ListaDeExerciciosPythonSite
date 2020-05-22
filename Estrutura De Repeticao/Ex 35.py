print('Ex 35 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Até que numero você quer saber todos os primos? \n'))

primo = 0
for x in range(1,n+1):
    for y in range(1,x+1):
        res = x%y
        if(res==0):
            primo = primo + 1
    if(primo==2):
        print(x,",", end=" ")
    else:
        primo = 0