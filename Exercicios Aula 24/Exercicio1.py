'''
Exercício 1
---
Crie um script que leia o nome completo de uma pessoa, depois mostre:
O nome com todas as letras maiúsculas
O nome com todas as letras minúsculas
Quantas letras tem o nome sem considerar os espaços?
Quantas letras possui o primeiro nome?
'''

nomeCompleto = input('Digite o seu nome completo: ')
print('O nome em letras maisculas: {}'.format(str.lower(nomeCompleto)))
print('O nome em letras minusculas: {}'.format(str.upper(nomeCompleto)))
print('O total de letras do nome é: {}'.format(len(nomeCompleto.replace(" ",""))))
nomeSeparado = nomeCompleto.split()
print('O tamanho do primeiro nome: {}'.format(len(nomeSeparado[0])))

