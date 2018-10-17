'''
Atribuicao multipla
'''

#Atribuicao simples
x = 10
y = 20
z = 30

# Atribuicao multipla
x, y, z = 10, 20, 30
print('{}, {}, {}'.format(x, y, z))

mais = menos = vezes = dividido = 2

mais = 1
mais = mais + 2
print(mais)
mais += 2
print(mais)

menos -= 5
print(menos)

vezes *= 5
print(vezes)

dividido /= 5
print(dividido)

nota = 6
if nota >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print('O Aluno com nota {} está {}'.format(nota, situacao))

situacao = 'Aprovado' if nota >= 7 else 'Reprovado'
print('O Aluno com nota {} está {}'.format(nota, situacao))

