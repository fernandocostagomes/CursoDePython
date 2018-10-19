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
print('Você possui: {} reais, o que equivale a {:.2f} dolares'.format(quantia, quantia/3,33))

'''
    Solicite o tamanho da largura e da altura da parede
    Depois exiba a área e a quantidade de tinta para pintá-la.
    Considerando que 1 litro de tinta, pinta uma área de 3m2
'''
largura = float(input('Digite a largura da parede: '))
altura = float(input('Digite a altura da parede: '))

print('A área dessa parede é de: {:.2f}m² e é necessário {:.2f} litros de tinta para pintá-la.'.format(largura*altura, (largura*altura)/3))

'''
    Solicite o valor do produto ao usuario;
    Devolva o valor com 10% de desconto.
'''
valorTotal = float(input('Digite o valor do produto: '))
print('O valor do produto com 10% de desconto é: R$ {:.2f}.'.format(valorTotal - 10 * (valorTotal/100)))


