print('Ex 25 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

tel = input('Telefonou para a vitima? (s/n) \n')
while tel != 's' and tel !='n':
    tel = input('Telefonou para a vitima? (s/n) \n')
local = input('Estava no local do crime? (s/n) \n')
while local != 's' and local !='n':
    local = input('Estava no local do crime? (s/n) \n')
mora = input('Mora perto da vítima? (s/n) \n')
while mora !='s' and mora != 'n':
    mora = input('Mora perto da vítima? (s/n) \n')
devia = input('Devia para a vitima? (s/n) \n')
while devia !='s' and devia != 'n':
    devia = input('Devia para a vitima? (s/n) \n')
trab = input('Trabalhou com a vitima? (s/n) \n')
while trab !='s' and devia !='n':
    trab = input('Trabalhou com a vitima? (s/n) \n')
suspeito = 0
if tel =='s':
    suspeito = suspeito + 1
if local =='s':
    suspeito = suspeito + 1
if mora =='s':
    suspeito = suspeito + 1
if devia =='s':
    suspeito = suspeito + 1
if trab =='s':
    suspeito = suspeito + 1

print(suspeito)

if suspeito < 2:
    print('Inocente')
if suspeito == 2:
    print('Suspeito')
if 3<=suspeito<=4:
    print('Cúmplice')
if suspeito == 5:
    print('Assassino')