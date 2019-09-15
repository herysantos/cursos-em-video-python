#
# Crie uma tupla com cinco números aleatórios e informe o maior e o menor.
#

from random import randint
max = menor = 10
min = maior = 0
num = (randint(min, max), randint(min, max), randint(min, max), randint(min, max), randint(min, max))

for i in num:
    if i < menor:
        menor = i
    if i > maior:
        maior = i
    print(i)
print(f'O Maior: {maior} \nO Menor: {menor}.')
