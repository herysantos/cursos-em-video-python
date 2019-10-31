#
# Crie um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta.
# No final mostre a lista ordenada.
#
lista = []
for i in range(0, 5):
    n = int(input('Insira um valor:'))

    if len(lista) == 0:
        lista.append(n)
        print('Adicionado no começo da lista.')
        continue

    for ii in range(0, len(lista)):
        if lista[ii] >= n:
            lista.insert(ii, n)
            print(f'Adicionado na posição {ii+1} da lista.')
            break

    if ii >= len(lista)-1:
        lista.append(n)
        print('Adicionado ao final da lista.')
print(f'Lista: {lista}')