print('Ex 12 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

salH = float(input('Valor da hora-trabalhada \n'))
trabH = float(input('Numero de horas trabalhadas \n'))

salM = salH*trabH

if(salM <= 900):
    dIR = 0.0
elif(1800 >= salM > 900):\
    dIR = 0.05
elif(2500>= salM > 1800):
    dIR = 0.10
else:
    dIR = 0.20

dIRb = dIR*salM
dINSS = salM*0.1
dFGTS = salM*0.11

print('Salário Bruto:(',salH,'*',trabH,'): \n R$', salM )
print('(-) IR (', dIR*100,'%) \n R$', dIRb)
print('(-) INSS (10%) \n R$', dINSS)
print('FGTS (11%) \n', dFGTS)
print('Total do desconto \n R$', dINSS+dIRb)
print('Salário liquido', salM-dINSS-dIRb)
