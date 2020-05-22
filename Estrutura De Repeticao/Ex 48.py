print('Ex 48 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

num = int(input('Insira um numero inteiro e positivo!'))
while num<0:
    num = int(input('Insira um numero inteiro e positivo!'))
sX = str(num)
y = len(str(num)) #Descobrir o tamanho do numero :D
mun = 0 #num Invertido
print('=>  ', end="")
for x in range(0,y):
    print(sX[y-(x+1):y-x], end="")