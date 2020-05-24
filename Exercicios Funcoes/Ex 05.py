print('Ex 05 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')

def somaImposto(taxaImposto, custo):
    custo += custo*taxaImposto/100
    return custo

imp = float(input('Qual é a taxa do importo? Em %'))
cust = float(input('Qual é o custo do objeto?'))

imprimir = somaImposto(imp,cust)

print(imprimir, ' reais')