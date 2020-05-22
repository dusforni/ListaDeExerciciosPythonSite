print('Ex 37 - Site https://wiki.python.org.br/EstruturaDeRepeticao \n Eduardo Sforni \n')

cod = {}
alt = {}
peso = {}

ponteiro = 0
somaAltura = 0
somaPeso = 0
mediaAltura = 0
mediaPeso = 0
duracao = 100

while duracao != 0:
    cod[ponteiro] = int(input('Qual é seu código?'))
    duracao = cod[ponteiro]
    if cod[ponteiro] != 0:
        alt[ponteiro] = float(input('Altura em metros?'))
        peso[ponteiro] = float(input('Peso em kg?'))
        somaPeso = somaPeso + peso[ponteiro]
        somaAltura = somaAltura + alt[ponteiro]
        if ponteiro == 0:
            maisAlto = alt[ponteiro]
            maisBaixo = alt[ponteiro]
            maisPesado = peso[ponteiro]
            maisLeve = peso[ponteiro]
        if maisAlto < alt[ponteiro]:
            maisAlto = alt[ponteiro]
            pMaisAlto = ponteiro
        elif maisBaixo > alt[ponteiro]:
            maisBaixo = alt[ponteiro]
            pMaisBaixo = ponteiro
        if maisPesado < peso[ponteiro]:
            maisPesado = peso[ponteiro]
            pMaisPesado = ponteiro
        elif maisLeve > peso[ponteiro]:
            maisLeve = peso[ponteiro]
            pMaisLeve = ponteiro
    ponteiro = ponteiro+1

NumClientes = len(alt)

mediaPeso = somaPeso/NumClientes
mediaAltura = somaAltura/NumClientes

print('O cod do cliente mais pesado é:', cod[pMaisPesado], 'pesando ', peso[pMaisPesado],' Altura ', alt[pMaisPesado])
print('O cod do  cliente mais leve é:', cod[pMaisLeve], 'pesando ', peso[pMaisLeve],' Altura ', alt[pMaisLeve])
print('O cod do  cliente mais alto é:', cod[pMaisAlto], 'pesando ', peso[pMaisAlto],' Altura ', alt[pMaisAlto])
print('O cod do  cliente mais baixo é:', cod[pMaisBaixo], 'pesando ', peso[pMaisBaixo],' Altura ', alt[pMaisBaixo])