print('Ex 30 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

ppao = float(input('Qual é o preço do pão? \n'))

print(' ***** Preço do pão:', ppao, ' ***** ')
print('Panificadora Pão de Ontem - Tabela de preços')


for x in range(1,51):
    ppaototal = ppao * x
    ppaototal = round(ppaototal,2)
    print(x,' - R$ ', ppaototal)