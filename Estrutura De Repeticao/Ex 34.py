print('Ex 34 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = int(input('Insira um numero inteiro que você deseja saber se é primo ou não! \n'))
primo = 0

for x in range(1,n+1):
    res = n%x
    if(res == 0):
        primo = primo + 1
if(primo==2):
    print('Esse numero é primo!')
else:
    print('não é primo')