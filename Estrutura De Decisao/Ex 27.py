print('Ex 27 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

maca = float(input('Quantos Kg de maça foram comprados? \n'))
morango = float(input('Quantos Kg de morago foram comprados? \n'))

totalKg = maca+morango

if(maca<=5):
    pMaca = maca*1.8
else: pMaca = maca*1.5
if(morango<=5):
    pMorango = morango*2.5
else: pMorango = morango*2.2

pTotal = pMorango+pMaca

if(totalKg > 8 or pTotal > 25):
    pTotal = pTotal - pTotal*0.1

print('O cliente pagará', pTotal)