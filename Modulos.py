from math import sqrt, ceil, floor, pow
#import math
'''
Utilizando modulos no python
'''

'''
Bebidas
Comidas
Doces
'''

num = int(input('Digite um valor: ') )

raiz = sqrt(num)
#raiz = math.sqrt(num)

#Arredondamento para cima
print('Número  {} - Raiz {}'.format(num, ceil(raiz)))
#print('Número  {} - Raiz {}'.format(num, math.ceil(raiz)))

#Arredondamento para baixo
print('Número  {} - Raiz {}'.format(num, floor(raiz)))
#print('Número  {} - Raiz {}'.format(num, math.floor(raiz)))

#Potencia
print('Potencia: {}'.format(pow(2,3)))
#print('Potencia: {}'.format(math.pow(2,3)))


