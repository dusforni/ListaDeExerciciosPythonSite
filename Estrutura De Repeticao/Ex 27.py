print('Ex 27 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

Alunos = {}
turmas = 0
nAlunos = 0
add = 's'
while add == 's':
    print('Adicione o numero de aluno na', turmas+1, end="")
    Alunos[turmas]= int(input(":\n"))
    while 0>Alunos[turmas] or Alunos[turmas]>40:
        print('Adicione o numero de aluno na', turmas + 1, end="")
        Alunos[turmas] = int(input(": - entre 0 e 40\n"))
    nAlunos = nAlunos+Alunos[turmas]
    turmas = turmas+1
    add = input("Adicionar outra turma? (s/n)")
nAlunos = nAlunos / turmas
nAlunos = round(nAlunos,2)
print('Numero de turmas:', turmas)
print('Média de alunos:', nAlunos)