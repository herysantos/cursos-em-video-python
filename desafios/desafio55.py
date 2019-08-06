
# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

print("Preciso que informe o peso de 5 pessoas: ")
pesos = []
for c in range(5):
    pesos.append(float(input('Informe um peso (Kg): ')))

maior = pesos[0]
menor = pesos[0]

for c in pesos:
    if maior < c:
        maior = c
    if maior > c:
        menor = c
print('O maior peso foi {:.1f} Kg e o menor foi {:.1f} Kg'.format(maior, menor))
