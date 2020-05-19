print('Ex 08 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

pre1 = float(input('Escreva o preço 1 \n'))
pre2 = float(input('Escreva o preço 2 \n'))
pre3 = float(input('Escreva o preço 3 \n'))

if (pre1<pre2 and pre1<pre3):
    print('Compre o pruduto 1')
if (pre2<pre1 and pre2<pre3):
    print('Compre o produto 2')
if (pre3<pre1 and pre3<pre2):
    print('Compre o produto 3')