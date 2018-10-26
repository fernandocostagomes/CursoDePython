'''
Analisar no nome digitado se contem o sobrenome Silva
'''

sobrenome = str(input('Digite seu nome completo por favor:'))

if 'Silva' in sobrenome:
    print('O nome digitado: "{}" possui o sobrenome "Silva"'.format(sobrenome))
else:
    print('O nome digitado: "{}" não possui o sobrenome "Silva"'.format(sobrenome))