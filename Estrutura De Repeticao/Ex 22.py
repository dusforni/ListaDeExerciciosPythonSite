print('Ex 22 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Digite um numero positivo? \n'))
while n<0:
    n = int(input('Digite um numero positivo? \n'))
primo = 0
for x in range(1, n+1):
    res = n%x
    if(res==0):
        primo = primo + 1
if primo == 2:
    print('Esse numero é primo')
else:
    print('Não é primo')
    print("Ele é divisivel por: ", end="")
    for x in range(1, n + 1):
        res = n % x
        if (res == 0):
            print(" ", x , ',', end="")