print('Ex 39 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

nAluno = [1,2,3,4,5,6,7,8,9,10]
AltAluno = [1.71,1.70,1.73,1.85,1.55,1.90,1.79,1.81,1.73,1.64]

for x in range(0,10):
    if x == 0:
        maisAlto = AltAluno[x]
        maisBaixo = AltAluno[x]
        ponteiroA = x
        ponteiroB = x
    if maisAlto < AltAluno[x]:
        maisAlto = AltAluno[x]
        ponteiroA = x
    if maisBaixo > AltAluno[x]:
        maisBaixo = AltAluno[x]
        ponteiroB = x

print('O aluno mais alto tem código:', nAluno[ponteiroA], 'medindo', AltAluno[ponteiroA])
print('O aluno mais baixo tem código:', nAluno[ponteiroB], 'medindo', AltAluno[ponteiroB])