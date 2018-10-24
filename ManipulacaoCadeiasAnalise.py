'''
Manipular cadeias de caracteres - ANALISE


+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10 ... 14
'''
frase = 'Curso de Python'
#tamanho da string
print(len(frase))

#quantas vezes aparece o caractere ex: o
print(frase.count('o'))
print(frase.count('s'))

#quantas vezes aparece o caractere ex: o
print(frase.count('o',0,5))
print(frase.count('o',0,4))
print(frase.count('o',0,15))

#buscar uma mencao ex: hon / -1 não existe
print(frase.find('hon'))
print(frase.find('php'))

# string em uma cadeia de caracteres retorna boolean
print('Cadeia' in frase)
print('Curso' in frase)




