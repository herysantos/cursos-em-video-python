#
# Crie um programa que vai ler vários números e colocar em uma lista.
#
# Depois disso, mostre:
#
# A) Quantos números foram digitados.
# B) A lista de valores, ordenados de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
#

lista = []

while True:
    lista.append(int(input("Digital um número: ")))
    c = str(input("Quer continuar? [S/N] ")).strip().upper()[0]
    if c != 'S':
        break

print(f"Tem {len(lista)} números na lista")
lista.sort(reverse=True)
print(f"A lista decrescente é: {lista}")
print(f"{'Não T' if 5 in lista else 'T'}em 5 na lista.")
