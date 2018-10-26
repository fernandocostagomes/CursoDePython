'''
Manipular cadeias de caracteres - DIVISAO

+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10 ... 14
'''

frase = 'Curso de Python e Banco de Dados'

print(frase.split())

palavras = frase.split()

print(palavras[2])

linguagem = palavras[3]
print(linguagem)

frase2 = '1,2,3,4,5'
print(frase2.split(' '))
print(frase2.split(','))
print(frase2.split(',', maxsplit=2))

frase3 = '-'.join(palavras)
print(frase3)