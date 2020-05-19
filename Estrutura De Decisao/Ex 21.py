print('Ex 21 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

saque = int(input('Quanto você quer sacar?\n'))
while saque >=600 or saque < 10:
    saque = int(input('Só pode sacar entre 10 e 600 reais\n'))

cem = saque//100
cinquenta = (saque%100)//50
dezena = (saque-cem*100-cinquenta*50)//10
cinco = (saque-cem*100-cinquenta*50-dezena*10)//5
unidade = saque-cem*100-cinquenta*50-dezena*10-cinco*5

print('Você sacará:', saque,'reias, as notas serão:')
if(cem==1):
    print(cem,'nota de 100')
if(cem>1):
    print(cem,'notas de 100')
if(cinquenta==1):
    print(cinquenta,'nota de 50')
if(cinquenta>1):
    print(cinquenta,'notas de 50')
if(dezena==1):
    print(dezena,'nota de 10')
if(dezena>1):
    print(dezena,'notas de 10')
if(cinco==1):
    print(cinco,'nota de 5')
if(cinco>1):
    print(cinco,'notas de 5')
if(unidade==1):
    print(unidade,'nota de 1')
if(unidade>1):
    print(unidade,'notas de 1')
