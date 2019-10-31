#
# Faça um progrmaa que leia 5 valores numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor vaores digitado e as suas respectivas posições na lista.
#

from random import randint

lista = []
maior = menor = 0
limite = 5

for n in range(0, limite):
    lista.append(randint(0, limite))

for n in range(0, limite):
    if n == 0:
        maior = menor = lista[n]
        continue
    if lista[n] > maior:
        maior = lista[n]
    if lista[n] < menor:
        menor = lista[n]

print(f'Lista{lista}')

print(f'Maior: {maior:^2} Índices: ', end='')
for i, v in enumerate(lista):
    if v == maior:
        print(f' {i}', end='')
print('.')
print(f'Menor: {menor:^2} Índices: ', end='')
for i, v in enumerate(lista):
    if v == menor:
        print(f' {i}', end='')
print('.')

