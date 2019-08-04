#
# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
#

n = int(input('Diga um número entre 0 e 9999: '))
num = '{:4}'.format(n).replace(' ', '0')

# [::-1] Passo menos um inverte de trás para frente os itens de uma lista
print('Unidade: {0[0]}\nDezena: {0[1]}\nCentena: {0[2]}\nMilhar: {0[3]}'.format(num.strip()[::-1]))

print('\nUnidade: {}'.format(n//1%10))
print('Dezena: {}'.format(n//10%10))
print('Centena: {}'.format(n//100%10))
print('Milhar: {}'.format(n//1000%10))
