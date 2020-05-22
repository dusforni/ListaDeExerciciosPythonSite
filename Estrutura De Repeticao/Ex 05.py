print('Ex 05 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

A = float(input('População da cidade um? (Com maior população) \n'))
B = float(input('População da cidade dois? (Menor população) \n'))
ano = 0
while A<B:
    print("População A tem que ser maior \n")

    A = float(input('População da cidade um? (Com maior população) \n'))
    while A < 1:
        A = float(input('População da cidade um? (Com maior população) - Numero positivo maior que um, por favor \n'))

    B = float(input('População da cidade dois? (Menor população) \n'))
    while B < 1:
            B = float(input('População da cidade um? (Menor população) - Numero positivo maior que um, por favor \n'))

taxaA = float(input('Taxa de crescimento da cidade A, em porcentagem \n'))
taxaB = float(input('Taxa de crescimento da cidade B, em porcentagem \n'))

while taxaA>taxaB:
    print('Taxa da cidade B precisa ser maior \n')
    taxaA = float(input('Qual é a taxa da cidade A?\n'))
    taxaB = float(input('Qual é a taxa de cidade B?\n'))

taxaA = (taxaA+100)/100
taxaB = (taxaB+100)/100
while A>B:
    A = A*taxaA
    B = B*taxaB
    ano = ano + 1
    print(ano, A, B)

print('\n Demorara', ano, ' anos para B ficar maior que A')