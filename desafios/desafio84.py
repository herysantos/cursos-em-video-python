#
# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# Quantas pessoas foram cadastradas.
# Umas listagem com as pessoas mais pesadas.
# Uma listagem com as pessoas mais leves.
#

lista = []
pessoa = []
cont = maior = menor = 0


while True:
    pessoa.append(str(input('Informe o nome: ')).strip())
    pessoa.append(float(input('Informe o peso: ').strip()))
    lista.append(pessoa[:])

    if len(lista) == 1:
        maior = menor = pessoa[1]
    elif maior < pessoa[1]:
        maior = pessoa[1]
    elif menor > pessoa[1]:
        menor = pessoa[1]

    pessoa.clear()

    c = str(input("Quer continuar? [S/N]")).strip().upper()[0]
    if c != 'S':
        break
print(f"Foram cadastradas {len(lista)} pessoas.")

print(f"O maior peso foi {maior}. De", end='')

for index, value in enumerate(lista):
    if value[1] == maior:
        print(f' {value[0]}', end='')
print('.')

print(f"O menor peso foi {menor}. De", end='')

for index, value in enumerate(lista):
    if value[1] == menor:
        print(f' {value[0]}', end='')
print('.')
