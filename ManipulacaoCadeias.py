'''
Manipular cadeias de caracteres - FATIAMENTO


+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|C|u|r|s|o| |d|e| |P|y|t|h|o|n|
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
 0 1 2 3 4 5 6 7 8 9 10 ... 14
'''
frase = 'Curso de Python'
print(frase)
print(frase[3])
print(frase[14])
print(frase[9:14])
print(frase[9:15])
#pular de n em n ex:2
print(frase[9:15:2])
print(frase[0:15:2])
#Omitir no inicio ou no fim vai considerar zero ou até o fim da cadeia
print(frase[:9])
print(frase[9:])
#Pegar tamanho total e tirar n ex: 5
print(frase[:-5])
#pulando de 2 sem colocar fim
print(frase[6::2])