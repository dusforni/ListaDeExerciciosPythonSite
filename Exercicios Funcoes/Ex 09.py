print('Ex 09 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def reverso(x):
    num = ''
    y = str(x)
    y = len(y)

    for z in range(1,y+1):
        res = x//(10**(y-z))
        res = str(res)
        num = res+num
        res = int(res)
        x -= res*(10**(y-z))
    num = int(num)
    print(num)

x = int(input('Digite um numero?'))
reverso(x)