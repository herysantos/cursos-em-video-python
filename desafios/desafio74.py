#
# Crie uma tupla com cinco números aleatórios e informe o maior e o menor.
#

limiteMax = 10
limiteMin = 0
from random import randint
num = (randint(limiteMin, limiteMax), randint(limiteMin, limiteMax), randint(limiteMin, limiteMax),
       randint(limiteMin, limiteMax), randint(limiteMin, limiteMax))

print(f'Os números sorteados foram: {num}\n')

print(f'O Maior: {max(num)} \nO Menor: {min(num)}.')


#for i in num:
#    if i < menor:
#        menor = i
#    if i > maior:
#        maior = i
#    print(i)
#print(f'O Maior: {maior} \nO Menor: {menor}.')
