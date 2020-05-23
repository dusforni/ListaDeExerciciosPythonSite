print('Ex 11 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

a = [1,3,5,7,9,11,13,15,17,19]
b = [2,4,6,8,10,12,14,16,18,20]
c = [21,22,23,24,25,26,27,28,29,30]
d = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ai = bi = ci = 0

for x in range(0, 30):
    if x%3 == 0:
        d.insert(x,a[ai])
        ai += 1
    if x%3 == 1:
        d.insert(x,b[bi])
        bi += 1
    if x%3 == 2:
        d.insert(x,c[ci])
        ci += 1
    print(d[x]," " , end="")