'''
Manipular cadeias de caracteres - TRANSFORMACAO


+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10 ... 14
'''

frase = 'curso de Python'

#replace
print(frase.replace('Python', 'PHP'))

#maiuscula
print(frase.upper())

#minuscula
print(frase.lower())

#Primeira letra da frase maiuscula
print(frase.capitalize())

#Primeira letra de cada palavra maiuscula
print(frase.title())

frase1 = '       Aprendendo    Python  '
#Contando toda a cadeia
print(len(frase1))
print(frase1)
#Eliminando os espaços do inicio e do fim
print(frase1.strip())
#Eliminando os espaços do inicio
print(frase1.lstrip())
#Eliminando os espaços do fim
print(frase1.rstrip())




