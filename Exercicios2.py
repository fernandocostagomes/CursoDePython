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
nota2 = int(input('Digite a segunda nota: '))
media = ((nota1 + nota2) / 2)
print('Nota 1: {} -- Nota 2: {} = Média: {}'.format(nota1, nota2, media))

'''
    Leia um valor em metros e depois exiba em cm e milimetros
'''
tamanho = float(input('Digite o tamanho em metros: '))
cm = (tamanho * 100)
mm = (tamanho * 1000)
print('O tamanho: {}m em Centimetros é: {}cm e em Milimetros é: {}mm'.format(tamanho, cm, mm))

'''
    O usuario digita um numero e vc digita a tabuada dele
'''
numeroTab = int(input('Digite um numero para sua tabuada: '))
contador = 1
while (contador <=10):
    print('{} x {} = {}'.format(numeroTab, contador, numeroTab*contador) )
    contador = contador +1

'''
    Solicite que o usuario digite quanto ele tem na carteira
    Depois exiba quantos dolares ela possui, usando a conversão U$ 1,00 = R$3,33
'''
quantia = float(input('Digite quanto você possui na carteira: '))
print('Você possui: {} reais, o que equivale a {} dolares'.format(quantia, quantia/3,33))


