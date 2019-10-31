#
# Crie um programa que crie uma matriz 3x3 e preencha e preencha com valores lidos pelo teclado.
#

matriz = [[]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Informe o valor de Matriz[{i}, {j}]: ")))
    if i < 2:
        matriz.append([])

for l in range(0, 3):
    for c in range(0, 3):
        print(f"[{matriz[l][c]:^5}] ", end='')
    print()