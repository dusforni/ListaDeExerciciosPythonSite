print('Ex 26 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

tipo = input('Qual foi o time de combustível? A - Alcool , G - Gasolina \n')
while tipo != 'A' and tipo != 'a' and tipo != 'G' and tipo != 'g':
    tipo = input('Qual foi o time de combustível? A - Alcool , G - Gasolina \n')
litros = float(input('Quantos litros foram vendidos?\n'))
pAlcool = 1.90
pGasolina = 2.50
pagar = 0
if (tipo=='a' or tipo=='A') and (litros<=20):
    pAlcool = 1.90-1.90*0.03
    tipo = 'Alcool'
    pagar = pAlcool*litros
if (tipo=='a' or tipo=='A') and (litros>20):
    pAlcool = 1.90-1.90*0.05
    tipo = 'Alcool'
    pagar = pAlcool * litros
if (tipo=='g' or tipo=='G') and (litros<=20):
    pGasolina = 2.50-2.50*0.04
    tipo = 'Gasolina'
    pagar = pGasolina * litros
if (tipo == 'g' or tipo == 'G') and (litros > 20):
    pGasolina = 2.50 - 2.50 * 0.06
    pagar = pGasolina * litros
    tipo = 'Gasolina'

print('Você comprou:', litros, 'de', tipo, '\n Preço total:', pagar)