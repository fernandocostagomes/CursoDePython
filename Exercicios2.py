'''
Exercicios
'''

# Crie um script onde o usuario digite um numero inteiro e na tela seja exibido o antecessor e o sucessor.

numero = numero1 = numero2 = int(input('Digite um número: '))
#numero = numero1 = numero2 = 10
print(numero)
numero1 -= 1
numero2 += 1
print('O antecessor do numero: ', numero,  'é:', numero1, 'e o sucessor é:', numero2 )

'''
Leia um numero e exiba na tela o seu dobro, o triplo e sua raiz quadrada.
A raiz quadrada é a mesma coisa que realizarmos a potencia de 0.5
'''

numero30 = numero31 = numero32 = numero33 = int(input('Digite um número: '))
numero31 *= 2
numero32 *= 3
numero33 **= 0.5

print('O dobro desse número é: {}, o triplo é: {}, e sua raiz quadrada é: {}'.format(numero31, numero32, numero33))

'''
    Faça um script que leia duas notas de um aluno, depois mostre sua media.
'''

nota1 = int(input('Digite a primeira nota: '))
nota2 = int(input('Digite a primeira nota: '))
media = ((nota1 + nota2) / 2)
print('Nota 1: {} -- Nota 2: {} = Média: {}'.format(nota1, nota2, media))

'''
    Leia um valor em metros e depois exiba em cm e milimetros
'''
tamanho = float(input('Digite o tamanho em metros: '))
cm = (tamanho * 100)
mm = (tamanho * 1000)
print('O tamanho: {} em Centimetros é: {} e em Milimetros é: {}'.format(tamanho, cm, mm))

