'''

Condições no Python

'''

idade = int(input('Qual a sua idade por favor?'))

if idade < 18:
    print('Sua idade não permite a entrada nesse estabelecimento!')

if idade >= 18:
    bebida = str(input('Seja bem, vindo!\nQual bebida deseja?'))
    print('Segue sua bebida {}'.format(bebida))

idade1 = int(input('Qual a sua idade por favor?'))
if idade1 < 18:
    print('Sua idade não permite a entrada nesse estabelecimento!')
else:
    bebida = str(input('Seja bem, vindo!\nQual bebida deseja?'))
    print('Segue sua bebida {}'.format(bebida))

