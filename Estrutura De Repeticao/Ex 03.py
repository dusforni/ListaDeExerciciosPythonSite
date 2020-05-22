print('Ex 03 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

nome = input('Nome?\n')
idade = int(input('Idade?\n'))
salario = float(input('Salário?\n'))
sexo = input('Sexo? (m/f) \n')
estadoCivil = input('Estado civil? (s,c,v,d)\n')

while len(nome)<=3:
    nome = input('Nome? - Deve conter mais que 3 digitos\n')
while 0>idade or idade>150:
    idade= int(input('Idade? - maior que 0 e menor que 150 \n'))
while salario<0:
    salario= float(input('Salário deve ser positivo, salário?\n'))
while sexo!='m' and sexo != 'n':
    sexo = input('Sexo? (m/f)\n')
while estadoCivil!= ('s' or 'c' or 'v' or 'd'):
    estadoCivil = input('Estado civil? (s,c,v,d)\n')