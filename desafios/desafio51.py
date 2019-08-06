
# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão aritimética.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Informe o primeiro termo de uma Progressão aritimética: '))
r = int(input('Informe a razão dessa progressão aritimética: '))

# Primeira maneira
ultimo = 9 * r + primeiro
for c in range(primeiro, ultimo+1, r):
    print(c)

#Segunda maneira
for c in range(0, 10):
    print(primeiro + r * c)
