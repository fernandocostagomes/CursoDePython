'''
Mostrar na frase digitada quantas vezes aparece a letra "a";
Em que posição ela aparece pela primeira vez.
Em que posição ela aparece pela ultima vez;
'''

frase = str(input('Digite uma frase por favor:'))

print('A letra "a" aparece na frase: {} vezes, apareceu pela primeira vez na '
      'posição {} e na posição {} pela ultima vez!'.format(frase.count('a'), frase.find('a'), frase.rfind('a')))