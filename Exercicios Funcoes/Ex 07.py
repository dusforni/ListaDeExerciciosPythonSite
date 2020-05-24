print('Ex 07 - Site https://wiki.python.org.br/ExerciciosFuncoes \n Eduardo Sforni \n')


conta = 0
info = 0
def valorPagamento(prestacao, atraso):
    if atraso != 0:
        prestacao += prestacao*0.03 + prestacao*0.001*atraso
    return prestacao


def verificaPrestacaoEAtraso(pr, at):
    if pr < 0:
        return 'erro'
    if at < 0:
        return 'erro'

presta = 30
while presta != 0:
    presta = float(input('Valor da prestação?'))
    if presta == 0:
        print('*'*20)
        print('DIA ENCERRADO')
        print(f'Contas: {conta}, totalizando: {info} reais')
    else:
        atra = int(input('Dias em atraso?'))
        error = verificaPrestacaoEAtraso(presta,atra)
        if error != 'erro':
            valorPagar = valorPagamento(presta,atra)
            info += valorPagar
            conta += 1
            print(f'Valor da prestação: {valorPagar}')

        else:
            print('Algum valor foi negativo, por favor digite novamente')
