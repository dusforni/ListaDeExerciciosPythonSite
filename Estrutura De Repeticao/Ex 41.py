print('Ex 41 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

d = float(input('Valor da dívida?'))
n =  int(input('Numero de parcelas? 0 - 3 - 6 - 9 - 12'))
juros = [0, 10, 15, 20, 25]
total = jurEncontra = jurosAplicados = 0
matriz = ([0,0],
          [1,1])
while n != 0 and n != 3 and n != 6 and n != 9 and n != 12:
    n = int(input('Numero de parcelas? 0 - 3 - 6 - 9 - 12'))

for x in range(0,5):
    jurEncontra = n - x*3
    if(jurEncontra == 0):
        jurosAplicados = juros[x]

total = d + d*(jurosAplicados)/100
print('n'*5)
print('***'*30)
print('Valor da dívida - Valor do juros - Quantidade de parcelas - Valor da parcela')
print(f'{d}            {d*(jurosAplicados)/100}                      {n}               {total/n}')
