#
# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha
# separados os valores pares e impares. No final mostre os valores pares e ímpares em ordem crescente.
#

lista = [[], []]

for i in range(0, 7):
    num = int(input(f"Digite o {i+1}º número: "))
    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)
lista[0].sort()
lista[1].sort()
print(f"Lista Pares {lista[0]}")
print(f"Lista Ímpares {lista[1]}")