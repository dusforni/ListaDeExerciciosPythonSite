print('Ex 36 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

t = int(input('Você quer a tabuada de qual numero?\n'))
it = int(input('Começando de qual numero?\n'))
ft = int(input('Terminando em qual numero?\n'))

print('** MONTAR A TABUADA DO ', t, '**' )
print('Começando por:', it)
print('Terminando em:', ft)

print('Vou montar a tabuada do', t,'começando em', it, 'e terminando em', ft)

for x in range(it,ft+1):
    res = t*x
    print(t,'x',x,'=', res)