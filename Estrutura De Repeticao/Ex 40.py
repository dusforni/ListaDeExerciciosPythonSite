print('Ex 40 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

cidade = {}
passeio = {}
AcComVitimas = {}

ponteiro = mediaVeiculos = media2k = maior = menor = pMaior = pMenor = 0

for x in range(0,5):
    ponteiro = x
    cidade[ponteiro] = int(input('Codigo da cidade?\n'))
    passeio[ponteiro] = int(input('Numero de carros de passeio na cidade?\n'))
    AcComVitimas[ponteiro] = int(input('Numero de carros de passeio na cidade?\n'))
    print('*****'*30)
    if ponteiro == 0:
        maior = AcComVitimas[ponteiro]
        menor = AcComVitimas[ponteiro]
    if maior < AcComVitimas[ponteiro]:
        maior = AcComVitimas[ponteiro]
        pMaior = ponteiro
    if menor > AcComVitimas[ponteiro]:
        menor = AcComVitimas[ponteiro]
        pMenor = ponteiro
    mediaVeiculos += passeio[ponteiro]
    if passeio[ponteiro]<2000:
        media2k += AcComVitimas[ponteiro]

mediaVeiculos = mediaVeiculos / 5
media2k = media2k / 5

print('\n'+'***'*30)
print(f'O menor indice de acidentes de transito é {menor} e pertence a cidade {cidade[pMenor]}')
print(f'O maior indice de acidentes de transito é {maior} e pertence a cidade {cidade[pMaior]}')
print(f'A média de veiculos da cidade é {mediaVeiculos}')
print(f'A média de acidentes em cidades com menos de 2000 veiculos é {media2k}')