print('Ex 23 - Site https://wiki.python.org.br/ExerciciosListas \n Eduardo Sforni \n')

valores = []
nome = []
mb = []

usuario = open('usuarios.txt', 'r')
index = 0
total = medio = arrumandoString = 0
for linha in usuario:
    valores = linha.split()
    nome.insert(index, valores[0])
    mb.insert(index, valores[1])
    index += 1

usuario.close()

for x in range(0,index):
    mb[x] = round(float(mb[x])/(1024*1024),2)
    total += mb[x]
    arrumandoString = 15-len(nome[x])
    nome[x] = nome[x]+" "*arrumandoString


medio = round(total/index,2)


rel = open('relatório.txt', 'w')
rel.writelines(f'ACME Inc.               Uso do espaço em disco pelos usuários\n')
rel.writelines(f'------------------------------------------------------------------------\n')
rel.writelines(f'Nr.  Usuário        Espaço utilizado     % do uso\n')
for x in range(0, index):
    rel.writelines(f'{x+1}    {nome[x]}       {mb[x]} MB         {round(mb[x]/total*100,2)}%\n')
rel.writelines('\n'*2)
rel.writelines(f'Espaço total ocupado: {total} MB\n')
rel.writelines(f'Espaço médio: {medio}')

rel.close()