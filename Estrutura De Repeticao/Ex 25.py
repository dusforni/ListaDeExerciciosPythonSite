print('Ex 25 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

n = [0,0,0,0,0,0,0,0,0,0]

div = 0
soma = 0
for x in range(0, len(n)):
    print("Idade", x+1, end="")
    n[x] = int(input(': \n'))
    while n[x]<0:
        print("Idade", x + 1, end="")
        n[x] = int(input(': \n'))
for x in range(0, len(n)):
    soma = soma + n[x]
    div = div +1
total = soma/div
print('A média da idade é:', total)
if(total<26):
    print("Jovem")
elif(total<60):
    print("Adulta")
else:
    print("Idosa")