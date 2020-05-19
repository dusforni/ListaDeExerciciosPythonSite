print('Ex 28 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

tipo = int(input('Tipo de carne? \n 1- Filé Duplo \n 2- Alcatra \n 3- Picanha \n'))
qnt = float(input('Quantidade, em Kg, da carne? \n'))
tipoPagamento = int(input('Tipo de pagamento: \n 1- Dinheiro \n 2- Cartão \n 3- Cartão tabajara \n'))
precoBruto = 0
precoDesconto = 0
precoLiquido = 0
if(qnt<=5):
    if(tipo == 1):
       precoBruto = qnt*4.9
       tipoT = 'Filé Duplo'
    if(tipo == 2):
        precoBruto = qnt*5.9
        tipoT = 'Alcatra'
    if (tipo == 3):
        precoBruto = qnt * 6.9
        tipoT = 'Picanha'
else:
    if(tipo == 1):
        precoBruto = qnt * 5.8
        tipoT = 'Filé Duplo'
    if (tipo == 2):
        precoBruto = qnt * 6.8
        tipoT = 'Alcatra'
    if (tipo == 3):
        precoBruto = qnt * 7.8
        tipoT = 'Picanha'
if(tipoPagamento == 3):
    precoLiquido = precoBruto - precoBruto*0.05

precoDesconto = precoBruto - precoLiquido
precoBruto = round(precoBruto, 3)
precoDesconto = round(precoDesconto, 3)
precoLiquido = round(precoLiquido,3)

print('*********NOTA FISCAL********')
print('Tipo da carne:', tipoT)
print('Preço total:', precoBruto)
print('Preço desconto (-):', precoDesconto)
print('A pagar:', precoLiquido)

