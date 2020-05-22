print('Ex 43 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')
cod = 1
spec = 'o'
cq = bs = bo = ha = ch = re = 0

while cod != 0:
    cod = int(input('Código do produto? - 0 para encerrar o pedido \n'))
    if cod == 100:
        cq = cq + int(input('Quantos novos pedidos? \n'))
    elif cod == 101:
        bs = bs + int(input('Quantos novos pedidos? \n'))
    elif cod == 102:
        bo = bo + int(input('Quantos novos pedidos? \n'))
    elif cod == 103:
        ha = ha + int(input('Quantos novos pedidos? \n'))
    elif cod == 104:
        ch += int(input('Quantos novos pedidos? \n'))
    elif cod == 105:
        re += int(input('Quantos novos pedidos? \n'))
    elif cod !=0:
        print('\n ** Código inválido, digite novamente **')

print('***'*30)
print(' *** Seu pedido foi encerrado ***')
print('Item             - Quantidade - Preço Unitário - Total')
print(f'Cachorro Quente - {cq}          - R$1,20        - R${round(1.2*cq,2)}')
print(f'Bauru simples   - {bs}          - R$1,30        - R${round(1.3*bs,2)}')
print(f'Bauru com ovo   - {bo}          - R$1,50        - R${round(1.5*bo,2)}')
print(f'Hamburguer      - {ha}          - R$1,20        - R${round(1.2*ha,2)}')
print(f'Cheeseburguer   - {ch}          - R$1,30        - R${round(1.3*ch,2)}')
print(f'Refrigerante    - {re}          - R$1,00        - R${round(1.0*re,2)}')
print('TOTAL '+'*'*38+f' - R${round(1.2*cq+1.3*bs+1.5*bo+1.2*ha+1.3*ch+1.0*re,0)}')