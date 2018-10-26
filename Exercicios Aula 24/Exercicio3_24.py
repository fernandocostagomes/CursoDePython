'''
O usuario entra com o nome de uma cidade.
Analisar se o nome da cidade começa ou não com "São"
'''

nome = str(input('Digite o nome de uma cidade por favor: '))

if nome.count('São', 0, 3):
    print('O nome da cidade começa com "São"!')
else:
    print('O nome da cidade não começa com "São"!')