print('Ex 19 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

numero = int(input('Digite um numero inteiro!\n'))
while numero >=1000 or numero < 1:
    numero = int(input('Digite um numero inteiro positivo, menor que 1000\n'))

centena = numero//100
dezena  = (numero%100)//10
unidade = (numero%100)%10

if(centena == 0 and dezena == 0 and unidade <= 1):
    print(numero,':',unidade,'unidade')
if(centena == 0 and dezena == 0 and unidade > 1):
    print(numero,':',unidade,'unidades')


if(centena == 0 and dezena == 1 and unidade <= 1):
    print(numero,':',dezena,'dezena' ,unidade,'unidade')
if(centena == 0 and dezena == 1 and unidade > 1):
    print(numero,':',dezena,'dezena' ,unidade,'unidades')
if(centena == 0 and dezena > 1 and unidade <= 1):
    print(numero,':',dezena,'dezenas' ,unidade,'unidade')
if(centena==0 and dezena > 1 and unidade>1):
    print(numero,':',dezena,'dezenas' ,unidade,'unidades')


if(centena==1 and dezena <=  1 and unidade<=1):
    print(numero,':',centena, 'centena', dezena,'dezena' ,unidade,'unidade')
if(centena==1 and dezena <= 1 and unidade>1):
    print(numero,':',centena, 'centena', dezena,'dezena' ,unidade,'unidades')
if (centena==1 and dezena > 1 and unidade<=1):
    print(numero, ':', centena, 'centena', dezena, 'dezenas', unidade, 'unidade')
if (centena==1 and dezena > 1 and unidade > 1):
    print(numero, ':', centena, 'centena', dezena, 'dezenas', unidade, 'unidades')
if(centena>1 and dezena <=  1 and unidade<=1):
    print(numero,':',centena, 'centenas', dezena,'dezena' ,unidade,'unidade')
if(centena>1 and dezena <= 1 and unidade>1):
    print(numero,':',centena, 'centenas', dezena,'dezena' ,unidade,'unidades')
if (centena>1 and dezena > 1 and unidade<=1):
    print(numero, ':', centena, 'centenas', dezena, 'dezenas', unidade, 'unidade')
if (centena>1 and dezena > 1 and unidade > 1):
    print(numero, ':', centena, 'centenas', dezena, 'dezenas', unidade, 'unidades')