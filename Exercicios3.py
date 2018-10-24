import math
import random
import pygame
'''
    Exercicios 3
'''

# '''
#     Crie um script que leia um numero real e exiba sua parte inteira.
#     Exemplo: 5.166 mostrar: 5
# '''
# numero = float(input('Digite um número real: '))
# print('A parte inteira deste número, é: {}'.format(math.floor(numero)))
#
# '''
#     Crie um script que leia um angulo do usuario final, depois exiba na tela o seno o coseno e a tangente.
# '''
# angulo = float(input('Digite um ângulo: '))
# print('Seno: {} \nCoseno: {} \nTagente: {}\n Número: {}'.format(math.sin(angulo), math.cos(angulo), math.tan(angulo), angulo))
#
# '''
#     Um professor quer sortear 3 de seus alunos para apagar o quadro.
#     Leia o nome desses tres alunos e depois exiba na tela o escolhido.
#     Modulo: random
# '''
# print('Digite os nomes dos Alunos para o sorteio de apagar o quadro:')
# aluno1 = input('Aluno 1: ')
# aluno2 = input('Aluno 2: ')
# aluno3 = input('Aluno 3: ')
# print('O Aluno sorteado foi {}'.format(random.choice([aluno1, aluno2, aluno3])))

'''
    Faça um script que abra e execute um arquivo mp3.
    Módulo> pygame
'''
print('Aperte enter para escutar uma música:')
input('')
try:
    pygame.init()
    pygame.mixer.music.load('musica.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()
except Exception:
    pygame.mixer.music.load('welcome.mp3')
    pygame.mixer.music.play()
