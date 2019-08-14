#
# Faça um programa que leia  um número qualquer e mostre seu fatorial.
#

c = int(input('Informe um número qualquer: '))
n = c
f = 1
while c != 0:
    f *= c
    c -= 1
print('O fatorial de {} é {}'.format(n, f))