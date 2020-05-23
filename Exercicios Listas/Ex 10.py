print('Ex 10 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

a = [1,3,5,7,9,11,13,15,17,19]
b = [2,4,6,8,10,12,14,16,18,20]
c = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ai = 0
bi = 0
for x in range(0, 20):
    if x%2 == 0:
        c.insert(x,a[ai])
        ai += 1
    else:
        c.insert(x,b[bi])
        bi += 1
    print(c[x]," " , end="")