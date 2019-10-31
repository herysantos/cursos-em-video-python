#
# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionad.
# No final serão exibidos todos os valores únicos digitados em ordem crescente.
#

lista = []
n = 0
while True:
    n = int(input('Insira um número:'))
    if n not in lista:
        lista.append(n)
    c = str(input('Quer continuar? [S/N]')).strip().upper()
    if c != 'S':
        break
lista.sort()

print(f'A lista com valores únicos e ordenados é {lista} contendo {len(lista)} valores.')

"""
from random import randint

lista= []
limite = 10
for n in range(0, limite):
    i = randint(0, limite)
    if i not in lista:
        lista.append(i)
lista.sort()

print(f'A lista com valores únicos e ordenados é {lista} contendo {len(lista)} valores.')
"""


