'''

Exercício 2
---
O usuário irá digitar um número entre 0 e 999, então exiba cada um dos dígitos separados.
Exemplo: Número: 547
Unidade: 7
Dezena: 4
Centena: 5

'''
import math

numero = int(input('Digite um número: '))
if int.bit_length(numero) == 1:
    print('O número digitado: {}\n Unidade: {}'.format(numero, numero))
#if int.bit_length(numero) == 2:
#     print('O número digitado: {}\n Dezena: {]\n Unidade: {}'.format(numero, int.))
# if int.bit_length(numero) == 1:
#     print('O número digitado: {}\n Centena: {}\n Dezena: {]\n Unidade: {}'.format(numero, math.))