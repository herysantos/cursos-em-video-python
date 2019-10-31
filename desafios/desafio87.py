#
# Aprimore o desafio anterior, mostrando no final.
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O Maior valor da segunda linha.
#

matriz = [[]]
maior_segunda_linha = soma_pares = soma_terceira = 0
for i in range(0, 3):
    for j in range(0, 3):
        matriz[i].append(int(input(f"Informe o valor de Matriz[{i}, {j}]: ")))
    if i < 2:
        matriz.append([])

for i in range(0, 3):
    for j in range(0, 3):
        if matriz[i][j] % 2 == 0:
            soma_pares += matriz[i][j]
        if i == 1:
            if j == 0:
                maior_segunda_linha = matriz[i][j]
            elif maior_segunda_linha < matriz[i][j]:
                maior_segunda_linha = matriz[i][j]
        if j == 2:
            soma_terceira += matriz[i][j]

print(f"Soma dos pares: {soma_pares}")
print(f"Soma da terceira coluna: {soma_terceira}")
print(f"Maior da segunda linha: {maior_segunda_linha}")
