print('Ex 13 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

DiaSemana = int(input('Digite um numero que corresponderá um dia da semana \n'))

semana = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"]
DiaSemana = DiaSemana-1  #Lista começa na referencia zero

if(1 <= DiaSemana <= 7):
    print(semana[DiaSemana])
else:
    print('Numero invalido')