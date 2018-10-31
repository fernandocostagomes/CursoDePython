'''
Condicoes2
'''

idade = int(input('Qual a sua idade por favor?'))

if idade < 18:
    print('Sua idade não permite a entrada nesse estabelecimento!')
elif (idade >= 18) and (idade < 21):
    print('Você pode consumir apenas refrigerante!')
else:
    bebida = str(input('Seja bem, vindo!\nQual bebida deseja?'))
    print('Segue sua bebida {}'.format(bebida))

