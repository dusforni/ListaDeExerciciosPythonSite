print('Ex 05 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

Nota1 = float(input('Insira a nota parcial 1 \n'))
while Nota1>10 or Nota1<0:
    Nota1 = float(input('Valor inválido, insira a nota parcial 1 \n'))
Nota2 = float(input('Insira a nota parcial 2 \n'))
while Nota2>10 or Nota2<0:
    Nota2 = float(input('Valor inválido, insira a nota parcial 2 \n'))

notaFinal = (Nota1+Nota2)/2

if(notaFinal==10):
    print('Aprovado com distinção')
elif(notaFinal>6 and notaFinal < 10):
    print('Aprovado')
else:
    print('Reprovado')