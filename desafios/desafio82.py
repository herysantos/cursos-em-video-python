#
# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados,
# respectivamente.
# Ao final, mostre o conteúdo das três listas geradas.
#

lista = []
pares = []
impares = []

while True:
    lista.append(int(input("Digital um número: ")))
    c = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if c != 'S':
        break

for i in range(0, len(lista)):
    if lista[i] % 2 == 0:
        pares.append(lista[i])
    else:
        impares.append(lista[i])

print(f"Lista:{lista}\n"
      f"Pares: {pares}\n"
      f"Ímpares: {impares}")
