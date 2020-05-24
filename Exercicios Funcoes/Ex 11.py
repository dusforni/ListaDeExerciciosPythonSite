print('Ex 11 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')


def diaExtenso(mm):
    mes = ['Janeiro', 'Fevereiro', 'Março', 'Abril','Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']
    ext = mes[mm-1]
    return ext

def verificaData(dd,mm,aaaa):
    if 1<mm and mm>12:
        return 'erro'
    if mm%2!=0 and (dd<0 or dd>31):
        return 'erro'
    elif mm == 2 and aaaa%4==0 and ((dd<0 or dd>29)):
        return 'erro'
    elif mm == 2 and aaaa%4!=0 and ((dd<0 or dd>28)):
        return 'erro'
    elif mm%2==0 and (dd<0 or dd>30):
        return 'erro'
    elif aaaa < 0:
        return 'erro'
    else:
        return 'data certo'

dia = mes = ano = 0
vdata = 'data certa'
dia = int(input('Que dia é hoje?'))
mes = int(input('Que mês é hoje?'))
ano = int(input('Que ano é hoje?'))

vdata = verificaData(dia,mes,ano)
if vdata == 'data certo':
    ext = diaExtenso(mes)
    print(f'{dia} de {ext} de {ano}')
else:
    print('Data errada')