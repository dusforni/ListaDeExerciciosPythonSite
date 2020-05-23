print('Ex 20 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

sal = []
abono = []
salario = 10
ind = maior = minPago = total = 0

while salario != 0:
    salario = input('Qual é o salário?')
    while salario.isalpha() or float(salario)<0:
        salario = input('Qual é o salário? - numero')
    salario = float(salario)
    if salario != 0:
        sal.insert(ind,salario)
        if salario*0.2 >= 100:
            abono.insert(ind,salario*0.2)
        else:
            abono.insert(ind,100.0)
        ind += 1
print('SALÁRIO -- ABONO')
for x in range(0, len(sal)):
    print(f'R$ {sal[x]} -- R${abono[x]}')
    minPago = abono.count(100)
    total += abono[x]
    if maior < abono[x]:
        maior = abono[x]

print(f'Foram processados {ind} colaboradores')
print(f'Total gasto com abonos:{total}')
print(f'Valor mínimo pago a {minPago} colaboradores')
print(f'Maior valor de abono pago: R$ {maior}')
