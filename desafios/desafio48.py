
# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.
s = 0
for c in range(0, 500, 3):
    if c % 2 == 1:
        s += c
print(s)
