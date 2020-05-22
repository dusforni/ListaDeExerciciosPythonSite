print('Ex 23 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Até que numero você quer ver todos os primos?\n'))
while n<0:
    n = int(input('Digite um numero positivo? \n'))
res = 0
primo = 0
div = 0
for x in range(1, n+1):
    for y in range(1, x+1):
        res = x%y
        div = div + 1
        if (res==0):
            primo = primo + 1;
    if(primo==2):
        print(x,',', end="")
    primo = 0
print('\n FIM')
print("Divisões totais:",div)