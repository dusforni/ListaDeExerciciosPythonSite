print('Ex 14 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

sus = ['o','o','o','o','o']
soma = 0

sus[0] = input('Telefonou para a vítima? s/n\n')
sus[1] = input('Esteve no local do crime? s/n \n')
sus[2] = input('Mora perto da vítima? s/n \n')
sus[3] = input('Devia para a vítima? s/n \n')
sus[4] = input('Já trabalhou com a vítima? s/n \n')

soma = sus.count('s')

if soma<2:
    print('inocente')
elif soma<3:
    print('Suspeito')
elif soma<5:
    print('Cúmplice')
else:
    print('Assassino')