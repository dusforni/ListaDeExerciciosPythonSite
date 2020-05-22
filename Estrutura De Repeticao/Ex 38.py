print('Ex 38 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

anoContratado = int(input('Ano de contratação?'))
anoAtual = int(input('Ano que estamos?'))
while anoContratado>anoAtual:
    anoAtual = int(input('Ano que estamos? (deve ser mais ou igual o ano de contratação'))
SalarioInicial  = float(input('Salário inicial do funcionário?'))

SalarioFinal = SalarioInicial
aumentoInicial = 0.015
tempoDeCasa = anoAtual - anoContratado

for x in range(1, tempoDeCasa+1):
    SalarioFinal = SalarioFinal*(1+aumentoInicial*x)

SalarioFinal = round(SalarioFinal,2)
print(SalarioFinal)
