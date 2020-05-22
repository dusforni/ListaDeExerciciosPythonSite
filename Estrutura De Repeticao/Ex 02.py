print('Ex 02 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

user = input('nome do usuário? \n')
password = input('senha?\n')
while user == password:
    print('Senha inválida, igual usuário')
    password = input('escreva outra senha\n')