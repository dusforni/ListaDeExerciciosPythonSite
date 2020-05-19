print('Ex 20 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

nota1 = float(input('Insira nota 1 \n'))
nota2 = float(input('Insira nota 2 \n'))
nota3 = float(input('Insira nota 3 \n'))

notafinal = (nota1+nota2+nota3)/3

if(notafinal >= 7 and notafinal < 10):
    print('Aprovado, nota final:', notafinal)
if(notafinal<7):
    print('Reprovado, nota final:', notafinal)
if(notafinal==10):
    print('Aprovado com distinção, nota final:', notafinal)