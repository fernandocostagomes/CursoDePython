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

numero1 = int(input('Digite um número entre 0 e 999: '))
uni = numero1 // 1 % 10
dez = numero1 // 10 % 10
cen = numero1 // 100 % 10

# Exibindo
print('Unidade : {}'.format(uni))
print('Dezena  : {}'.format(dez))
print('Centena : {}'.format(cen))

numero = str(input('Digite um número entre 0 e 999: '))
# if int.bit_length(numero) == 1:
#     print('O número digitado: {}\n Unidade: {}'.format(numero, numero))
# if int.bit_length(numero) == 2:
#     print('O número digitado: {}\n Dezena: {]\n Unidade: {}'.format(numero, int.))
#  if int.bit_length(numero) == 1:
#      print('O número digitado: {}\n Centena: {}\n Dezena: {]\n Unidade: {}'.format(numero, math.))

print('O número digitado: {}\n Unidade: {}\n Dezena{}\n Centena{}'.format(numero, numero[2], numero[1], numero[0]))