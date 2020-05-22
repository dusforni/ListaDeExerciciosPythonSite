print('Ex 20 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')


repetir = 's'
while repetir == 's':
    n = int(input('Fale o numero fatorial que você deseja? de 0 16 \n'))
    while 0>n or n>16:
        n = int(input('Fale o numero fatorial que você deseja? de 0 16 \n'))
    n1= n
    n2 = 0
    if n == 0:
        n2 = 1
    for x in range(1,n):
        n2 = n1*(n-x)
        n1 = n2
    print(n2)
    repetir = input('Deseja fazer outro fatorial? s/n\n')


