'''
    Formatando exibicoes de tela - Format
'''

cor = input('Escolha uma cor: ')
print('A cor escolhida foi: ' + cor)
#numero de caracteres
print('A cor escolhida foi: {:10}. '.format( cor ))
print('A cor escolhida foi: {:>10}. '.format( cor ))
print('A cor escolhida foi: {:<10}. '.format( cor ))
print('A cor escolhida foi: {:=^10}. '.format( cor ))
print('A cor escolhida foi: {:*^10}. '.format( cor ))

n1 = 7
n2 = 3
print('A Soma de {}'.format(n1), 'mais {}'.format(n2), 'é: ', n1 + n2 )

so = n1 + n2
su = n1 - n2
mu = n1 * n2
di = n1 / n2
dii = n1 // n2
ex = n1 ** n2

print('Soma: {} \nSubtração: {} \nMultiplicação: {} \nDivisão: {:.2f} \nDivisão inteira: {} \nPotência: {}'.format(so, su, mu, di, dii, ex))