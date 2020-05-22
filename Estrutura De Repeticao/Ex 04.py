print('Ex 04 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')
A = 80000
B = 200000
ano = 0
while B>A:
    A = A*1.03
    B = B*1.015
    ano = ano+1

print('Demorará', ano,' anos para a cidade A ficar maisor que a cidade B')