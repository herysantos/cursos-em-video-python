
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares,
# Se o valor digitado for ímpar desconsidere-o.

v = []
s = 0

print('Preciso que você digite 6 números: ')
for c in range(0, 6):
    v.append(int(input('Insira um número: ')))

for c in v:
    if c % 2 == 0:
        s += c

print('A soma dos pares é: {}'. format(s))
