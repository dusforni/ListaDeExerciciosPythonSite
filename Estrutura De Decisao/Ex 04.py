print('Ex 04 - Site https://wiki.python.org.br/EstruturaDeDecisao \n Eduardo Sforni \n')

letra = str(input('Digite uma letra \n'))
vogal = ['a','e','i','o','u','A','E','I','O','U',]

if(letra in vogal):
    print('É uma vogal')
else:
    print('É uma consoante')

